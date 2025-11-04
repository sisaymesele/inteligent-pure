class FinancialStrategyService:
    """Service class for Financial Perspective strategies"""

    def get_financial_hierarchy(self):
        return {
            "Revenue Growth & Diversification": {
                "Enhance Total Revenue Performance": {
                    "Total revenue growth (%)": "(Current revenue - Previous revenue) / Previous revenue * 100",
                    "Quarterly revenue growth rate (%)": "Quarter-over-quarter revenue increase percentage",
                    "Annual revenue growth acceleration": "Year-over-year growth rate improvement",
                    "Revenue per customer growth ($)": "(Current revenue/customer - Previous) / Previous * 100"
                },
                "Strengthen Market Share & Positioning": {
                    "Market share growth (%)": "(Current market share - Previous market share) / Previous * 100",
                    "Revenue in target segments growth (%)": "Growth in priority customer segments",
                    "Geographic expansion revenue ($)": "Revenue from new geographic markets",
                    "Competitive win rate (%)": "(Contracts won / Total bids) * 100"
                },
                # ... include all other financial objectives from your original code
            },
            "Cost Management & Efficiency": {
                "Enhance Operational Efficiency": {
                    "Cost per unit reduction (%)": "(Current cost/unit - Previous) / Previous * 100",
                    "Labor productivity growth (%)": "(Current output/employee - Previous) / Previous * 100",
                    "Process efficiency improvement (%)": "Reduction in process cycle time",
                    "Energy efficiency ratio": "Output per unit of energy consumed"
                },
                # ... other cost management objectives
            },
            "Agriculture/ Agro-Business": {
                "Enhance Operational Efficiency": {
                    "Cost per unit reduction (%)": "(Current cost/unit - Previous) / Previous * 100",
                    "Labor productivity growth (%)": "(Current output/employee - Previous) / Previous * 100",
                    "Process efficiency improvement (%)": "Reduction in process cycle time",
                    "Energy efficiency ratio": "Output per unit of energy consumed"
                },
                # ... other cost management objectives
            },
            # ... other financial pillars
        }