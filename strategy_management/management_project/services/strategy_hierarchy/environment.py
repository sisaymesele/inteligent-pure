from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE

ENVIRONMENT_PERSPECTIVE = {
    "Financial Perspective": {
        # Core generic financial objectives
        **GENERIC_FINANCE_PERSPECTIVE['Financial Perspective'],

        # ==================== 1. Environmental Revenue Growth & Funding ====================
        "Environmental Revenue Growth & Funding": {
            "Expand External Environmental Funding": {
                "Environmental grant revenue ($)": "Total funding received for environmental projects",
                "Grant share of total funding (%)": "(Environmental grants / Total grants) * 100",
                "Grant success rate (%)": "(Grants awarded / Grants applied) * 100",
                "Grant utilization efficiency (%)": "(Spent / Allocated) * 100"
            },
            "Promote Climate Project Funding": {
                "Climate project investment growth (%)": "(Current - Previous) / Previous * 100",
                "Number of climate grants received": "Count of approved grants",
                "Average grant size ($)": "Total funding / Number of grants",
                "Timely fund disbursement (%)": "(Grants disbursed on time / Total grants) * 100"
            },
            "Leverage Public & Private Environmental Funding": {
                "PPP eco-project ratio (%)": "(PPP-funded environmental projects / Total projects) * 100",
                "Private contribution ($)": "Funding from private partners",
                "Co-funded projects count": "Number of joint funding projects",
                "Average project completion time (months)": "Average duration of funded projects"
            },
            "Optimize Grant Impact": {
                "Grant ROI (%)": "(Value of outcomes / Investment) * 100",
                "Community beneficiaries reached": "Number of people impacted by grant projects",
                "Environmental impact score": "Composite score of environmental improvement",
                "Grant spend efficiency (%)": "(Planned spend / Actual spend) * 100"
            },
            "Revenue from Environmental Services": {
                "Eco-service revenue ($)": "Income from consulting, recycling, or carbon credits",
                "Carbon credit revenue ($)": "Revenue from carbon trading",
                "Sustainable product sales ($)": "Revenue from eco-products",
                "External partnership contributions ($)": "Revenue from NGOs or private sector collaborations"
            },
            "Enhance ROI & Sustainability": {
                "Revenue growth from environmental initiatives (%)": "(Current - Previous) / Previous * 100",
                "Operational cost savings ($)": "Savings achieved via sustainability measures",
                "Profit margin eco-projects (%)": "(Net profit / Revenue) * 100",
                "Long-term sustainability index": "Score based on environmental and financial outcomes"
            },
            "Strengthen Compliance & Reporting": {
                "Timely grant reporting (%)": "(Reports submitted on time / Total reports) * 100",
                "Audit compliance (%)": "(Compliant audits / Total audits) * 100",
                "Accuracy of financial reporting (%)": "(Correct entries / Total entries) * 100",
                "Policy adherence (%)": "(Projects compliant with environmental policy / Total projects) * 100"
            },
            "Develop Green Partnerships": {
                "Number of collaborations with NGOs": "Count of active NGO partnerships",
                "Number of corporate sustainability partners": "Count of active corporate partners",
                "Joint investment value ($)": "Total funds co-invested in green initiatives",
                "Partnership success rate (%)": "(Projects completed successfully / Total projects) * 100"
            }
        },

        # ==================== 3. Environmental Profitability & Return ====================
        "Environmental Profitability & Return": {
            "Improve Overall Profit Margin": {
                "Net profit margin (%)": "(Net income / Total revenue) * 100 | Target: 25%",
                "Gross margin (%)": "(Revenue - Direct costs) / Revenue * 100 | Target: 35%",
                "EBITDA margin (%)": "(EBITDA / Revenue) * 100 | Target: 30%",
                "Operating profit growth (%)": "(Current - Previous) / Previous * 100 | Target: 15%"
            },
            "Enhance Project Profitability": {
                "Project ROI (%)": "(Revenue - Project cost) / Project cost * 100 | Target: 20%",
                "Cost per environmental project ($)": "Total spend / Number of projects | Target: <$100k",
                "Profit margin per project (%)": "(Net profit / Revenue) * 100 | Target: 25%",
                "Break-even project count (#)": "Number of projects required to cover fixed costs | Target: 4"
            },
            "Increase Research & Innovation Profitability": {
                "Research ROI (%)": "(Revenue from research - Cost) / Cost * 100 | Target: 15%",
                "Overhead recovery rate (%)": "(Indirect costs recovered / Total research cost) * 100 | Target: 90%",
                "Research income growth (%)": "(Current - Previous) / Previous * 100 | Target: 12%",
                "Research cost efficiency (%)": "(Research output value / Research spending) * 100 | Target: 110%"
            },
            "Optimize Auxiliary Environmental Services": {
                "Eco-service profit margin (%)": "(Profit / Revenue) * 100 | Target: 20%",
                "Revenue per consulting project ($)": "Income per environmental consulting project | Target: $50k",
                "Event service profitability (%)": "(Profit / Revenue) * 100 | Target: 15%",
                "Sustainable product ROI (%)": "(Revenue from eco-products - Cost) / Cost * 100 | Target: 25%"
            },
            "Enhance Cost Recovery for Subsidized Programs": {
                "Subsidy recovery ratio (%)": "(Revenue / Total cost) * 100 | Target: 90%",
                "Funding efficiency index": "Proportion of funded projects completed successfully | Target: 95%",
                "Fee waiver impact (%)": "(Waived revenue / Total project revenue) * 100 | Target: <5%",
                "Funding leverage ratio": "(External funding / Internal funding) * 100 | Target: 120%"
            },
            "Align Revenue-Cost for Profitability": {
                "Revenue-cost ratio": "Total revenue / Total cost | Target: >1.2",
                "Operating leverage ratio": "(Revenue growth / Cost growth) | Target: 1.5",
                "Profit variance (%)": "(Budgeted profit - Actual) / Budgeted * 100 | Target: <10%",
                "Fixed cost absorption rate (%)": "(Revenue contribution / Fixed cost) * 100 | Target: >80%"
            },
            "Maximize Return on Environmental Assets": {
                "ROA (%)": "(Net income / Total assets) * 100 | Target: 12%",
                "Asset utilization ratio": "Revenue / Average asset value | Target: >1.0",
                "Idle asset reduction (%)": "(Previous idle assets - Current) / Previous * 100 | Target: 20%",
                "Asset maintenance cost ratio (%)": "(Maintenance / Asset value) * 100 | Target: <5%"
            },
            "Increase Financial Sustainability": {
                "Operating surplus ratio (%)": "(Operating surplus / Operating revenue) * 100 | Target: 15%",
                "Liquidity ratio": "Current assets / Current liabilities | Target: >1.5",
                "Debt service coverage ratio": "Operating cash flow / Debt service | Target: >2",
                "Self-financing ratio (%)": "(Internal funds / Total funding) * 100 | Target: 40%"
            }
        },

        # ==================== 2. Environmental Infrastructure & Asset Finance ====================
        "Environmental Infrastructure & Asset Finance": {
            "Green Infrastructure Investment": {
                "Renewable energy project investment ($)": "Total investment in solar, wind, and hydro projects",
                "Green infrastructure ratio (%)": "(Green projects / Total capital projects) * 100",
                "ROI on green projects (%)": "(Net return from green projects / Investment) * 100",
                "Maintenance cost per green asset ($)": "Total maintenance spend / Number of green assets"
            },
            "Modernize Eco-Friendly Facilities": {
                "Eco-classroom construction rate (%)": "(New green classrooms / Total classrooms) * 100",
                "Green lab upgrade ratio (%)": "(Labs upgraded with green tech / Total labs) * 100",
                "Sustainable office renovations (%)": "(Offices meeting green standards / Total offices) * 100",
                "Capital expenditure per eco-asset ($)": "Total spend / Total eco-assets"
            },
            "Optimize Asset Utilization": {
                "Facility occupancy rate (%)": "(Hours used / Total available hours) * 100",
                "Lab and research station utilization (%)": "(Hours in use / Total available hours) * 100",
                "Multi-purpose space adaptation (%)": "(Flexible spaces / Total spaces) * 100",
                "Idle asset reduction (%)": "(Previously unused assets - Current) / Previous * 100"
            },
            "Preventive Maintenance & Lifecycle Management": {
                "Preventive maintenance coverage (%)": "(Assets maintained preventively / Total assets) * 100",
                "Average repair turnaround (days)": "Average days to repair eco-assets",
                "Functional asset rate (%)": "(Functional assets / Total assets) * 100",
                "Backlog reduction (%)": "(Previous backlog - Current) / Previous * 100"
            },
            "Improve Resource Efficiency": {
                "Energy cost per facility ($)": "Total energy spend / Number of facilities",
                "Water cost per facility ($)": "Total water spend / Number of facilities",
                "Waste reduction (%)": "(Previous waste - Current) / Previous * 100",
                "Utility cost savings ($)": "Savings from efficiency improvements"
            },
            "Leverage PPP for Asset Development": {
                "PPP-funded green project ratio (%)": "(PPP-funded projects / Total green projects) * 100",
                "Private capital attracted ($)": "Investment from private partners",
                "Number of co-funded green initiatives": "Count of PPP collaborations",
                "Average project completion time (months)": "Average duration to complete PPP projects"
            },
            "Maximize Return on Environmental Assets": {
                "Revenue per eco-asset ($)": "Revenue from renewable energy or green services per asset",
                "Asset contribution to environmental impact": "Score of asset efficiency in achieving environmental goals",
                "Revenue growth from green assets (%)": "(Current - Previous) / Previous * 100",
                "Facility productivity index": "Output hours per m² of eco-facility"
            },
            "Strengthen Asset Register & Compliance": {
                "Verified eco-assets (%)": "(Verified green assets / Total green assets) * 100",
                "Accuracy of green asset valuation (%)": "(Correctly valued green assets / Total green assets) * 100",
                "Timely reporting rate (%)": "(Reports submitted on time / Total reports) * 100",
                "Compliance with green asset policies (%)": "(Assets managed per policy / Total green assets) * 100"
            }
        },

        # ==================== 4. Environmental Financial Risk Management ====================
        "Environmental Financial Risk Management": {
            "Climate Financial Resilience": {
                "Climate risk exposure ($)": "Estimated financial impact of climate events | Target: < $1M",
                "Insurance coverage for green assets (%)": "(Insured value / Total asset value) * 100 | Target: 90%",
                "Contingency fund adequacy (%)": "(Available contingency funds / Recommended funds) * 100 | Target: 100%",
                "Disaster recovery readiness (%)": "(Prepared recovery plans / Critical assets) * 100 | Target: 95%"
            },
            "Environmental Compliance Risk Management": {
                "Compliance with environmental regulations (%)": "(Compliant projects / Total projects) * 100 | Target: 100%",
                "Fines and penalties ($)": "Total amount paid due to non-compliance | Target: 0",
                "Audit findings closed (%)": "(Resolved audit issues / Total findings) * 100 | Target: 100%",
                "Risk assessment coverage (%)": "(Projects with risk assessment / Total projects) * 100 | Target: 100%"
            },
            "Investment Risk Mitigation": {
                "Portfolio diversification ratio (%)": "(Diversified investments / Total investments) * 100 | Target: >50%",
                "Green project risk-adjusted ROI (%)": "(Risk-adjusted ROI / Target ROI) * 100 | Target: >90%",
                "Contingency project fund coverage (%)": "(Funds available for project risks / Total project cost) * 100 | Target: 20%",
                "Scenario planning implementation (%)": "(Plans implemented / Required scenarios) * 100 | Target: 100%"
            },
            "Financial Impact of Climate Initiatives": {
                "Revenue protection from climate projects ($)": "Income preserved through climate initiatives | Target: $500k",
                "Cost avoidance from environmental risks ($)": "Estimated avoided costs due to mitigation | Target: $200k",
                "Insurance claims ratio (%)": "(Claims settled / Claims filed) * 100 | Target: 95%",
                "Contingency fund utilization rate (%)": "(Used funds / Allocated contingency) * 100 | Target: <50%"
            }
        },

        # ==================== 5. Environmental Cost Efficiency ====================
        "Environmental Cost Efficiency": {
            "Optimize Operational Costs": {
                "Cost per ton of CO2 reduced ($)": "Total spend / Tons of CO2 reduced | Target: < $50",
                "Administrative cost as % of environmental funding (%)": "(Admin costs / Total environmental funding) * 100 | Target: <10%",
                "Project cost variance (%)": "(Planned - Actual) / Planned * 100 | Target: <5%",
                "Unit cost efficiency (%)": "(Output per $ spent / Target output) * 100 | Target: >90%"
            },
            "Reduce Energy & Resource Waste": {
                "Energy cost savings ($)": "Savings achieved via energy efficiency | Target: $50k",
                "Water cost savings ($)": "Savings from water efficiency | Target: $20k",
                "Waste reduction rate (%)": "(Previous waste - Current) / Previous * 100 | Target: 25%",
                "Resource utilization index": "Ratio of utilized to available resources | Target: >85%"
            },
            "Streamline Procurement Processes": {
                "Procurement cycle time reduction (%)": "(Previous - Current) / Previous * 100 | Target: 20%",
                "Supplier compliance rate (%)": "(On-time & quality compliant orders / Total orders) * 100 | Target: 95%",
                "Contract cost savings ($)": "Negotiated savings via contracts | Target: $30k",
                "Procurement error rate (%)": "(Errors / Total orders) * 100 | Target: <2%"
            },
            "Enhance Project Cost Management": {
                "Average project cost per unit ($)": "Total project cost / Units delivered | Target: <$1000",
                "Variance from budget (%)": "(Planned - Actual) / Planned * 100 | Target: <5%",
                "Cost per beneficiary ($)": "Total spend / People impacted | Target: <$50",
                "Expenditure growth efficiency (%)": "(Spending growth / Output growth) * 100 | Target: <1.1"
            }
        },

        # ==================== 6. Long-term Sustainability & Strategic Investment ====================
        "Long-term Sustainability & Strategic Investment": {
            "Develop Green Investment Portfolio": {
                "Green investment pipeline value ($)": "Total committed funds for green projects | Target: $5M",
                "Projected 5-year environmental ROI (%)": "Expected ROI over 5 years | Target: 12%",
                "Sustainable project adoption rate (%)": "(Projects meeting sustainability criteria / Total projects) * 100 | Target: 80%",
                "R&D spend for sustainability (%)": "(R&D for green projects / Total R&D) * 100 | Target: 15%"
            },
            "Promote Renewable Energy Investments": {
                "Renewable energy project ROI (%)": "(Revenue - Cost) / Cost * 100 | Target: 15%",
                "Share of energy from renewable sources (%)": "(Renewable energy produced / Total energy) * 100 | Target: 40%",
                "Cost savings from renewable adoption ($)": "Avoided costs via renewable energy | Target: $100k",
                "Green energy infrastructure investment ($)": "Capital spent on renewable infrastructure | Target: $1M"
            },
            "Strengthen Long-term Financial Sustainability": {
                "Reserve fund growth (%)": "(Current reserve - Previous) / Previous * 100 | Target: 20%",
                "Debt to equity ratio": "Total debt / Total equity | Target: <1",
                "Self-financing capacity (%)": "(Internal funding / Total funding) * 100 | Target: 50%",
                "Endowment fund growth (%)": "(Current - Previous) / Previous * 100 | Target: 15%"
            },
            "Enhance Strategic Environmental Investments": {
                "High-impact project investment ($)": "Capital allocated to priority projects | Target: $2M",
                "Portfolio risk-adjusted ROI (%)": "(Expected ROI / Risk factor) * 100 | Target: >10%",
                "Project alignment with national sustainability goals (%)": "(Aligned projects / Total projects) * 100 | Target: 90%",
                "Leveraged co-funding ratio (%)": "(External co-funding / Total investment) * 100 | Target: 30%"
            }
        },
    },

    "CUSTOMER_PERSPECTIVE": {

        # ---------------- GENERIC CUSTOMER PERSPECTIVE ----------------
        **GENERIC_CUSTOMER_PERSPECTIVE['Customer Perspective'],

        # ---------------- ENERGY SECTOR SPECIFIC ----------------

        "Access & Reliability": {
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

        "Infrastructure": {
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

        "Environmental Development": {
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
            "Waste & water management": {
                "Waste recycling rate (%)": "Recycled waste / Total waste * 100",
                "Water usage reduction (%)": "Reduction in water consumption",
                "Compliance with disposal regulations (%)": "Regulatory compliance score",
                "Waste diversion projects (#)": "Number of projects implemented"
            },
            "Support biodiversity & ecosystem initiatives": {
                "Number of initiatives (#)": "Projects supporting biodiversity",
                "Habitat area protected (ha)": "Total area protected",
                "Species conservation impact (#)": "Number of species conserved",
                "Community engagement (%)": "Community involvement in initiatives"
            },
            "Promote sustainable procurement & supply chain": {
                "Supplier compliance (%)": "Suppliers meeting sustainability standards",
                "Sustainable procurement ratio (%)": "Procurement from sustainable sources / Total procurement",
                "Audits conducted (#)": "Number of sustainability audits",
                "Training coverage (%)": "Staff trained in sustainable procurement"
            }
        },

        "Community-Focused": {
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

        "Environmental & Social Development": {
            "Encourage green buildings & sustainable infrastructure": {
                "Green buildings developed (#)": "Number of certified green buildings",
                "Energy efficiency (%)": "Energy savings compared to baseline",
                "Compliance with standards (%)": "Buildings meeting sustainability codes",
                "Community satisfaction (%)": "Survey on green building impact"
            },
            "Promote renewable energy adoption in community": {
                "Households using renewable energy (#)": "Number of households adopting",
                "Capacity installed (MW)": "Total renewable capacity installed in community",
                "Annual generation (MWh)": "Energy generated from renewables",
                "Satisfaction (%)": "Survey feedback from community"
            },
            "Waste reduction campaigns": {
                "Campaigns held (#)": "Number of awareness campaigns",
                "Waste reduced (tons)": "Waste reduction achieved",
                "Participation rate (%)": "Community participation in campaigns",
                "Impact awareness (%)": "Survey on waste reduction knowledge"
            },
            "Water conservation programs": {
                "Programs conducted (#)": "Total water conservation programs",
                "Water saved (m³)": "Volume of water saved",
                "Community participation (#)": "Number of participants",
                "Satisfaction (%)": "Survey feedback on programs"
            },
            "Environmental education for households": {
                "Households reached (#)": "Number of households educated",
                "Workshops conducted (#)": "Number of sessions held",
                "Knowledge improvement (%)": "Survey increase in awareness",
                "Follow-up actions (#)": "Number of households implementing recommendations"
            },
            "Community climate resilience initiatives": {
                "Projects implemented (#)": "Number of resilience projects",
                "People reached (#)": "Community members impacted",
                "Impact score": "Composite measure of resilience improvement",
                "Satisfaction (%)": "Survey on community resilience awareness"
            }
        }

    }

}
