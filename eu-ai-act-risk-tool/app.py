"""
EU AI Act Risk Self-Assessment Tool
Streamlit UI — delegates all classification logic to risk_classifier.py

Reflects: European Commission draft Article 6 guidelines, 19 May 2026
Source: https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems
"""

import json
from pathlib import Path

import streamlit as st

from report_generator import generate_pdf
from risk_classifier import AssessmentInput, AssessmentResult, RiskTier, classify

# ----------------------------------------------------------------
# Page config
# ----------------------------------------------------------------
st.set_page_config(
    page_title="EU AI Act Risk Self-Assessment | Tolt Innovations",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------
# Load Annex III reference data
# ----------------------------------------------------------------
DATA_PATH = Path(__file__).parent / "data" / "annex_iii.json"
with open(DATA_PATH) as f:
    ANNEX_III = json.load(f)["areas"]

ANNEX_III_BY_ID: dict[str, dict] = {a["id"]: a for a in ANNEX_III}

# ----------------------------------------------------------------
# Styling — Tolt brand palette (extracted from tolt.ie CSS variables)
# --bg:#f6f4ef  --ink:#0b1b2b  --accent:#4f46e5  --line:#e4dfd4
# ----------------------------------------------------------------
st.markdown(
    """
    <style>
    /* ── Global background & text ── */
    .stApp, .main, section[data-testid="stSidebar"],
    div[data-testid="stAppViewContainer"], div[data-testid="stHeader"] {
        background-color: #f6f4ef !important;
    }
    html, body, [class*="css"],
    p, li, span, label, div,
    .stMarkdown, .stText, .stCaption,
    .element-container, .stAlert p {
        color: #0b1b2b !important;
    }

    /* ── Headings ── */
    h1, h2, h3, h4 { color: #0b1b2b; font-weight: 700; }

    /* ── Dividers ── */
    hr { border-color: #e4dfd4 !important; }

    /* ── Primary button → Tolt indigo ── */
    .stButton > button[kind="primary"] {
        background-color: #4f46e5 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.4rem !important;
    }
    .stButton > button[kind="primary"]:hover {
        background-color: #6366f1 !important;
    }

    /* ── Download button ── */
    .stDownloadButton > button {
        background-color: #0b1b2b !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        border: none !important;
    }
    .stDownloadButton > button:hover {
        background-color: #1a2a3d !important;
    }

    /* ── Expanders ── */
    .streamlit-expanderHeader {
        background-color: #ffffff !important;
        border: 1px solid #e4dfd4 !important;
        border-radius: 8px !important;
        color: #0b1b2b !important;
        font-weight: 600 !important;
    }
    .streamlit-expanderContent {
        background-color: #ffffff !important;
        border: 1px solid #e4dfd4 !important;
        border-top: none !important;
    }

    /* ── Info / warning / error boxes ── */
    .stAlert { border-radius: 8px !important; }

    /* ── Tier result banners ── */
    .tier-prohibited {
        background: #fff0f0;
        border-left: 5px solid #be123c;
        padding: 18px 20px;
        border-radius: 8px;
        margin: 12px 0;
    }
    .tier-high {
        background: #fff7ed;
        border-left: 5px solid #c2410c;
        padding: 18px 20px;
        border-radius: 8px;
        margin: 12px 0;
    }
    .tier-limited {
        background: #eeeafe;
        border-left: 5px solid #4f46e5;
        padding: 18px 20px;
        border-radius: 8px;
        margin: 12px 0;
    }
    .tier-minimal {
        background: #f0fdf4;
        border-left: 5px solid #15803d;
        padding: 18px 20px;
        border-radius: 8px;
        margin: 12px 0;
    }

    /* ── Caption / muted text ── */
    .caption-note, small, .stCaption { color: #6b7a8c !important; }

    /* ── Text inputs & text areas ── */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #ffffff !important;
        border: 1px solid #e4dfd4 !important;
        border-radius: 8px !important;
        color: #0b1b2b !important;
    }

    /* ── Checkboxes ── */
    .stCheckbox label { color: #1a2a3d !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------
# Header
# ----------------------------------------------------------------
col_logo, col_title = st.columns([1, 6])
with col_title:
    st.title("EU AI Act Risk Self-Assessment Tool")
    st.caption(
        "Reflects the European Commission draft Article 6 classification guidelines "
        "published **19 May 2026** · Consultation closes 23 June 2026 · "
        "Produced as a demonstration for [Tolt Innovations](https://www.tolt.ie)"
    )

st.divider()

# ----------------------------------------------------------------
# SECTION 1 — System identification
# ----------------------------------------------------------------
st.header("1. Your AI system")
st.markdown(
    "Describe the system you want to classify. The more specific you are, "
    "the more accurate the classification will be."
)

col1, col2 = st.columns([3, 1])
with col1:
    intended_purpose = st.text_area(
        "Intended purpose of the AI system",
        placeholder=(
            "e.g. 'A machine learning model that scores individual loan applications "
            "for a retail bank, outputting an approve/decline recommendation.'"
        ),
        height=100,
        help="Describe what the system does and how it makes or influences decisions.",
    )
with col2:
    organisation_name = st.text_input(
        "Organisation name (optional)",
        placeholder="e.g. Acme Bank plc",
    )
    is_regulated_fs = st.checkbox(
        "CBI-regulated financial services firm",
        help=(
            "Tick if your organisation is regulated by the Central Bank of Ireland. "
            "This adds a CBI 2026 Supervisory Outlook overlay to your report."
        ),
    )

st.divider()

# ----------------------------------------------------------------
# SECTION 2 — Article 5 prohibited practices
# ----------------------------------------------------------------
st.header("2. Prohibited practices (Article 5)")
st.markdown(
    "**Tick any that apply.** If any box is ticked, the system is outright banned "
    "in the EU regardless of any other factors — maximum penalty €35M or 7% of global turnover."
)

with st.expander("Article 5 prohibited practices — expand to review"):
    prohibited_checks = {
        "uses_subliminal_manipulation": st.checkbox(
            "Uses subliminal techniques beyond conscious awareness to materially distort behaviour, "
            "causing or likely causing significant harm (Art 5(1)(a))"
        ),
        "exploits_vulnerabilities": st.checkbox(
            "Exploits vulnerabilities of a specific group due to age, disability, or "
            "social/economic situation to distort behaviour, causing significant harm (Art 5(1)(b))"
        ),
        "social_scoring": st.checkbox(
            "Social scoring of natural persons by public authorities or on their behalf — "
            "evaluating or classifying people based on social behaviour (Art 5(1)(c))"
        ),
        "predictive_policing_profiling": st.checkbox(
            "Individual risk assessment for likelihood of offending based solely on "
            "profiling or personality traits, without objective facts (Art 5(1)(d))"
        ),
        "untargeted_facial_scraping": st.checkbox(
            "Untargeted scraping of facial images from the internet or CCTV to build "
            "or expand facial recognition databases (Art 5(1)(e))"
        ),
        "emotion_recognition_workplace_education": st.checkbox(
            "Emotion recognition systems used in the workplace or educational institutions "
            "(Art 5(1)(f))"
        ),
        "biometric_categorisation_sensitive": st.checkbox(
            "Biometric categorisation inferring sensitive attributes: race, political opinions, "
            "trade union membership, religious/philosophical beliefs, sex life or sexual orientation "
            "(Art 5(1)(g))"
        ),
        "realtime_remote_biometric_id": st.checkbox(
            "Real-time remote biometric identification in publicly accessible spaces for "
            "law enforcement purposes (Art 5(1)(h)) — narrow exceptions exist for missing persons, "
            "imminent terrorist threats, etc."
        ),
    }

st.divider()

# ----------------------------------------------------------------
# SECTION 3 — Article 6(1) safety component
# ----------------------------------------------------------------
st.header("3. Safety component of a regulated product (Article 6(1))")
st.markdown(
    "This path applies to AI systems that are safety components of, or are themselves, "
    "products regulated under EU harmonisation legislation (Annex I) — e.g. medical devices, "
    "machinery, toys, in vitro diagnostics, lifts, radio equipment."
)

col3a, col3b = st.columns(2)
with col3a:
    is_safety_component = st.checkbox(
        "The AI system is a safety component of, or itself a product under, "
        "EU harmonisation legislation listed in Annex I (Art 6(1)(a))",
        help=(
            "Annex I includes: Machinery Regulation, Medical Devices, "
            "In Vitro Diagnostics, Radio Equipment, Toys, Lifts, "
            "Personal Protective Equipment, Pressure Equipment, etc."
        ),
    )
with col3b:
    requires_conformity = st.checkbox(
        "The product/safety component must undergo third-party conformity assessment "
        "under the relevant Annex I legislation (Art 6(1)(b))",
        disabled=not is_safety_component,
    )

st.divider()

# ----------------------------------------------------------------
# SECTION 4 — Annex III use cases
# ----------------------------------------------------------------
st.header("4. Annex III use case areas (Article 6(2))")
st.markdown(
    "Tick any Annex III areas that match the system's intended purpose. "
    "A match here provisionally classifies the system as high-risk — subject to the "
    "Article 6(3) filter check in Section 5."
)

selected_areas: list[str] = []

for area in ANNEX_III:
    with st.expander(f"{area['annex_reference']} — {area['name']}"):
        area_ticked = False
        for use_case in area["use_cases"]:
            if st.checkbox(use_case, key=f"annex_{area['id']}_{use_case[:30]}"):
                area_ticked = True
        if area_ticked:
            selected_areas.append(area["id"])

if selected_areas:
    st.info(
        f"**Annex III areas matched:** {', '.join(ANNEX_III_BY_ID[a]['name'] for a in selected_areas)}. "
        "Proceed to Section 5 to check for Article 6(3) filter eligibility."
    )

st.divider()

# ----------------------------------------------------------------
# SECTION 5 — Article 6(3) filter
# ----------------------------------------------------------------
st.header("5. Article 6(3) high-risk exemption filter")

if not selected_areas:
    st.markdown(
        "*No Annex III areas were selected in Section 4, so the Article 6(3) filter is not applicable. "
        "Proceed to classify.*"
    )
    filter_visible = False
else:
    filter_visible = True
    st.markdown(
        "The Article 6(3) filter can reduce a provisional Annex III high-risk classification "
        "if the system meets one of the four conditions below **and** does **not** perform "
        "profiling of natural persons. "
        "Per the Commission's May 2026 draft guidelines, these conditions must be **interpreted narrowly**."
    )

    st.warning(
        "**Profiling blocker:** If the system performs profiling of natural persons, "
        "none of the filter conditions below apply — the system remains HIGH-RISK regardless.",
        icon="⚠️",
    )

    performs_profiling = st.checkbox(
        "The system performs **profiling of natural persons** "
        "(i.e. automated processing of personal data to evaluate aspects of a person)",
        help=(
            "Profiling is defined under GDPR Art 4(4) as automated processing of personal "
            "data to evaluate personal aspects, especially to analyse or predict behaviour, "
            "location, health, preferences, reliability, etc."
        ),
    )

    st.markdown("**Article 6(3) filter conditions** — tick if the system meets any of the following:")

    narrow_procedural = st.checkbox(
        "*(a)* The AI system performs a **narrow procedural task only**",
        help="Per Commission draft guidelines: the task must be tightly scoped and procedural in nature.",
        disabled=performs_profiling,
    )
    improves_human = st.checkbox(
        "*(b)* The AI system only **improves the result of a previously completed human activity** "
        "— it does not replace or influence the prior human assessment",
        disabled=performs_profiling,
    )
    detects_patterns = st.checkbox(
        "*(c)* The AI system **detects decision-making patterns or deviations** from prior human "
        "assessments without replacing or influencing those assessments",
        disabled=performs_profiling,
    )
    preparatory_task = st.checkbox(
        "*(d)* The AI system performs **only a preparatory task** to an assessment relevant "
        "to the Annex III use cases listed in Section 4",
        disabled=performs_profiling,
    )

filter_inputs = {}
if filter_visible:
    filter_inputs = {
        "performs_profiling": performs_profiling,
        "narrow_procedural_task": narrow_procedural,
        "improves_completed_human_activity": improves_human,
        "detects_patterns_no_replacement": detects_patterns,
        "preparatory_task_only": preparatory_task,
    }
else:
    filter_inputs = {
        "performs_profiling": False,
        "narrow_procedural_task": False,
        "improves_completed_human_activity": False,
        "detects_patterns_no_replacement": False,
        "preparatory_task_only": False,
    }

st.divider()

# ----------------------------------------------------------------
# Classify button
# ----------------------------------------------------------------
_, btn_col, _ = st.columns([2, 2, 2])
with btn_col:
    classify_clicked = st.button(
        "⚖️  Classify this AI system",
        type="primary",
        use_container_width=True,
    )

if classify_clicked:
    assessment_input = AssessmentInput(
        uses_subliminal_manipulation=prohibited_checks["uses_subliminal_manipulation"],
        exploits_vulnerabilities=prohibited_checks["exploits_vulnerabilities"],
        social_scoring=prohibited_checks["social_scoring"],
        predictive_policing_profiling=prohibited_checks["predictive_policing_profiling"],
        untargeted_facial_scraping=prohibited_checks["untargeted_facial_scraping"],
        emotion_recognition_workplace_education=prohibited_checks[
            "emotion_recognition_workplace_education"
        ],
        biometric_categorisation_sensitive=prohibited_checks["biometric_categorisation_sensitive"],
        realtime_remote_biometric_id=prohibited_checks["realtime_remote_biometric_id"],
        is_safety_component_annex_i=is_safety_component,
        requires_third_party_conformity=requires_conformity,
        annex_iii_areas=selected_areas,
        performs_profiling=filter_inputs["performs_profiling"],
        narrow_procedural_task=filter_inputs["narrow_procedural_task"],
        improves_completed_human_activity=filter_inputs["improves_completed_human_activity"],
        detects_patterns_no_replacement=filter_inputs["detects_patterns_no_replacement"],
        preparatory_task_only=filter_inputs["preparatory_task_only"],
        is_regulated_fs_firm=is_regulated_fs,
        intended_purpose=intended_purpose,
    )

    st.session_state["result"] = classify(assessment_input)
    st.session_state["intended_purpose"] = intended_purpose
    st.session_state["organisation_name"] = organisation_name

# ----------------------------------------------------------------
# Result rendering
# ----------------------------------------------------------------
if "result" in st.session_state:
    result: AssessmentResult = st.session_state["result"]
    ip: str = st.session_state.get("intended_purpose", "")
    org: str = st.session_state.get("organisation_name", "")

    st.divider()
    st.header("Assessment result")

    # Tier colour mapping — Tolt palette
    tier_css = {
        RiskTier.PROHIBITED: ("tier-prohibited", "🚫", "#be123c"),
        RiskTier.HIGH_RISK:  ("tier-high",       "🔴", "#c2410c"),
        RiskTier.LIMITED:    ("tier-limited",     "◆",  "#4f46e5"),
        RiskTier.MINIMAL:    ("tier-minimal",     "✓",  "#15803d"),
    }
    css_class, icon, colour = tier_css[result.tier]

    st.markdown(
        f"""
        <div class="{css_class}">
            <h2 style="margin:0;color:{colour}">{icon} {result.tier.value.upper()}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Pathway
    st.subheader("Classification pathway")
    st.info(result.pathway)

    if result.article_citations:
        st.caption("**Relevant articles:** " + " · ".join(result.article_citations))

    # Obligations
    st.subheader("Obligations triggered")
    for ob in result.obligations:
        st.markdown(f"- {ob}")

    # Penalty
    st.subheader("Maximum penalty exposure")
    st.error(result.max_penalty, icon="⚖️")

    # CBI overlay
    if result.cbi_overlay:
        st.subheader("Central Bank of Ireland — 2026 Supervisory Overlay")
        st.markdown(
            "Your organisation is CBI-regulated. The following supervisory expectations "
            "apply in addition to EU AI Act obligations:"
        )
        for item in result.cbi_overlay:
            st.markdown(f"- {item}")

    # Next steps
    st.subheader("Recommended next steps")
    for step in result.next_steps:
        st.markdown(f"- {step}")

    # Art 6(3) filter note
    if result.filter_applied:
        st.success(
            "ℹ️ Article 6(3) exemption filter applied — this system is NOT classified as "
            "high-risk, but documentation (Art 6(4)) and registration (Art 49(2)) obligations remain.",
            icon="ℹ️",
        )

    # PDF download
    st.divider()
    st.subheader("Download report")
    pdf_bytes = generate_pdf(result, ip, org or None)
    st.download_button(
        label="📥  Download PDF report",
        data=pdf_bytes,
        file_name=f"eu-ai-act-assessment-{result.tier.name.lower()}.pdf",
        mime="application/pdf",
        use_container_width=False,
    )
    st.caption(
        "This report is a first-pass screen and does not constitute legal advice. "
        "Produced as a demonstration tool by Advaith A Bijoor for Tolt Innovations."
    )

# ----------------------------------------------------------------
# Footer
# ----------------------------------------------------------------
st.divider()
st.markdown(
    """
    <div style='text-align:center;color:#6b7a8c;font-size:0.8em;border-top:1px solid #e4dfd4;padding-top:16px;'>
    Sources: <a href='https://artificialintelligenceact.eu/article/5/' target='_blank'>EU AI Act Article 5</a> ·
    <a href='https://artificialintelligenceact.eu/article/6/' target='_blank'>Article 6</a> ·
    <a href='https://artificialintelligenceact.eu/annex/3/' target='_blank'>Annex III</a> ·
    <a href='https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems' target='_blank'>
    Commission draft guidelines (19 May 2026)</a> ·
    <a href='https://www.centralbank.ie/docs/default-source/publications/regulatory-and-supervisory-outlook-reports/regulatory-supervisory-outlook-report-2026.pdf' target='_blank'>
    CBI 2026 RSO</a>
    <br>Built for <a href='https://www.tolt.ie' target='_blank'>Tolt Innovations</a> by Advaith A Bijoor
    </div>
    """,
    unsafe_allow_html=True,
)
