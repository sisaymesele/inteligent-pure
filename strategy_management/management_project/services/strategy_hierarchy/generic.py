from management_project.services.strategy_hierarchy.finance import FinancialStrategyService
from management_project.services.strategy_hierarchy.customer import CustomerStrategyService
from management_project.services.strategy_hierarchy.internal_process import InternalProcessStrategyService
from management_project.services.strategy_hierarchy.learning_and_growth import LearningGrowthStrategyService


class StrategyHierarchyChoicesService:
    def __init__(self):
        self.financial_service = FinancialStrategyService()
        self.customer_service = CustomerStrategyService()
        self.internal_service = InternalProcessStrategyService()
        self.learning_service = LearningGrowthStrategyService()

    def get_full_hierarchy(self):
        """Get complete strategy hierarchy from all sectors"""
        return {
            "Financial Perspective": self.financial_service.get_financial_hierarchy(),
            "Customer Perspective": self.customer_service.get_customer_hierarchy(),
            "Internal Process Perspective": self.internal_service.get_internal_hierarchy(),
            "Learning & Growth Perspective": self.learning_service.get_learning_hierarchy(),
        }

    # Getters for forms
    def get_perspective_choices(self):
        return [(p, p) for p in self.get_full_hierarchy().keys()]

    def get_pillar_choices(self, perspective):
        hierarchy = self.get_full_hierarchy()
        return [(p, p) for p in hierarchy.get(perspective, {}).keys()]

    def get_objective_choices(self, perspective, pillar):
        hierarchy = self.get_full_hierarchy()
        return [(o, o) for o in hierarchy.get(perspective, {}).get(pillar, {}).keys()]

    def get_kpi_choices(self, perspective, pillar, objective):
        hierarchy = self.get_full_hierarchy()
        return [
            (kpi, kpi)
            for kpi in hierarchy.get(perspective, {})
            .get(pillar, {})
            .get(objective, {})
            .keys()
        ]

    def get_formula(self, perspective, pillar, objective, kpi):
        hierarchy = self.get_full_hierarchy()
        return (
            hierarchy
            .get(perspective, {})
            .get(pillar, {})
            .get(objective, {})
            .get(kpi, "")
        )