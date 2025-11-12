from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE
from management_project.services.strategy_hierarchy.internal_process_perspective import (
    GENERIC_INTERNAL_PROCESS_PERSPECTIVE,
)
from management_project.services.strategy_hierarchy.learning_and_growth_perspective import (
    GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE,
)

HOSPITALITY_AND_TOURISM_PERSPECTIVE = {
    "Financial Perspective": {
        # Core generic financial objectives
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],

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
    },

    # =========================================================
    # Hospitality & Tourism Customer Perspective
    # =========================================================
    "Customer Perspective": {

        # ---------------- GENERIC CUSTOMER PERSPECTIVE ----------------
        **GENERIC_CUSTOMER_PERSPECTIVE["Customer Perspective"],
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
    },

    "Internal Process Perspective": {

        **GENERIC_INTERNAL_PROCESS_PERSPECTIVE["Internal Process Perspective"],

        # -------------------- 1. Front Office & Guest Services --------------------
        "Front Office & Guest Services": {
            "Streamline check-in/check-out processes": {
                "Average processing time (minutes)": "Time from arrival to room assignment",
                "Staff adherence to protocol (%)": "(Tasks completed as per SOP / Total tasks) * 100",
                "Queue management efficiency": "Internal score of queue handling",
                "Error rate in guest data entry (%)": "(Incorrect entries / Total entries) * 100"
            },
            "Enhance internal room assignment procedures": {
                "Room allocation accuracy (%)": "(Correct room assignments / Total assignments) * 100",
                "Staff coordination efficiency": "Internal scheduling and handoff score",
                "Internal room status update time (min)": "Average time to update room status",
                "Priority handling response time (min)": "Average time for VIP/priority requests"
            },
            "Optimize internal reservation handling": {
                "Reservation entry accuracy (%)": "(Correct entries / Total reservations) * 100",
                "Processing time per reservation (min)": "Average internal processing time",
                "Internal confirmation rate (%)": "(Confirmed internally / Total reservations) * 100",
                "Cancellation update time (hours)": "Average internal update time"
            },
            "Strengthen concierge & service coordination": {
                "Internal request fulfillment rate (%)": "(Requests completed / Total requests) * 100",
                "Response time to service requests (min)": "Average internal response time",
                "Staff task completion adherence (%)": "Tasks done as per internal SOP",
                "Coordination errors (#)": "Internal communication mistakes logged"
            },
            "Manage internal complaint logging & resolution": {
                "Complaint logging accuracy (%)": "(Logged correctly / Total complaints) * 100",
                "Resolution follow-up rate (%)": "(Followed-up / Total complaints) * 100",
                "Internal response time (hours)": "Average response time to complaints",
                "Escalation handling efficiency": "Internal escalation resolution score"
            },
            "Ensure internal guest data management compliance": {
                "Data entry accuracy (%)": "(Accurate entries / Total entries) * 100",
                "Data audit completion rate (%)": "(Audited / Total required) * 100",
                "Access authorization compliance (%)": "(Authorized access / Total accesses) * 100",
                "Data correction turnaround (hours)": "Average time to correct errors"
            },
        },

        # -------------------- 2. Housekeeping & Facility Management --------------------
        "Housekeeping & Facility Management": {
            "Improve internal room cleaning procedures": {
                "Room readiness time (minutes)": "Average internal cleaning time",
                "Cleaning checklist compliance (%)": "(Tasks completed / Total tasks) * 100",
                "Inspection pass rate (%)": "(Passed inspections / Total rooms checked) * 100",
                "Rework rate (%)": "(Rooms needing rework / Total rooms) * 100"
            },
            "Optimize linen and inventory management": {
                "Inventory update accuracy (%)": "(Correct entries / Total entries) * 100",
                "Replenishment lead time (hours)": "Average internal lead time",
                "Stock discrepancy rate (%)": "(Discrepancies / Total inventory) * 100",
                "Internal audit completion (%)": "(Completed audits / Total audits) * 100"
            },
            "Enhance preventive maintenance scheduling": {
                "Maintenance schedule adherence (%)": "(Completed on time / Total planned) * 100",
                "Average downtime per asset (hours)": "Internal downtime tracking",
                "Work order completion rate (%)": "(Completed / Assigned) * 100",
                "Equipment inspection compliance (%)": "(Inspected / Total equipment) * 100"
            },
            "Strengthen waste management & sustainability": {
                "Waste segregation compliance (%)": "(Compliant / Total areas) * 100",
                "Internal recycling rate (%)": "(Recycled / Total waste) * 100",
                "Hazardous waste handling errors (#)": "Logged internal errors",
                "Sustainability initiative completion (%)": "(Completed / Planned) * 100"
            },
            "Manage internal facility safety checks": {
                "Safety checklist completion (%)": "(Completed / Total required) * 100",
                "Internal hazard reporting rate (#)": "Reported hazards",
                "Corrective actions implemented (%)": "(Implemented / Identified) * 100",
                "Inspection follow-up time (hours)": "Average internal follow-up time"
            },
            "Optimize room and facility allocation internally": {
                "Room utilization planning accuracy (%)": "(Correct allocations / Total allocations) * 100",
                "Internal changeover coordination time (min)": "Average internal handoff time",
                "Facility booking internal adherence (%)": "(Adherence / Total bookings) * 100",
                "Internal conflict resolution time (min)": "Average time to resolve conflicts"
            },
        },

        # -------------------- 3. Food & Beverage Operations --------------------
        "Food & Beverage Operations": {
            "Improve internal kitchen workflow": {
                "Order prep time (minutes)": "Internal preparation time",
                "Recipe compliance (%)": "(Correct preparation / Total dishes) * 100",
                "Internal quality check pass rate (%)": "(Passed / Total checks) * 100",
                "Inventory usage variance (%)": "(Planned - Actual usage) / Planned * 100"
            },
            "Optimize inventory & stock rotation": {
                "Stock replenishment accuracy (%)": "(Accurate / Total items) * 100",
                "Internal wastage rate (%)": "(Wasted / Total stock) * 100",
                "FIFO adherence (%)": "(Compliant / Total items) * 100",
                "Stock discrepancy logs (#)": "Internal tracking of mismatches"
            },
            "Strengthen internal hygiene & safety compliance": {
                "Internal hygiene inspection pass rate (%)": "(Passed / Total inspections) * 100",
                "Corrective action closure rate (%)": "(Closed / Total issues) * 100",
                "Internal safety training completion (%)": "(Trained / Total staff) * 100",
                "Internal hazard reporting rate (#)": "Reported hazards"
            },
            "Enhance internal food preparation scheduling": {
                "Prep schedule adherence (%)": "(On-time / Total scheduled) * 100",
                "Internal cross-functional coordination efficiency": "Score of coordination",
                "Average preparation delay (min)": "Internal measurement",
                "Internal menu update implementation (%)": "(Implemented / Planned) * 100"
            },
            "Manage internal catering & banquet operations": {
                "Internal event setup adherence (%)": "(On-time / Total events) * 100",
                "Internal resource allocation accuracy (%)": "(Correct allocation / Total resources) * 100",
                "Internal service sequence compliance (%)": "(Compliant / Total steps) * 100",
                "Internal client request implementation (%)": "(Implemented / Requested) * 100"
            },
            "Ensure internal equipment maintenance & calibration": {
                "Kitchen equipment inspection rate (%)": "(Inspected / Total equipment) * 100",
                "Internal maintenance completion (%)": "(Completed / Planned) * 100",
                "Calibration compliance (%)": "(Calibrated / Total equipment) * 100",
                "Internal downtime tracking (hours)": "Total internal downtime"
            },
        },

        # -------------------- 4. Event & Conference Management --------------------
        "Event & Conference Management": {
            "Improve internal event planning processes": {
                "Internal event checklist completion (%)": "(Completed / Total steps) * 100",
                "Internal timeline adherence (%)": "(On-time / Total milestones) * 100",
                "Internal task allocation accuracy (%)": "(Assigned correctly / Total tasks) * 100",
                "Internal risk identification rate (%)": "(Identified / Expected risks) * 100"
            },
            "Optimize internal resource allocation": {
                "Internal venue utilization (%)": "(Utilized / Available) * 100",
                "Internal equipment readiness (%)": "(Ready / Required) * 100",
                "Internal staffing schedule adherence (%)": "(Compliant / Planned) * 100",
                "Internal conflict resolution time (hours)": "Average internal resolution time"
            },
            "Enhance internal vendor coordination": {
                "Internal contract compliance (%)": "(Compliant / Total contracts) * 100",
                "Internal delivery tracking accuracy (%)": "(Accurate / Total deliveries) * 100",
                "Internal payment processing efficiency (%)": "(Processed on time / Total payments) * 100",
                "Internal service quality monitoring (%)": "(Monitored / Planned checks) * 100"
            },
            "Strengthen internal setup & teardown procedures": {
                "Internal setup time adherence (%)": "(On-time / Planned) * 100",
                "Internal teardown time adherence (%)": "(On-time / Planned) * 100",
                "Internal checklist compliance (%)": "(Compliant / Total steps) * 100",
                "Internal damage incident logs (#)": "Recorded internally"
            },
            "Manage internal scheduling conflicts": {
                "Internal booking conflict resolution (%)": "(Resolved / Total conflicts) * 100",
                "Internal double-booking prevention (%)": "(Prevented / Total events) * 100",
                "Internal adjustment time (hours)": "Average internal time to adjust",
                "Internal notification compliance (%)": "(Notified / Total changes) * 100"
            },
            "Ensure internal risk management": {
                "Internal contingency plan implementation (%)": "(Implemented / Planned) * 100",
                "Internal incident reporting compliance (%)": "(Reported / Total incidents) * 100",
                "Internal hazard mitigation completion (%)": "(Mitigated / Identified) * 100",
                "Internal audit completion (%)": "(Completed / Planned audits) * 100"
            },
        },

        # -------------------- 5. Spa & Wellness Operations --------------------
        "Spa & Wellness Operations": {
            "Optimize internal appointment scheduling": {
                "Internal schedule adherence (%)": "(On-time / Total appointments) * 100",
                "Internal resource allocation accuracy (%)": "(Correctly allocated / Total resources) * 100",
                "Average internal wait time (min)": "Measured internally",
                "Internal service preparation compliance (%)": "(Compliant / Total preparations) * 100"
            },
            "Enhance internal treatment protocols": {
                "Internal protocol adherence (%)": "(Followed / Total treatments) * 100",
                "Internal treatment quality score": "Average internal assessment",
                "Internal adverse event rate (%)": "(Events / Total treatments) * 100",
                "Internal staff compliance (%)": "(Compliant / Total staff) * 100"
            },
            "Strengthen internal hygiene & safety": {
                "Internal hygiene inspection pass rate (%)": "(Passed / Total checks) * 100",
                "Internal safety procedure compliance (%)": "(Compliant / Total steps) * 100",
                "Internal corrective action completion (%)": "(Completed / Planned) * 100",
                "Internal incident reporting (#)": "Logged internally"
            },
            "Manage internal product & supply inventory": {
                "Inventory accuracy (%)": "(Accurate / Total items) * 100",
                "Internal replenishment lead time (hours)": "Average internal lead time",
                "Internal stock discrepancy logs (#)": "Recorded internally",
                "Internal usage variance (%)": "(Planned - Actual) / Planned * 100"
            },
            "Improve internal staff training & skills": {
                "Training completion rate (%)": "(Completed / Required) * 100",
                "Internal competency assessment score": "Average internal evaluation",
                "Internal skill refresh adherence (%)": "(Followed / Planned) * 100",
                "Internal mentoring completion (%)": "(Completed / Planned) * 100"
            },
            "Ensure internal equipment maintenance": {
                "Inspection completion (%)": "(Completed / Planned) * 100",
                "Internal maintenance adherence (%)": "(On-time / Planned) * 100",
                "Internal downtime (hours)": "Tracked internally",
                "Internal equipment failure rate (%)": "(Failures / Total equipment) * 100"
            },
        },

        # -------------------- 6. Tour & Excursion Operations --------------------
        "Tour & Excursion Operations": {
            "Optimize internal itinerary planning": {
                "Internal itinerary accuracy (%)": "(Correct / Total itineraries) * 100",
                "Internal schedule adherence (%)": "(On-time / Planned) * 100",
                "Internal resource allocation (%)": "(Correct / Total resources) * 100",
                "Internal contingency implementation (%)": "(Implemented / Planned) * 100"
            },
            "Enhance internal transport coordination": {
                "Internal vehicle readiness (%)": "(Ready / Total vehicles) * 100",
                "Internal route adherence (%)": "(Followed / Planned) * 100",
                "Internal trip delay tracking (min)": "Average internal delay",
                "Internal maintenance compliance (%)": "(Vehicles maintained / Total vehicles) * 100"
            },
            "Strengthen internal guide & staff management": {
                "Internal training completion (%)": "(Completed / Required) * 100",
                "Internal competency score": "Average internal assessment",
                "Internal staff scheduling adherence (%)": "(Followed / Planned) * 100",
                "Internal incident handling (#)": "Logged internally"
            },
            "Manage internal safety & risk procedures": {
                "Internal safety audit completion (%)": "(Completed / Planned) * 100",
                "Internal emergency drill compliance (%)": "(Completed / Planned drills) * 100",
                "Internal hazard mitigation (%)": "(Mitigated / Identified) * 100",
                "Internal incident reporting rate (%)": "(Reported / Expected) * 100"
            },
            "Optimize internal booking & group coordination": {
                "Internal group booking accuracy (%)": "(Correct / Total bookings) * 100",
                "Internal schedule coordination efficiency": "Internal score",
                "Internal resource allocation adherence (%)": "(Allocated / Planned) * 100",
                "Internal conflict resolution time (hours)": "Average time internally"
            },
            "Enhance internal feedback processing": {
                "Internal feedback logging (%)": "(Logged / Total feedback) * 100",
                "Internal follow-up completion (%)": "(Followed-up / Total feedback) * 100",
                "Internal response time (hours)": "Average internal response time",
                "Internal improvement implementation (%)": "(Implemented / Planned) * 100"
            },
        },

        # -------------------- 7. Entertainment & Recreation Operations --------------------
        "Entertainment & Recreation Operations": {
            "Optimize internal activity scheduling": {
                "Internal schedule adherence (%)": "(On-time / Planned) * 100",
                "Internal resource allocation accuracy (%)": "(Correct / Total resources) * 100",
                "Internal delay tracking (min)": "Average internal delay",
                "Internal coordination efficiency score": "Internal measurement"
            },
            "Enhance internal staff & performer management": {
                "Internal training completion (%)": "(Completed / Required) * 100",
                "Internal competency assessment": "Average internal score",
                "Internal scheduling adherence (%)": "(Followed / Planned) * 100",
                "Internal incident reporting (#)": "Logged internally"
            },
            "Strengthen internal equipment management": {
                "Internal inspection compliance (%)": "(Completed / Planned) * 100",
                "Internal maintenance adherence (%)": "(On-time / Planned) * 100",
                "Internal failure logs (#)": "Recorded internally",
                "Internal downtime (hours)": "Tracked internally"
            },
            "Manage internal safety procedures": {
                "Internal safety audit completion (%)": "(Completed / Planned) * 100",
                "Internal hazard mitigation (%)": "(Mitigated / Identified) * 100",
                "Internal emergency drill compliance (%)": "(Completed / Planned) * 100",
                "Internal incident response time (minutes)": "Average internal response"
            },
            "Improve internal guest experience operations": {
                "Internal quality check compliance (%)": "(Compliant / Total checks) * 100",
                "Internal SOP adherence (%)": "(Followed / Total procedures) * 100",
                "Internal corrective actions (%)": "(Implemented / Planned) * 100",
                "Internal delay resolution time (min)": "Average internal time"
            },
            "Optimize internal logistics & resource flow": {
                "Internal resource availability (%)": "(Available / Required) * 100",
                "Internal logistics compliance (%)": "(Followed / Planned) * 100",
                "Internal equipment allocation accuracy (%)": "(Correct / Total equipment) * 100",
                "Internal coordination score": "Internal measurement"
            },
        },

        # -------------------- 8. Procurement & Vendor Coordination --------------------
        "Procurement & Vendor Coordination": {
            "Optimize internal supplier selection": {
                "Internal supplier evaluation completion (%)": "(Completed / Planned) * 100",
                "Internal approval cycle time (days)": "Average internal time",
                "Internal contract compliance (%)": "(Compliant / Total contracts) * 100",
                "Internal vendor performance score": "Average internal score"
            },
            "Enhance internal purchase order processing": {
                "PO processing time (days)": "Internal average time",
                "Internal PO accuracy (%)": "(Correct / Total POs) * 100",
                "Internal approval adherence (%)": "(Followed / Required) * 100",
                "Internal duplicate PO detection (#)": "Logged internally"
            },
            "Strengthen internal inventory control": {
                "Internal stock reconciliation accuracy (%)": "(Accurate / Total items) * 100",
                "Internal cycle count completion (%)": "(Completed / Planned) * 100",
                "Internal reorder point adherence (%)": "(Followed / Total items) * 100",
                "Internal discrepancy resolution time (hours)": "Average internal resolution time"
            },
            "Manage internal vendor coordination": {
                "Internal delivery timeliness (%)": "(On-time / Total deliveries) * 100",
                "Internal contract fulfillment (%)": "(Fulfilled / Total contracts) * 100",
                "Internal communication logs (#)": "Logged internally",
                "Internal performance review completion (%)": "(Completed / Planned reviews) * 100"
            },
            "Improve internal procurement cost management": {
                "Internal cost variance (%)": "(Budgeted - Actual) / Budgeted * 100",
                "Internal expense approval adherence (%)": "(Compliant / Total approvals) * 100",
                "Internal cost-saving initiative completion (%)": "(Implemented / Planned) * 100",
                "Internal budget reconciliation (%)": "(Reconciled / Total accounts) * 100"
            },
            "Ensure internal compliance & quality": {
                "Internal procurement audit completion (%)": "(Completed / Planned) * 100",
                "Internal quality check compliance (%)": "(Compliant / Total checks) * 100",
                "Internal corrective action closure (%)": "(Closed / Total issues) * 100",
                "Internal regulatory adherence (%)": "(Compliant / Total checks) * 100"
            },
        },
    },

    "Learning & Growth Perspective": {
        **GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE["Learning & Growth Perspective"],
    },

}
