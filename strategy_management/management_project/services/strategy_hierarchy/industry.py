from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE

INDUSTRY_PERSPECTIVE = {
    "Financial Perspective": {
        # Import generic financial KPIs
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],

        # -------------------- Industry Economic Development --------------------
        "Industry Economic Development": {
            "Enhance Manufacturing Output & Efficiency": {
                "Production volume growth (%)": "(Current production - Previous production) / Previous production * 100",
                "Production cost per unit ($)": "Total production cost / Units produced",
                "Capacity utilization rate (%)": "(Actual output / Maximum capacity) * 100",
                "Defect rate reduction (%)": "(Previous defects - Current defects) / Previous defects * 100"
            },
            "Promote Innovation & Technology Adoption": {
                "New technologies implemented (#)": "Number of new production technologies deployed",
                "R&D investment ($)": "Funds allocated to research & development",
                "Automation adoption rate (%)": "(Automated production lines / Total lines) * 100",
                "Process improvement savings ($)": "Cost reduction from efficiency improvements"
            },
            "Support SME Suppliers & Local Industry": {
                "SME suppliers engaged (#)": "Number of local SMEs supplying raw materials or components",
                "Procurement from local SMEs ($)": "Total spending on SMEs",
                "SME revenue growth (%)": "(Current SME revenue - Previous) / Previous * 100",
                "SME satisfaction rate (%)": "Average satisfaction score from SME surveys"
            },
            "Promote Workforce Development & Skills": {
                "Employees trained (#)": "Total number of employees trained",
                "Training completion rate (%)": "(Completed trainings / Total enrolled) * 100",
                "Employee productivity improvement (%)": "Output per employee growth %", 
                "Workforce retention rate (%)": "(Employees retained / Total hired) * 100"
            },
            "Encourage Sustainable & Green Manufacturing": {
                "Energy efficiency improvement (%)": "Reduction in energy consumption per unit produced",
                "Waste reduction (%)": "(Previous waste - Current) / Previous * 100",
                "Recycling rate (%)": "(Recycled waste / Total waste) * 100",
                "Green certified production lines (#)": "Number of certified sustainable lines"
            },
            "Increase Economic Contribution & GDP": {
                "Contribution to GDP ($)": "Estimated economic contribution from industrial activities",
                "Export revenue ($)": "Revenue from products exported",
                "Local supplier revenue growth ($)": "Revenue growth of local suppliers",
                "Community engagement programs (#)": "Number of initiatives supporting local economy"
            },
            "Boost Profitability & Financial Sustainability": {
                "Revenue growth (%)": "(Current revenue - Previous) / Previous * 100",
                "Cost reduction (%)": "(Previous cost - Current) / Previous * 100",
                "Operating margin improvement (%)": "(Current margin - Previous margin) / Previous margin * 100",
                "Return on investment (%)": "(Net benefits / Total investment) * 100"
            },
            "Ensure Safety & Regulatory Compliance": {
                "Safety incidents reduction (%)": "(Previous incidents - Current) / Previous * 100",
                "Regulatory compliance rate (%)": "(Compliant processes / Total processes) * 100",
                "Safety training programs conducted (#)": "Number of safety trainings implemented",
                "Audit pass rate (%)": "(Projects passing audits / Total audited projects) * 100"
            },
            "Foster Export & Market Diversification": {
                "New markets entered (#)": "Number of new domestic and international markets served",
                "Export revenue growth (%)": "(Current export revenue - Previous) / Previous * 100",
                "Product diversification (%)": "(Number of new products / Total products) * 100",
                "Revenue from new markets ($)": "Revenue generated from new markets"
            }
        }
    }
}
