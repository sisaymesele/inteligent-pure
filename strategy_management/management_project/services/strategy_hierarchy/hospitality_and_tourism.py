from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE

HOSPITALITY_AND_TOURISM_PERSPECTIVE = {
    "Financial Perspective": {
        # Core generic financial objectives
        **GENERIC_FINANCE_PERSPECTIVE['Financial Perspective'],

        # ==================== 1. Hospitality Revenue Growth & Funding ====================
        "Hospitality Revenue Growth & Funding": {
            "Increase Room Revenue": {
                "Total room revenue ($)": "Revenue from all accommodation types",
                "Average daily rate ($)": "Average revenue per occupied room",
                "Occupancy rate (%)": "Occupied rooms / Total rooms * 100",
                "Revenue per available room (RevPAR)": "Total room revenue / Total rooms"
            },
            "Increase Food & Beverage Revenue": {
                "Restaurant revenue ($)": "Revenue from dining services",
                "Bar & lounge revenue ($)": "Revenue from beverage sales",
                "Event catering revenue ($)": "Revenue from catered events",
                "Room service revenue ($)": "Revenue from in-room dining"
            },
            "Diversify Revenue Streams": {
                "Spa & wellness revenue ($)": "Revenue from wellness services",
                "Tour package revenue ($)": "Income from organized tours",
                "Leisure & recreation revenue ($)": "Revenue from recreational services",
                "Event hosting revenue ($)": "Income from hosted events"
            },
            "Optimize Payer & Booking Mix": {
                "Corporate booking ratio (%)": "Revenue from corporate clients / Total revenue * 100",
                "Online booking share (%)": "Revenue from online platforms / Total revenue * 100",
                "Direct booking share (%)": "Revenue from direct reservations / Total revenue * 100",
                "Travel agency booking share (%)": "Revenue from travel agents / Total revenue * 100"
            },
            "Leverage Partnerships": {
                "Corporate partnership revenue ($)": "Revenue from corporate agreements",
                "Travel agency partnership revenue ($)": "Revenue via travel agency partnerships",
                "Event sponsorship revenue ($)": "Revenue from sponsored events",
                "Tour operator collaboration revenue ($)": "Income from tour operator deals"
            }
        },

        # ==================== 2. Hospitality Infrastructure & Asset Finance ====================
        "Hospitality Infrastructure & Asset Finance": {
            "Modernize Facilities": {
                "Hotel modernization investment ($)": "Capital spent on facility upgrades",
                "Room refurbishment ratio (%)": "Refurbished rooms / Total rooms * 100",
                "Digital infrastructure investment ($)": "Spending on IT and digital systems",
                "Facility expansion capacity (%)": "Added capacity / Current capacity * 100"
            },
            "Optimize Asset Utilization": {
                "Room occupancy rate (%)": "Occupied rooms / Total rooms * 100",
                "Event hall utilization (%)": "Hours used / Total hours * 100",
                "Restaurant table turnover rate": "Customers served per table per day",
                "Spa equipment utilization rate (%)": "Hours used / Available hours * 100"
            },
            "Enhance Technology & Services": {
                "Property management system ROI (%)": "(Benefits - Cost) / Cost * 100",
                "Booking platform efficiency (%)": "Successful bookings / Total attempts * 100",
                "Digital service adoption rate (%)": "Digital services used / Total services * 100",
                "Guest service technology investment ($)": "Spending on guest service tech"
            },
            "Preventive Maintenance & Lifecycle": {
                "Equipment uptime (%)": "Available hours / Total hours * 100",
                "Preventive maintenance compliance (%)": "Assets maintained / Total assets * 100",
                "Asset replacement cycle (years)": "Average lifespan of equipment",
                "Maintenance cost per asset ($)": "Total maintenance spend / Number of assets"
            },
            "Improve Facility Efficiency": {
                "Energy cost per room ($)": "Total energy cost / Number of rooms",
                "Space utilization efficiency (%)": "Utilized space / Total space * 100",
                "Guest flow optimization score": "Efficiency of guest movement through facilities",
                "Infrastructure cost per guest ($)": "Facility costs / Number of guests served"
            }
        },

        # ==================== 3. Hospitality Profitability & Return ====================
        "Hospitality Profitability & Return": {
            "Improve Overall Profit Margins": {
                "Net service margin (%)": "(Revenue - Costs) / Revenue * 100",
                "Operating margin (%)": "Operating income / Revenue * 100",
                "EBITDA margin (%)": "EBITDA / Revenue * 100",
                "Contribution margin per service (%)": "(Revenue - Variable costs) / Revenue * 100"
            },
            "Food & Beverage Profitability": {
                "Restaurant profit margin (%)": "(Revenue - Costs) / Revenue * 100",
                "Bar & lounge profit margin (%)": "(Revenue - Costs) / Revenue * 100",
                "Event catering profit margin (%)": "(Revenue - Costs) / Revenue * 100",
                "Room service profit margin (%)": "(Revenue - Costs) / Revenue * 100"
            },
            "Room & Accommodation Profitability": {
                "Room revenue profit margin (%)": "(Room revenue - Costs) / Revenue * 100",
                "Occupancy profit efficiency (%)": "Revenue per occupied room / Cost per room * 100",
                "Suite & premium room ROI (%)": "(Revenue - Costs) / Costs * 100",
                "Corporate booking profit margin (%)": "(Revenue from corporate bookings - Costs) / Revenue * 100"
            },
            "Event & Leisure Services Profitability": {
                "Event hosting ROI (%)": "(Revenue - Event cost) / Event cost * 100",
                "Leisure service profit margin (%)": "(Revenue - Costs) / Revenue * 100",
                "Spa & wellness profit margin (%)": "(Revenue - Costs) / Revenue * 100",
                "Tour package profit margin (%)": "(Revenue - Costs) / Revenue * 100"
            },
            "Optimize Resource Utilization": {
                "Cost per guest ($)": "Total costs / Number of guests",
                "Staff productivity (service units/staff)": "Efficiency per staff member",
                "Staffing cost efficiency (%)": "Actual staffing cost / Budgeted * 100",
                "Supplies cost per service ($)": "Cost of consumables / Service count"
            },
            "Maximize Contract & Partner Performance": {
                "Contractual allowance rate (%)": "Adjustments / Revenue * 100",
                "Denial rate (%)": "Claims denied / Claims submitted * 100",
                "Collection rate (%)": "Amount collected / Amount billed * 100",
                "Days in accounts receivable": "Average collection time"
            }
        },

        # ==================== 4. Hospitality Financial Risk Management ====================
        "Hospitality Financial Risk Management": {
            "Manage Operational Risk": {
                "Business interruption insurance coverage (%)": "Covered risks / Total risks * 100",
                "Disaster recovery readiness score": "Preparedness for emergency scenarios",
                "Supply chain disruption cost ($)": "Financial impact of supply shortages",
                "Staffing shortage impact ($)": "Cost of temporary staff and overtime"
            },
            "Mitigate Regulatory & Compliance Risk": {
                "Health & safety audit score (%)": "Compliance score from inspections",
                "Licensing compliance rate (%)": "Compliant licenses / Total licenses * 100",
                "Accreditation maintenance cost ($)": "Cost to maintain certifications",
                "Regulatory penalty avoidance ($)": "Estimated savings from compliance"
            },
            "Address Market & Competition Risk": {
                "Market share volatility (%)": "Variation in guest volume and market position",
                "Competitive pricing pressure index": "Impact of competitor pricing on margins",
                "Seasonality revenue variation (%)": "Revenue fluctuation across periods",
                "Service demand forecasting accuracy (%)": "Actual demand / Forecasted demand * 100"
            }
        },

        # ==================== 5. Hospitality Cost Efficiency ====================
        "Hospitality Cost Efficiency": {
            "Optimize Operations Costs": {
                "Cost per guest ($)": "Total operational cost / Number of guests",
                "Food & beverage cost per guest ($)": "Cost of F&B / Number of guests",
                "Housekeeping cost per room ($)": "Cost / Number of rooms",
                "Utility cost per guest ($)": "Utilities / Number of guests"
            },
            "Reduce Administrative Overhead": {
                "Administrative cost ratio (%)": "Admin costs / Total revenue * 100",
                "IT support cost per user ($)": "IT costs / Number of system users",
                "Billing and accounting cost ($)": "Revenue cycle costs",
                "Facility overhead per square foot ($)": "Overhead costs / Total facility space"
            },
            "Improve Staffing Efficiency": {
                "Staff hours per guest": "Total staff hours / Number of guests",
                "Staff to guest ratio": "Number of staff / Guests",
                "Overtime cost (%)": "Overtime / Total labor costs * 100",
                "Employee turnover cost ($)": "Recruitment and training cost for replacements"
            },
            "Enhance Supply Chain Management": {
                "Food cost savings ($)": "Savings from group purchasing",
                "Inventory turnover ratio": "Cost of goods sold / Average inventory",
                "Waste reduction (%)": "Reduced waste / Previous waste * 100",
                "Supplier contract savings ($)": "Savings from negotiated contracts"
            }
        },

        # ==================== 6. Long-term Hospitality Sustainability & Investment ====================
        "Long-term Hospitality Sustainability & Investment": {
            "Develop Strategic Service Lines": {
                "F&B investment ROI (%)": "(Revenue - Investment) / Investment * 100",
                "Room product adoption rate (%)": "New room offerings / Total launched * 100",
                "Facility upgrade cost ($)": "Investment in facilities",
                "Market leadership index": "Competitive ranking in key service areas"
            },
            "Invest in Innovation": {
                "Digital hospitality technology ROI (%)": "(Efficiency gains - Cost) / Cost * 100",
                "Booking platform adoption ROI (%)": "(Revenue - Implementation cost) / Cost * 100",
                "Guest experience innovation investment ($)": "Funding for new services",
                "Technology upgrade cycle (years)": "Average equipment refresh rate"
            },
            "Ensure Financial Sustainability": {
                "Days cash on hand": "Cash reserves / Average daily expenses",
                "Debt service coverage ratio": "Operating income / Debt payments",
                "Capital expenditure ratio (%)": "Capital spending / Depreciation * 100",
                "Reserve fund growth (%)": "Current reserves - Previous / Previous * 100"
            },
            "Build Community & Partnerships": {
                "Community program investment ($)": "Funding for community initiatives",
                "Partnership revenue growth (%)": "Current - Previous / Previous * 100",
                "Customer loyalty ROI (%)": "Value from loyalty programs / Cost",
                "Sustainability program impact ($)": "Savings or revenue from sustainability efforts"
            }
        }
    }
}
