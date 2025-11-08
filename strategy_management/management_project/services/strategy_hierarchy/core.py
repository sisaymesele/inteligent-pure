from management_project.services.strategy_hierarchy.agriculture import AGRICULTURE_PERSPECTIVE
from management_project.services.strategy_hierarchy.health import HEALTH_SECTOR
from management_project.services.strategy_hierarchy.banking import BANKING_PERSPECTIVE
from management_project.services.strategy_hierarchy.default import DEFAULT_SECTOR

class StrategyHierarchyChoiceService:
    # Define sector-specific hierarchies
    SECTOR_MAP = {
        "agriculture": AGRICULTURE_PERSPECTIVE,
        "health": HEALTH_SECTOR,
        "banking": BANKING_PERSPECTIVE,
        "default": DEFAULT_SECTOR
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