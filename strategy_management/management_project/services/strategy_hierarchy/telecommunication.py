from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE

TELECOMMUNICATION_PERSPECTIVE = {
    # -------------------- Financial Perspective --------------------
    "Financial Perspective": {
        # Use generic financial KPIs
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],
    },

    # -------------------- Customer Perspective --------------------
    "Customer Perspective": {
        **GENERIC_CUSTOMER_PERSPECTIVE['Customer Perspective'],

        # -------------------- Telecom-specific Customer Focus --------------------
        "Telecom Service & Network Access": {
            "Increase Network Coverage": {
                "Network coverage area (%)": "Covered geographic area / Total target area * 100",
                "Population coverage (%)": "Population with network access / Total population * 100",
                "New tower deployment (#)": "Number of new towers or base stations installed",
                "Network accessibility complaints (#)": "Number of complaints about access issues"
            },
            "Enhance Service Quality & Reliability": {
                "Call drop rate (%)": "Dropped calls / Total calls * 100",
                "Network uptime (%)": "Time network is operational / Total time * 100",
                "Average data speed (Mbps)": "Measured throughput for customers",
                "Service issue resolution time (hrs)": "Average hours to resolve service issues"
            },
            "Promote Digital Services Adoption": {
                "Digital app users (#)": "Number of active users on telecom app",
                "Online self-service transactions (#)": "Transactions performed via app or portal",
                "Digital service satisfaction (%)": "Survey score of digital users",
                "Growth in mobile data usage (%)": "(Current - Previous period) / Previous * 100"
            },
            "Ensure Accessibility for All Customer Segments": {
                "Coverage in rural areas (%)": "Rural population with access / Total rural population * 100",
                "Affordable service plan adoption (%)": "Subscribers using low-cost plans / Total subscribers * 100",
                "Customer inclusion programs (#)": "Programs targeting underserved communities",
                "Customer complaints resolved (%)": "Resolved complaints / Total complaints * 100"
            }
        }
    }
}
