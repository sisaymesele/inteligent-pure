class InternalProcessStrategyService:
    """Service class for Internal Process Perspective strategies"""

    def get_internal_hierarchy(self):
        return {
            "Operational Excellence & Quality": {
                "Reduce process cycle times": {
                    "Cycle time reduction percentage": "((Previous cycle time - Current cycle time) / Previous cycle time) * 100",
                    "Process throughput improvement": "((Current throughput - Previous throughput) / Previous throughput) * 100",
                    "On-time completion rate": "(Processes completed on time / Total processes) * 100",
                    "Process efficiency score improvement": "Current process efficiency score - Previous score"
                },
                # ... other operational excellence objectives
            },
            "Innovation & New Product Development": {
                "Accelerate time-to-market for new products": {
                    "Development cycle time reduction": "((Previous cycle time - Current) / Previous) * 100",
                    "Time from idea to launch reduction": "Previous time - Current time",
                    "Market readiness score improvement": "Current readiness score - Previous score",
                    "Project timeline adherence percentage": "(On-time milestones / Total milestones) * 100"
                },
                # ... other innovation objectives
            },
            # ... other internal process pillars
        }