

from management_project.services.swot.agriculture import AGRICULTURE_SWOT
from management_project.services.swot.banking import BANKING_SWOT

from management_project.services.swot.ict import ICT_SWOT
from management_project.services.swot.default import DEFAULT_SWOT

class SwotHierarchyChoiceService:
    # Define sector-specific SWOT hierarchies
    SECTOR_MAP = {
        "agriculture": AGRICULTURE_SWOT,
        "banking": BANKING_SWOT,

        "ict": ICT_SWOT,

    }

    def get_sector_hierarchy(self, sector):
        # Return the sector hierarchy or DEFAULT_SWOT if sector not found
        return self.SECTOR_MAP.get(sector) or DEFAULT_SWOT

    def get_swot_types(self, sector):
        hierarchy = self.get_sector_hierarchy(sector)
        return [(swot_type, swot_type) for swot_type in hierarchy.keys()]

    def get_pillars(self, sector, swot_type):
        hierarchy = self.get_sector_hierarchy(sector)
        if not swot_type:
            return []
        return [(pillar, pillar) for pillar in hierarchy.get(swot_type, {}).keys()]

    def get_factors(self, sector, swot_type, pillar):
        hierarchy = self.get_sector_hierarchy(sector)
        if not swot_type or not pillar:
            return []
        return [(factor, factor) for factor in hierarchy.get(swot_type, {}).get(pillar, [])]

