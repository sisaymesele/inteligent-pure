from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE

CONSTRUCTION_PERSPECTIVE = {
    "Financial Perspective": {
        # Import generic financial KPIs
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],

        # -------------------- Construction Economic Development --------------------
        "Construction Economic Development": {
            "Promote Infrastructure Development": {
                "Projects completed on schedule (%)": "(Completed projects / Total projects) * 100",
                "Capital investment in infrastructure ($)": "Total funds allocated to projects",
                "New infrastructure projects initiated (#)": "Number of projects started",
                "Revenue from infrastructure projects ($)": "Revenue generated from completed projects"
            },
            "Enhance Local Employment & Skills": {
                "Jobs created in construction projects": "Number of new jobs generated",
                "Skilled workers trained (#)": "Total construction personnel trained",
                "Employee retention rate (%)": "(Employees retained / Total hired) * 100",
                "Workforce productivity improvement (%)": "Output per worker growth %"
            },
            "Support SME & Local Contractor Participation": {
                "SME contractors engaged (#)": "Number of local SMEs contracted",
                "Procurement from local contractors ($)": "Total spending on local SMEs",
                "SME revenue growth (%)": "(Current - Previous) / Previous * 100",
                "SME satisfaction rate (%)": "Average satisfaction score from SME surveys"
            },
            "Promote Safety & Regulatory Compliance": {
                "Safety incident reduction (%)": "(Previous incidents - Current) / Previous * 100",
                "Compliance with construction regulations (%)": "(Compliant projects / Total projects) * 100",
                "Safety training programs conducted (#)": "Number of trainings implemented",
                "Audit pass rate (%)": "(Projects passing audits / Total audited projects) * 100"
            },
            "Encourage Sustainable Construction Practices": {
                "Green building adoption rate (%)": "(Green certified projects / Total projects) * 100",
                "Energy efficiency improvements (%)": "Reduction in energy usage per project",
                "Waste reduction (%)": "(Previous waste - Current) / Previous * 100",
                "Sustainable materials usage (%)": "Sustainable materials / Total materials * 100"
            },
            "Increase Construction Productivity & Efficiency": {
                "Project delivery efficiency (%)": "(Projects delivered on time / Total projects) * 100",
                "Cost variance reduction (%)": "(Planned cost - Actual cost) / Planned cost * 100",
                "Labor productivity (output per worker)": "Units of work completed / Total workers",
                "Equipment utilization rate (%)": "(Equipment used effectively / Total available) * 100"
            },
            "Boost Economic Contribution & GDP": {
                "Contribution to GDP ($)": "Estimated economic contribution from construction activities",
                "Local supplier revenue growth ($)": "Revenue growth of local material suppliers",
                "Public infrastructure benefit ($)": "Estimated benefit to public from completed projects",
                "Community engagement initiatives (#)": "Number of community programs implemented"
            },
            "Support Innovation & Technology Adoption": {
                "New construction technologies deployed (#)": "Number of tech solutions implemented",
                "Digital project management adoption (%)": "Projects using digital tools / Total projects * 100",
                "BIM (Building Information Modeling) utilization (%)": "BIM projects / Total projects * 100",
                "Cost savings from innovation ($)": "Estimated cost reduction due to new technologies"
            },
            "Improve Project Financing & Investment": {
                "External investment attracted ($)": "Funds received from private/public investors",
                "Public-private partnership projects (#)": "Number of PPP projects",
                "Return on construction investment (%)": "(Net project benefits / Total investment) * 100",
                "Funding utilization efficiency (%)": "(Used funds / Allocated funds) * 100"
            }
        }
    },

    "Customer Perspective": {

        **GENERIC_CUSTOMER_PERSPECTIVE['Customer Perspective'],
    }
}
