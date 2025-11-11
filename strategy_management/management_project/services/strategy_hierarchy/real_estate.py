from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE

REAL_ESTATE_PERSPECTIVE = {

    # -------------------- Financial Perspective --------------------
    "Financial Perspective": {

        # -------------------- Rental & Sale Revenue Growth & Diversification --------------------
        "Rental & Sale Revenue Growth & Diversification": {
            "Increase residential sales revenue": {
                "Sales growth rate (%)": "(Current residential sales - Previous) / Previous * 100",
                "Revenue per residential unit ($)": "Total revenue / Number of units sold",
                "Customer collection rate (%)": "(Collected payments / Billed sales) * 100",
                "Pricing optimization (%)": "(Units sold at optimal pricing / Total units sold) * 100"
            },
            "Expand commercial rental income streams": {
                "Rental revenue growth (%)": "(Current - Previous) / Previous * 100",
                "Occupancy rate (%)": "(Occupied units / Total rentable units) * 100",
                "Average rent per unit ($)": "Total rental income / Number of units rented",
                "Tenant retention rate (%)": "(Returning tenants / Total tenants) * 100"
            },
            "Develop value-added services (property management, amenities)": {
                "Service revenue ($)": "Total income from services",
                "Service utilization rate (%)": "(Utilized services / Available services) * 100",
                "Contribution to total revenue (%)": "Service revenue / Total revenue * 100",
                "Growth in service revenue (%)": "(Current - Previous) / Previous * 100"
            },
            "Diversify property types and markets": {
                "Revenue from new property types ($)": "Revenue from commercial, mixed-use, or new residential segments",
                "Revenue growth from new markets (%)": "(Current - Previous) / Previous * 100",
                "Portfolio diversification index": "Number of property types / Total revenue",
                "New market contribution (%)": "Revenue from new markets / Total revenue * 100"
            }
        },

        # -------------------- Profitability & Return Optimization --------------------
        "Real Estate Return": {

            "Residential Property Profitability": {
                "Gross margin per residential unit (%)": "(Residential revenue - Residential costs) / Residential revenue * 100",
                "Residential profit growth (%)": "(Current - Previous) / Previous * 100",
                "High-demand location margin (%)": "Revenue from high-demand locations - Costs / Revenue * 100",
                "Average net profit per unit ($)": "Net profit / Units sold"
            },

            "Commercial Property Profitability": {
                "Gross margin per commercial unit (%)": "(Commercial revenue - Commercial costs) / Commercial revenue * 100",
                "Commercial profit growth (%)": "(Current - Previous) / Previous * 100",
                "Premium commercial space margin (%)": "(Revenue from premium units - Costs) / Revenue * 100",
                "Net profit per commercial property ($)": "Net income from commercial properties / Number of properties"
            },

            "Rental Portfolio Profitability": {
                "Residential rental profit ($)": "Rental revenue - Operating costs",
                "Commercial rental profit ($)": "Rental revenue - Operating costs",
                "Occupancy-driven profitability (%)": "(Revenue from occupied units - Vacant costs) / Revenue * 100",
                "Tenant turnover cost ($)": "Revenue lost due to tenant churn"
            },

            "Luxury & Premium Unit Profitability": {
                "Gross margin for luxury units (%)": "(Revenue from luxury units - Costs) / Revenue * 100",
                "Profit growth for premium units (%)": "(Current - Previous) / Previous * 100",
                "High-end unit contribution to total profit (%)": "Profit from luxury units / Total profit * 100",
                "Average profit per high-end unit ($)": "Net profit / Luxury units sold"
            },

            "Sustainable & Green Building Profitability": {
                "Green building gross margin (%)": "(Revenue from certified green units - Costs) / Revenue * 100",
                "Profit growth from sustainable units (%)": "(Current - Previous) / Previous * 100",
                "Sustainable project ROI (%)": "(Revenue - Cost) / Cost * 100",
                "Contribution of green buildings to total profit (%)": "Profit from green units / Total profit * 100"
            },

            "Shareholder Value & Return": {
                "Return on equity (ROE %)": "Net income / Shareholders' equity * 100",
                "Net profit per shareholder ($)": "Net income / Number of shareholders",
                "Dividend payout ratio (%)": "Dividends / Net income * 100",
                "Shareholder value added ($)": "Net profit - Cost of equity"
            }
        },

        # -------------------- Asset Utilization & Capital Performance --------------------
        "Asset Utilization & Capital Performance": {

            "Occupancy & Utilization Efficiency": {
                "Residential occupancy rate (%)": "Occupied residential units / Total units * 100",
                "Commercial occupancy rate (%)": "Occupied commercial units / Total units * 100",
                "Vacancy reduction (%)": "(Previous vacancies - Current vacancies) / Previous * 100",
                "Space utilization index": "Revenue per sq. meter / Optimal revenue per sq. meter"
            },

            "Return on Real Estate Assets (ROA)": {
                "ROA (%)": "Net operating income / Total real estate assets * 100",
                "Revenue per property ($)": "Revenue / Number of properties",
                "Asset utilization ratio (%)": "Revenue-producing assets / Total assets * 100",
                "Capital efficiency": "Revenue / Capital invested"
            },

            "Capital Investment & Deployment": {
                "Capital utilization rate (%)": "Invested capital / Allocated capital * 100",
                "Development ROI (%)": "(Revenue - Cost) / Cost * 100",
                "Unused capital (%)": "(Allocated - Used) / Allocated * 100",
                "Project funding efficiency": "Actual project output / Capital invested"
            },

            "Portfolio Risk-Adjusted Performance": {
                "Revenue-weighted property ROI (%)": "Sum of (ROI per property * Revenue share)",
                "Capital-at-risk coverage (%)": "Insured or hedged capital / Total capital * 100",
                "Return per high-value asset ($)": "Net profit per premium or strategic property",
                "Portfolio diversification efficiency": "Revenue from diverse segments / Total revenue * 100"
            }
        }
    },

    # -------------------- Customer Perspective --------------------
    "Customer Perspective": {

        # Generic customer perspective
        **GENERIC_CUSTOMER_PERSPECTIVE,

        # Real Estate Development Specific Focus Area
        "Real Estate Development": {

            "Increase affordable housing availability": {
                "Affordable units delivered (#)": "Number of affordable housing units completed",
                "Affordable housing delivery growth (%)": "(Current - Previous) / Previous * 100",
                "Customer satisfaction with affordable units (%)": "Satisfied residents / Total surveyed * 100",
                "Occupancy rate (%)": "Occupied units / Total units * 100"
            },

            "Promote sustainable & green building projects": {
                "Green building ratio (%)": "Green-certified units / Total units * 100",
                "Energy-efficient unit adoption (%)": "Units with energy-saving features / Total units * 100",
                "Resident satisfaction with sustainability (%)": "Satisfied residents / Total surveyed * 100",
                "Sustainable project delivery on-time (%)": "Green projects delivered on schedule / Total green projects * 100"
            },

            "Enhance customer experience & satisfaction": {
                "Customer satisfaction index": "Survey score average",
                "Net promoter score (NPS)": "Promoters - Detractors / Total respondents * 100",
                "Complaint resolution time (days)": "Total days to resolve complaints / Number of complaints",
                "Repeat customer rate (%)": "Returning buyers / Total buyers * 100"
            },

            "Improve community engagement & social impact": {
                "Community programs initiated (#)": "Number of social or community programs",
                "Resident participation rate (%)": "Residents participating / Total residents * 100",
                "CSR project coverage (%)": "CSR projects delivered / Planned projects * 100",
                "Local employment contribution (#)": "Jobs created for local community"
            },

            "Strengthen investor & stakeholder relations": {
                "Investor satisfaction (%)": "Satisfied investors / Total surveyed * 100",
                "Stakeholder engagement events (#)": "Number of investor or stakeholder events held",
                "Project transparency score": "Internal rating of disclosures and reporting",
                "Timely reporting compliance (%)": "Reports delivered on time / Total reports * 100"
            },

            "Digital & online customer adoption": {
                "Digital platform usage (%)": "Users on online portal / Total customers * 100",
                "Online property viewing bookings (#)": "Total bookings made online",
                "Online feedback resolution (%)": "Complaints handled via portal / Total online complaints * 100",
                "Mobile app adoption (%)": "Active mobile users / Total customers * 100"
            }
        }
    }
}
