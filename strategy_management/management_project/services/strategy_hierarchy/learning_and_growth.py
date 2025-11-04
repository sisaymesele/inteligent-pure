class LearningGrowthStrategyService:
    """Service class for Learning & Growth Perspective strategies"""

    def get_learning_hierarchy(self):
        return {
            "People & Culture Development": {
                "Improve employee engagement": {
                    "Employee engagement survey score": "Average survey score across engagement questions",
                    "Voluntary turnover rate reduction": "((Previous voluntary turnover - current) / previous) * 100",
                    "Employee net promoter score": "Promoters % - Detractors %",
                    "Engagement action plan completion rate": "(Completed action plans / total plans) * 100"
                },
                # ... other people development objectives
            },
            "Leadership & Talent Management": {
                "Enhance leadership development": {
                    "Leadership competency score improvement": "Current score - previous score",
                    "Leadership program completion rate": "(Completed participants / total participants) * 100",
                    "360-degree feedback score improvement": "Current 360 feedback - previous feedback",
                    "Leadership bench strength index": "Weighted index of ready-now leaders"
                },
                # ... other leadership objectives
            },
            # ... other learning & growth pillars
        }