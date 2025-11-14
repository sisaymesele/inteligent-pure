
from management_project.services.strategy_hierarchy.agriculture import AGRICULTURE_PERSPECTIVE
from management_project.services.strategy_hierarchy.banking import BANKING_PERSPECTIVE
from management_project.services.strategy_hierarchy.construction import CONSTRUCTION_PERSPECTIVE
from management_project.services.strategy_hierarchy.education import EDUCATION_PERSPECTIVE
from management_project.services.strategy_hierarchy.energy import ENERGY_PERSPECTIVE
from management_project.services.strategy_hierarchy.environment import ENVIRONMENT_PERSPECTIVE
from management_project.services.strategy_hierarchy.hospitality_and_tourism import HOSPITALITY_AND_TOURISM_PERSPECTIVE
from management_project.services.strategy_hierarchy.health import HEALTH_PERSPECTIVE
from management_project.services.strategy_hierarchy.ict import ICT_PERSPECTIVE
from management_project.services.strategy_hierarchy.industry import INDUSTRY_PERSPECTIVE
from management_project.services.strategy_hierarchy.insurance import INSURANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.mining import MINING_PERSPECTIVE
from management_project.services.strategy_hierarchy.real_estate import REAL_ESTATE_PERSPECTIVE
from management_project.services.strategy_hierarchy.retail import RETAIL_PERSPECTIVE
from management_project.services.strategy_hierarchy.transport_and_logistics import TRANSPORT_AND_LOGISTICS_PERSPECTIVE
from management_project.services.strategy_hierarchy.water_and_sanitation import WATER_AND_SANITATION_PERSPECTIVE


from management_project.services.strategy_hierarchy.default import DEFAULT_PERSPECTIVE

class StrategyHierarchyChoiceService:
    # Define sector-specific hierarchies
    SECTOR_MAP = {
        "agriculture": AGRICULTURE_PERSPECTIVE,
        "banking": BANKING_PERSPECTIVE,
        "construction": CONSTRUCTION_PERSPECTIVE,
        "education": EDUCATION_PERSPECTIVE,
        "energy": ENERGY_PERSPECTIVE,
        "environment": ENVIRONMENT_PERSPECTIVE,
        "hospitality_and_tourism": HOSPITALITY_AND_TOURISM_PERSPECTIVE,
        "health": HEALTH_PERSPECTIVE,
        "ict": ICT_PERSPECTIVE,
        "industry": INDUSTRY_PERSPECTIVE,
        "insurance": INSURANCE_PERSPECTIVE,
        "mining": MINING_PERSPECTIVE,
        "real_estate": REAL_ESTATE_PERSPECTIVE,
        "retail": RETAIL_PERSPECTIVE,
        "transport_and_logistics": TRANSPORT_AND_LOGISTICS_PERSPECTIVE,
        "water_and_sanitation": WATER_AND_SANITATION_PERSPECTIVE,
        "default": DEFAULT_PERSPECTIVE
    }

    def get_sector_hierarchy(self, sector):
        return self.SECTOR_MAP.get(sector, self.SECTOR_MAP["default"])

    def get_perspectives(self, sector):
        hierarchy = self.get_sector_hierarchy(sector)
        return [(p, p) for p in hierarchy.keys()]

    def get_pillars(self, sector, perspective):
        hierarchy = self.get_sector_hierarchy(sector)
        if not perspective:
            return []
        return [(p, p) for p in hierarchy.get(perspective, {}).keys()]

    def get_objectives(self, sector, perspective, pillar):
        hierarchy = self.get_sector_hierarchy(sector)
        if not perspective or not pillar:
            return []
        return [(o, o) for o in hierarchy.get(perspective, {}).get(pillar, {}).keys()]

    def get_kpis(self, sector, perspective, pillar, objective):
        hierarchy = self.get_sector_hierarchy(sector)
        if not perspective or not pillar or not objective:
            return []
        return [
            (kpi, kpi)
            for kpi in hierarchy.get(perspective, {})
            .get(pillar, {})
            .get(objective, {})
            .keys()
        ]

    def get_kpi_formula(self, sector, perspective, pillar, objective, kpi):
        hierarchy = self.get_sector_hierarchy(sector)
        if not perspective or not pillar or not objective or not kpi:
            return ""
        return (
            hierarchy
            .get(perspective, {})
            .get(pillar, {})
            .get(objective, {})
            .get(kpi, "")
        )