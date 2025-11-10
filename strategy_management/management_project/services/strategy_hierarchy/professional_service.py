
from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE

PROFESSIONAL_SERVICE_PERSPECTIVE = {
    "Financial Perspective": {
        # Use generic financial KPIs
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],
    }
}
