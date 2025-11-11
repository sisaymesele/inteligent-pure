
from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE


MINING_PERSPECTIVE = {
    "Financial Perspective": {

        **GENERIC_FINANCE_PERSPECTIVE['Financial Perspective'],

        # -------------------- Revenue Growth & Diversification --------------------
        "Mining Revenue Growth & Diversification": {
            "Increase revenue from core minerals": {
                "Revenue growth rate (%)": "(Current revenue - Previous revenue) / Previous revenue * 100",
                "Revenue per ton of mineral produced": "Total revenue / Total tons produced",
                "Customer collection rate (%)": "(Collected sales / Billed sales) * 100",
                "Pricing optimization per mineral (%)": "(Optimal pricing segments / Total pricing segments) * 100"
            },
            "Expand sales to new geographic markets": {
                "New market revenue growth (%)": "(Revenue from new markets - Previous) / Previous * 100",
                "Number of new market customers": "Count of customers in new markets",
                "Market penetration rate (%)": "(Active customers / Total target population) * 100",
                "Revenue contribution from new markets (%)": "Revenue from new markets / Total revenue * 100"
            },
            "Develop value-added processing or by-products": {
                "Revenue from value-added products ($)": "Total revenue from by-products",
                "Growth in by-product revenue (%)": "(Current - Previous) / Previous * 100",
                "Contribution to total revenue (%)": "By-product revenue / Total revenue * 100",
                "Units sold of value-added products (#)": "Total units sold"
            },
            "Increase revenue from exploration projects": {
                "Exploration revenue ($)": "Revenue from exploration output",
                "Revenue growth (%)": "(Current - Previous) / Previous * 100",
                "Exploration ROI (%)": "(Revenue - Cost) / Cost * 100",
                "Number of exploration projects contributing to revenue": "Count of projects"
            }
        },

        # -------------------- Cost Efficiency & Operational Optimization --------------------
        "Mining Cost Efficiency & Operational Optimization": {
            "Reduce extraction and processing costs per ton": {
                "Cost per ton mined ($)": "Total costs / Total tons mined",
                "Reduction in cost (%)": "(Previous cost - Current) / Previous * 100",
                "Direct labor cost per ton ($)": "Labor costs / Tons mined",
                "Energy cost per ton ($)": "Total energy cost / Tons mined"
            },
            "Optimize energy consumption in mining operations": {
                "Energy efficiency ratio": "Energy used / Tons mined",
                "Renewable energy usage (%)": "Renewable energy / Total energy used * 100",
                "Cost savings from energy optimization ($)": "Previous cost - Current cost",
                "Energy consumption reduction (%)": "(Previous - Current) / Previous * 100"
            },
            "Reduce maintenance costs of heavy machinery": {
                "Maintenance cost per machine ($)": "Total maintenance / Machines",
                "Downtime reduction (%)": "(Previous downtime - Current) / Previous * 100",
                "Preventive maintenance ratio (%)": "(Preventive maintenance hours / Total maintenance hours) * 100",
                "Repair cost reduction (%)": "(Previous repair costs - Current) / Previous * 100"
            },
            "Improve labor productivity per ton mined": {
                "Tons per worker": "Total tons / Number of workers",
                "Labor productivity growth (%)": "(Current - Previous) / Previous * 100",
                "Overtime reduction (%)": "(Previous overtime - Current) / Previous * 100",
                "Cost per ton of labor ($)": "Labor cost / Tons mined"
            }
        },

        # -------------------- Profitability & Return Optimization --------------------
        "Mining Profitability & Return Optimization": {
            "Improve gross margin per ton of ore": {
                "Gross margin per ton (%)": "(Revenue - Direct costs) / Revenue * 100",
                "Gross margin growth (%)": "(Current - Previous) / Previous * 100",
                "High-margin ore ratio (%)": "Revenue from high-margin ore / Total revenue * 100",
                "Gross profit ($)": "Revenue - Direct costs"
            },
            "Optimize return on mining assets (ROA)": {
                "ROA (%)": "Net income / Total assets * 100",
                "Return per mine ($)": "Net profit per mine",
                "Asset utilization ratio (%)": "Revenue / Total assets * 100",
                "Capital efficiency ratio": "Output / Capital invested"
            },
            "Reduce operational cost-to-revenue ratio": {
                "Cost-to-revenue ratio (%)": "Operational costs / Revenue * 100",
                "Reduction in ratio (%)": "(Previous - Current) / Previous * 100",
                "Indirect cost efficiency": "Revenue / Indirect costs",
                "Operational leverage ratio": "Revenue growth / Cost growth"
            },
            "Maximize return on equity (ROE)": {
                "ROE (%)": "Net income / Shareholders' equity * 100",
                "Profit growth (%)": "(Current - Previous) / Previous * 100",
                "Net profit per shareholder ($)": "Net income / Number of shareholders",
                "Shareholder value added ($)": "Net profit - Cost of equity"
            }
        },

        # -------------------- Investment & Capital Management --------------------
        "Mining Investment & Capital Management": {
            "Optimize investment in new mining equipment": {
                "Equipment ROI (%)": "(Revenue or savings - Cost) / Cost * 100",
                "Equipment utilization rate (%)": "(Operational hours / Available hours) * 100",
                "Capex efficiency ratio": "Output / Capital expenditure",
                "Reduction in project overruns (%)": "(Planned - Actual) / Planned * 100"
            },
            "Diversify mining portfolio by commodity": {
                "Revenue diversification index": "Number of revenue sources / Total revenue",
                "Revenue share per commodity (%)": "Revenue by commodity / Total revenue * 100",
                "Contribution of new commodities (%)": "Revenue from new commodities / Total revenue * 100",
                "Risk-adjusted return per commodity (%)": "Return / Volatility measure"
            },
            "Minimize capital project overruns (%)": {
                "Project completion on budget (%)": "(Projects on budget / Total projects) * 100",
                "Cost variance ratio (%)": "(Budgeted - Actual cost) / Budgeted * 100",
                "Schedule adherence (%)": "(On-time projects / Total projects) * 100",
                "Stakeholder satisfaction": "Average project satisfaction score"
            },
            "Ensure efficient utilization of exploration and development capital": {
                "Capital utilization rate (%)": "Used capital / Allocated capital * 100",
                "Exploration ROI (%)": "(Revenue - Cost) / Cost * 100",
                "Development efficiency index": "Output / Capital invested",
                "Unutilized capital (%)": "(Allocated - Used) / Allocated * 100"
            }
        },

        # -------------------- Risk Management & Solvency --------------------
        "Mining Risk Management & Solvency": {
            "Hedge commodity price volatility": {
                "Hedging coverage (%)": "(Hedged production / Total production) * 100",
                "Revenue volatility reduction (%)": "(Previous volatility - Current) / Previous * 100",
                "Hedging ROI (%)": "(Revenue gained from hedging - Cost) / Cost * 100",
                "Number of hedged contracts": "Count of hedged contracts"
            },
            "Maintain sufficient insurance coverage for operations": {
                "Insurance coverage ratio (%)": "Insured value / Total asset value * 100",
                "Claims settlement ratio (%)": "(Settled claims / Total claims) * 100",
                "Premium efficiency ratio": "Insurance cost / Covered value * 100",
                "Coverage adequacy index": "Internal score for risk coverage"
            },
            "Reduce exposure to environmental penalties": {
                "Penalty incidence rate (%)": "(Penalties incurred / Total operations) * 100",
                "Penalty cost ($)": "Total penalty amount",
                "Compliance improvement (%)": "(Previous violations - Current) / Previous * 100",
                "Regulatory adherence ratio (%)": "(Compliant operations / Total operations) * 100"
            },
            "Monitor and maintain regulatory compliance costs": {
                "Compliance cost ratio (%)": "Regulatory costs / Revenue * 100",
                "Regulatory audit success rate (%)": "(Passed audits / Total audits) * 100",
                "Compliance efficiency index": "Output per compliance $ spent",
                "Penalty avoidance rate (%)": "(Penalties avoided / Total potential) * 100"
            }
        },

        # -------------------- Liquidity & Cash Flow Management --------------------
        "Mining Liquidity & Cash Flow Management": {
            "Ensure timely revenue collection from buyers": {
                "Days sales outstanding (DSO)": "Average collection period",
                "Collection efficiency (%)": "(Collected / Billed) * 100",
                "Past due ratio (%)": "Overdue invoices / Total invoices * 100",
                "Cash conversion cycle (days)": "DSO + Inventory days - Payables days"
            },
            "Maintain working capital for operational continuity": {
                "Current ratio": "Current assets / Current liabilities",
                "Quick ratio": "(Current assets - Inventory) / Current liabilities",
                "Working capital adequacy (%)": "Available working capital / Required working capital * 100",
                "Liquidity buffer ($)": "Cash and equivalents available for operations"
            },
            "Forecast cash flow for capital-intensive projects": {
                "Forecast accuracy (%)": "(Actual - Forecast) / Forecast * 100",
                "Operating cash balance ($)": "Cash available for operations",
                "Cash flow variance ($)": "Actual - Forecasted inflows",
                "Capital project coverage ratio (%)": "Forecasted cash / Project requirement * 100"
            },
            "Reduce idle cash and optimize reserve allocation": {
                "Idle cash ratio (%)": "Idle cash / Total cash * 100",
                "Excess reserve ratio (%)": "Excess reserves / Required reserves * 100",
                "Cash optimization ($)": "Amount released from idle/excess cash",
                "Reserve utilization efficiency (%)": "Reserves used / Total reserves * 100"
            }
        },
    },


"Customer Perspective": {

    **GENERIC_CUSTOMER_PERSPECTIVE['Customer Perspective'],

    # ------------------ 1. COMMUNITY & SOCIAL LICENSE ------------------
        "Community & Social License": {
            "Strengthen community trust and engagement": {
                "Community satisfaction rate (%)": "(Satisfied respondents / Total surveyed) * 100",
                "Community grievance resolution rate (%)": "(Resolved cases / Total cases) * 100",
                "CSR investment ($)": "Total funds allocated to community projects",
                "Local employment share (%)": "(Local employees / Total employees) * 100"
            },
            "Enhance local employment and skills development": {
                "Local workforce ratio (%)": "(Local workers / Total workers) * 100",
                "Training participation (#)": "Number of local trainees in mining programs",
                "Skill certification attainment (%)": "(Certified trainees / Total trained) * 100",
                "Post-training employment rate (%)": "(Employed trainees / Total trained) * 100"
            },
            "Promote equitable community benefit sharing": {
                "Revenue shared with communities ($)": "Funds disbursed to community trusts or programs",
                "Projects benefiting community (#)": "Community development initiatives completed",
                "Community benefit satisfaction (%)": "Surveyed satisfaction with benefit distribution",
                "Transparency disclosure rate (%)": "(Disclosed benefit reports / Total expected) * 100"
            },
            "Enhance corporate social responsibility performance": {
                "CSR index score": "Composite index from social, education, and health investments",
                "Volunteer hours (#)": "Total hours of staff volunteering",
                "Impact projects completed (#)": "CSR projects achieving measurable outcomes",
                "Community partnership programs (#)": "Collaborative initiatives with NGOs/local orgs"
            },
            "Foster environmental responsibility awareness": {
                "Community awareness programs (#)": "Environmental education events held",
                "Public environmental feedback score": "Average satisfaction with company’s green initiatives",
                "Waste reduction campaigns (#)": "Community-led clean-up or recycling events",
                "Air and water quality index (AQI/WQI)": "Measured environmental health indicators"
            },
            "Promote long-term community resilience": {
                "Livelihood diversification index": "Proportion of households with multiple income sources",
                "Household income growth (%)": "(Current average - Previous average) / Previous * 100",
                "Community dependency ratio (%)": "(Mining-dependent households / Total households) * 100",
                "Sustainability of local projects (%)": "(Active after 3 years / Total initiated) * 100"
            },
            "Improve local infrastructure support": {
                "Community infrastructure projects (#)": "Schools, clinics, roads built/upgraded",
                "Access to basic services (%)": "Households gaining new access to water/power",
                "Infrastructure satisfaction score": "Community survey rating",
                "Maintenance compliance rate (%)": "(Maintained projects / Total infrastructure) * 100"
            },
            "Ensure transparent community communication": {
                "Public meetings held (#)": "Formal stakeholder consultations conducted",
                "Information disclosure rate (%)": "(Published reports / Required reports) * 100",
                "Feedback turnaround time (days)": "Average response time to inquiries",
                "Trust index": "Survey-based composite of perceived transparency and fairness"
            },
        },

        # ------------------ 2. CITIZEN & NATIONAL BENEFIT ------------------
        "Citizen & National Benefit": {
            "Enhance contribution to national development": {
                "GDP contribution ($)": "Mining sector’s contribution to national GDP",
                "Local procurement ratio (%)": "(Local procurement / Total procurement) * 100",
                "Export revenue ($)": "Annual export income from minerals",
                "National employment share (%)": "(National employees / Total workforce) * 100"
            },
            "Promote fair and transparent resource management": {
                "Transparency compliance rate (%)": "(Reports published / Required disclosures) * 100",
                "Public disclosure score": "Evaluation of open data reporting",
                "Corruption incidents reported (#)": "Verified cases of malpractice",
                "Revenue reconciliation gap (%)": "(Reported vs actual payments difference / Total) * 100"
            },
            "Increase national beneficiation and value addition": {
                "Value-added exports (%)": "(Processed minerals / Total exports) * 100",
                "Local refining capacity utilization (%)": "(Actual / Installed capacity) * 100",
                "Jobs in value-added industries (#)": "Employment created in downstream sectors",
                "Technology transfer initiatives (#)": "Partnerships improving national capacity"
            },
            "Improve public perception of mining benefits": {
                "Citizen trust index": "Survey-based trust score in mining operations",
                "Media sentiment ratio (%)": "(Positive coverage / Total coverage) * 100",
                "Public awareness campaigns (#)": "Educational outreach programs conducted",
                "Perceived benefit distribution fairness (%)": "Survey-based fairness rating"
            },
            "Support local economic diversification": {
                "Non-mining SMEs supported (#)": "Entrepreneurs assisted through funding or training",
                "Local business survival rate (%)": "(Active SMEs / Total supported) * 100",
                "Employment outside mining (%)": "(Non-mining jobs / Total regional employment) * 100",
                "Microcredit disbursed ($)": "Funds extended to local entrepreneurs"
            },
            "Enhance citizen participation in resource governance": {
                "Public consultations (#)": "National or regional engagement events",
                "Citizen engagement index": "Composite score for inclusiveness",
                "Public input incorporated (%)": "(Policy changes based on input / Total proposals) * 100",
                "Satisfaction with participation (%)": "Citizen survey on engagement effectiveness"
            },
            "Ensure equitable taxation and royalty distribution": {
                "Royalty payments to regions ($)": "Amount disbursed to local governments",
                "Revenue transparency score": "Open data compliance indicator",
                "Delayed transfers (%)": "(Late payments / Total payments) * 100",
                "Beneficiary coverage (%)": "(Communities receiving shares / Total eligible) * 100"
            },
            "Promote long-term national resource sustainability": {
                "Resource depletion rate (%)": "(Extracted reserves / Total reserves) * 100",
                "Mine reclamation compliance (%)": "(Reclaimed sites / Closed sites) * 100",
                "Investment in restoration ($)": "Funds allocated to ecological recovery",
                "Public satisfaction with restoration (%)": "Citizen survey after site closure"
            },
        },

        # ------------------ 3. INVESTOR & PARTNER RELATIONS ------------------
        "Investor & Partner Relations": {
            "Improve investor confidence and transparency": {
                "Investor satisfaction rate (%)": "(Satisfied investors / Total investors) * 100",
                "Financial disclosure compliance (%)": "(Reports published / Required) * 100",
                "Timely reporting rate (%)": "(On-time reports / Total) * 100",
                "Investor retention rate (%)": "(Returning investors / Total investors) * 100"
            },
            "Promote ESG (Environmental, Social, Governance) excellence": {
                "ESG score": "External ESG performance rating",
                "Sustainability reporting compliance (%)": "(Published reports / Required reports) * 100",
                "ESG investment ratio (%)": "(Funds in ESG projects / Total investment) * 100",
                "Stakeholder ESG satisfaction (%)": "Investor perception of ESG performance"
            },
            "Enhance joint venture collaboration": {
                "Partnership satisfaction score": "Survey score from JV partners",
                "Project milestones achieved on time (%)": "(Achieved / Planned milestones) * 100",
                "Conflict incidents (#)": "Recorded partnership conflicts",
                "Joint investment volume ($)": "Total capital deployed in joint ventures"
            },
            "Attract new investors and diversify funding sources": {
                "New investors acquired (#)": "Investors entering in current year",
                "Funding diversity index": "Ratio of funding types used",
                "Capital inflow growth (%)": "(Current inflow - Previous) / Previous * 100",
                "Investor conversion rate (%)": "(Interested / Actual investors) * 100"
            },
            "Strengthen investor communication and reporting": {
                "Reports published on schedule (%)": "(Published on time / Total planned) * 100",
                "Investor briefing sessions (#)": "Meetings or calls held with investors",
                "Feedback response time (days)": "Average days to respond to investor inquiries",
                "Transparency index score": "Third-party evaluation of disclosure"
            },
            "Improve credit and risk perception": {
                "Credit rating score": "External or national rating agency score",
                "Risk mitigation plans implemented (%)": "(Implemented / Total plans) * 100",
                "Insurance coverage ratio (%)": "(Insured assets / Total assets) * 100",
                "Investment default rate (%)": "(Defaults / Total projects) * 100"
            },
            "Increase shareholder value": {
                "Dividend payout ratio (%)": "(Dividends / Net income) * 100",
                "Return on equity (%)": "(Net income / Equity) * 100",
                "Market valuation ($)": "Current valuation of firm",
                "Earnings per share ($)": "Total earnings / Shares outstanding"
            },
            "Encourage long-term partnerships": {
                "Partnership renewal rate (%)": "(Renewed partnerships / Total expiring) * 100",
                "Partner Net Promoter Score (NPS)": "Average likelihood of partners recommending the firm",
                "Collaborative innovation projects (#)": "Joint R&D or efficiency programs",
                "Shared investment growth (%)": "(Partner investment current - previous) / previous * 100"
            },
        },

        # ------------------ 4. GOVERNMENT & REGULATORY RELATIONS ------------------
        "Government & Regulatory Relations": {
            "Ensure full legal and regulatory compliance": {
                "Regulatory compliance rate (%)": "(Compliant processes / Total inspected) * 100",
                "Audit pass rate (%)": "(Audits passed / Total conducted) * 100",
                "Licensing renewal success (%)": "(Renewed licenses / Total due) * 100",
                "Violations reported (#)": "Number of compliance violations"
            },
            "Strengthen intergovernmental cooperation": {
                "Policy dialogue sessions (#)": "Meetings held with government bodies",
                "Joint initiatives implemented (#)": "Collaborative projects executed",
                "Government satisfaction score": "Evaluation from counterpart agencies",
                "Policy alignment index": "Degree of alignment with national mining strategy"
            },
            "Enhance public reporting and accountability": {
                "Reports submitted on time (%)": "(On-time submissions / Total required) * 100",
                "Audit findings resolved (%)": "(Resolved issues / Total findings) * 100",
                "Transparency compliance (%)": "(Reports published / Expected reports) * 100",
                "Regulatory rating score": "External assessment of compliance integrity"
            },
            "Improve responsiveness to government directives": {
                "Response time to directives (days)": "Average time to comply",
                "Implementation rate (%)": "(Implemented recommendations / Total received) * 100",
                "Government communication frequency (#)": "Number of bilateral updates per quarter",
                "Satisfaction with responsiveness (%)": "Survey-based rating from regulators"
            },
            "Promote good governance in the mining sector": {
                "Governance index score": "Composite rating for governance performance",
                "Anti-corruption policy adherence (%)": "(Compliant units / Total units) * 100",
                "Ethics training completion (%)": "(Staff trained / Total staff) * 100",
                "Reported ethical violations (#)": "Confirmed ethical breaches"
            },
            "Increase local government capacity building": {
                "Local officials trained (#)": "Government representatives trained",
                "Policy workshops conducted (#)": "Capacity-building sessions held",
                "Adoption of mining best practices (%)": "(Local govs adopting best practices / Total) * 100",
                "Satisfaction with training (%)": "Feedback from trained officials"
            },
            "Support policy innovation and reform": {
                "Policy studies commissioned (#)": "Research projects initiated",
                "Recommendations adopted (%)": "(Implemented / Proposed reforms) * 100",
                "New policy frameworks supported (#)": "Developed or amended policies",
                "Regulatory improvement index": "Independent score of regulatory enhancement"
            },
            "Foster inter-agency collaboration": {
                "Collaborative programs (#)": "Inter-ministerial or agency programs",
                "Joint reports published (#)": "Multi-agency publications",
                "Coordinated inspections (%)": "(Joint inspections / Total inspections) * 100",
                "Stakeholder alignment score": "Surveyed alignment across agencies"
            },
        },

        # ------------------ 5. SUPPLY CHAIN & CONTRACTORS ------------------
        "Supply Chain & Contractors": {
            "Promote local supplier participation": {
                "Local supplier ratio (%)": "(Local suppliers / Total suppliers) * 100",
                "Procurement from local vendors ($)": "Spend on domestic suppliers",
                "Local content development projects (#)": "Programs for supplier capacity building",
                "Supplier satisfaction score": "Survey feedback on partnership quality"
            },
            "Ensure supplier quality and reliability": {
                "Supplier on-time delivery rate (%)": "(On-time deliveries / Total deliveries) * 100",
                "Contract compliance rate (%)": "(Compliant suppliers / Total suppliers) * 100",
                "Defective supplies rate (%)": "(Defective shipments / Total shipments) * 100",
                "Approved supplier ratio (%)": "(Certified suppliers / Total suppliers) * 100"
            },
            "Enhance supplier capacity and training": {
                "Suppliers trained (#)": "Number of contractors attending development sessions",
                "Certification attainment rate (%)": "(Certified suppliers / Trained suppliers) * 100",
                "Post-training improvement index": "Performance score improvement after training",
                "Supplier innovation projects (#)": "Initiatives co-developed with suppliers"
            },
            "Encourage ethical sourcing": {
                "Supplier code compliance (%)": "(Compliant suppliers / Total) * 100",
                "Audited suppliers (#)": "Vendors audited for ethical standards",
                "Non-compliance cases (#)": "Confirmed violations",
                "Corrective actions implemented (%)": "(Completed actions / Total identified) * 100"
            },
            "Optimize procurement efficiency": {
                "Procurement cycle time (days)": "Average time per purchase cycle",
                "E-procurement adoption rate (%)": "(Digital transactions / Total) * 100",
                "Cost savings achieved (%)": "(Baseline cost - Actual cost) / Baseline * 100",
                "Process automation index": "Level of automation in procurement workflow"
            },
            "Promote supplier diversity and inclusion": {
                "SME suppliers engaged (#)": "Small and medium suppliers under contract",
                "Women-owned suppliers (%)": "(Women-owned suppliers / Total) * 100",
                "Diverse supplier spend (%)": "(Spend on diverse suppliers / Total spend) * 100",
                "Supplier diversity index": "Composite diversity performance score"
            },
            "Improve contractor performance management": {
                "Contractor evaluation score": "Average performance rating",
                "Contract renewal rate (%)": "(Renewed / Total expiring contracts) * 100",
                "Penalty incidents (#)": "Number of contract breaches",
                "Contract closure success rate (%)": "(Completed without issues / Total contracts) * 100"
            },
            "Enhance strategic supplier partnerships": {
                "Long-term agreements signed (#)": "Strategic partnerships with key vendors",
                "Joint development projects (#)": "Collaborations on innovation or sustainability",
                "Supplier retention rate (%)": "(Returning suppliers / Total) * 100",
                "Partnership growth index": "Supplier contribution growth over baseline"
            },
        }
    },

"Internal Process Perspective": {
    "Mining Operations Excellence": {
        "Optimize Production Efficiency": {
            "Ore production rate": "Tons of ore produced per operating hour",
            "Equipment productivity": "Tons moved per equipment hour",
            "Mining recovery rate": "(Ore recovered / Total ore in place) * 100",
            "Dilution control": "Reduction in waste material in ore"
        },
        "Enhance Mine Planning": {
            "Mine plan adherence": "(Actual vs planned production) * 100",
            "Reserve utilization efficiency": "Percentage of reserves efficiently extracted",
            "Grade control effectiveness": "Accuracy of grade estimation and control",
            "Mine sequencing optimization": "Efficiency of mine development sequence"
        },
        "Improve Drilling & Blasting": {
            "Drilling accuracy": "Deviation from planned drill patterns",
            "Blasting efficiency": "Fragmentation quality vs energy consumption",
            "Vibration control": "Compliance with vibration limits",
            "Explosives consumption optimization": "Explosives used per ton broken"
        },
        "Optimize Loading & Hauling": {
            "Truck productivity": "Tons hauled per truck hour",
            "Loader efficiency": "Tons loaded per loader hour",
            "Haul road maintenance": "Haul road condition index",
            "Cycle time optimization": "Reduction in load-haul-dump cycle times"
        }
    },

    "Mineral Processing Excellence": {
        "Enhance Processing Efficiency": {
            "Plant throughput rate": "Tons processed per operating hour",
            "Recovery rate optimization": "(Metal recovered / Metal in ore) * 100",
            "Grade improvement": "Concentrate grade achieved",
            "Processing cost efficiency": "Cost per ton processed"
        },
        "Improve Crushing & Grinding": {
            "Crushing circuit efficiency": "Throughput vs energy consumption",
            "Grinding optimization": "Particle size distribution control",
            "Mill availability": "(Operating time / Available time) * 100",
            "Media consumption efficiency": "Grinding media consumption per ton"
        },
        "Optimize Separation Processes": {
            "Separation efficiency": "Effectiveness of mineral separation",
            "Reagent consumption optimization": "Reagents used per ton processed",
            "Water usage efficiency": "Water consumed per ton processed",
            "Circuit stability": "Consistency of process performance"
        },
        "Enhance Dewatering & Tailings": {
            "Moisture content control": "Achievement of target moisture levels",
            "Tailings density optimization": "Solid content in tailings",
            "Water recovery rate": "(Water recycled / Total water used) * 100",
            "Tailings storage efficiency": "Space utilization in tailings facilities"
        }
    },

    "Maintenance & Reliability": {
        "Improve Equipment Reliability": {
            "Mean time between failures": "Average operating hours between equipment failures",
            "Equipment availability": "(Available hours / Total hours) * 100",
            "Reliability-centered maintenance": "Effectiveness of reliability programs",
            "Component life optimization": "Actual life vs expected life of components"
        },
        "Enhance Maintenance Efficiency": {
            "Maintenance cost control": "Maintenance cost as percentage of operating cost",
            "Preventive maintenance compliance": "(Completed PM / Scheduled PM) * 100",
            "Maintenance planning accuracy": "Accuracy of maintenance schedules and estimates",
            "Work order completion rate": "(Completed work orders / Total work orders) * 100"
        },
        "Optimize Spare Parts Management": {
            "Inventory turnover ratio": "Cost of parts used / Average inventory",
            "Critical spares availability": "Availability of critical spare parts",
            "Parts obsolescence reduction": "Reduction in obsolete inventory",
            "Supplier response time": "Time for parts delivery from suppliers"
        },
        "Develop Maintenance Capability": {
            "Maintenance technician certification": "(Certified technicians / Total technicians) * 100",
            "Training effectiveness": "Improvement in maintenance performance post-training",
            "Technology adoption in maintenance": "Use of advanced maintenance technologies",
            "Continuous improvement in maintenance": "Number of maintenance process improvements"
        }
    },

    "Supply Chain & Logistics": {
        "Enhance Procurement Efficiency": {
            "Supplier performance rating": "Average rating of supplier performance",
            "Procurement cycle time": "Time from requisition to delivery",
            "Cost reduction achievement": "Savings from procurement initiatives",
            "Supplier relationship management": "Effectiveness of supplier partnerships"
        },
        "Optimize Inventory Management": {
            "Inventory accuracy": "(Accurate inventory records / Total items) * 100",
            "Stock-out prevention": "Reduction in production interruptions from stock-outs",
            "Inventory carrying cost": "Cost of inventory as percentage of total cost",
            "Inventory turnover improvement": "Increase in inventory turnover rate"
        },
        "Improve Logistics Operations": {
            "Shipping efficiency": "Cost per ton shipped",
            "Port and terminal operations": "Efficiency of export logistics",
            "Customs clearance time": "Reduction in border clearance delays",
            "Transport safety performance": "Safety record in logistics operations"
        },
        "Strengthen Supply Chain Resilience": {
            "Supply chain risk assessment": "Completeness of supply chain risk evaluation",
            "Alternative sourcing development": "Availability of backup suppliers",
            "Logistics contingency planning": "Effectiveness of logistics backup plans",
            "Supply chain visibility": "Transparency across supply chain stages"
        }
    },

    "Safety, Health & Environment": {
        "Enhance Safety Performance": {
            "Lost time injury frequency rate": "Number of lost time injuries per million hours",
            "Total recordable injury rate": "Total recordable incidents per million hours",
            "Safety training completion": "(Completed safety training / Required training) * 100",
            "Safety observation participation": "Percentage of employees participating in safety observations"
        },
        "Improve Health Management": {
            "Occupational health compliance": "Adherence to health regulations and standards",
            "Health surveillance coverage": "(Monitored employees / Total employees) * 100",
            "Wellness program effectiveness": "Participation and outcomes of wellness programs",
            "Dust and noise exposure control": "Reduction in exposure to workplace hazards"
        },
        "Strengthen Environmental Management": {
            "Environmental compliance rate": "(Compliant operations / Total operations) * 100",
            "Emissions reduction": "((Previous emissions - Current emissions) / Previous emissions) * 100",
            "Water management effectiveness": "Efficiency of water use and treatment",
            "Biodiversity protection": "Effectiveness of biodiversity conservation measures"
        },
        "Enhance Emergency Preparedness": {
            "Emergency response capability": "Score from emergency response drills",
            "Crisis management effectiveness": "Response quality in actual emergencies",
            "Business continuity planning": "Completeness and testing of continuity plans",
            "Community emergency coordination": "Effectiveness of community emergency planning"
        }
    },

    "Technology & Innovation": {
        "Implement Mining Technology": {
            "Automation adoption rate": "(Automated processes / Total processes) * 100",
            "Digital mine implementation": "Progress in digital transformation initiatives",
            "Remote operations capability": "Percentage of operations controllable remotely",
            "Real-time monitoring coverage": "(Monitored processes / Total processes) * 100"
        },
        "Advance Geological Systems": {
            "Geological modeling accuracy": "Accuracy of resource models vs actual results",
            "Exploration technology adoption": "Use of advanced exploration technologies",
            "Grade control system effectiveness": "Accuracy of grade control systems",
            "Data management quality": "Quality and accessibility of geological data"
        },
        "Enhance Process Optimization": {
            "Process control system utilization": "Use of advanced process control systems",
            "Analytical capability": "Speed and accuracy of process analysis",
            "Optimization algorithm effectiveness": "Performance of process optimization algorithms",
            "Digital twin implementation": "Use of digital twins for process simulation"
        },
        "Develop Innovation Pipeline": {
            "R&D project success rate": "(Successful projects / Total projects) * 100",
            "Technology implementation success": "(Successfully implemented technologies / Total technologies) * 100",
            "Innovation culture assessment": "Employee engagement in innovation activities",
            "Intellectual property generation": "Number of patents and proprietary technologies"
        }
    }
},

"Learning & Growth Perspective": {
    "Workforce Development & Capability": {
        "Enhance Technical Skills": {
            "Technical training completion": "(Completed technical training / Required training) * 100",
            "Certification achievement": "(Certified employees / Total employees) * 100",
            "Skills assessment performance": "Results from skills competency assessments",
            "Cross-functional training": "Percentage of employees with cross-functional skills"
        },
        "Improve Operational Competence": {
            "Equipment operation certification": "(Certified operators / Total operators) * 100",
            "Process knowledge assessment": "Employee understanding of mining processes",
            "Safety competency development": "Safety skills and knowledge levels",
            "Maintenance capability enhancement": "Improvement in maintenance skills"
        },
        "Develop Leadership Talent": {
            "Leadership program completion": "(Completed programs / Eligible leaders) * 100",
            "Succession planning coverage": "Percentage of key roles with identified successors",
            "Management competency assessment": "Score from management capability evaluations",
            "Mentoring program effectiveness": "Quality and impact of mentoring programs"
        },
        "Enhance Digital Literacy": {
            "Digital skills proficiency": "(Proficient users / Total users) * 100",
            "Software application mastery": "Proficiency in mining software systems",
            "Data analytics capability": "Ability to use data for operational decisions",
            "Automation system proficiency": "Skill level with automation and control systems"
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
            "Patent and IP generation": "Number of mining-related patents filed",
            "Research collaboration effectiveness": "Success rate of research partnerships",
            "Innovation pipeline strength": "Number of innovations in development pipeline"
        },
        "Improve Technology Infrastructure": {
            "IT system reliability": "Uptime percentage of critical mining systems",
            "Data security compliance": "Score from cybersecurity and data protection audits",
            "Network performance optimization": "Speed and reliability of mine communication networks",
            "Technology scalability readiness": "Ability to scale technological solutions across operations"
        },
        "Advance Automation & AI": {
            "Process automation level": "Percentage of automatable processes automated",
            "AI implementation success": "(Successful AI implementations / Total AI projects) * 100",
            "Machine learning model accuracy": "Performance of ML models in mining applications",
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
            "Energy efficiency improvement": "((Previous consumption - Current consumption) / Previous consumption) * 100",
            "Water stewardship effectiveness": "Improvement in water management practices",
            "Biodiversity management enhancement": "Effectiveness of biodiversity conservation"
        },
        "Enhance Sustainable Practices": {
            "Waste reduction achievement": "Reduction in mining and processing waste",
            "Recycling and reuse rates": "Percentage of materials recycled or reused",
            "Green procurement adoption": "Percentage of sustainable purchases",
            "Environmental management system certification": "Maintenance of environmental certifications"
        },
        "Develop Circular Economy": {
            "Resource efficiency improvement": "((Previous resource use - Current use) / Previous use) * 100",
            "Waste valorization rate": "(Waste converted to value / Total waste) * 100",
            "By-product utilization": "Percentage of by-products commercially used",
            "Mine closure planning integration": "Integration of closure planning into operations"
        },
        "Strengthen Environmental Management": {
            "Environmental risk assessment": "Thoroughness of environmental risk evaluation",
            "Compliance assurance systems": "Effectiveness of compliance monitoring",
            "Stakeholder environmental engagement": "Quality of environmental stakeholder dialogue",
            "Sustainability reporting quality": "Quality and transparency of sustainability reports"
        }
    },

    "Health, Safety & Wellbeing": {
        "Enhance Workplace Safety": {
            "Safety culture assessment": "Employee rating of safety culture",
            "Behavior-based safety effectiveness": "Impact of behavior-based safety programs",
            "Safety leadership development": "Effectiveness of safety leadership training",
            "Incident investigation quality": "Thoroughness and learning from incidents"
        },
        "Improve Employee Wellbeing": {
            "Employee health assessment": "Results from health and wellbeing surveys",
            "Work-life balance satisfaction": "Employee rating of work-life balance",
            "Stress management effectiveness": "Reduction in stress-related absences",
            "Wellbeing program participation": "Percentage of employees in wellbeing programs"
        },
        "Strengthen Occupational Health": {
            "Health risk assessment completeness": "Thoroughness of occupational health risk assessments",
            "Exposure monitoring effectiveness": "Quality of workplace exposure monitoring",
            "Health surveillance coverage": "(Monitored employees / Total employees) * 100",
            "Mental health support accessibility": "Employee access to mental health resources"
        },
        "Develop Safety Systems": {
            "Safety management system effectiveness": "Score from safety management audits",
            "Emergency response capability": "Readiness for safety emergencies",
            "Safety technology adoption": "Use of advanced safety technologies",
            "Contractor safety management": "Effectiveness of contractor safety oversight"
        }
    },

    "Stakeholder & Community Development": {
        "Promote Industry Leadership": {
            "Industry standard participation": "Involvement in mining industry standards development",
            "Thought leadership impact": "Influence in mining industry discussions",
            "Professional association engagement": "Level of participation in professional organizations",
            "Industry education contribution": "Contribution to mining education and training"
        },
        "Enhance Community Relations": {
            "Local community investment": "Investment in local community development",
            "Community partnership effectiveness": "Success rate of community partnership projects",
            "Local economic impact": "Contribution to local economic development",
            "Community perception improvement": "Improvement in community satisfaction scores"
        },
        "Develop Supply Chain Partnerships": {
            "Supplier development programs": "Number of supplier capability development initiatives",
            "Local business support": "Effectiveness of local business development programs",
            "Community procurement integration": "Integration of local businesses in supply chain",
            "Partner capability enhancement": "Improvement in partner capabilities through collaboration"
        },
        "Strengthen Social Performance": {
            "Social impact assessment quality": "Thoroughness of social impact evaluations",
            "Stakeholder engagement effectiveness": "Quality of stakeholder relationship management",
            "Human rights compliance": "Adherence to human rights standards",
            "Social license maintenance": "Effectiveness in maintaining social acceptance"
        }
    }
}
}
