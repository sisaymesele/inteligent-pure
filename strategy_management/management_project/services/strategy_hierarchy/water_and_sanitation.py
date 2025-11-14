
from management_project.services.strategy_hierarchy.default import DEFAULT_PERSPECTIVE



WATER_AND_SANITATION_PERSPECTIVE = {
    # ----------------------------- FINANCIAL PERSPECTIVE -----------------------------
    "Financial Perspective": {
        **DEFAULT_PERSPECTIVE["Financial Perspective"],

    },

    # ----------------------------- CUSTOMER PERSPECTIVE -----------------------------
    "Customer Perspective": {
        **DEFAULT_PERSPECTIVE["Customer Perspective"],

        # -------------------- 1. Service Quality & Reliability --------------------
        "Water Service Quality": {
            "Ensure 24/7 Water Supply": {
                "Continuity of supply (hours/day)": "Average supply duration",
                "Customer interruption frequency": "Average service disruptions per customer/year",
                "Service coverage (%)": "Population served / Total population * 100",
                "Customer complaints on supply (%)": "Supply complaints / Total complaints * 100"
            },
            "Improve Water Quality Standards": {
                "Compliance with national standards (%)": "Tests meeting standards / Total tests * 100",
                "Water quality testing frequency": "Tests conducted per month",
                "Customer satisfaction on water quality (%)": "Survey satisfaction score",
                "Response time to water quality issues (hrs)": "Average time to address contamination"
            }
        },

        # -------------------- 2. Sanitation Service & Hygiene Improvement --------------------
        "Sanitation Service Delivery": {
            "Expand Sanitation Coverage": {
                "Sanitation service coverage (%)": "Population served / Total population * 100",
                "New sanitation connections (#)": "Newly connected households",
                "Wastewater treated (%)": "Volume treated / Volume collected * 100",
                "Reuse of treated wastewater (%)": "Volume reused / Volume treated * 100"
            },
            "Promote Hygiene & Public Awareness": {
                "Awareness campaigns conducted (#)": "Community hygiene programs per year",
                "Community participation rate (%)": "Participants / Target population * 100",
                "Schools with hygiene programs (%)": "Schools with WASH activities / Total schools * 100",
                "Improvement in hygiene behavior (%)": "Pre vs post intervention change"
            }
        },


        # -------------------- 3. Environmental & Social Responsibility --------------------
        "Environmental & Social Responsibility": {
            "Promote Environmental Sustainability": {
                "CO₂ emissions per m³": "Total CO₂ emissions / Water produced",
                "Wastewater safely disposed (%)": "Volume safely disposed / Total wastewater * 100",
                "Sludge reused or treated (%)": "Volume treated / Total generated * 100",
                "Green initiatives implemented (#)": "Number of environmental initiatives"
            },
            "Enhance Community Social Impact": {
                "Low-income households supported (%)": "Beneficiaries / Total customers * 100",
                "Water affordability index": "Average tariff / Median household income",
                "Community satisfaction level (%)": "Survey satisfaction rating",
                "CSR investment in WASH ($)": "Funds allocated to social initiatives"
            }
        },
    },
    "Internal Process Perspective": {
        **DEFAULT_PERSPECTIVE["Internal Process Perspective"],
    },
    "Learning & Growth Perspective": {
        **DEFAULT_PERSPECTIVE["Learning & Growth Perspective"],
    },
}
