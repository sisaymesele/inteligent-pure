from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE

WATER_AND_SANITATION_PERSPECTIVE = {
    # ----------------------------- FINANCIAL PERSPECTIVE -----------------------------
    "Financial Perspective": {
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],

        # -------------------- 1. Revenue Growth & Diversification --------------------
        "Water Revenue Growth & Diversification": {
            "Increase Water Sales Revenue": {
                "Revenue growth rate (%)": "(Current - Previous) / Previous * 100",
                "Average revenue per m³": "Total water revenue / Total volume sold",
                "Customer collection efficiency (%)": "Revenue collected / Revenue billed * 100",
                "Unbilled consumption ratio (%)": "Unbilled volume / Total production * 100"
            },
            "Expand Non-Tariff Revenue Streams": {
                "Revenue from sanitation fees ($)": "Total collected from sanitation services",
                "Revenue from industrial users ($)": "Income from commercial/industrial clients",
                "Revenue from recycled water ($)": "Income from treated wastewater reuse",
                "Revenue from consulting & laboratory services ($)": "Service-based income"
            }
        },

        # -------------------- 2. Cost Efficiency & Resource Optimization --------------------
        "Operational Cost Optimization": {
            "Reduce Energy Cost per m³": {
                "Energy cost per m³ ($)": "Total energy cost / Water volume produced",
                "Energy efficiency improvement (%)": "(Baseline - Current) / Baseline * 100",
                "Renewable energy use (%)": "Renewable energy consumption / Total * 100",
                "Cost savings achieved ($)": "Difference in total O&M cost vs baseline"
            },
            "Improve Non-Revenue Water (NRW) Performance": {
                "NRW (%)": "Volume lost / Total system input * 100",
                "Pipe leak reduction (%)": "(Previous leaks - Current) / Previous * 100",
                "Metering accuracy (%)": "Calibrated meters / Total meters * 100",
                "Value of water losses ($)": "Volume lost * Average tariff"
            }
        },

        # -------------------- 3. Financial Sustainability & Capital Utilization --------------------
        "Financial Sustainability & Capital Utilization": {
            "Improve Cost Recovery Ratio": {
                "Operating cost recovery (%)": "Operating revenue / Operating cost * 100",
                "Debt service coverage ratio": "Operating income / Debt obligations",
                "Subsidy dependency (%)": "Government subsidy / Total income * 100",
                "Tariff adjustment implementation (%)": "Tariff revisions executed / Planned * 100"
            },
            "Enhance Capital Project Efficiency": {
                "Capital budget utilization (%)": "Spent / Allocated * 100",
                "Project completion rate (%)": "Completed projects / Planned projects * 100",
                "Return on infrastructure investment (%)": "Benefit / Cost * 100",
                "Average project delay (days)": "Sum of project delays / Projects completed"
            }
        },

        # -------------------- 4. Economic Development Impact --------------------
        "Water & Sanitation Economic Development": {
            "Increase Access in Rural Areas": {
                "New rural connections (#)": "Number of new rural households connected",
                "Rural service coverage (%)": "Rural population served / Total rural population * 100",
                "Investment in rural systems ($)": "Funds allocated to rural expansion",
                "Employment created in rural projects (#)": "New jobs generated"
            },
            "Promote Public-Private Partnerships (PPP)": {
                "PPP investment mobilized ($)": "Private investment in water/sanitation",
                "Active PPP contracts (#)": "Current operational PPP projects",
                "PPP project performance rating (%)": "Average evaluation score",
                "Private sector contribution (%)": "Private funds / Total funds * 100"
            }
        }
    },

    # ----------------------------- CUSTOMER PERSPECTIVE -----------------------------
    "Customer Perspective": {
        **GENERIC_CUSTOMER_PERSPECTIVE["Customer Perspective"],

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

        # -------------------- 3. Customer Engagement & Responsiveness --------------------
        "Customer Engagement": {
            "Improve Customer Feedback Mechanisms": {
                "Complaints resolved on time (%)": "Resolved within SLA / Total complaints * 100",
                "Average complaint resolution time (hrs)": "Sum of resolution times / Total complaints",
                "Customer satisfaction index (%)": "Weighted survey score",
                "Digital service usage (%)": "Online interactions / Total interactions * 100"
            },
            "Enhance Transparency & Accountability": {
                "Information disclosure compliance (%)": "Reports published / Required reports * 100",
                "Public meetings conducted (#)": "Community consultation sessions per year",
                "Citizen trust index (%)": "Public perception of integrity",
                "Feedback incorporation rate (%)": "Suggestions implemented / Total received * 100"
            }
        },

        # -------------------- 4. Environmental & Social Responsibility --------------------
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
        }
    }
}
