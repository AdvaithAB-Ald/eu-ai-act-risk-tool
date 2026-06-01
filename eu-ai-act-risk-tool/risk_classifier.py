"""
EU AI Act Risk Classifier
Implements the Article 5/6 classification decision tree.

Sources:
  - EU AI Act Article 5 (Prohibited AI practices):
    https://artificialintelligenceact.eu/article/5/
  - EU AI Act Article 6 (Classification rules for high-risk AI):
    https://artificialintelligenceact.eu/article/6/
  - EU AI Act Annex III (High-risk AI systems):
    https://artificialintelligenceact.eu/annex/3/
  - EU AI Act Article 99 (Penalties):
    https://artificialintelligenceact.eu/article/99/
  - European Commission draft guidelines on Article 6 classification
    (published 19 May 2026, consultation open until 23 June 2026):
    https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems

This module is intentionally free of UI dependencies so it can be imported
into any application (e.g. a FastAPI service) independently of Streamlit.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class RiskTier(Enum):
    PROHIBITED = "Prohibited"
    HIGH_RISK = "High-risk"
    LIMITED = "Limited risk"
    MINIMAL = "Minimal risk"


@dataclass
class AssessmentInput:
    # ----------------------------------------------------------------
    # ARTICLE 5 — Prohibited AI practices
    # Any single YES → system is PROHIBITED
    # ----------------------------------------------------------------
    uses_subliminal_manipulation: bool = False
    # Art 5(1)(a): subliminal techniques beyond consciousness that materially
    # distort behaviour causing/likely causing significant harm

    exploits_vulnerabilities: bool = False
    # Art 5(1)(b): exploits vulnerabilities of specific groups (age, disability,
    # social/economic situation) causing/likely causing significant harm

    social_scoring: bool = False
    # Art 5(1)(c): social scoring by public authorities or on their behalf

    predictive_policing_profiling: bool = False
    # Art 5(1)(d): individual risk assessments for criminal offending based
    # solely on profiling or personality traits

    untargeted_facial_scraping: bool = False
    # Art 5(1)(e): scraping of facial images from internet/CCTV for recognition DBs

    emotion_recognition_workplace_education: bool = False
    # Art 5(1)(f): emotion recognition in workplace or educational institutions

    biometric_categorisation_sensitive: bool = False
    # Art 5(1)(g): biometric categorisation inferring sensitive attributes
    # (race, political opinions, trade union membership, religious/philosophical
    # beliefs, sex life/sexual orientation) — except lawfully acquired labelling

    realtime_remote_biometric_id: bool = False
    # Art 5(1)(h): real-time remote biometric identification in publicly
    # accessible spaces for law enforcement (narrow exceptions apply)

    # ----------------------------------------------------------------
    # ARTICLE 6(1) — Safety component of regulated product path
    # Both conditions must be TRUE → HIGH-RISK
    # ----------------------------------------------------------------
    is_safety_component_annex_i: bool = False
    # Art 6(1)(a): AI system is a safety component of, or itself a product
    # falling under EU harmonisation legislation listed in Annex I
    # (e.g. medical devices, machinery, toys, in vitro diagnostics)

    requires_third_party_conformity: bool = False
    # Art 6(1)(b): the product/safety component must undergo third-party
    # conformity assessment under the relevant Annex I legislation

    # ----------------------------------------------------------------
    # ARTICLE 6(2) — Annex III use case path
    # Non-empty list + filter check → HIGH-RISK or exempted
    # ----------------------------------------------------------------
    annex_iii_areas: list[str] = field(default_factory=list)
    # IDs from data/annex_iii.json matching the system's intended purpose.
    # e.g. ["employment", "essential_services"]

    # ----------------------------------------------------------------
    # ARTICLE 6(3) — High-risk exemption filter
    # (only relevant if annex_iii_areas is non-empty)
    # Applies if ANY condition is met AND performs_profiling is False.
    # Per Art 6(3), these must be interpreted NARROWLY.
    # Per Commission draft guidelines (19 May 2026), four conditions:
    # ----------------------------------------------------------------
    narrow_procedural_task: bool = False
    # Condition (a): AI performs a narrow procedural task only

    improves_completed_human_activity: bool = False
    # Condition (b): AI only improves the result of a previously completed
    # human activity (it does not replace or influence the prior assessment)

    detects_patterns_no_replacement: bool = False
    # Condition (c): AI detects decision-making patterns or deviations from
    # prior human assessments without replacing or influencing those assessments

    preparatory_task_only: bool = False
    # Condition (d): AI performs only a preparatory task to an assessment
    # relevant to the Annex III use cases

    performs_profiling: bool = False
    # BLOCKER: if the AI performs profiling of natural persons, none of the
    # Art 6(3) filter conditions apply — system remains HIGH-RISK. Art 6(3) last sentence.

    # ----------------------------------------------------------------
    # Context
    # ----------------------------------------------------------------
    is_regulated_fs_firm: bool = False
    # Whether the deploying organisation is a CBI-regulated financial services firm.
    # Triggers additional CBI 2026 RSO overlay in the output.

    intended_purpose: str = ""
    # Free-text description of what the AI system does.


@dataclass
class AssessmentResult:
    tier: RiskTier
    pathway: str
    article_citations: list[str]
    obligations: list[str]
    max_penalty: str
    cbi_overlay: Optional[list[str]]
    next_steps: list[str]
    filter_applied: bool = False
    # True when an Art 6(3) exemption reduced the classification from high-risk


# ----------------------------------------------------------------
# Helper builders
# ----------------------------------------------------------------

def _high_risk_result(pathway: str, annex_areas: list[str], is_fs: bool) -> AssessmentResult:
    """Shared builder for all HIGH-RISK outcomes."""
    citations = ["Article 6", "Article 9", "Article 10", "Article 11",
                 "Article 12", "Article 13", "Article 14", "Article 15",
                 "Article 99(4)"]

    obligations = [
        "Art 9 — Establish and maintain a risk management system throughout the lifecycle",
        "Art 10 — Implement data governance and management practices for training/validation/testing data",
        "Art 11 — Prepare and maintain technical documentation before placing on market",
        "Art 12 — Enable automatic logging of events (record-keeping) for traceability",
        "Art 13 — Ensure transparency and provision of information to deployers",
        "Art 14 — Design for effective human oversight — enable operators to monitor, override, or halt",
        "Art 15 — Achieve appropriate levels of accuracy, robustness, and cybersecurity",
        "Art 43 — Undergo conformity assessment before deployment",
        "Art 49 — Register in the EU public database of high-risk AI systems before deployment",
    ]

    # Art 99(4): up to €15M or 3% of worldwide annual turnover
    max_penalty = (
        "€15,000,000 or 3% of worldwide annual turnover (whichever is higher) "
        "for non-compliance with high-risk obligations — Article 99(4). "
        "Note: if any prohibited practice is also present, the threshold rises "
        "to €35,000,000 or 7% — Article 99(3)."
    )

    cbi_overlay = None
    if is_fs:
        cbi_overlay = [
            "CBI 2026 RSO: Model risk governance — document model purpose, data lineage, "
            "validation methodology, and performance metrics before deployment",
            "CBI 2026 RSO: Explainability — AI-driven decisions affecting customers must be "
            "interpretable and explainable to regulators and affected individuals",
            "CBI 2026 RSO: Human oversight — maintain clear human accountability for all "
            "AI-generated outputs; automated decisions must have defined escalation paths",
            "CBI 2026 RSO: Third-party AI accountability — firms remain fully accountable for "
            "outcomes generated by AI systems operated by third parties or vendors",
            "CBI 2026 RSO: Data quality — demonstrate fitness for purpose of training and "
            "input data, including bias assessment and ongoing monitoring",
        ]

    next_steps = [
        "1. Appoint an internal AI Compliance Lead or engage an external advisor",
        "2. Conduct a full risk management assessment per Article 9 before deployment",
        "3. Prepare technical documentation package per Article 11 (Annex IV checklist)",
        "4. Implement logging and record-keeping infrastructure per Article 12",
        "5. Register the system in the EU AI Act public database before go-live (Article 49)",
    ]

    return AssessmentResult(
        tier=RiskTier.HIGH_RISK,
        pathway=pathway,
        article_citations=citations,
        obligations=obligations,
        max_penalty=max_penalty,
        cbi_overlay=cbi_overlay,
        next_steps=next_steps,
    )


# ----------------------------------------------------------------
# Main classifier — follows the decision tree exactly
# ----------------------------------------------------------------

def classify(inp: AssessmentInput) -> AssessmentResult:
    """
    Classify an AI system under the EU AI Act risk framework.

    Decision tree:
      1. Article 5  — Prohibited?           → PROHIBITED (stop)
      2. Article 6(1) — Safety component?   → HIGH-RISK (stop)
      3. Article 6(2) — Annex III hit?      → proceed to filter
         3a. Article 6(3) filter applies?   → LIMITED (with documentation obligations)
         3b. Filter does not apply          → HIGH-RISK (stop)
      4. Default                            → LIMITED or MINIMAL
    """

    # ------------------------------------------------------------------
    # STEP 1: Article 5 — Prohibited practices
    # Any single flag → outright ban, max penalty 7% / €35M
    # ------------------------------------------------------------------
    prohibited_flags = {
        "subliminal manipulation (Art 5(1)(a))": inp.uses_subliminal_manipulation,
        "exploitation of vulnerabilities (Art 5(1)(b))": inp.exploits_vulnerabilities,
        "social scoring (Art 5(1)(c))": inp.social_scoring,
        "predictive policing via profiling alone (Art 5(1)(d))": inp.predictive_policing_profiling,
        "untargeted facial image scraping (Art 5(1)(e))": inp.untargeted_facial_scraping,
        "emotion recognition in workplace/education (Art 5(1)(f))": inp.emotion_recognition_workplace_education,
        "biometric categorisation by sensitive attributes (Art 5(1)(g))": inp.biometric_categorisation_sensitive,
        "real-time remote biometric ID in public spaces (Art 5(1)(h))": inp.realtime_remote_biometric_id,
    }

    triggered = [label for label, flag in prohibited_flags.items() if flag]

    if triggered:
        return AssessmentResult(
            tier=RiskTier.PROHIBITED,
            pathway=(
                f"Article 5 — Prohibited AI practice: {'; '.join(triggered)}. "
                "This system cannot legally be placed on the EU market or put into service."
            ),
            article_citations=["Article 5", "Article 99(3)"],
            obligations=[
                "Do not deploy, market, or put this system into service in the EU — Article 5",
                "Notify the relevant national supervisory authority if the system is already deployed",
                "Conduct an immediate risk mitigation review to determine whether the system "
                "can be redesigned to remove the prohibited characteristic",
            ],
            max_penalty=(
                "€35,000,000 or 7% of worldwide annual turnover (whichever is higher) "
                "— Article 99(3). The highest penalty tier under the EU AI Act."
            ),
            cbi_overlay=(
                [
                    "CBI 2026 RSO: Immediate escalation to Board and Compliance required. "
                    "Regulatory notification to Central Bank of Ireland likely required "
                    "under existing model risk and conduct obligations.",
                ]
                if inp.is_regulated_fs_firm
                else None
            ),
            next_steps=[
                "1. Halt deployment immediately if system is live",
                "2. Engage legal counsel specialising in EU AI Act compliance",
                "3. Notify senior leadership and Board-level governance",
                "4. Assess whether a redesigned system can remove the prohibited element",
                "5. Engage national market surveillance authority proactively",
            ],
        )

    # ------------------------------------------------------------------
    # STEP 2: Article 6(1) — Safety component of Annex I regulated product
    # Both conditions must be true.
    # ------------------------------------------------------------------
    if inp.is_safety_component_annex_i and inp.requires_third_party_conformity:
        return _high_risk_result(
            pathway=(
                "Article 6(1) — The AI system is a safety component of (or is itself) "
                "a product covered by EU harmonisation legislation listed in Annex I "
                "(e.g. medical devices, machinery, toys, in vitro diagnostics), and that "
                "product requires third-party conformity assessment. Classified HIGH-RISK."
            ),
            annex_areas=[],
            is_fs=inp.is_regulated_fs_firm,
        )

    # ------------------------------------------------------------------
    # STEP 3: Article 6(2) — Annex III use case
    # ------------------------------------------------------------------
    if inp.annex_iii_areas:
        # STEP 4: Article 6(3) — High-risk exemption filter
        # All four conditions must be interpreted NARROWLY per Art 6(3).
        # BLOCKER: profiling of natural persons disables the filter entirely.
        filter_conditions_met = any([
            inp.narrow_procedural_task,
            inp.improves_completed_human_activity,
            inp.detects_patterns_no_replacement,
            inp.preparatory_task_only,
        ])

        if filter_conditions_met and not inp.performs_profiling:
            # Filter applies → NOT classified as high-risk
            # But provider must document the assessment (Art 6(4)) and
            # register it in the EU database under Art 49(2).
            return AssessmentResult(
                tier=RiskTier.LIMITED,
                pathway=(
                    f"Annex III area(s) matched: {', '.join(inp.annex_iii_areas)}. "
                    "However, Article 6(3) exemption filter applies — the system meets "
                    "one or more narrow-task conditions and does not perform profiling of "
                    "natural persons. NOT classified as high-risk. "
                    "Note: per the Commission's draft guidelines (19 May 2026), "
                    "these conditions must be interpreted narrowly."
                ),
                article_citations=["Article 6(2)", "Article 6(3)", "Article 6(4)", "Article 49(2)"],
                obligations=[
                    "Art 6(4) — Document why the Article 6(3) filter applies; retain this "
                    "assessment and make it available to national competent authorities on request",
                    "Art 49(2) — Register the system in the EU AI Act public database",
                    "Art 50 — Apply transparency obligations where the system interacts "
                    "with natural persons or generates synthetic content",
                    "Ongoing — Monitor Commission finalisation of Article 6 guidelines "
                    "(consultation closes 23 June 2026) to confirm exemption remains valid",
                ],
                max_penalty=(
                    "Up to €7,500,000 or 1% of worldwide annual turnover for providing "
                    "incorrect or misleading information to authorities — Article 99(5). "
                    "Lower than high-risk tier, but documentation obligations are mandatory."
                ),
                cbi_overlay=(
                    [
                        "CBI 2026 RSO: Even where EU AI Act high-risk classification is exempted, "
                        "CBI supervisory expectations on model governance, explainability, and "
                        "human oversight apply independently under Irish financial services law.",
                        "CBI 2026 RSO: Third-party AI accountability remains — the firm cannot "
                        "transfer responsibility to a vendor by citing Art 6(3) exemption.",
                    ]
                    if inp.is_regulated_fs_firm
                    else None
                ),
                next_steps=[
                    "1. Prepare and retain Article 6(4) documentation explaining the exemption",
                    "2. Register in the EU AI Act public database (Article 49(2))",
                    "3. Apply transparency disclosures per Article 50",
                    "4. Monitor Commission guidelines finalisation (23 June 2026 consultation close)",
                    "5. Review classification annually or whenever the system's intended purpose changes",
                ],
                filter_applied=True,
            )

        # Filter does not apply (or profiling blocks it) → HIGH-RISK confirmed
        profiling_note = (
            " Note: Article 6(3) filter was unavailable because the system performs "
            "profiling of natural persons — this is an explicit blocker under Article 6(3)."
            if inp.performs_profiling
            else ""
        )

        return _high_risk_result(
            pathway=(
                f"Article 6(2) — Annex III area(s): {', '.join(inp.annex_iii_areas)}. "
                "No Article 6(3) exemption filter condition met." + profiling_note
            ),
            annex_areas=inp.annex_iii_areas,
            is_fs=inp.is_regulated_fs_firm,
        )

    # ------------------------------------------------------------------
    # STEP 5: Default — no prohibited or high-risk triggers
    # Classify as LIMITED (if interacts with humans) or MINIMAL
    # ------------------------------------------------------------------
    return AssessmentResult(
        tier=RiskTier.MINIMAL,
        pathway=(
            "No Article 5 prohibited practices, no Article 6(1) safety-component match, "
            "and no Annex III use cases identified. Classified as MINIMAL risk. "
            "If the system interacts directly with natural persons or generates synthetic "
            "content, LIMITED risk transparency obligations apply under Article 50."
        ),
        article_citations=["Article 50"],
        obligations=[
            "Art 50 — If the system interacts with natural persons: disclose that they "
            "are interacting with an AI system (unless obvious from context)",
            "Art 50 — If the system generates synthetic audio/video/image/text intended "
            "to appear authentic: label it as AI-generated",
            "Maintain basic internal records of the system's purpose, data inputs, "
            "and operational boundaries as good governance practice",
        ],
        max_penalty=(
            "No mandatory conformity assessment or registration. "
            "Transparency obligation breaches under Art 50 subject to penalties "
            "set by each EU member state."
        ),
        cbi_overlay=(
            [
                "CBI 2026 RSO: AI systems at minimal EU AI Act risk level may still attract "
                "CBI supervisory scrutiny if they affect regulated activities or customer outcomes.",
                "CBI 2026 RSO: Maintain basic model documentation and governance even for "
                "low-risk systems — supervisory expectation applies regardless of EU AI Act tier.",
            ]
            if inp.is_regulated_fs_firm
            else None
        ),
        next_steps=[
            "1. Apply Article 50 transparency disclosures if the system interacts with users",
            "2. Maintain basic internal documentation of the system's purpose and data inputs",
            "3. Schedule periodic reviews if the system's intended purpose expands",
            "4. Monitor EU AI Act guidance updates — low-risk designation can change if use case evolves",
            "5. Check CBI supervisory expectations separately if operating in regulated FS",
        ],
    )
