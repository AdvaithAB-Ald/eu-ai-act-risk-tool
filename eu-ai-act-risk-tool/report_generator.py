"""
PDF report generator for the EU AI Act Risk Self-Assessment Tool.
Uses ReportLab to produce a professional, Tolt-branded output.

Source: ReportLab documentation — https://docs.reportlab.com/
"""

from datetime import date
from io import BytesIO
from typing import Optional

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from risk_classifier import AssessmentResult, RiskTier

# ----------------------------------------------------------------
# Tolt brand colours — sourced from tolt.ie CSS variables
# --bg:#f6f4ef  --ink:#0b1b2b  --accent:#4f46e5  --line:#e4dfd4
# ----------------------------------------------------------------
TOLT_DARK   = colors.HexColor("#0b1b2b")   # --ink
TOLT_ACCENT = colors.HexColor("#4f46e5")   # --accent (indigo)
TOLT_BG     = colors.HexColor("#f6f4ef")   # --bg (warm cream)
TOLT_LINE   = colors.HexColor("#e4dfd4")   # --line (border)
TOLT_MUTED  = colors.HexColor("#6b7a8c")   # --muted

TIER_COLOURS = {
    RiskTier.PROHIBITED: colors.HexColor("#be123c"),   # rose-700
    RiskTier.HIGH_RISK:  colors.HexColor("#c2410c"),   # orange-700
    RiskTier.LIMITED:    colors.HexColor("#4f46e5"),   # Tolt indigo
    RiskTier.MINIMAL:    colors.HexColor("#15803d"),   # green-700
}

TIER_BG = {
    RiskTier.PROHIBITED: colors.HexColor("#fff0f0"),
    RiskTier.HIGH_RISK:  colors.HexColor("#fff7ed"),
    RiskTier.LIMITED:    colors.HexColor("#eeeafe"),   # --accent-soft
    RiskTier.MINIMAL:    colors.HexColor("#f0fdf4"),
}


def _build_styles() -> dict:
    base = getSampleStyleSheet()

    styles = {}

    styles["title"] = ParagraphStyle(
        "title",
        parent=base["Title"],
        fontSize=22,
        textColor=TOLT_DARK,
        spaceAfter=4,
        fontName="Helvetica-Bold",
    )
    styles["subtitle"] = ParagraphStyle(
        "subtitle",
        parent=base["Normal"],
        fontSize=10,
        textColor=colors.HexColor("#555555"),
        spaceAfter=2,
    )
    styles["section_head"] = ParagraphStyle(
        "section_head",
        parent=base["Heading2"],
        fontSize=13,
        textColor=TOLT_DARK,
        spaceBefore=14,
        spaceAfter=4,
        fontName="Helvetica-Bold",
        borderPad=0,
    )
    styles["body"] = ParagraphStyle(
        "body",
        parent=base["Normal"],
        fontSize=10,
        leading=15,
        textColor=TOLT_DARK,
        spaceAfter=6,
    )
    styles["bullet"] = ParagraphStyle(
        "bullet",
        parent=base["Normal"],
        fontSize=10,
        leading=15,
        leftIndent=14,
        bulletIndent=4,
        textColor=TOLT_DARK,
        spaceAfter=3,
    )
    styles["tier_label"] = ParagraphStyle(
        "tier_label",
        parent=base["Normal"],
        fontSize=16,
        fontName="Helvetica-Bold",
        spaceAfter=4,
        alignment=TA_CENTER,
    )
    styles["footer"] = ParagraphStyle(
        "footer",
        parent=base["Normal"],
        fontSize=8,
        textColor=colors.HexColor("#888888"),
        alignment=TA_CENTER,
    )
    styles["article"] = ParagraphStyle(
        "article",
        parent=base["Normal"],
        fontSize=9,
        textColor=colors.HexColor("#444444"),
        leading=14,
        leftIndent=10,
        spaceAfter=2,
    )

    return styles


