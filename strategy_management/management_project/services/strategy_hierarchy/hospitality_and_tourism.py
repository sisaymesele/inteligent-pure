from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE

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

        # =========================================================
        # Hospitality & Tourism Customer Perspective
        # =========================================================
        "CUSTOMER_PERSPECTIVE": {

            # ---------------- GENERIC CUSTOMER PERSPECTIVE ----------------
            **GENERIC_CUSTOMER_PERSPECTIVE['Customer Perspective'],
            "Customer Experience & Satisfaction": {
                "Enhance overall guest satisfaction": {
                    "Guest satisfaction score (1–5)": "Average survey rating",
                    "Repeat guest rate (%)": "(Returning guests / Total guests) * 100",
                    "Complaint resolution rate (%)": "(Resolved complaints / Total complaints) * 100",
                    "Net Promoter Score (NPS)": "(Promoters - Detractors) / Total respondents * 100",
                },
                "Improve check-in and check-out efficiency": {
                    "Average check-in time (minutes)": "Total time / Guests checked in",
                    "Average check-out time (minutes)": "Total time / Guests checked out",
                    "Self-service kiosk usage (%)": "(Guests using kiosk / Total guests) * 100",
                    "Queue reduction (%)": "((Baseline wait - Current wait)/Baseline)*100",
                },
                "Enhance guest comfort and amenities": {
                    "Room comfort satisfaction (%)": "(Satisfied / Total surveyed) * 100",
                    "Amenity utilization rate (%)": "(Used amenities / Total amenities) * 100",
                    "Room service satisfaction (%)": "(Satisfied / Total orders) * 100",
                    "Average time to fulfill requests (minutes)": "Sum(time to fulfill) / Total requests",
                },
                "Provide personalized guest experiences": {
                    "Personalized service utilization (%)": "(Guests receiving personalized service / Total guests) * 100",
                    "Custom itinerary adoption rate (%)": "(Guests following custom itineraries / Total guests) * 100",
                    "Guest preference satisfaction (%)": "(Satisfied / Total surveyed) * 100",
                    "Loyalty program enrollment (%)": "(Enrolled guests / Total guests) * 100",
                },
                "Enhance food and beverage satisfaction": {
                    "Dining satisfaction score (1–5)": "Average rating",
                    "Meal delivery timeliness (%)": "(On-time deliveries / Total orders) * 100",
                    "Menu variety rating (1–5)": "Average guest score",
                    "Special dietary request fulfillment (%)": "(Requests fulfilled / Total requests) * 100",
                },
                "Improve guest feedback mechanisms": {
                    "Feedback response rate (%)": "(Responded feedback / Total feedback) * 100",
                    "Average time to address complaints (hours)": "Sum(time to resolve)/Total complaints",
                    "Guest suggestion adoption rate (%)": "(Implemented suggestions / Total suggestions) * 100",
                    "Post-stay survey completion rate (%)": "(Surveys completed / Total guests) * 100",
                },
            },

            "Service Accessibility & Convenience": {
                "Increase online booking adoption": {
                    "Online booking rate (%)": "(Online bookings / Total bookings) * 100",
                    "Booking confirmation time (hours)": "Average time to confirm",
                    "Mobile app usage rate (%)": "(Guests using app / Total guests) * 100",
                    "Booking error rate (%)": "(Booking errors / Total bookings) * 100",
                },
                "Enhance transportation and transfer services": {
                    "Shuttle utilization rate (%)": "(Guests using shuttle / Total guests) * 100",
                    "Transfer punctuality (%)": "(On-time transfers / Total transfers) * 100",
                    "Guest satisfaction with transfers (%)": "(Satisfied / Total surveyed) * 100",
                    "Average transfer wait time (minutes)": "Sum(wait time) / Total transfers",
                },
                "Improve accessibility for special needs guests": {
                    "Accessible room availability (%)": "(Accessible rooms / Total rooms) * 100",
                    "Assistive service usage (%)": "(Guests using service / Total needing) * 100",
                    "Special needs satisfaction (%)": "(Satisfied / Total surveyed) * 100",
                    "Staff trained in accessibility (%)": "(Trained / Total staff) * 100",
                },
                "Increase information availability": {
                    "Information desk utilization (%)": "(Guests assisted / Total guests) * 100",
                    "Digital guide usage (%)": "(Guests using app / Total guests) * 100",
                    "Guest satisfaction with information (%)": "(Satisfied / Total surveyed) * 100",
                    "Multilingual support coverage (%)": "(Languages offered / Required languages) * 100",
                },
                "Enhance booking flexibility": {
                    "Flexible cancellation rate (%)": "(Bookings using flexibility / Total bookings) * 100",
                    "Booking modification success rate (%)": "(Successful modifications / Total requests) * 100",
                    "Guest satisfaction with policies (%)": "(Satisfied / Total surveyed) * 100",
                    "Refund processing time (hours)": "Average time to process refund",
                },
                "Support loyalty and rewards programs": {
                    "Loyalty program participation (%)": "(Participants / Eligible guests) * 100",
                    "Reward redemption rate (%)": "(Redeemed / Total rewards) * 100",
                    "Guest satisfaction with rewards (%)": "(Satisfied / Total surveyed) * 100",
                    "Repeat booking increase (%)": "((Repeat bookings current - Baseline)/Baseline)*100",
                },
            },

            "Safety, Hygiene & Trust": {
                "Enhance food safety standards": {
                    "Hygiene inspection compliance (%)": "(Passed inspections / Total inspections) * 100",
                    "Guest satisfaction with food hygiene (%)": "(Satisfied / Total surveyed) * 100",
                    "Reported food safety incidents": "Number of incidents",
                    "Staff trained in food safety (%)": "(Trained staff / Total staff) * 100",
                },
                "Improve facility cleanliness": {
                    "Daily cleanliness audit compliance (%)": "(Compliant / Total areas) * 100",
                    "Guest satisfaction with cleanliness (%)": "(Satisfied / Total surveyed) * 100",
                    "Incident rate due to hygiene lapses": "Number of reported incidents",
                    "Cleaning staff coverage (%)": "(Active staff / Required staff) * 100",
                },
                "Strengthen emergency preparedness": {
                    "Emergency drill completion (%)": "(Drills conducted / Planned drills) * 100",
                    "Staff trained in emergency response (%)": "(Trained staff / Total staff) * 100",
                    "Guest awareness of emergency procedures (%)": "(Guests aware / Total guests) * 100",
                    "Average response time to emergencies (minutes)": "Total response time / Number of events",
                },
                "Enhance cybersecurity and guest data protection": {
                    "Guest data breach incidents": "Number of incidents",
                    "Staff cybersecurity training (%)": "(Trained / Total staff) * 100",
                    "System uptime (%)": "(Available hours / Total hours) * 100",
                    "Guest satisfaction with digital security (%)": "(Satisfied / Total surveyed) * 100",
                },
                "Improve safety perception": {
                    "Guest perception of safety score (1–5)": "Average rating",
                    "Incident reporting rate (%)": "(Reported incidents / Total guests) * 100",
                    "Resolution satisfaction (%)": "(Satisfied with resolution / Total complaints) * 100",
                    "Safety signage compliance (%)": "(Compliant signs / Total required) * 100",
                },
                "Strengthen travel insurance and guarantees": {
                    "Guest uptake of insurance (%)": "(Guests insured / Total guests) * 100",
                    "Claims settlement success rate (%)": "(Successful claims / Total claims) * 100",
                    "Guest satisfaction with coverage (%)": "(Satisfied / Total surveyed) * 100",
                    "Insurance claim processing time (days)": "Average time to settle claim",
                },
            },

            "Digital Access & Engagement": {
                "Increase online check-in adoption": {
                    "Online check-in rate (%)": "(Checked-in online / Total guests) * 100",
                    "Mobile app adoption (%)": "(Guests using app / Total guests) * 100",
                    "Average check-in time reduction (%)": "((Baseline - Current)/Baseline)*100",
                    "Guest satisfaction with digital check-in (%)": "(Satisfied / Total surveyed) * 100",
                },
                "Improve Wi-Fi and connectivity services": {
                    "Wi-Fi uptime (%)": "(Available hours / Total hours) * 100",
                    "Guest satisfaction with Wi-Fi (%)": "(Satisfied / Total surveyed) * 100",
                    "Bandwidth adequacy (%)": "(Sufficient bandwidth hours / Total hours) * 100",
                    "Connectivity complaint rate (%)": "(Complaints / Total guests) * 100",
                },
                "Enhance digital guest engagement": {
                    "App engagement rate (%)": "(Active app users / Total registered guests) * 100",
                    "Digital concierge utilization (%)": "(Guests using digital concierge / Total guests) * 100",
                    "Online service requests completed (%)": "(Requests completed / Total requests) * 100",
                    "Guest satisfaction with digital services (%)": "(Satisfied / Total surveyed) * 100",
                },
                "Provide virtual tours and experiences": {
                    "Virtual tour participation (%)": "(Participants / Total guests) * 100",
                    "Feedback on virtual tours (1–5)": "Average rating",
                    "Conversion rate from virtual tours (%)": "(Bookings / Virtual tour participants) * 100",
                    "Repeat virtual engagement (%)": "(Repeat participants / Total virtual guests) * 100",
                },
                "Strengthen cybersecurity for digital bookings": {
                    "Secure booking transaction rate (%)": "(Secure transactions / Total transactions) * 100",
                    "System uptime (%)": "(Available hours / Total hours) * 100",
                    "Data breach incidents": "Number of incidents",
                    "Guest satisfaction with digital security (%)": "(Satisfied / Total surveyed) * 100",
                },
                "Leverage guest data analytics": {
                    "Personalized offer adoption rate (%)": "(Guests using personalized offers / Total guests) * 100",
                    "Guest retention increase (%)": "((Retention current - Baseline)/Baseline)*100",
                    "Predictive satisfaction score accuracy (%)": "(Correct predictions / Total predictions) * 100",
                    "Engagement growth rate (%)": "((Current - Previous)/Previous)*100",
                },
            },
        }
    }
}
