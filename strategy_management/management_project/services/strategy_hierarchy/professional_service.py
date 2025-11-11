from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE

PROFESSIONAL_SERVICE_PERSPECTIVE = {
    "Financial Perspective": {
        # Use generic financial KPIs
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],
    },

    "Customer Perspective": {

        **GENERIC_CUSTOMER_PERSPECTIVE['Customer Perspective'],

    },
}
