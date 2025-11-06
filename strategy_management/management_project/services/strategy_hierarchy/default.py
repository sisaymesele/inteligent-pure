from django.db.models import Sum

DEFAULT_SECTOR = {
    "Financial Perspective": {
        "Revenue Growth & Diversification": {
            "Enhance Total Revenue Performance": {
                "Total revenue growth (%)": "(Current revenue - Previous revenue) / Previous revenue * 100",
                "Quarterly revenue growth rate (%)": "Quarter-over-quarter revenue increase percentage"
            }
        }
    },
    "Customer Perspective": {
        "Customer Acquisition & Market Reach": {
            "Increase qualified lead generation": {
                "Number of qualified leads per month": "Count of leads meeting qualification criteria per month",
                "Lead-to-opportunity conversion rate": "(Leads converted to opportunities / Total leads) * 100"
            }
        }
    },
    "Internal Process Perspective": {
        "Operational Excellence & Quality": {
            "Reduce process cycle times": {
                "Cycle time reduction percentage": "((Previous cycle time - Current cycle time) / Previous cycle time) * 100",
                "Process throughput improvement": "((Current throughput - Previous throughput) / Previous throughput) * 100"
            }
        }
    },
    "Learning & Growth Perspective": {
        "People & Culture Development": {
            "Improve employee engagement": {
                "Employee engagement survey score": "Average survey score across engagement questions",
                "Voluntary turnover rate reduction": "((Previous voluntary turnover - current) / previous) * 100"
            }
        }
    }
}