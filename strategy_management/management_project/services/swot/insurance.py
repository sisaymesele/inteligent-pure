from .default import DEFAULT_SWOT

INSURANCE_SWOT = {
    "Strength": {
        **DEFAULT_SWOT["Strength"],

        "Capital & Solvency Strength": [
            "High solvency ratio exceeding regulatory requirements",
            "Strong capital reserves and risk buffers",
            "Effective reinsurance arrangements",
            "Robust investment portfolio management",
            "Stable underwriting capital allocation",
            "Efficient risk-based capital planning",
            "Diversified asset-liability management",
            "Strong regulatory compliance track record",
            "High financial resilience to market shocks",
            "Effective contingency planning for large claims"
        ],
        "Underwriting & Risk Management Excellence": [
            "Comprehensive risk assessment frameworks",
            "Diversified product portfolio across life, health, and property",
            "Strong actuarial analysis capabilities",
            "Effective claims risk mitigation strategies",
            "Advanced fraud detection mechanisms",
            "High customer retention due to reliable coverage",
            "Accurate pricing and rating models",
            "Robust catastrophe modeling capabilities",
            "Strong underwriting guidelines and compliance",
            "Proactive portfolio monitoring"
        ],

    },

    "Weakness": {
        **DEFAULT_SWOT["Weakness"],

        "Claims & Risk Exposure Weaknesses": [
            "High claims processing cycle time",
            "Low efficiency in complex claims handling",
            "Under-reserved risk exposures",
            "Limited catastrophe risk coverage",
            "High exposure to specific market segments",
            "Gaps in fraud detection capabilities",
            "Limited actuarial talent in niche areas",
            "Reactive risk management approach",
            "Slow claims adjustment processes",
            "Limited data-driven underwriting insights"
        ],
        "Underwriting & Risk Management Gaps": [
            "Incomplete or outdated risk assessment frameworks",
            "Limited diversification in product portfolio",
            "Insufficient actuarial analysis capabilities",
            "Weak claims risk mitigation strategies",
            "Inadequate fraud detection mechanisms",
            "Low customer retention in some segments",
            "Pricing and rating models not fully accurate",
            "Weak catastrophe modeling and preparedness",
            "Gaps in underwriting guidelines compliance",
            "Reactive portfolio monitoring and reporting"
        ],

    },

    "Opportunity": {
        **DEFAULT_SWOT["Opportunity"],
    },

    "Threat": {
        **DEFAULT_SWOT["Threat"],
    }
}
