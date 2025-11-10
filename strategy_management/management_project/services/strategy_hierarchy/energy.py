from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE

ENERGY_PERSPECTIVE = {
    # ---------------- FINANCIAL PERSPECTIVE ----------------
    "Financial Perspective": {
        **GENERIC_FINANCE_PERSPECTIVE['Financial Perspective'],

        "Economic Development & GDP Contribution of Energy": {
            "Increase Local Employment": {
                "Local jobs created (#)": "Number of jobs generated locally in energy sector",
                "Employment growth rate (%)": "(Current - Previous)/Previous * 100",
                "Jobs for disadvantaged groups (#)": "Number employed from target groups",
                "Retention of local workforce (%)": "(Retained / Hired) * 100"
            },
            "Promote Renewable Energy Investment": {
                "Renewable capacity installed (MW)": "Total MW of renewable sources installed",
                "Investment in renewables ($)": "Capital invested",
                "Renewable share of total capacity (%)": "(Renewable / Total) * 100",
                "Project completion on time (%)": "(Completed on schedule / Total projects) * 100"
            },
            "Enhance Energy Access in Rural Areas": {
                "Rural electrification rate (%)": "(Electrified households / Total households) * 100",
                "New rural connections (#)": "Number of new connections",
                "Average connection time (days)": "Average days to connect",
                "Customer satisfaction in rural areas (%)": "Survey rating"
            },
            "Support Industrial Growth": {
                "Industrial energy supplied (MWh)": "Total energy supplied to industrial sector",
                "Industrial customer growth (#)": "Number of industrial customers served",
                "Revenue from industrial supply ($)": "Revenue generated",
                "Industrial energy reliability (%)": "Percentage uptime for industrial customers"
            },
            "Boost Local GDP Contribution": {
                "Energy sector contribution to GDP (%)": "Sector GDP / National GDP * 100",
                "Tax contribution ($)": "Taxes paid to government",
                "Indirect economic impact ($)": "Estimated local multiplier effect",
                "Regional investment projects (#)": "Count of local infrastructure projects"
            },
            "Energy Infrastructure Investment": {
                "Transmission & distribution expansion ($)": "Capital invested in T&D infrastructure",
                "New substation projects (#)": "Number of substations built",
                "Smart grid deployment (%)": "(Smart grid enabled areas / Total coverage) * 100",
                "Infrastructure project completion on time (%)": "(Completed on schedule / Total projects) * 100"
            }
        }
    },

    # ---------------- CUSTOMER PERSPECTIVE ----------------
    "Customer Perspective": {
        **GENERIC_CUSTOMER_PERSPECTIVE['Customer Perspective'],

        "Energy Access & Reliability": {
            "Expand electricity access to rural areas": {
                "Rural electrification rate (%)": "(Number of households with electricity / Total rural households) * 100",
                "New connections added (#)": "Number of new household or business connections",
                "Average connection time (days)": "Average days from application to connection",
                "Customer satisfaction (%)": "Survey score of reliability and service"
            },
            "Improve electricity reliability": {
                "SAIDI (minutes/year)": "System Average Interruption Duration Index",
                "SAIFI (interruptions/year)": "System Average Interruption Frequency Index",
                "Average downtime per outage (hours)": "Total downtime / Total outages",
                "Customer complaints (#)": "Total complaints regarding outages"
            },
            "Enhance renewable energy adoption": {
                "Percentage renewable energy (%)": "(Renewable energy generated / Total energy generated) * 100",
                "Number of households using solar (#)": "Installed solar systems in households",
                "Installed renewable capacity (MW)": "Total installed renewable capacity",
                "Customer adoption satisfaction (%)": "Survey on renewable services"
            },
            "Reduce power theft & losses": {
                "Technical losses (%)": "(Energy lost / Total energy supplied) * 100",
                "Non-technical losses (%)": "(Theft & pilferage / Total energy supplied) * 100",
                "Revenue recovery rate (%)": "(Revenue billed / Revenue expected) * 100",
                "Detection & enforcement cases (#)": "Number of theft cases detected"
            },
            "Implement smart metering & monitoring": {
                "Smart meter coverage (%)": "(Number of smart meters / Total meters) * 100",
                "Data accuracy (%)": "Meter reading accuracy vs standard",
                "Remote disconnection & reconnection (#)": "Number of remote actions completed",
                "Customer satisfaction (%)": "Survey on meter services"
            },
            "Support energy affordability programs": {
                "Subsidized connection uptake (#)": "Number of customers in subsidy programs",
                "Average monthly bill reduction (%)": "Average cost savings due to program",
                "Participation rate (%)": "(Eligible customers in program / Total eligible) * 100",
                "Customer satisfaction (%)": "Program survey results"
            }
        },

        "Energy Infrastructure": {
            "Upgrade transmission & distribution networks": {
                "Transmission line length upgraded (km)": "Total km of upgraded lines",
                "Distribution network efficiency (%)": "Energy delivered / Energy input * 100",
                "Outage frequency reduction (%)": "(Previous outages - Current outages) / Previous * 100",
                "Project completion rate (%)": "Completed projects / Planned projects * 100"
            },
            "Increase grid stability & resilience": {
                "Grid downtime (hours)": "Total downtime per year",
                "Frequency stability (%)": "Time frequency within target range / Total time * 100",
                "Grid resilience index": "Composite score of stability measures",
                "Critical infrastructure incidents (#)": "Number of failures affecting large areas"
            },
            "Expand energy storage solutions": {
                "Installed storage capacity (MW)": "Total energy storage capacity",
                "Storage utilization rate (%)": "Actual stored energy / Installed capacity * 100",
                "Storage performance efficiency (%)": "Output vs input efficiency",
                "Integration with grid (%)": "Storage capacity actively supporting grid"
            },
            "Develop off-grid & mini-grid solutions": {
                "Off-grid population served (#)": "Number of households/businesses served",
                "Mini-grid operational uptime (%)": "Operational time / Total time * 100",
                "Projects commissioned (#)": "Number of new mini-grid projects",
                "Community satisfaction (%)": "Survey feedback from served communities"
            },
            "Enhance electric vehicle (EV) infrastructure": {
                "EV charging stations installed (#)": "Number of stations installed",
                "Charging station uptime (%)": "Available hours / Total hours * 100",
                "EV adoption rate (%)": "EV registrations / Total vehicles * 100",
                "Customer satisfaction (%)": "EV users survey score"
            },
            "Ensure infrastructure safety & compliance": {
                "Safety incidents (#)": "Number of accidents or hazards",
                "Compliance with standards (%)": "Audits meeting regulatory standards",
                "Training completion (%)": "Staff trained in safety protocols",
                "Inspection completion rate (%)": "Inspections done / Planned inspections * 100"
            }
        },

        "Energy Environmental Development": {
            "Reduce carbon footprint of operations": {
                "CO2 emissions reduction (%)": "(Previous CO2 - Current CO2) / Previous * 100",
                "Energy efficiency improvement (%)": "Efficiency gains in operations",
                "Renewable energy usage (%)": "Share of renewable energy used",
                "Emission compliance (%)": "Operations meeting environmental standards"
            },
            "Promote renewable energy generation": {
                "Renewable energy capacity (MW)": "Total renewable capacity installed",
                "Projects completed (#)": "Number of renewable energy projects",
                "Annual generation (MWh)": "Energy produced annually from renewable sources",
                "Community adoption (%)": "Households or businesses using renewable energy"
            },
            "Enhance energy efficiency programs": {
                "Energy saved (MWh)": "Energy saved via programs",
                "Program participation (#)": "Number of participants",
                "Cost savings ($)": "Financial savings from efficiency programs",
                "Customer satisfaction (%)": "Survey on program effectiveness"
            },
            "Waste & water management in energy facilities": {
                "Waste recycling rate (%)": "Recycled waste / Total waste * 100",
                "Water usage reduction (%)": "Reduction in water consumption",
                "Compliance with disposal regulations (%)": "Regulatory compliance score",
                "Waste diversion projects (#)": "Number of projects implemented"
            },
            "Support biodiversity near energy sites": {
                "Number of initiatives (#)": "Projects supporting biodiversity",
                "Habitat area protected (ha)": "Total area protected",
                "Species conservation impact (#)": "Number of species conserved",
                "Community engagement (%)": "Community involvement in initiatives"
            },
            "Sustainable procurement & supply chain for energy": {
                "Supplier compliance (%)": "Suppliers meeting sustainability standards",
                "Sustainable procurement ratio (%)": "Procurement from sustainable sources / Total procurement",
                "Audits conducted (#)": "Number of sustainability audits",
                "Training coverage (%)": "Staff trained in sustainable procurement"
            }
        },

        "Energy - Community-Focused": {
            "Increase community tree planting initiatives": {
                "Number of trees planted (#)": "Total trees planted",
                "Community participation (#)": "Number of participants in programs",
                "Survival rate (%)": "Trees surviving after 1 year / Total planted * 100",
                "Impact awareness (%)": "Survey on community knowledge increase"
            },
            "Promote community recycling programs": {
                "Recycling participation (#)": "Number of households or businesses participating",
                "Waste diverted (tons)": "Waste collected and recycled",
                "Program frequency (#)": "Number of recycling drives per year",
                "Community satisfaction (%)": "Survey feedback"
            },
            "Implement school environmental programs": {
                "Schools participating (#)": "Number of schools involved",
                "Students reached (#)": "Total students participating",
                "Programs conducted (#)": "Number of environmental activities",
                "Knowledge improvement (%)": "Survey improvement in awareness"
            },
            "Foster community awareness & workshops": {
                "Workshops held (#)": "Total workshops conducted",
                "Participants (#)": "Number of attendees",
                "Knowledge improvement (%)": "Survey increase in awareness",
                "Follow-up actions (#)": "Number of community actions taken post-workshops"
            },
            "Support local environmental volunteering": {
                "Volunteer participants (#)": "Number of active volunteers",
                "Volunteer hours (#)": "Total hours volunteered",
                "Projects completed (#)": "Number of environmental projects",
                "Community satisfaction (%)": "Survey on volunteer impact"
            },
            "Encourage local environmental clubs & groups": {
                "Number of clubs formed (#)": "Total clubs created in community",
                "Participation rate (%)": "(Active members / Total targeted community members) * 100",
                "Projects completed (#)": "Total initiatives completed by clubs",
                "Community satisfaction (%)": "Survey score of club impact"
            }
        }
    }
}
