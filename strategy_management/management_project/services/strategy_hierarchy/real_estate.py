from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE
from management_project.services.strategy_hierarchy.internal_process_perspective import (
    GENERIC_INTERNAL_PROCESS_PERSPECTIVE,
)
from management_project.services.strategy_hierarchy.learning_and_growth_perspective import (
    GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE,
)

REAL_ESTATE_PERSPECTIVE = {
    "Financial Perspective": {
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],
    },
    "Customer Perspective": {
        **GENERIC_CUSTOMER_PERSPECTIVE["Customer Perspective"],
    },
    "Internal Process Perspective": {
        **GENERIC_INTERNAL_PROCESS_PERSPECTIVE["Internal Process Perspective"],
    },
    "Learning & Growth Perspective": {
        **GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE["Learning & Growth Perspective"],
    },
}