def generate_pdf(
    result: AssessmentResult,
    intended_purpose: str,
    organisation_name: Optional[str] = None,
) -> bytes:
    """
    Generate a Tolt-branded PDF report for the given assessment result.

    Returns raw PDF bytes suitable for a Streamlit download_button.
    """
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2 * cm,
        bottomMargin=2.5 * cm,
    )

    styles = _build_styles()
    story = []

    # ----------------------------------------------------------------
    # Header
    # ----------------------------------------------------------------
    story.append(Paragraph("EU AI Act", styles["subtitle"]))
    story.append(Paragraph("Risk Self-Assessment Report", styles["title"]))
    story.append(Paragraph(
        f"Prepared by Tolt Innovations Demonstration Tool · {date.today().strftime('%d %B %Y')}",
        styles["subtitle"],
    ))
    story.append(HRFlowable(width="100%", thickness=1.5, color=TOLT_ACCENT, spaceAfter=12))  # indigo rule

    # Organisation + purpose
    if organisation_name:
        story.append(Paragraph(f"<b>Organisation:</b> {organisation_name}", styles["body"]))
    story.append(Paragraph(f"<b>AI system description:</b> {intended_purpose or '(not provided)'}", styles["body"]))
    story.append(Spacer(1, 6))

    # ----------------------------------------------------------------
    # Risk tier banner
    # ----------------------------------------------------------------
    tier_colour = TIER_COLOURS.get(result.tier, colors.grey)
    tier_bg = TIER_BG.get(result.tier, colors.HexColor("#F5F5F5"))

    tier_table = Table(
        [[Paragraph(
            f"<font color='{tier_colour.hexval()}'>■</font>  "
            f"<b>{result.tier.value.upper()}</b>",
            styles["tier_label"],
        )]],
        colWidths=["100%"],
    )
    tier_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), tier_bg),
        ("BOX", (0, 0), (-1, -1), 1.5, tier_colour),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [tier_bg]),
    ]))
    story.append(tier_table)
    story.append(Spacer(1, 10))

    # ----------------------------------------------------------------
    # Classification pathway
    # ----------------------------------------------------------------
    story.append(Paragraph("Classification pathway", styles["section_head"]))
    story.append(Paragraph(result.pathway, styles["body"]))

    # Article citations
    if result.article_citations:
        story.append(Paragraph(
            "<b>Relevant articles:</b> " + " · ".join(result.article_citations),
            styles["body"],
        ))

    # ----------------------------------------------------------------
    # Obligations triggered
    # ----------------------------------------------------------------
    story.append(Paragraph("Obligations triggered", styles["section_head"]))
    for obligation in result.obligations:
        story.append(Paragraph(f"• {obligation}", styles["bullet"]))

    # ----------------------------------------------------------------
    # Penalty exposure
    # ----------------------------------------------------------------
    story.append(Paragraph("Maximum penalty exposure", styles["section_head"]))
    story.append(Paragraph(result.max_penalty, styles["body"]))

    # ----------------------------------------------------------------
    # CBI overlay (if applicable)
    # ----------------------------------------------------------------
    if result.cbi_overlay:
        story.append(Paragraph(
            "Central Bank of Ireland — 2026 Supervisory Overlay",
            styles["section_head"],
        ))
        story.append(Paragraph(
            "Your organisation is identified as a CBI-regulated financial services firm. "
            "The following supervisory expectations apply in addition to EU AI Act obligations:",
            styles["body"],
        ))
        for item in result.cbi_overlay:
            story.append(Paragraph(f"• {item}", styles["bullet"]))

    # ----------------------------------------------------------------
    # Recommended next steps
    # ----------------------------------------------------------------
    story.append(Paragraph("Recommended next steps", styles["section_head"]))
    for step in result.next_steps:
        story.append(Paragraph(step, styles["bullet"]))

    # ----------------------------------------------------------------
    # Sources & footer
    # ----------------------------------------------------------------
    story.append(HRFlowable(width="100%", thickness=0.5, color=TOLT_LINE, spaceBefore=16, spaceAfter=8))
    story.append(Paragraph(
        "<b>Key sources:</b> EU AI Act (Regulation (EU) 2024/1689) · "
        "European Commission draft Article 6 classification guidelines (19 May 2026) · "
        "Central Bank of Ireland Regulatory & Supervisory Outlook 2026",
        styles["article"],
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "This report is a first-pass screen and does not constitute legal advice. "
        "It was prepared as a demonstration tool by Advaith A Bijoor for Tolt Innovations. "
        "Organisations should engage qualified legal and compliance advisors before making "
        "deployment decisions based on this output.",
        styles["footer"],
    ))

    doc.build(story)
    return buffer.getvalue()
