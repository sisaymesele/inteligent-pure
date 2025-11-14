

from management_project.services.strategy_hierarchy.default import DEFAULT_PERSPECTIVE


ENERGY_PERSPECTIVE = {
    # ---------------- FINANCIAL PERSPECTIVE ----------------
    "Financial Perspective": {
        **DEFAULT_PERSPECTIVE["Financial Perspective"],

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
        **DEFAULT_PERSPECTIVE["Customer Perspective"],

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
        },
    },

    "Internal Process Perspective": {

        **DEFAULT_PERSPECTIVE["Internal Process Perspective"],

        # -------------------- 1. Energy Generation & Supply Optimization --------------------
        "Energy Generation & Supply Optimization": {
            "Increase energy generation efficiency": {
                "Plant efficiency (%)": "(Actual output / Theoretical output) * 100",
                "Heat rate (kJ/kWh)": "Energy input / Output",
                "Capacity utilization (%)": "(Actual generation / Installed capacity) * 100",
                "Energy loss rate (%)": "(Lost energy / Generated energy) * 100"
            },
            "Enhance reliability of power supply": {
                "System reliability index (SAIDI/SAIFI)": "Standard utility measure",
                "Forced outage rate (%)": "(Forced outage hours / Total hours) * 100",
                "Mean time to repair (hours)": "Total downtime / Incidents",
                "Supply continuity rate (%)": "(Continuous supply hours / Total hours) * 100"
            },
            "Optimize fuel consumption": {
                "Fuel efficiency (MJ/kWh)": "Fuel input / Energy output",
                "Fuel cost per kWh": "Total fuel cost / Energy produced",
                "Renewable fuel utilization (%)": "(Renewable fuel / Total fuel) * 100",
                "Carbon intensity (kg CO₂/kWh)": "Emissions / Energy produced"
            },
            "Improve asset performance": {
                "Equipment availability (%)": "(Available hours / Total hours) * 100",
                "Maintenance backlog (%)": "(Pending tasks / Total tasks) * 100",
                "Asset utilization index": "Composite utilization score",
                "Downtime frequency (#)": "Number of downtime events"
            },
            "Strengthen operational planning & dispatch": {
                "Forecast accuracy (%)": "(Accurate forecasts / Total forecasts) * 100",
                "Load balancing efficiency (%)": "(Balanced load / Total load) * 100",
                "Dispatch deviation (%)": "(Planned - Actual dispatch) / Planned * 100",
                "Response time to grid fluctuations (s)": "Average response time"
            },
            "Enhance supply chain reliability": {
                "Fuel delivery reliability (%)": "(On-time deliveries / Total deliveries) * 100",
                "Inventory turnover ratio": "COGS / Average inventory",
                "Spare parts availability (%)": "(Available / Required) * 100",
                "Procurement cycle time (days)": "Average time to procure"
            },
            "Reduce technical and non-technical losses": {
                "Transmission loss (%)": "(Energy lost / Energy sent out) * 100",
                "Distribution loss (%)": "(Energy lost / Energy distributed) * 100",
                "Non-technical loss (%)": "(Unbilled / Total distributed) * 100",
                "Loss reduction initiative success (%)": "(Achieved / Planned) * 100"
            },
            "Enhance grid stability": {
                "Frequency deviation (Hz)": "Average deviation from 50/60 Hz",
                "Voltage fluctuation index": "Measured variance",
                "Reactive power balance (%)": "(Optimal / Total system) * 100",
                "Grid stability compliance (%)": "(Stable hours / Total hours) * 100"
            },
        },

        # -------------------- 2. Renewable Energy & Sustainability --------------------
        "Renewable Energy & Sustainability": {
            "Increase renewable energy generation": {
                "Renewable energy share (%)": "(Renewable output / Total output) * 100",
                "Installed renewable capacity (MW)": "Sum of renewable assets",
                "Renewable project completion rate (%)": "(Completed / Planned) * 100",
                "CO₂ reduction from renewables (tons)": "Baseline - Actual emissions"
            },
            "Enhance sustainability initiatives": {
                "Sustainability project implementation (%)": "(Implemented / Planned) * 100",
                "Emission reduction (%)": "(Baseline - Current) / Baseline * 100",
                "Energy efficiency improvement (%)": "(Baseline - Current) / Baseline * 100",
                "Environmental compliance rate (%)": "(Compliant / Total facilities) * 100"
            },
            "Promote energy conservation programs": {
                "Energy saved (MWh)": "Baseline - Actual consumption",
                "Program participation rate (%)": "(Participants / Target group) * 100",
                "Awareness campaign reach (%)": "(Reached / Target population) * 100",
                "Cost savings achieved (%)": "(Savings / Target savings) * 100"
            },
            "Enhance carbon management": {
                "Carbon intensity (kg CO₂/kWh)": "Emissions / Output",
                "Carbon offset (%)": "(Offset / Emitted) * 100",
                "Carbon credit utilization (%)": "(Used / Available credits) * 100",
                "Net-zero compliance progress (%)": "(Achieved / Target) * 100"
            },
            "Develop green innovation & R&D": {
                "R&D investment (% of revenue)": "R&D spend / Total revenue * 100",
                "New green technology pilots (#)": "Number implemented",
                "Technology adoption rate (%)": "(Adopted / Piloted) * 100",
                "Patent registrations (#)": "New patents granted"
            },
            "Optimize renewable integration to grid": {
                "Renewable curtailment rate (%)": "(Curtailment / Total renewable output) * 100",
                "Grid readiness score": "Internal integration index",
                "Smart grid compatibility (%)": "(Integrated / Total grid nodes) * 100",
                "Balancing cost (USD/MWh)": "Total balancing cost / Energy dispatched"
            },
            "Promote circular economy in operations": {
                "Recycled waste (%)": "(Recycled / Total waste) * 100",
                "Water reuse rate (%)": "(Reused / Total water) * 100",
                "Energy recovery rate (%)": "(Recovered / Wasted energy) * 100",
                "Material recovery efficiency (%)": "(Recovered / Used materials) * 100"
            },
            "Ensure environmental compliance": {
                "Audit compliance rate (%)": "(Compliant / Audited) * 100",
                "Environmental incidents (#)": "Reported incidents",
                "Permit renewal timeliness (%)": "(On-time renewals / Total) * 100",
                "Corrective action closure rate (%)": "(Closed / Total issues) * 100"
            },
        },

        # -------------------- 3. Safety, Maintenance & Reliability --------------------
        "Safety, Maintenance & Reliability": {
            "Ensure zero-incident operations": {
                "Lost time injury frequency rate (LTIFR)": "Standard safety metric",
                "Incident-free days (#)": "Number of days",
                "Safety compliance rate (%)": "(Compliant / Total sites) * 100",
                "Corrective action implementation (%)": "(Implemented / Identified) * 100"
            },
            "Strengthen preventive maintenance": {
                "Preventive maintenance completion (%)": "(Completed / Planned) * 100",
                "Maintenance cost variance (%)": "(Actual - Budgeted) / Budgeted * 100",
                "Equipment downtime reduction (%)": "(Previous - Current) / Previous * 100",
                "Maintenance schedule adherence (%)": "(On-time tasks / Total tasks) * 100"
            },
            "Enhance emergency response capability": {
                "Emergency drill frequency (#/year)": "Count per year",
                "Response time to incidents (minutes)": "Average response",
                "Preparedness score": "Internal readiness index",
                "Recovery time objective (hours)": "Average recovery period"
            },
            "Improve asset integrity management": {
                "Integrity inspection coverage (%)": "(Inspected / Total assets) * 100",
                "Defect rate (%)": "(Defects / Inspections) * 100",
                "Condition-based maintenance adoption (%)": "(Adopted / Total assets) * 100",
                "Failure recurrence rate (%)": "(Repeat failures / Total failures) * 100"
            },
            "Enhance safety culture": {
                "Safety training participation (%)": "(Trained / Total staff) * 100",
                "Behavior-based safety observations (#)": "Recorded observations",
                "Near-miss reporting rate (%)": "(Reported / Expected) * 100",
                "Safety leadership index": "Composite cultural measure"
            },
            "Monitor maintenance performance": {
                "Maintenance backlog (%)": "(Pending tasks / Total tasks) * 100",
                "Planned maintenance ratio (%)": "(Planned / Total maintenance) * 100",
                "Mean time between failures (MTBF)": "Reliability metric",
                "Maintenance productivity index": "Internal score"
            },
            "Implement predictive maintenance": {
                "AI/IoT sensor coverage (%)": "(Sensor-enabled assets / Total assets) * 100",
                "Prediction accuracy (%)": "(Accurate / Total predictions) * 100",
                "Unplanned downtime reduction (%)": "(Previous - Current) / Previous * 100",
                "Cost savings from prediction (%)": "(Saved / Total maintenance cost) * 100"
            },
            "Ensure contractor safety compliance": {
                "Contractor compliance rate (%)": "(Compliant / Total contractors) * 100",
                "Contractor incident rate (#)": "Incidents per 1,000 workers",
                "Training completion rate (%)": "(Completed / Required) * 100",
                "Audit pass rate (%)": "(Passed / Total audits) * 100"
            },
        },
        # -------------------- 4. Smart Energy Operations --------------------
        "Smart Energy Operations": {
            "Optimize energy demand response": {
                "Peak load reduction (%)": "(Reduced load / Total peak load) * 100",
                "Demand response participation rate (%)": "(Participants / Eligible customers) * 100",
                "Response time to demand events (minutes)": "Average response time",
                "Energy cost savings from demand response (%)": "(Savings / Baseline cost) * 100"
            },
            "Enhance smart grid performance": {
                "Grid automation coverage (%)": "(Automated nodes / Total nodes) * 100",
                "Voltage deviation incidents (#)": "Number of deviations from nominal voltage",
                "Frequency stability index": "Internal stability score",
                "Power quality compliance (%)": "(Compliant measurements / Total measurements) * 100"
            },
            "Implement predictive maintenance for smart assets": {
                "Predictive maintenance coverage (%)": "(Assets monitored / Total assets) * 100",
                "Prediction accuracy (%)": "(Correct predictions / Total predictions) * 100",
                "Unplanned downtime reduction (%)": "(Previous - Current) / Previous * 100",
                "Maintenance cost savings (%)": "(Saved / Total maintenance cost) * 100"
            },
            "Improve energy storage & management": {
                "Storage utilization (%)": "(Used capacity / Total capacity) * 100",
                "Charge/discharge efficiency (%)": "(Energy delivered / Energy stored) * 100",
                "Storage system availability (%)": "(Operational hours / Total hours) * 100",
                "Cycle life utilization (%)": "(Used cycles / Expected cycles) * 100"
            },
            "Optimize renewable energy integration": {
                "Renewable dispatch efficiency (%)": "(Dispatched / Available output) * 100",
                "Curtailment reduction (%)": "(Previous - Current) / Previous * 100",
                "Grid balancing cost savings (%)": "(Saved / Baseline cost) * 100",
                "Renewable energy penetration (%)": "(Renewable generation / Total generation) * 100"
            },
            "Enhance real-time monitoring & analytics": {
                "Monitoring coverage (%)": "(Monitored assets / Total assets) * 100",
                "Data processing latency (s)": "Average time from data capture to analytics",
                "Anomaly detection accuracy (%)": "(Correctly detected anomalies / Total anomalies) * 100",
                "Operational decision support usage (%)": "(Decisions aided / Total decisions) * 100"
            },
            "Strengthen cyber & operational security": {
                "Cybersecurity compliance (%)": "(Compliant systems / Total systems) * 100",
                "Incident response time (minutes)": "Average time to detect and respond",
                "Security breach attempts (#)": "Number of attempted breaches",
                "Critical system uptime (%)": "(Operational time / Total time) * 100"
            },
            "Promote smart energy innovation & R&D": {
                "New smart solutions implemented (#)": "Number of deployed solutions",
                "R&D investment in smart tech (% of revenue)": "(Investment / Total revenue) * 100",
                "Pilot project success rate (%)": "(Successful pilots / Total pilots) * 100",
                "Technology adoption rate (%)": "(Adopted solutions / Total piloted) * 100"
            }
        },
    },

    "Learning & Growth Perspective": {
        **DEFAULT_PERSPECTIVE["Learning & Growth Perspective"],
    },

}
