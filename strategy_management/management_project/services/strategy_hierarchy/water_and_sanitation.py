from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE

WATER_AND_SANITATION_PERSPECTIVE = {
    "Financial Perspective": {
        # Import the generic financial KPIs
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],

        # -------------------- Revenue Growth & Diversification --------------------
        "Revenue Growth & Diversification": {
            "Maximize Utility Service Revenue": {
                "Water Service Revenue Growth": "(Current Water Revenue - Previous Water Revenue) / Previous Water Revenue * 100",
                "Energy Service Revenue Growth": "(Current Energy Revenue - Previous Energy Revenue) / Previous Energy Revenue * 100",
                "Combined Utility Revenue Optimization": "Optimal Combined Revenue / Total Potential Revenue * 100",
                "Service Tier Revenue Diversification": "Diversified Tier Revenue / Total Revenue * 100"
            },
            "Expand Renewable Energy Revenue": {
                "Renewable Energy Revenue Growth": "(Current Renewable Revenue - Previous Renewable Revenue) / Previous Renewable Revenue * 100",
                "Green Energy Premium Revenue": "Green Premium Revenue / Total Energy Revenue * 100",
                "Carbon Credit Revenue Generation": "Carbon Credit Revenue / Total Revenue * 100",
                "Renewable Certificate Sales Growth": "(Current REC Sales - Previous REC Sales) / Previous REC Sales * 100"
            },
            "Develop Water Reuse Revenue Streams": {
                "Recycled Water Revenue Growth": "(Current Recycled Water Revenue - Previous) / Previous * 100",
                "Industrial Water Reuse Contracts": "Industrial Reuse Revenue / Total Water Revenue * 100",
                "Agricultural Reuse Program Revenue": "Agricultural Reuse Revenue / Total Water Revenue * 100",
                "Graywater System Revenue Contribution": "Graywater Revenue / Total Water Revenue * 100"
            },
            "Enhance Energy Efficiency Services Revenue": {
                "ESCO Revenue Growth": "(Current ESCO Revenue - Previous ESCO Revenue) / Previous ESCO Revenue * 100",
                "Energy Audit Service Revenue": "Energy Audit Revenue / Total Service Revenue * 100",
                "Efficiency Retrofit Project Revenue": "Retrofit Project Revenue / Total Revenue * 100",
                "Demand Response Program Revenue": "Demand Response Revenue / Total Energy Revenue * 100"
            },
            "Diversify Infrastructure Services Revenue": {
                "Infrastructure Consulting Revenue": "Consulting Revenue / Total Revenue * 100",
                "Smart Grid Service Revenue Growth": "(Current Smart Grid Revenue - Previous) / Previous * 100",
                "Water Infrastructure Management Revenue": "Infrastructure Management Revenue / Total Revenue * 100",
                "Public-Private Partnership Revenue": "PPP Revenue / Total Revenue * 100"
            }
        },


         # -------------------- Asset Management & Investment --------------------
        "Water Asset Management & Investment": {
            "Improve Infrastructure Asset Performance": {
                "Asset Utilization Rate": "Utilized Assets / Total Assets * 100",
                "Infrastructure Reliability Index": "Reliable Infrastructure / Total Infrastructure * 100",
                "Asset Condition Improvement": "(Current Condition Score - Previous Condition Score) / Previous Condition Score * 100",
                "Critical Asset Performance": "Performing Critical Assets / Total Critical Assets * 100"
            },
            "Optimize Capital Investment Returns": {
                "ROI on Infrastructure Projects": "Net Project Benefits / Project Costs * 100",
                "Capital Budget Adherence": "Adhered Capital Budget / Total Capital Budget * 100",
                "Project Delivery Efficiency": "Efficient Project Deliveries / Total Projects * 100",
                "Infrastructure Investment Performance": "Performing Investments / Total Investments * 100"
            },
            "Enhance Renewable Energy Assets": {
                "Renewable Asset Capacity Utilization": "Utilized Renewable Capacity / Total Renewable Capacity * 100",
                "Solar Farm Performance Ratio": "Actual Output / Theoretical Output * 100",
                "Wind Farm Capacity Factor": "Actual Output / Maximum Possible Output * 100",
                "Hydroelectric Efficiency Improvement": "(Current Hydro Efficiency - Previous) / Previous * 100"
            },
            "Strengthen Water Infrastructure Assets": {
                "Water Treatment Plant Efficiency": "Efficient Treatment Plants / Total Plants * 100",
                "Pipeline Network Performance": "Performing Pipeline Network / Total Network * 100",
                "Reservoir Storage Optimization": "Optimal Storage Utilization / Total Storage * 100",
                "Pumping Station Reliability": "Reliable Pumping Stations / Total Stations * 100"
            },
            "Improve Grid and Network Assets": {
                "Grid Reliability Improvement": "(Current Reliability - Previous Reliability) / Previous Reliability * 100",
                "Transmission Line Performance": "Performing Transmission Lines / Total Lines * 100",
                "Substation Asset Health": "Healthy Substations / Total Substations * 100",
                "Distribution Network Efficiency": "Efficient Distribution Network / Total Network * 100"
            }
        },

        # -------------------- Water & Sanitation Economic Development --------------------
        "Water & Sanitation Economic Development": {
            "Expand Access to Safe Water": {
                "Population with improved water access (%)": "(Population with access / Total population) * 100",
                "New water connections": "Number of new connections installed",
                "Revenue from new connections ($)": "Revenue from newly connected households",
                "Capital investment in access expansion ($)": "Funds invested in extending networks"
            },
            "Improve Sanitation Coverage": {
                "Population with improved sanitation (%)": "(Population with sanitation / Total population) * 100",
                "New sanitation facilities installed": "Number of facilities constructed",
                "Revenue from sanitation services ($)": "Revenue from sanitation services",
                "Capital investment in sanitation infrastructure ($)": "Funds invested in sanitation expansion"
            },
            "Enhance Service Reliability & Quality": {
                "Service uptime (%)": "(Hours service available / Total hours) * 100",
                "Water quality compliance (%)": "Samples passing regulatory standards / Total samples * 100",
                "Customer complaints reduction (%)": "(Previous complaints - Current) / Previous * 100",
                "Operational efficiency index": "Water delivered / Energy and cost used"
            },
            "Promote Sustainability & Environmental Protection": {
                "Non-revenue water reduction (%)": "(Lost water / Total water produced) * 100",
                "Energy efficiency in treatment plants (%)": "Energy consumed per m³ treated water",
                "Renewable energy adoption (%)": "Energy from renewable sources / Total energy used * 100",
                "Wastewater treated (%)": "Volume of wastewater treated / Total wastewater generated * 100"
            },
            "Contribute to Economic & Community Development": {
                "Jobs created in water projects": "Number of new jobs generated by water initiatives",
                "Local community engagement programs (#)": "Number of community programs implemented",
                "GDP contribution from water projects ($)": "Estimated economic contribution from water infrastructure",
                "Investment in public health initiatives ($)": "Funds allocated to hygiene and sanitation education"
            }
        }
    }
}
