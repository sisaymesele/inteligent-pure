
from management_project.services.strategy_hierarchy.default import DEFAULT_PERSPECTIVE


REAL_ESTATE_PERSPECTIVE = {
    "Financial Perspective": {
        **DEFAULT_PERSPECTIVE["Financial Perspective"],
    },
    "Customer Perspective": {
        **DEFAULT_PERSPECTIVE["Customer Perspective"],
    },
    "Internal Process Perspective": {
        **DEFAULT_PERSPECTIVE["Internal Process Perspective"],
    },
    "Learning & Growth Perspective": {
        **DEFAULT_PERSPECTIVE["Learning & Growth Perspective"],
    },
}
