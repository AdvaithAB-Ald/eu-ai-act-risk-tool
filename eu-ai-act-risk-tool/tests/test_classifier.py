"""
Unit tests for the EU AI Act risk classifier.

These tests double as living documentation of key classification decisions.
They should be readable by a compliance professional, not just a developer.

Run with: pytest tests/test_classifier.py -v
"""

import pytest
from risk_classifier import AssessmentInput, RiskTier, classify


def _base() -> AssessmentInput:
    """Return a minimal input with all flags False — default is MINIMAL risk."""
    return AssessmentInput()


# ----------------------------------------------------------------
# Test 1: Prohibited — subliminal manipulation
# Article 5(1)(a)
# ----------------------------------------------------------------
def test_subliminal_manipulation_is_prohibited():
    """
    An AI system that uses subliminal techniques beyond consciousness to
    distort behaviour must be classified PROHIBITED under Article 5(1)(a),
    regardless of any other factors.
    """
    inp = _base()
    inp.uses_subliminal_manipulation = True
    result = classify(inp)

    assert result.tier == RiskTier.PROHIBITED
    assert "Article 5" in result.article_citations
    assert "Article 99(3)" in result.article_citations
    assert "35,000,000" in result.max_penalty or "7%" in result.max_penalty


# ----------------------------------------------------------------
# Test 2: High-risk — credit scoring via Annex III (essential services)
# Article 6(2), Annex III(5)
# ----------------------------------------------------------------
def test_credit_scoring_for_natural_persons_is_high_risk_via_annex_iii():
    """
    An AI system used for credit scoring or creditworthiness evaluation of
    natural persons falls under Annex III(5) (essential private services)
    and must be classified HIGH-RISK under Article 6(2).
    """
    inp = _base()
    inp.annex_iii_areas = ["essential_services"]
    inp.intended_purpose = "Credit scoring model for retail bank loan applications"
    result = classify(inp)

    assert result.tier == RiskTier.HIGH_RISK
    assert any("6" in c for c in result.article_citations)
    assert any("Art 9" in ob for ob in result.obligations)
    assert any("Art 14" in ob for ob in result.obligations)


# ----------------------------------------------------------------
# Test 3: High-risk — medical device AI via Article 6(1) safety component
# Article 6(1)(a) + (b)
# ----------------------------------------------------------------
def test_medical_device_ai_is_high_risk_via_article_6_1():
    """
    An AI system that is a safety component of a medical device (covered by
    EU MDR under Annex I of the AI Act) that requires third-party conformity
    assessment must be classified HIGH-RISK under Article 6(1).
    This path is independent of Annex III.
    """
    inp = _base()
    inp.is_safety_component_annex_i = True
    inp.requires_third_party_conformity = True
    result = classify(inp)

    assert result.tier == RiskTier.HIGH_RISK
    assert "Article 6" in result.article_citations or any(
        "6" in c for c in result.article_citations
    )


# ----------------------------------------------------------------
# Test 4: Profiling blocks Article 6(3) filter — stays HIGH-RISK
# Article 6(3) last sentence
# ----------------------------------------------------------------
def test_recruitment_ai_with_profiling_cannot_use_filter_exemption():
    """
    A recruitment AI that matches an Annex III(4) employment use case AND
    performs profiling of natural persons cannot use the Article 6(3) filter
    — the profiling blocker explicitly disables all filter conditions.
    The system must remain HIGH-RISK even if a narrow-task condition is met.
    """
    inp = _base()
    inp.annex_iii_areas = ["employment"]
    inp.performs_profiling = True
    inp.narrow_procedural_task = True  # would otherwise qualify for filter
    result = classify(inp)

    assert result.tier == RiskTier.HIGH_RISK
    assert result.filter_applied is False


# ----------------------------------------------------------------
# Test 5: Minimal risk — generic product recommendation chatbot
# ----------------------------------------------------------------
def test_marketing_chatbot_is_minimal_risk():
    """
    A general product recommendation chatbot for a retailer does not match
    any Article 5 prohibited practices, is not a safety component under
    Annex I, and does not fall into any Annex III use case area.
    It should be classified MINIMAL risk.
    """
    inp = _base()
    inp.intended_purpose = "Product recommendation chatbot for e-commerce retailer"
    result = classify(inp)

    assert result.tier == RiskTier.MINIMAL
    assert "Article 50" in result.article_citations


# ----------------------------------------------------------------
# Test 6: Article 6(3) filter applies — reduces to LIMITED
# Article 6(2) + 6(3) + 6(4)
# ----------------------------------------------------------------
def test_preparatory_task_ai_gets_filter_exemption():
    """
    An AI system that falls under an Annex III area but only performs a
    preparatory task (condition (d)) and does NOT perform profiling should
    have the Article 6(3) filter applied, reducing its classification from
    HIGH-RISK to LIMITED, with documentation obligations under Art 6(4).
    """
    inp = _base()
    inp.annex_iii_areas = ["employment"]
    inp.preparatory_task_only = True
    inp.performs_profiling = False
    result = classify(inp)

    assert result.tier == RiskTier.LIMITED
    assert result.filter_applied is True
    assert any("6(4)" in c for c in result.article_citations)
    assert any("49(2)" in c for c in result.article_citations)


# ----------------------------------------------------------------
# Test 7: CBI overlay appears for regulated FS firms
# ----------------------------------------------------------------
def test_cbi_overlay_present_for_regulated_fs_firm():
    """
    When is_regulated_fs_firm is True, the assessment result should include
    a non-empty CBI overlay with Central Bank of Ireland supervisory guidance,
    for both high-risk and minimal-risk classifications.
    """
    inp = _base()
    inp.is_regulated_fs_firm = True
    result = classify(inp)

    assert result.cbi_overlay is not None
    assert len(result.cbi_overlay) > 0
    assert any("CBI" in item for item in result.cbi_overlay)


# ----------------------------------------------------------------
# Test 8: No CBI overlay for non-FS organisations
# ----------------------------------------------------------------
def test_no_cbi_overlay_for_non_fs_firm():
    """
    When is_regulated_fs_firm is False, the CBI overlay should be None.
    """
    inp = _base()
    inp.is_regulated_fs_firm = False
    result = classify(inp)

    assert result.cbi_overlay is None
