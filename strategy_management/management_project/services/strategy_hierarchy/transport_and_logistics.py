
from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE


TRANSPORT_AND_LOGISTICS_PERSPECTIVE = {
    "Financial Perspective": {
# -------------------- Generic Finance --------------------
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],

        # -------------------- Passenger Revenue & Profitability Management --------------------
        "Passenger Revenue & Profitability Management": {
            "Maximize Passenger Revenue": {
                "Passenger fare revenue growth": "((Current passenger revenue - Previous) / Previous) * 100",
                "Revenue per passenger/km": "Total passenger revenue / Total passenger kilometers",
                "Average revenue per passenger trip": "Total passenger trip revenue / Number of trips",
                "Load factor revenue contribution": "(Revenue from full occupancy / Total passenger revenue) * 100"
            },
            "Maximize Passenger Profit": {
                "Passenger profit margin": "(Passenger revenue - Passenger total costs) / Passenger revenue * 100",
                "Net profit per passenger trip": "Total passenger profit / Number of trips",
                "Profit per passenger/km": "Passenger profit / Total passenger kilometers",
                "High-margin route contribution": "(Revenue from high-margin routes / Total passenger revenue) * 100"
            },
            "Enhance Passenger Revenue Diversification": {
                "Revenue from value-added passenger services": "(Revenue from passenger auxiliary services / Total passenger revenue) * 100",
                "Contract vs spot passenger revenue ratio": "(Contract passenger revenue / Spot passenger revenue) * 100",
                "Seasonal passenger revenue optimization": "Revenue stability across peak and low passenger demand periods",
                "Multi-modal passenger revenue contribution": "(Revenue from intermodal passenger services / Total passenger revenue) * 100"
            },
            "Optimize Passenger Pricing": {
                "Dynamic passenger pricing effectiveness": "Revenue improvement from dynamic passenger pricing",
                "Passenger contract rate compliance": "(Contracts with agreed passenger rates / Total passenger contracts) * 100",
                "Passenger fuel surcharge recovery rate": "Percentage of passenger fuel cost increases recovered through surcharges",
                "Passenger price premium achievement": "(Actual fare - Market average fare) / Market average fare * 100"
            }
        },

        # -------------------- Freight Revenue & Profitability Management --------------------
        "Freight Revenue & Profitability Management": {
            "Maximize Freight Revenue": {
                "Freight revenue growth": "((Current freight revenue - Previous) / Previous) * 100",
                "Revenue per ton/km": "Total freight revenue / Total ton kilometers",
                "Average revenue per freight trip": "Total freight trip revenue / Number of trips",
                "On-time delivery revenue contribution": "(Revenue from on-time deliveries / Total freight revenue) * 100"
            },
            "Maximize Freight Profit": {
                "Freight profit margin": "(Freight revenue - Freight total costs) / Freight revenue * 100",
                "Net profit per freight trip": "Total freight profit / Number of trips",
                "Profit per ton/km": "Freight profit / Total ton kilometers",
                "High-margin freight route contribution": "(Revenue from high-margin freight routes / Total freight revenue) * 100"
            },
            "Enhance Freight Revenue Diversification": {
                "Revenue from value-added freight services": "(Revenue from logistics or value-added freight services / Total freight revenue) * 100",
                "Contract vs spot freight revenue ratio": "(Contract freight revenue / Spot freight revenue) * 100",
                "Seasonal freight revenue optimization": "Revenue stability across high/low freight demand periods",
                "Multi-modal freight revenue contribution": "(Revenue from intermodal freight services / Total freight revenue) * 100"
            },
            "Optimize Freight Pricing": {
                "Dynamic freight pricing effectiveness": "Revenue improvement from dynamic freight pricing",
                "Freight contract rate compliance": "(Contracts with agreed freight rates / Total freight contracts) * 100",
                "Freight fuel surcharge recovery rate": "Percentage of freight fuel cost increases recovered through surcharges",
                "Freight price premium achievement": "(Actual freight rate - Market average) / Market average * 100"
            }
        },

        # -------------------- Passenger & Freight Cost Management --------------------
        "Passenger Cost Management & Efficiency": {
            "Optimize Passenger Operating Costs": {
                "Passenger cost per passenger/km": "Total passenger costs / Total passenger kilometers",
                "Passenger fuel & energy cost per passenger": "Allocated fuel cost / Total passengers",
                "Passenger maintenance cost per passenger": "Maintenance cost for passenger vehicles / Total passengers",
                "Passenger staff cost efficiency": "Passengers served per staff cost unit"
            },
            "Reduce Passenger Route Costs": {
                "Passenger route cost efficiency": "Actual passenger route cost / Optimal route cost",
                "Passenger empty running reduction": "Reduction in empty passenger vehicle movements (%)",
                "Passenger toll and road cost management": "Toll costs as percentage of passenger route costs",
                "Passenger border crossing cost optimization": "Cost and time efficiency for passenger border crossings"
            },
            "Passenger Labor Productivity": {
                "Revenue per passenger employee": "Total passenger revenue / Number of passenger employees",
                "Passenger labor cost % of revenue": "(Passenger labor costs / Passenger revenue) * 100",
                "Passenger driver productivity": "Kilometers driven per passenger driver per day",
                "Passenger maintenance labor efficiency": "Passenger maintenance tasks completed per labor hour"
            }
        },
        "Freight Cost Management & Efficiency": {
            "Optimize Freight Operating Costs": {
                "Freight cost per ton/km": "Total freight costs / Total ton kilometers",
                "Freight fuel & energy cost per ton": "Allocated fuel cost / Total tons transported",
                "Freight maintenance cost per ton": "Maintenance cost for freight vehicles / Total tons",
                "Freight staff cost efficiency": "Tons transported per staff cost unit"
            },
            "Reduce Freight Route Costs": {
                "Freight route cost efficiency": "Actual freight route cost / Optimal route cost",
                "Freight empty running reduction": "Reduction in empty freight vehicle movements (%)",
                "Freight toll and road cost management": "Toll costs as percentage of freight route costs",
                "Freight border crossing cost optimization": "Cost and time efficiency for freight border crossings"
            },
            "Freight Labor Productivity": {
                "Revenue per freight employee": "Total freight revenue / Number of freight employees",
                "Freight labor cost % of revenue": "(Freight labor costs / Freight revenue) * 100",
                "Freight driver productivity": "Tons/km moved per freight driver per day",
                "Freight maintenance labor efficiency": "Freight maintenance tasks completed per labor hour"
            }
        },

        # -------------------- Passenger & Freight Capital Management --------------------
        "Passenger Capital Management & Investment": {
            "Enhance Passenger Asset Utilization": {
                "Passenger vehicle utilization rate": "(Actual passenger vehicle usage hours / Available hours) * 100",
                "Passenger fleet turnover ratio": "Passenger revenue / Average passenger fleet value",
                "Passenger trailer utilization rate": "(Loaded passenger trailers / Total trailer time) * 100",
                "Passenger terminal capacity utilization": "(Passenger throughput / Design capacity) * 100"
            },
            "Passenger Working Capital Management": {
                "Passenger cash conversion cycle (days)": "Days inventory + Days sales outstanding - Days payables outstanding",
                "Passenger working capital turnover": "Passenger revenue / Average passenger working capital",
                "Passenger accounts receivable collection period": "Average days to collect passenger payments",
                "Passenger fuel inventory turnover": "Passenger fuel cost / Average passenger fuel inventory"
            },
            "Passenger Investment Optimization": {
                "Return on passenger fleet investments": "(Net benefits from passenger fleet / Total fleet investment) * 100",
                "Passenger technology adoption payback period": "Investment cost / Annual net passenger benefits",
                "Passenger infrastructure ROI": "(Passenger benefits from infrastructure / Infrastructure cost) * 100",
                "Passenger vehicle replacement optimization": "Achievement of optimal replacement timing"
            }
        },
        "Freight Capital Management & Investment": {
            "Enhance Freight Asset Utilization": {
                "Freight vehicle utilization rate": "(Actual freight vehicle usage hours / Available hours) * 100",
                "Freight fleet turnover ratio": "Freight revenue / Average freight fleet value",
                "Freight trailer utilization rate": "(Loaded freight trailers / Total trailer time) * 100",
                "Freight terminal capacity utilization": "(Freight throughput / Design capacity) * 100"
            },
            "Freight Working Capital Management": {
                "Freight cash conversion cycle (days)": "Days inventory + Days sales outstanding - Days payables outstanding",
                "Freight working capital turnover": "Freight revenue / Average freight working capital",
                "Freight accounts receivable collection period": "Average days to collect freight payments",
                "Freight fuel inventory turnover": "Freight fuel cost / Average freight fuel inventory"
            },
            "Freight Investment Optimization": {
                "Return on freight fleet investments": "(Net benefits from freight fleet / Total fleet investment) * 100",
                "Freight technology adoption payback period": "Investment cost / Annual net freight benefits",
                "Freight infrastructure ROI": "(Freight benefits from infrastructure / Infrastructure cost) * 100",
                "Freight vehicle replacement optimization": "Achievement of optimal replacement timing"
            }
        }
    },

    # -------------------- Transport & Logistics Economic Development --------------------
    "Transport Economic Development": {

        "Transport GDP Contribution": {
            "Increase national GDP contribution": {
                "Transport sector contribution to GDP (%)": "Value added by transport / Total GDP * 100",
                "Annual GDP growth from transport (%)": "(Current - Previous) / Previous * 100",
                "Indirect GDP impact ($)": "Estimated GDP generated via logistics multiplier effect",
                "Transport value added per capita ($)": "Total transport sector value added / Population"
            },
            "Enhance freight & passenger GDP impact": {
                "Freight sector GDP contribution (%)": "Value added by freight / Total GDP * 100",
                "Passenger transport GDP contribution (%)": "Value added by passenger transport / Total GDP * 100",
                "Intermodal GDP efficiency index": "GDP per unit transport / Total GDP",
                "Transport GDP multiplier effect": "Indirect economic impact per $ invested"
            }
        },

        "Support Local Entrepreneurship & SMEs": {
            "Promote local transport startups": {
                "New transport startups funded": "Number of local startups financially supported",
                "Revenue from funded startups ($)": "Revenue generated by funded transport startups",
                "Startup survival rate (%)": "Startups still operational after 1 year / Total funded * 100",
                "Jobs created by startups": "Number of new jobs generated by supported startups"
            },
            "Enhance SME participation in logistics": {
                "SME suppliers engaged": "Number of SMEs supplying logistics services",
                "Procurement from SMEs ($)": "Total purchases from SMEs",
                "SME revenue growth (%)": "(Current SME revenue - Previous) / Previous * 100",
                "SME satisfaction rate (%)": "Average satisfaction score from SME surveys"
            }
        },
        "Create Employment Opportunities": {
            "Direct logistics job creation": {
                "Jobs created in transport & logistics": "Number of direct jobs created",
                "Part-time employment growth (%)": "(Current - Previous) / Previous * 100",
                "Youth employment (%)": "Number of youth employed / Total new hires * 100",
                "Employee retention rate (%)": "Employees retained / Total hired * 100"
            },
            "Promote workforce skills & training": {
                "Training programs conducted": "Number of skill development programs",
                "Employees trained": "Total number of employees trained",
                "Training completion rate (%)": "Completed trainings / Total enrolled * 100",
                "Workforce productivity improvement (%)": "Revenue per employee growth %"
            }
        },
        "Regional & Rural Development": {
            "Expand regional logistics networks": {
                "Revenue from regional hubs ($)": "Revenue generated in regional areas",
                "Regional jobs created": "Number of jobs created in regional hubs",
                "Regional hub growth (%)": "(Current hubs - Previous) / Previous * 100",
                "Customer satisfaction in regions (%)": "Average satisfaction score from regional customers"
            },
            "Support rural transport & connectivity": {
                "Revenue from rural services ($)": "Revenue generated in rural areas",
                "Rural employment created": "Number of jobs created in rural areas",
                "Rural service coverage (%)": "Population served / Total population * 100",
                "Community engagement initiatives (#)": "Number of programs promoting rural inclusion"
            }
        },
        "Promote Innovation & Digital Transformation": {
            "Invest in digital logistics solutions": {
                "Investment in logistics tech ($)": "Amount invested in technology",
                "New digital tools deployed": "Number of digital tools implemented",
                "Online booking revenue growth (%)": "(Current - Previous) / Previous * 100",
                "Customer adoption of digital solutions (%)": "Digital users / Total customers * 100"
            },
            "Encourage sustainable transport solutions": {
                "Revenue from green logistics ($)": "Revenue from eco-friendly operations",
                "Fleet electrification ratio (%)": "Electric vehicles / Total fleet * 100",
                "Reduction in carbon emissions (%)": "(Previous - Current) / Previous * 100",
                "Number of sustainable initiatives": "Count of projects promoting green logistics"
            }
        },
    },

    "Customer Perspective": {
        "Service Quality & Reliability": {
            "Enhance On-Time Performance": {
                "On-time delivery rate": "(On-time deliveries / Total deliveries) * 100",
                "Schedule adherence": "(Trips completed on schedule / Total trips) * 100",
                "Transit time reliability": "Consistency of actual vs promised transit times",
                "Pick-up window compliance": "(Pick-ups within promised window / Total pick-ups) * 100"
            },
            "Improve Service Quality": {
                "Damage-free delivery rate": "(Damage-free deliveries / Total deliveries) * 100",
                "Documentation accuracy": "(Accurate documentation / Total shipments) * 100",
                "Cargo security performance": "Percentage of shipments with no security incidents",
                "Temperature control compliance": "(Maintained temperature / Required temperature control) * 100"
            },
            "Enhance Customer Experience": {
                "Customer satisfaction score": "Average rating from customer surveys",
                "First-contact resolution rate": "(Issues resolved first contact / Total issues) * 100",
                "Proactive communication effectiveness": "Customer rating of communication quality",
                "Ease of doing business score": "Customer rating of business process simplicity"
            },
            "Strengthen Service Consistency": {
                "Service level agreement compliance": "(SLA requirements met / Total SLAs) * 100",
                "Performance variance reduction": "Reduction in service performance fluctuations",
                "Quality certification achievement": "(Services meeting quality standards / Total services) * 100",
                "Customer complaint resolution": "(Resolved complaints / Total complaints) * 100"
            },
            "Optimize Service Flexibility": {
                "Service customization capability": "Ability to customize services for customer needs",
                "Emergency response effectiveness": "Response time and quality for urgent requests",
                "Service adaptation rate": "Speed of adapting services to changing customer requirements",
                "Special handling capability": "Ability to handle specialized cargo requirements"
            }
        },

        "Accessibility & Convenience": {
            "Improve Service Accessibility": {
                "Geographic coverage expansion": "Percentage increase in service areas",
                "Service frequency optimization": "Trips per week on key routes",
                "Last-mile delivery coverage": "Percentage of population covered by last-mile services",
                "24/7 service availability": "Hours of service availability per week"
            },
            "Enhance Digital Access": {
                "Online booking adoption": "(Online bookings / Total bookings) * 100",
                "Mobile app utilization": "Percentage of customers using mobile services",
                "Digital documentation usage": "(Electronic documents / Total documents) * 100",
                "Self-service portal engagement": "Customer usage of self-service features"
            },
            "Strengthen Network Connectivity": {
                "Intermodal connection efficiency": "Time and cost efficiency of mode transfers",
                "Route network density": "Number of connected destinations",
                "Transit point accessibility": "Ease of access to loading/unloading facilities",
                "Remote area service coverage": "Percentage of remote areas served"
            },
            "Optimize Customer Touchpoints": {
                "Customer service center availability": "Hours of customer service operation",
                "Multi-channel service integration": "Seamlessness of service across channels",
                "Local presence effectiveness": "Quality of local customer service representation",
                "Digital assistant utilization": "Usage rate of AI-powered customer assistance"
            }
        },

        "Safety & Security": {
            "Enhance Safety Performance": {
                "Accident rate reduction": "((Previous accidents - Current accidents) / Previous accidents) * 100",
                "Safety compliance score": "Results from safety audits and inspections",
                "Driver safety training completion": "(Trained drivers / Total drivers) * 100",
                "Vehicle safety inspection pass rate": "(Passed inspections / Total inspections) * 100"
            },
            "Improve Cargo Security": {
                "Cargo theft prevention": "Reduction in cargo theft incidents",
                "Security protocol compliance": "Adherence to security procedures",
                "Tracking system coverage": "(Tracked shipments / Total shipments) * 100",
                "Tamper-evident seal usage": "(Sealed shipments / Total shipments) * 100"
            },
            "Strengthen Cybersecurity": {
                "Data protection effectiveness": "Score from cybersecurity audits",
                "Privacy compliance rate": "Adherence to data privacy regulations",
                "System breach prevention": "Reduction in cybersecurity incidents",
                "Customer data security": "Protection level for customer information"
            },
            "Enhance Facility Security": {
                "Terminal security assessment": "Score from facility security evaluations",
                "Access control effectiveness": "Control of facility access points",
                "Surveillance system coverage": "Percentage of facilities with adequate surveillance",
                "Emergency response preparedness": "Readiness for security emergencies"
            }
        },

        "Customer Relationship Management": {
            "Increase Customer Loyalty": {
                "Customer retention rate": "(Retained customers / Total customers) * 100",
                "Net Promoter Score (NPS)": "Percentage of promoters minus percentage of detractors",
                "Customer lifetime duration": "Average duration of customer relationships",
                "Repeat business rate": "(Repeat customers / Total customers) * 100"
            },
            "Improve Customer Service": {
                "Response time efficiency": "Average time to respond to customer inquiries",
                "Service recovery effectiveness": "Customer satisfaction after service recovery",
                "Account management quality": "Customer rating of account management services",
                "Proactive service notification": "Percentage of service issues communicated proactively"
            },
            "Enhance Customer Insights": {
                "Customer feedback utilization": "Percentage of feedback implemented in improvements",
                "Customer needs anticipation": "Ability to predict and meet emerging customer needs",
                "Segmentation effectiveness": "Accuracy of customer segmentation strategies",
                "Customer value understanding": "Depth of understanding of customer business needs"
            },
            "Optimize Pricing Perception": {
                "Price transparency rating": "Customer rating of pricing clarity",
                "Value for money perception": "Customer assessment of service value",
                "Competitive pricing positioning": "Price comparison with competitor offerings",
                "Billing accuracy rate": "(Accurate invoices / Total invoices) * 100"
            }
        },

        "Stakeholder & Community Relations": {
            "Strengthen Community Engagement": {
                "Community investment ratio": "(Community investment / Total profit) * 100",
                "Local employment contribution": "(Local employees / Total employees) * 100",
                "Community partnership projects": "Number of active community development initiatives",
                "Community perception score": "Results from community satisfaction surveys"
            },
            "Manage Regulatory Relationships": {
                "Regulatory compliance rate": "(Compliant operations / Total operations) * 100",
                "Permit acquisition efficiency": "Time and cost of regulatory permit acquisition",
                "Government relationship quality": "Effectiveness of government stakeholder engagement",
                "Policy advocacy effectiveness": "Success in influencing favorable transport policies"
            },
            "Enhance Industry Collaboration": {
                "Industry association participation": "Level of engagement in industry organizations",
                "Standardization contribution": "Involvement in industry standards development",
                "Knowledge sharing initiatives": "Number of industry knowledge sharing activities",
                "Collaborative innovation projects": "Participation in joint industry innovation"
            },
            "Develop Sustainable Community Impact": {
                "Local economic development": "Contribution to local economic growth",
                "Environmental impact mitigation": "Reduction of negative environmental impacts",
                "Social responsibility initiatives": "Number and impact of CSR programs",
                "Stakeholder trust index": "Composite measure of stakeholder confidence"
            }
        }
    },

    "Internal Process Perspective": {
        "Fleet Operations Management": {
            "Optimize Vehicle Utilization": {
                "Vehicle availability rate": "(Available vehicles / Total fleet) * 100",
                "Load factor optimization": "Average vehicle capacity utilization",
                "Deadhead reduction": "Percentage reduction in empty running",
                "Preventive maintenance compliance": "(Completed PM / Scheduled PM) * 100"
            },
            "Enhance Maintenance Efficiency": {
                "Mean time between failures": "Average operating hours between failures",
                "Maintenance cost per km": "Total maintenance cost / Total kilometers",
                "Roadside breakdown reduction": "Reduction in unscheduled roadside repairs",
                "First-time fix rate": "(Issues fixed first time / Total issues) * 100"
            },
            "Improve Fleet Performance": {
                "Vehicle uptime percentage": "(Operational hours / Total available hours) * 100",
                "Fuel efficiency improvement": "((Previous consumption - Current consumption) / Previous consumption) * 100",
                "Tire life optimization": "Average tire life vs expected life",
                "Component replacement optimization": "Optimal timing of component replacements"
            },
            "Optimize Fleet Composition": {
                "Right-sizing effectiveness": "Match between fleet composition and operational needs",
                "Specialized equipment adequacy": "Adequacy of specialized transport equipment",
                "Fleet age optimization": "Optimal balance of vehicle ages",
                "Technology integration in fleet": "Percentage of fleet with modern technology"
            }
        },

        "Route & Network Optimization": {
            "Improve Route Efficiency": {
                "Route optimization savings": "Cost savings from optimized routing",
                "Fuel efficiency per route": "Fuel consumption by route type",
                "Congestion cost reduction": "Reduction in congestion-related costs",
                "Border crossing time optimization": "Average time reduction at borders"
            },
            "Enhance Network Design": {
                "Hub efficiency improvement": "Throughput per hub operation cost",
                "Load consolidation effectiveness": "Percentage improvement in load consolidation",
                "Intermodal connectivity": "Seamless transfer between transport modes",
                "Network coverage optimization": "Service coverage vs operating cost balance"
            },
            "Optimize Dispatch Operations": {
                "Dispatch accuracy rate": "(Accurate dispatches / Total dispatches) * 100",
                "Load planning efficiency": "Time and cost of load planning",
                "Real-time routing adjustment": "Effectiveness of real-time route changes",
                "Capacity allocation optimization": "Optimal matching of capacity to demand"
            },
            "Strengthen Terminal Operations": {
                "Terminal throughput efficiency": "Units handled per terminal operating hour",
                "Dock door utilization": "(Used dock doors / Available dock doors) * 100",
                "Cross-docking effectiveness": "Percentage of freight handled through cross-docking",
                "Yard management optimization": "Efficiency of yard operations and storage"
            }
        },

        "Technology & Digital Transformation": {
            "Implement Fleet Technology": {
                "Telematics adoption rate": "(Vehicles with telematics / Total fleet) * 100",
                "GPS tracking utilization": "(Tracked vehicles / Total fleet) * 100",
                "Electronic logging device compliance": "(Compliant vehicles / Total fleet) * 100",
                "Predictive maintenance implementation": "Percentage of fleet under predictive maintenance"
            },
            "Advance Digital Operations": {
                "Digital dispatch efficiency": "Reduction in dispatch processing time",
                "Automated routing adoption": "(Automated routes / Total routes) * 100",
                "Real-time visibility implementation": "(Shipments with real-time tracking / Total shipments) * 100",
                "API integration success": "Number of successful system integrations"
            },
            "Enhance Data Analytics": {
                "Predictive analytics usage": "Extent of predictive modeling in operations",
                "Performance dashboard utilization": "Usage rate of operational performance dashboards",
                "Data-driven decision making": "Percentage of decisions based on data analytics",
                "Machine learning implementation": "Number of ML applications in operations"
            },
            "Develop Automation Solutions": {
                "Process automation rate": "Percentage of automated operational processes",
                "Robotic process implementation": "Number of RPA applications in operations",
                "Autonomous vehicle readiness": "Preparation level for autonomous vehicle integration",
                "Digital twin utilization": "Use of digital twins for operational simulation"
            }
        },

        "Supply Chain Integration": {
            "Enhance End-to-End Visibility": {
                "Supply chain visibility level": "Percentage of supply chain with real-time visibility",
                "Exception management effectiveness": "Speed and accuracy of exception handling",
                "Event prediction accuracy": "Accuracy of supply chain event predictions",
                "Multi-party collaboration platform": "Effectiveness of collaborative platforms"
            },
            "Optimize Inventory in Motion": {
                "In-transit inventory optimization": "Reduction in excess in-transit inventory",
                "Stock-out prevention": "Reduction in stock-outs due to transport issues",
                "Inventory velocity improvement": "Increase in inventory turnover through better transport",
                "Safety stock optimization": "Reduction in safety stock requirements"
            },
            "Strengthen Partner Integration": {
                "Supplier integration effectiveness": "Seamlessness of supplier integration",
                "Carrier management efficiency": "Effectiveness of carrier relationship management",
                "Customer system integration": "Depth of integration with customer systems",
                "Information sharing quality": "Quality and timeliness of partner information sharing"
            }
        },

        "Safety & Compliance Management": {
            "Enhance Safety Systems": {
                "Safety management system effectiveness": "Score from safety management audits",
                "Incident investigation quality": "Thoroughness and effectiveness of incident investigations",
                "Safety training completion rate": "(Completed safety training / Required training) * 100",
                "Safety culture assessment": "Employee rating of safety culture"
            },
            "Improve Regulatory Compliance": {
                "Regulatory audit performance": "Results from regulatory compliance audits",
                "Documentation compliance rate": "(Compliant documentation / Total documentation) * 100",
                "Permit management efficiency": "Timeliness and accuracy of permit management",
                "Environmental regulation adherence": "Compliance with environmental regulations"
            },
            "Strengthen Risk Management": {
                "Risk assessment coverage": "(Assessed risks / Total potential risks) * 100",
                "Business continuity planning": "Completeness and effectiveness of continuity plans",
                "Crisis management capability": "Effectiveness in handling emergency situations",
                "Insurance optimization": "Adequacy and cost-effectiveness of insurance coverage"
            }
        },

        "Quality Management & Control": {
            "Implement Quality Assurance": {
                "Quality management system certification": "Maintenance of quality certifications",
                "Process standardization rate": "(Standardized processes / Total processes) * 100",
                "Quality audit performance": "Results from quality assurance audits",
                "Continuous improvement implementation": "Number of implemented improvement initiatives"
            },
            "Enhance Process Control": {
                "Process capability index": "Statistical measure of process performance",
                "Variation reduction": "Decrease in process variability over time",
                "Standard operating procedure adherence": "(Compliant operations / Total operations) * 100",
                "Performance monitoring effectiveness": "Quality of performance monitoring systems"
            },
            "Improve Service Delivery": {
                "Service level achievement": "(Achieved service levels / Target service levels) * 100",
                "Customer requirement fulfillment": "(Met requirements / Total requirements) * 100",
                "Service innovation rate": "Number of new service improvements implemented",
                "Quality cost optimization": "Balance of prevention, appraisal, and failure costs"
            }
        }
    },

    "Learning & Growth Perspective": {
        "Workforce Development & Capability": {
            "Enhance Driver Capabilities": {
                "Driver training completion rate": "(Trained drivers / Total drivers) * 100",
                "Driver certification achievement": "(Certified drivers / Total drivers) * 100",
                "Safety training effectiveness": "Reduction in safety incidents post-training",
                "Cross-training implementation": "Percentage of drivers with multiple skill sets"
            },
            "Improve Technical Skills": {
                "Maintenance technician certification": "(Certified technicians / Total technicians) * 100",
                "Technology proficiency score": "Assessment of technology skills",
                "Specialized equipment training": "Percentage of staff trained on specialized equipment",
                "Continuous learning participation": "Hours of training per employee per year"
            },
            "Develop Management Talent": {
                "Leadership development program completion": "(Completed programs / Eligible managers) * 100",
                "Succession planning coverage": "Percentage of key roles with identified successors",
                "Management competency assessment": "Score from management capability evaluations",
                "Cross-functional experience": "Percentage of managers with cross-functional experience"
            },
            "Enhance Digital Literacy": {
                "Digital skills proficiency": "(Proficient users / Total users) * 100",
                "Software application mastery": "Proficiency in key operational software",
                "Data analytics capability": "Ability to use data for decision making",
                "Automation tool proficiency": "Skill level with automation tools and systems"
            }
        },

        "Technology & Innovation Ecosystem": {
            "Foster Innovation Culture": {
                "Innovation proposal rate": "Number of improvement suggestions per employee",
                "Technology adoption success": "(Successfully adopted technologies / Total technologies implemented) * 100",
                "R&D investment effectiveness": "Return on technology research investment",
                "Digital transformation progress": "Progress in digital maturity assessment"
            },
            "Enhance Research & Development": {
                "New technology development": "Number of new technologies developed annually",
                "Patent and IP generation": "Number of transport-related patents filed",
                "Research collaboration effectiveness": "Success rate of research partnerships",
                "Innovation pipeline strength": "Number of innovations in development pipeline"
            },
            "Improve Technology Infrastructure": {
                "IT system reliability": "Uptime percentage of critical IT systems",
                "Data security compliance": "Score from cybersecurity and data protection audits",
                "Network performance optimization": "Speed and reliability of communication networks",
                "Technology scalability readiness": "Ability to scale technological solutions"
            },
            "Advance Automation & AI": {
                "Process automation level": "Percentage of automatable processes automated",
                "AI implementation success": "(Successful AI implementations / Total AI projects) * 100",
                "Machine learning model accuracy": "Performance of ML models in operational applications",
                "Robotic process automation coverage": "Percentage of RPA-eligible processes automated"
            }
        },

        "Organizational Culture & Structure": {
            "Align Corporate Culture": {
                "Employee engagement score": "Results from employee engagement surveys",
                "Values alignment assessment": "Employee alignment with organizational values",
                "Cultural transformation progress": "Progress in cultural change initiatives",
                "Diversity and inclusion index": "Measure of workplace diversity and inclusion"
            },
            "Improve Organizational Agility": {
                "Change implementation speed": "Time to implement organizational changes",
                "Adaptation to market changes": "Speed of response to market shifts",
                "Employee empowerment index": "Level of decision-making authority at all levels",
                "Resource allocation flexibility": "Ability to quickly reallocate resources"
            },
            "Enhance Communication & Collaboration": {
                "Internal communication effectiveness": "Score from communication satisfaction surveys",
                "Cross-functional collaboration": "Level of inter-departmental cooperation",
                "Knowledge sharing culture": "Extent of knowledge sharing across organization",
                "Team performance metrics": "Performance indicators for team achievements"
            },
            "Develop Organizational Learning": {
                "Lessons learned implementation": "Percentage of lessons incorporated into practices",
                "Best practice sharing": "Extent of sharing successful approaches",
                "Continuous improvement culture": "Employee engagement in improvement activities",
                "Knowledge retention rate": "Preservation of organizational knowledge"
            }
        },

        "Sustainability & Environmental Stewardship": {
            "Improve Environmental Performance": {
                "Carbon emission reduction": "((Previous emissions - Current emissions) / Previous emissions) * 100",
                "Fuel efficiency improvement": "((Previous consumption - Current consumption) / Previous consumption) * 100",
                "Alternative fuel vehicle adoption": "(Alternative fuel vehicles / Total fleet) * 100",
                "Eco-driving training completion": "(Trained drivers / Total drivers) * 100"
            },
            "Enhance Sustainable Practices": {
                "Waste reduction achievement": "Reduction in operational waste",
                "Recycling program effectiveness": "Percentage of waste recycled",
                "Green procurement adoption": "Percentage of sustainable purchases",
                "Environmental compliance rate": "(Compliant operations / Total operations) * 100"
            },
            "Develop Circular Economy": {
                "Resource efficiency improvement": "((Previous resource use - Current use) / Previous use) * 100",
                "Waste valorization rate": "(Waste converted to value / Total waste) * 100",
                "Component reuse and recycling": "Percentage of components reused or recycled",
                "Sustainable packaging adoption": "Percentage of sustainable packaging materials"
            },
            "Strengthen Environmental Management": {
                "Environmental management system certification": "Maintenance of environmental certifications",
                "Carbon footprint monitoring": "Accuracy and completeness of emissions tracking",
                "Environmental risk assessment": "Thoroughness of environmental risk evaluation",
                "Sustainability reporting quality": "Quality and transparency of sustainability reports"
            }
        },

        "Health, Safety & Wellbeing": {
            "Enhance Workplace Safety": {
                "Workplace accident reduction": "((Previous accidents - Current accidents) / Previous accidents) * 100",
                "Safety training completion rate": "(Completed safety training / Required training) * 100",
                "Ergonomics improvement": "Reduction in ergonomic-related incidents",
                "Safety equipment utilization": "Percentage of required safety equipment used"
            },
            "Improve Employee Wellbeing": {
                "Employee health assessment": "Results from health and wellbeing surveys",
                "Work-life balance satisfaction": "Employee rating of work-life balance",
                "Stress management effectiveness": "Reduction in stress-related absences",
                "Wellbeing program participation": "Percentage of employees in wellbeing programs"
            },
            "Strengthen Occupational Health": {
                "Health surveillance coverage": "(Monitored employees / Total employees) * 100",
                "Preventive health measure implementation": "Number of preventive health initiatives",
                "Mental health support accessibility": "Employee access to mental health resources",
                "Health risk assessment completeness": "Thoroughness of occupational health risk assessments"
            }
        },

        "Stakeholder & Community Development": {
            "Promote Industry Leadership": {
                "Industry standard participation": "Involvement in transport industry standards development",
                "Thought leadership impact": "Influence in transport industry discussions",
                "Professional association engagement": "Level of participation in professional organizations",
                "Industry education contribution": "Contribution to transport education and training"
            },
            "Enhance Community Relations": {
                "Local community investment": "Investment in local community development",
                "Community partnership effectiveness": "Success rate of community partnership projects",
                "Local economic impact": "Contribution to local economic development",
                "Community perception improvement": "Improvement in community satisfaction scores"
            },
            "Develop Supply Chain Partnerships": {
                "Supplier development programs": "Number of supplier capability development initiatives",
                "Carrier relationship quality": "Quality assessment of carrier partnerships",
                "Customer collaboration depth": "Depth of collaborative relationships with customers",
                "Partner capability enhancement": "Improvement in partner capabilities through collaboration"
            }
        }
    }
}
