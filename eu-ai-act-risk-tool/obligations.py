"""
Obligations and penalty reference data for EU AI Act risk tiers.

This module exists as a standalone reference so the mapping between risk
tier and legal obligations can be maintained independently of classifier logic.

Source: EU AI Act Articles 9-15, 50, 99
https://artificialintelligenceact.eu/
"""

from risk_classifier import RiskTier

OBLIGATIONS_MAP: dict[RiskTier, dict] = {
    RiskTier.PROHIBITED: {
        "summary": "System is banned. Cannot be placed on the EU market or put into service.",
        "articles": [
            {
                "article": "Article 5",
                "title": "Prohibited AI practices",
                "obligation": "Do not deploy, market, or put the system into service in the EU.",
            },
            {
                "article": "Article 99(3)",
                "title": "Penalty — prohibited practices",
                "obligation": (
                    "Maximum penalty: €35,000,000 or 7% of worldwide annual turnover "
                    "(whichever is higher)."
                ),
            },
        ],
    },
    RiskTier.HIGH_RISK: {
        "summary": (
            "Full EU AI Act compliance regime applies before deployment. "
            "Conformity assessment and EU database registration are mandatory."
        ),
        "articles": [
            {
                "article": "Article 9",
                "title": "Risk management system",
                "obligation": (
                    "Establish, implement, document, and maintain a risk management system "
                    "throughout the entire lifecycle of the high-risk AI system."
                ),
            },
            {
                "article": "Article 10",
                "title": "Data and data governance",
                "obligation": (
                    "Apply data governance practices covering training, validation, and testing "
                    "datasets. Data must be relevant, representative, free of errors, and complete "
                    "to the extent possible. Bias assessment required."
                ),
            },
            {
                "article": "Article 11",
                "title": "Technical documentation",
                "obligation": (
                    "Draw up and maintain technical documentation (Annex IV checklist) before "
                    "placing the system on the market. Must be available to national authorities."
                ),
            },
            {
                "article": "Article 12",
                "title": "Record-keeping and logging",
                "obligation": (
                    "Ensure the system automatically generates logs throughout operation "
                    "to the extent technically feasible. Logs must support traceability of outputs."
                ),
            },
            {
                "article": "Article 13",
                "title": "Transparency and information",
                "obligation": (
                    "Provide deployers with clear instructions for use, including capabilities, "
                    "limitations, accuracy metrics, human oversight measures, and technical means."
                ),
            },
            {
                "article": "Article 14",
                "title": "Human oversight",
                "obligation": (
                    "Design and build the system to allow effective human oversight. "
                    "Operators must be able to understand capabilities/limitations, monitor "
                    "operation, override or halt the system as appropriate."
                ),
            },
            {
                "article": "Article 15",
                "title": "Accuracy, robustness, cybersecurity",
                "obligation": (
                    "Achieve and maintain appropriate levels of accuracy for intended purpose. "
                    "Implement resilience against errors, faults, and adversarial attacks."
                ),
            },
            {
                "article": "Article 43",
                "title": "Conformity assessment",
                "obligation": (
                    "Conduct a conformity assessment procedure before placing on market. "
                    "For most Annex III systems this is a self-assessment against Annex VI "
                    "or Annex VII; some require third-party notified body involvement."
                ),
            },
            {
                "article": "Article 49",
                "title": "EU database registration",
                "obligation": (
                    "Register the high-risk AI system in the EU AI Act public database "
                    "before placing on the market or putting into service."
                ),
            },
            {
                "article": "Article 99(4)",
                "title": "Penalty — high-risk obligations",
                "obligation": (
                    "Maximum penalty for non-compliance with high-risk obligations: "
                    "€15,000,000 or 3% of worldwide annual turnover (whichever is higher)."
                ),
            },
        ],
    },
    RiskTier.LIMITED: {
        "summary": (
            "Transparency obligations apply. If Annex III use case identified but "
            "Article 6(3) filter applied, documentation and registration still required."
        ),
        "articles": [
            {
                "article": "Article 50",
                "title": "Transparency obligations",
                "obligation": (
                    "Notify natural persons when they are interacting with an AI system "
                    "(unless this is obvious from context). Label AI-generated synthetic "
                    "content (audio, video, image, text) as artificially generated."
                ),
            },
            {
                "article": "Article 6(4)",
                "title": "Documentation of Article 6(3) assessment",
                "obligation": (
                    "Where Article 6(3) exemption filter is applied: document the assessment "
                    "in writing and make it available to national competent authorities on request."
                ),
            },
            {
                "article": "Article 49(2)",
                "title": "EU database registration (Article 6(3) systems)",
                "obligation": (
                    "Register the system in the EU AI Act public database before deployment, "
                    "even where the Article 6(3) filter applies."
                ),
            },
            {
                "article": "Article 99(5)",
                "title": "Penalty — incorrect information",
                "obligation": (
                    "Penalty for providing incorrect, incomplete, or misleading information "
                    "to national authorities: up to €7,500,000 or 1% of worldwide annual turnover."
                ),
            },
        ],
    },
    RiskTier.MINIMAL: {
        "summary": (
            "No mandatory conformity assessment or EU database registration. "
            "Article 50 transparency obligations apply where the system interacts "
            "with natural persons or generates synthetic content."
        ),
        "articles": [
            {
                "article": "Article 50",
                "title": "Transparency obligations",
                "obligation": (
                    "If the system interacts with natural persons: disclose that it is an AI "
                    "system unless this is obvious from context. "
                    "If the system generates AI-produced content: mark it as such."
                ),
            },
        ],
    },
}


PENALTY_SUMMARY: dict[RiskTier, str] = {
    RiskTier.PROHIBITED: "€35M or 7% global turnover — Article 99(3)",
    RiskTier.HIGH_RISK: "€15M or 3% global turnover — Article 99(4)",
    RiskTier.LIMITED: "€7.5M or 1% global turnover (incorrect info to authorities) — Article 99(5)",
    RiskTier.MINIMAL: "Member-state penalties for Art 50 breaches — amounts vary by jurisdiction",
}


def get_obligations(tier: RiskTier) -> dict:
    """Return the obligations mapping for a given risk tier."""
    return OBLIGATIONS_MAP.get(tier, {})


def get_penalty_summary(tier: RiskTier) -> str:
    """Return the one-line penalty summary for a given risk tier."""
    return PENALTY_SUMMARY.get(tier, "Unknown tier")
