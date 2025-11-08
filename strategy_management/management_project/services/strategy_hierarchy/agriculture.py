from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE_DATA

AGRICULTURE_PERSPECTIVE = {

    "Financial Perspective": {
        **GENERIC_FINANCE_PERSPECTIVE_DATA['Financial Perspective'],
        # ==================== CROP ENTERPRISE FINANCE ====================
        "Crop Revenue Growth & Diversification": {
            "Enhance Crop Revenue Performance": {
                "Total crop revenue growth (%)": "(Current revenue - Previous) / Previous * 100",
                "Revenue per hectare ($/ha)": "Total revenue / Cultivated area",
                "Seasonal revenue growth rate (%)": "Revenue change across seasons",
                "Revenue per farmer growth (%)": "(Current revenue per farmer - Previous) / Previous * 100"
            },
            "Strengthen Market Share & Crop Positioning": {
                "Market share in key crops (%)": "(Production / Total market supply) * 100",
                "Revenue in high-value crops ($)": "Income from selected high-value crops",
                "Geographic expansion revenue ($)": "Revenue from new regions or export markets",
                "Competitive win rate (%)": "(Contracts won / Total bids) * 100"
            },
            "Accelerate New Crop Product Revenue": {
                "Revenue from improved crop varieties (%)": "(Revenue from new varieties / Total revenue) * 100",
                "Time-to-revenue for new crops (months)": "Speed from planting to harvest and sale",
                "R&D ROI from crop innovations (%)": "(Revenue from new varieties / R&D investment) * 100",
                "Adoption rate of new farming techniques (%)": "Farmers adopting new techniques"
            },
            "Diversify Crop Revenue Streams": {
                "Revenue diversity index": "1 - (Top 3 crop revenue / Total revenue)",
                "Revenue from intercropping/secondary crops ($)": "Income from non-main crops",
                "Revenue from processed crop products ($)": "Income from value-added crop products",
                "Passive income growth (%)": "Growth in non-farm or non-seasonal income"
            }
        },

        "Crop Profitability Optimization": {
            "Maximize Net Crop Income": {
                "Net profit margin (%)": "(Net income / Total revenue) * 100",
                "Profit growth rate (%)": "(Current profit - Previous) / Previous * 100",
                "Return per hectare ($/ha)": "Profit per cultivated area",
                "Earnings quality index": "Stability and sustainability of crop earnings"
            },
            "Enhance Gross Margin Performance": {
                "Gross margin (%)": "(Revenue - Direct costs) / Revenue * 100",
                "Crop-specific margin improvement (%)": "Increase in least profitable crops",
                "Direct input cost efficiency (%)": "Reduction in seeds, fertilizer, labor costs",
                "Pricing strategy effectiveness": "Impact of price adjustments on gross margin"
            },
            "Improve Operating Profitability": {
                "Operating profit margin (%)": "(Operating income / Revenue) * 100",
                "Operating leverage ratio": "Revenue growth vs. operating cost growth",
                "Profitability by crop type": "Profit contribution by crop categories",
                "Break-even production reduction": "Reduced production needed to break even"
            },
            "Optimize Contribution Margins": {
                "Average contribution margin (%)": "(Revenue - Variable costs) / Revenue * 100",
                "Farmer group profitability index": "Profit contribution by farmer groups",
                "Crop mix margin optimization (%)": "Weighted margin across crops",
                "Variable cost control efficiency (%)": "Reduction in direct input costs"
            }
        },

        "Livestock Revenue Growth & Diversification": {
            "Enhance Livestock Revenue Performance": {
                "Total livestock revenue growth (%)": "(Current revenue - Previous) / Previous * 100",
                "Revenue per head ($/head)": "Total revenue / Total animals",
                "Seasonal revenue growth rate (%)": "Revenue change across seasons",
                "Revenue per farm growth (%)": "(Current revenue per farm - Previous) / Previous * 100"
            },
            "Strengthen Market Share & Livestock Positioning": {
                "Market share in key livestock products (%)": "(Production / Total market supply) * 100",
                "Revenue in premium livestock products ($)": "Income from selected high-value animals",
                "Geographic expansion revenue ($)": "Revenue from new regions or export markets",
                "Contracted supply revenue ($)": "Revenue from contract farming or agreements"
            },
            "Accelerate New Livestock Product Revenue": {
                "Revenue from processed livestock products (%)": "(Processed product sales / Total revenue) * 100",
                "R&D ROI from breeding programs (%)": "(Revenue from improved breeds / R&D investment) * 100",
                "Time-to-revenue for new livestock breeds (months)": "Speed from breeding to market",
                "Adoption rate of improved feeding/management (%)": "Share of farms adopting new practices"
            },
            "Diversify Livestock Revenue Streams": {
                "Revenue diversity index": "1 - (Top 3 livestock product revenue / Total revenue)",
                "Revenue from dairy & by-products ($)": "Income from milk, cheese, leather",
                "Revenue from value-added meat products ($)": "Income from processed meat products",
                "Revenue from ancillary services ($)": "Revenue from veterinary or consultancy services"
            }
        },

        "Livestock Profitability Optimization": {
            "Maximize Net Livestock Income": {
                "Net profit margin (%)": "(Net income / Total revenue) * 100",
                "Profit growth rate (%)": "(Current profit - Previous) / Previous * 100",
                "Return per head ($/head)": "Profit per animal",
                "Earnings quality index": "Stability and sustainability of livestock earnings"
            },
            "Enhance Gross Margin Performance": {
                "Gross margin (%)": "(Revenue - Direct costs) / Revenue * 100",
                "Product-specific margin improvement (%)": "Increase in least profitable livestock products",
                "Direct input cost efficiency (%)": "Reduction in feed, medicine, labor costs",
                "Pricing strategy effectiveness": "Impact of price adjustments on gross margin"
            },
            "Improve Operating Profitability": {
                "Operating profit margin (%)": "(Operating income / Revenue) * 100",
                "Operating leverage ratio": "Revenue growth vs. operating cost growth",
                "Profitability by livestock type": "Profit contribution by species",
                "Break-even production reduction": "Reduced production needed to break even"
            },
            "Optimize Contribution Margins": {
                "Average contribution margin (%)": "(Revenue - Variable costs) / Revenue * 100",
                "Farm group profitability index": "Profit contribution by farm groups",
                "Product mix margin optimization (%)": "Weighted margin across livestock products",
                "Variable cost control efficiency (%)": "Reduction in direct feed and veterinary costs"
            }
        },

        # ==================== LIVESTOCK ENTERPRISE FINANCE ====================
        "Livestock Enterprise Finance": {
            "Maximize Livestock Revenue Performance": {
                "Revenue per animal unit": "Total livestock revenue divided by total animal units",
                "Meat yield revenue efficiency": "Actual meat revenue divided by potential meat revenue times 100",
                "Dairy production revenue per cow": "Total dairy revenue divided by number of milking cows",
                "Livestock product premium capture": "Premium product price minus standard price divided by standard price times 100"
            },
            "Optimize Livestock Input Cost Management": {
                "Feed conversion efficiency": "Feed cost per unit of weight gain or milk production",
                "Veterinary cost per animal": "Total veterinary costs divided by total animal units",
                "Livestock housing cost efficiency": "Housing costs divided by animal units",
                "Breeding cost per offspring": "Total breeding costs divided by number of viable offspring"
            },
            "Improve Livestock Profitability": {
                "Livestock gross margin per unit": "Livestock revenue minus direct livestock costs divided by animal units",
                "Livestock break-even weight": "Total livestock costs divided by market price per kg",
                "Livestock return on investment": "Livestock net profit divided by total livestock investment times 100",
                "Cost of production per kg": "Total production cost divided by total meat or milk output"
            }
        },

        "Fishery Revenue Growth & Diversification": {
            "Enhance Fishery Revenue Performance": {
                "Total fishery revenue growth (%)": "(Current revenue - Previous) / Previous * 100",
                "Revenue per ton of fish ($)": "Total revenue / Total catch or production",
                "Seasonal revenue growth rate (%)": "Revenue change across fishing seasons",
                "Revenue per fisher growth (%)": "(Current revenue per fisher - Previous) / Previous * 100"
            },
            "Strengthen Market Reach & Fishery Positioning": {
                "Market share in key species (%)": "(Catch or production / Total market supply) * 100",
                "Export fish revenue growth (%)": "(Export sales - Previous) / Previous * 100",
                "Contracted aquaculture income (%)": "(Contracted sales / Total sales) * 100",
                "Geographic expansion revenue ($)": "Revenue from new regions or export markets"
            },
            "Accelerate New Product & Value-Added Revenue": {
                "Revenue from processed fish products (%)": "(Processed product sales / Total sales) * 100",
                "Revenue from aquaculture innovations (%)": "(Revenue from improved farming methods / Total revenue) * 100",
                "R&D ROI on aquaculture technology (%)": "(Revenue from new techniques / R&D cost) * 100",
                "Adoption rate of improved fish feed (%)": "Farmers/fishers adopting new feed technology"
            },
            "Diversify Fishery Revenue Streams": {
                "Revenue diversity index": "1 - (Top 3 species revenue / Total revenue)",
                "Revenue from ornamental/secondary species ($)": "Income from non-main species",
                "Revenue from processed & value-added products (%)": "(Processed product sales / Total revenue) * 100",
                "Revenue from ecosystem services or eco-tourism ($)": "Revenue from conservation-linked activities"
            }
        },

        "Fishery Profitability Optimization": {
            "Maximize Net Fishery Income": {
                "Net profit margin (%)": "(Net income / Total revenue) * 100",
                "Profit growth rate (%)": "(Current profit - Previous) / Previous * 100",
                "Return per ton of fish ($/t)": "Profit per ton produced or caught",
                "Earnings quality index": "Stability and sustainability of earnings per season"
            },
            "Enhance Fishery Gross Margin Performance": {
                "Gross margin (%)": "(Revenue - Direct costs) / Revenue * 100",
                "Species-specific margin improvement (%)": "Increase in least profitable species",
                "Direct input cost efficiency (%)": "Reduction in feed, labor, and fuel costs",
                "Pricing strategy effectiveness": "Impact of price adjustments on gross margin"
            },
            "Improve Operating Profitability": {
                "Operating profit margin (%)": "(Operating income / Revenue) * 100",
                "Operating leverage ratio": "Revenue growth vs. operating cost growth",
                "Profitability by fishery segment": "Profit contribution by aquaculture, capture fishery, and processed products",
                "Break-even production reduction": "Reduced production needed to break even"
            },
            "Optimize Fishery Contribution Margins": {
                "Average contribution margin (%)": "(Revenue - Variable costs) / Revenue * 100",
                "Fisher group profitability index": "Profit contribution by fisher groups",
                "Species mix margin optimization (%)": "Weighted margin across species",
                "Variable cost control efficiency (%)": "Reduction in feed, fuel, and labor costs"
            }
        },

        "Forestry Revenue Growth & Diversification": {
            "Enhance Forestry Revenue Performance": {
                "Total forestry revenue growth (%)": "(Current revenue - Previous) / Previous * 100",
                "Revenue per hectare ($/ha)": "Total revenue / Managed forest area",
                "Revenue from timber sales growth (%)": "Growth in timber revenue over periods",
                "Revenue per forest enterprise growth (%)": "(Current revenue per enterprise - Previous) / Previous * 100"
            },
            "Strengthen Market Reach & Forest Product Positioning": {
                "Market share in timber/non-timber products (%)": "(Production / Total market supply) * 100",
                "Export forestry revenue growth (%)": "(Export sales - Previous) / Previous * 100",
                "Contract-based forest product income (%)": "(Contracted sales / Total sales) * 100",
                "Geographic expansion revenue ($)": "Revenue from new markets or regions"
            },
            "Accelerate New Product & Value-Added Revenue": {
                "Revenue from processed timber products (%)": "(Processed product sales / Total sales) * 100",
                "Revenue from ecosystem services ($)": "Payments for carbon credits, water, or biodiversity services",
                "R&D ROI on forest improvement (%)": "(Revenue from improved practices / R&D cost) * 100",
                "Adoption rate of sustainable forestry practices (%)": "Share of enterprises adopting certified methods"
            },
            "Diversify Forestry Revenue Streams": {
                "Revenue diversity index": "1 - (Top 3 product revenue / Total revenue)",
                "Revenue from non-timber forest products ($)": "Income from fruits, resins, medicinal plants, etc.",
                "Revenue from carbon credits & ecosystem services ($)": "Revenue from environmental services",
                "Revenue from eco-tourism & recreation ($)": "Income from forest-related tourism"
            }
        },

        "Forestry Profitability Optimization": {
            "Maximize Net Forestry Income": {
                "Net profit margin (%)": "(Net income / Total revenue) * 100",
                "Profit growth rate (%)": "(Current profit - Previous) / Previous * 100",
                "Return per hectare ($/ha)": "Profit per forest area managed",
                "Earnings quality index": "Stability and sustainability of earnings over years"
            },
            "Enhance Gross Margin Performance": {
                "Gross margin (%)": "(Revenue - Direct costs) / Revenue * 100",
                "Product-specific margin improvement (%)": "Increase in low-margin timber or NTFP products",
                "Direct input cost efficiency (%)": "Reduction in planting, harvesting, and labor costs",
                "Pricing strategy effectiveness": "Impact of price adjustments on gross margin"
            },
            "Improve Operating Profitability": {
                "Operating profit margin (%)": "(Operating income / Revenue) * 100",
                "Operating leverage ratio": "Revenue growth vs. operating cost growth",
                "Profitability by product segment": "Profit contribution by timber, NTFPs, and ecosystem services",
                "Break-even yield reduction": "Reduced production needed to break even"
            },
            "Optimize Contribution Margins": {
                "Average contribution margin (%)": "(Revenue - Variable costs) / Revenue * 100",
                "Enterprise profitability index": "Profit contribution by forestry enterprises",
                "Product mix margin optimization (%)": "Weighted margin across timber and NTFP products",
                "Variable cost control efficiency (%)": "Reduction in direct harvesting and processing costs"
            }
        },

        # ==================== FARM OPERATIONAL EFFICIENCY ====================
        "Farm Operational Efficiency": {
            "Optimize Land Utilization": {
                "Land productivity index": "Total farm output divided by total land area",
                "Crop rotation efficiency": "Yield improvement from rotation divided by standard yield times 100",
                "Multiple cropping index": "Total cropped area divided by total cultivable area times 100",
                "Fallow land reduction": "Previous fallow area minus current fallow area divided by previous fallow area times 100"
            },
            "Improve Labor Productivity": {
                "Revenue per farm worker": "Total farm revenue divided by number of farm workers",
                "Crop output per labor hour": "Total crop output divided by total labor hours",
                "Livestock output per labor hour": "Total livestock output divided by total labor hours",
                "Seasonal labor efficiency": "Peak season output divided by regular season output times 100"
            },
            "Enhance Machinery Efficiency": {
                "Machinery cost per hectare": "Total machinery costs divided by total operated hectares",
                "Equipment utilization rate": "Actual machine hours divided by available machine hours times 100",
                "Fuel efficiency per operation": "Fuel cost per hectare for each farming operation",
                "Maintenance cost optimization": "Planned maintenance divided by total maintenance times 100"
            }
        },

        "Agricultural Economic Development": {

            "Increase agriculture contribution to GDP": {
                "Agriculture GDP share (%)": "(Value of agricultural output / National GDP) * 100",
                "Growth rate of agricultural GDP (%)": "(Current agri GDP - Previous agri GDP) / Previous agri GDP * 100",
                "Value-added per hectare ($)": "Total value minus input costs per hectare",
                "Agricultural sector productivity index": "Output per unit of land, labor, or capital"
            },

            "Boost rural household income": {
                "Average rural household income ($)": "Mean annual income of farm households",
                "Income growth rate (%)": "(Current - Previous income) / Previous income * 100",
                "Poverty reduction rate (%)": "(Households above poverty line / Total rural households) * 100",
                "Livelihood diversification index": "Number of income sources per household"
            },

            "Promote agricultural exports": {
                "Agricultural export value ($)": "Total value of exported agricultural products",
                "Export growth rate (%)": "(Current exports - Previous exports) / Previous exports * 100",
                "Share of agricultural exports (%)": "(Agriculture exports / Total exports) * 100",
                "Export market diversification index": "Number of export markets accessed"
            },

            "Enhance domestic market penetration": {
                "Marketed production ratio (%)": "(Quantity sold / Total production) * 100",
                "Local market share (%)": "(Products sold domestically / Total production) * 100",
                "Price realization (%)": "(Actual selling price / Benchmark price) * 100",
                "Supply chain efficiency index": "Time and cost to move products from farm to market"
            },

            "Increase rural employment in agriculture": {
                "Total agricultural employment (#)": "Number of people employed in agriculture",
                "Youth employment rate (%)": "(Youth employed / Total youth) * 100",
                "Female employment rate (%)": "(Women employed / Total female workforce) * 100",
                "Seasonal vs permanent employment ratio (%)": "(Seasonal jobs / Permanent jobs) * 100"
            },

            "Enhance farm labor productivity": {
                "Output per worker ($/worker)": "Agricultural output / Number of workers",
                "Mechanization index (%)": "Share of land using mechanized equipment",
                "Extension service coverage (%)": "(Farmers with advisory services / Total farmers) * 100",
                "Training completion rate (%)": "(Farmers/workers trained / Enrolled) * 100"
            },

            "Promote value addition in agriculture": {
                "Share of processed products (%)": "(Revenue from processed products / Total agri revenue) * 100",
                "Agro-processing employment (#)": "Jobs created in agri-processing",
                "Value addition per unit ($)": "Revenue from processed goods minus raw costs",
                "Industrial linkages index": "Number of linkages between farms and processors"
            },

            "Improve agricultural investment": {
                "Agricultural investment growth rate (%)": "(Current investment - Previous investment) / Previous * 100",
                "Return on agricultural investment (%)": "(Net return / Investment) * 100",
                "Private sector participation (%)": "(Private investment / Total agri investment) * 100",
                "Public-private partnership projects (#)": "Number of PPP projects in agriculture"
            },

            "Strengthen rural financial inclusion": {
                "Access to credit (%)": "(Farmers with credit / Total farmers) * 100",
                "Microfinance coverage (%)": "(Farmers with microloans / Total farmers) * 100",
                "Loan repayment rate (%)": "(Loans repaid / Total loans) * 100",
                "Insurance coverage (%)": "(Value insured / Total farm value) * 100"
            },

            "Improve resilience to climate shocks": {
                "Climate-adapted crop area (%)": "(Hectares with climate-resilient crops / Total hectares) * 100",
                "Disaster resilience index": "Ability of farms to recover from shocks",
                "Early warning system coverage (%)": "(Farms with alerts / Total farms) * 100",
                "Crop/livestock insurance coverage (%)": "(Insured value / Total value) * 100"
            },

            "Increase productivity per hectare": {
                "Yield per hectare (tons/ha)": "Total output / Hectares planted",
                "Input efficiency index": "Output / Input costs ratio",
                "Water productivity": "Output per unit of water used",
                "Fertilizer use efficiency (%)": "Crop yield per unit of fertilizer"
            },

            "Strengthen agricultural research and innovation": {
                "R&D investment share (%)": "(Agri-R&D spending / Total agri investment) * 100",
                "Number of improved varieties released (#)": "New crops/seed varieties developed",
                "Technology adoption rate (%)": "(Farms using new tech / Total farms) * 100",
                "Innovation impact index": "Yield/productivity improvement from innovations"
            },

            "Promote agroforestry and conservation": {
                "Agroforestry coverage (%)": "(Hectares under agroforestry / Total farm area) * 100",
                "Forest product contribution ($)": "Revenue from agroforestry products",
                "Soil health index": "Soil organic carbon or fertility indicator",
                "Biodiversity conservation index": "Number of species preserved or restored"
            },

            "Enhance irrigation and water management": {
                "Irrigated area (%)": "(Hectares under irrigation / Total cultivated area) * 100",
                "Water use efficiency": "Crop output per unit water",
                "Irrigation infrastructure coverage (%)": "(Farms with irrigation access / Total farms) * 100",
                "Reduction in water stress (%)": "(Previous water loss - Current water loss) / Previous * 100"
            },

            "Promote crop and livestock diversification": {
                "Crop diversity index": "Number of crop types per farm",
                "Livestock diversity index": "Number of livestock species per farm",
                "Revenue diversification index": "Share of income from multiple crops/livestock",
                "Adoption rate of mixed farming (%)": "(Farms practicing mixed farming / Total farms) * 100"
            },

            "Strengthen agri-markets and trade networks": {
                "Number of markets accessed (#)": "Domestic and international markets reached",
                "Market linkages index": "Farms connected to buyers/processors",
                "Market infrastructure coverage (%)": "(Farms with storage/transport access / Total farms) * 100",
                "Market price stability index": "Variation in farm-gate prices"
            },

            "Promote sustainable agriculture finance": {
                "Share of climate-smart investments (%)": "(Investments in sustainable practices / Total investments) * 100",
                "Return on sustainable investment (%)": "(Net return from sustainable projects / Investment) * 100",
                "Green finance access (%)": "(Farmers accessing green funds / Total farmers) * 100",
                "Eco-certification coverage (%)": "(Certified sustainable farms / Total farms) * 100"
            },

            "Strengthen rural entrepreneurship": {
                "Agri-startups created (#)": "Number of new agricultural businesses",
                "Employment in rural SMEs (#)": "Jobs created in rural agri-enterprises",
                "Revenue growth of rural SMEs (%)": "(Current revenue - Previous) / Previous * 100",
                "Entrepreneurship training coverage (%)": "(Individuals trained / Total targeted) * 100"
            },

            "Promote agri-tourism and value-added services": {
                "Agri-tourism revenue ($)": "Income from farm-based tourism activities",
                "Number of farms offering services (#)": "Farms with agro-experience, processing or retail services",
                "Service sector employment (#)": "Jobs in agri-tourism and value-added activities",
                "Customer satisfaction index": "Survey-based satisfaction of visitors/customers"
            },

            "Improve policy and institutional efficiency": {
                "Timely policy implementation rate (%)": "(Policies implemented on schedule / Total policies) * 100",
                "Budget utilization efficiency (%)": "(Funds spent / Funds allocated) * 100",
                "Farmer satisfaction with services (%)": "Survey of farmers' perception of ministry support",
                "Inter-agency coordination index": "Effectiveness of collaboration across agricultural agencies"
            },
        },
    },

    "Customer Perspective": {
        "Food Security & Nutrition": {
            "Enhance Household Food Security": {
                "Household food security status": "(Households meeting food security criteria / Total households) * 100",
                "Food self-sufficiency ratio": "(Food produced for own consumption / Total food needs) * 100",
                "Dietary diversity improvement": "Increase in number of food groups consumed",
                "Food storage capacity": "Months of food storage capacity per household"
            },
            "Improve Food Quality & Safety": {
                "Food safety compliance": "(Products meeting safety standards / Total products) * 100",
                "Quality grade achievement": "(Produce meeting quality standards / Total production) * 100",
                "Nutritional value enhancement": "Increase in nutrient content of food products",
                "Food contamination prevention": "Reduction in food contamination incidents"
            },
            "Increase Food Affordability": {
                "Food price stability index": "Standard deviation of food prices over time",
                "Affordable diet coverage": "(Population able to afford nutritious diet / Total population) * 100",
                "Food expenditure share reduction": "((Previous food expenditure share - Current) / Previous) * 100",
                "Local food availability index": "Availability of locally produced food in markets"
            },
            "Strengthen Food Distribution Systems": {
                "Food distribution efficiency": "(Food reaching consumers / Total production) * 100",
                "Market access for consumers": "(Consumers with market access / Total population) * 100",
                "Food waste reduction": "((Previous food waste - Current waste) / Previous waste) * 100",
                "Emergency food reserve adequacy": "(Available reserves / Required reserves) * 100"
            },
            "Enhance Nutritional Outcomes": {
                "Micronutrient availability": "Access to vitamin and mineral rich foods",
                "Food fortification reach": "Population coverage of fortified products",
                "Special dietary need accommodation": "Availability of specialized food products",
                "Nutrition education impact": "Improvement in nutritional knowledge and practices"
            }
        },

        "Farmer Welfare & Livelihoods": {
            "Improve Farmer Incomes": {
                "Average farm household income growth": "((Current income - Previous income) / Previous income) * 100",
                "Income diversification index": "Number of income sources per farming household",
                "Debt-to-income ratio improvement": "((Previous ratio - Current ratio) / Previous ratio) * 100",
                "Profit margin per enterprise": "Net income per farming enterprise"
            },
            "Enhance Social Protection": {
                "Social safety net coverage": "(Farmers covered by safety nets / Total farmers) * 100",
                "Health insurance access": "(Farmers with health insurance / Total farmers) * 100",
                "Disaster relief effectiveness": "Timeliness and adequacy of disaster support",
                "Old-age security provision": "(Elderly farmers with security / Total elderly farmers) * 100"
            },
            "Promote Rural Livelihoods": {
                "Rural employment generation": "Number of jobs created in rural areas",
                "Local economic multiplier": "Local economic impact per unit investment",
                "Rural enterprise development": "Number of new rural enterprises established",
                "Income inequality reduction": "Reduction in Gini coefficient for rural income"
            },
            "Strengthen Smallholder Resilience": {
                "Smallholder income diversification rate": "(Farmers with multiple income sources / Total farmers) * 100",
                "Risk mitigation strategy adoption": "(Farmers using risk strategies / Total farmers) * 100",
                "Emergency savings adequacy": "(Households with adequate savings / Total households) * 100",
                "Climate adaptation practice implementation": "(Area under adaptation practices / Total area) * 100"
            },
            "Improve Rural Infrastructure Access": {
                "Rural road connectivity": "Percentage of farms with all-weather road access",
                "Electricity access reliability": "Hours of reliable electricity supply per day",
                "Communication network coverage": "Mobile and internet connectivity quality",
                "Market infrastructure proximity": "Distance to nearest market facilities"
            }
        },

        "Market Access & Value Chain Development": {
            "Expand Market Opportunities": {
                "Smallholder market participation": "(Smallholders in formal markets / Total smallholders) * 100",
                "Number of market options": "Count of accessible market channels",
                "Market information access": "(Smallholders with market info / Total smallholders) * 100",
                "Collective marketing participation": "(Smallholders in collective marketing / Total smallholders) * 100"
            },
            "Enhance Value Addition": {
                "Processing level improvement": "Increase in value addition through processing",
                "Packaging and branding development": "Quality of packaging and branding",
                "Product differentiation success": "Effectiveness of product differentiation strategies",
                "Quality standardization achievement": "(Products meeting standards / Total products) * 100"
            },
            "Improve Market Infrastructure": {
                "Collection center accessibility": "(Smallholders near collection points / Total smallholders) * 100",
                "Storage facility availability": "Adequacy of storage infrastructure",
                "Transport access improvement": "Reduction in transport constraints",
                "Market facility utilization": "Usage rate of market facilities"
            },
            "Develop Digital Market Solutions": {
                "Online sales participation": "(Farmers selling online / Total farmers) * 100",
                "Digital payment utilization": "(Transactions using digital payments / Total transactions) * 100",
                "E-platform engagement": "Frequency and depth of platform usage",
                "Digital marketing effectiveness": "Revenue from digital marketing efforts"
            },
            "Enhance Export Competitiveness": {
                "Export certification compliance": "Percentage of products meeting export standards",
                "International market access": "Number of countries with market access",
                "Export logistics efficiency": "Time and cost of export procedures",
                "Global value chain integration": "Position in international supply chains"
            }
        },

        "Quality & Standards Compliance": {
            "Implement Quality Assurance Systems": {
                "Quality management system adoption": "(Farms with quality systems / Total farms) * 100",
                "Quality control compliance": "(Quality standards met / Total quality checks) * 100",
                "Traceability system implementation": "(Traceable products / Total products) * 100",
                "Quality documentation completeness": "(Complete quality records / Total records) * 100"
            },
            "Enhance Certification Systems": {
                "Certification scheme participation": "(Farmers in certification schemes / Total farmers) * 100",
                "Certification maintenance rate": "(Maintained certifications / Total certifications) * 100",
                "Premium certification achievement": "(Products with premium certification / Total products) * 100",
                "International standard compliance": "(Products meeting international standards / Total products) * 100"
            },
            "Improve Quality Infrastructure": {
                "Testing facility access": "(Farmers with testing access / Total farmers) * 100",
                "Laboratory service quality": "Quality score of testing services",
                "Standardization participation": "Involvement in standards development",
                "Quality infrastructure investment": "Level of investment in quality infrastructure"
            },
            "Strengthen Consumer Confidence": {
                "Product recall rate reduction": "((Previous recalls - Current recalls) / Previous recalls) * 100",
                "Consumer satisfaction score": "Average consumer satisfaction rating",
                "Brand reputation index": "Composite score of brand perception",
                "Product quality consistency": "Standard deviation of quality measurements"
            },
            "Enhance Food Safety Systems": {
                "HACCP implementation rate": "Percentage of operations with HACCP systems",
                "Food safety audit performance": "Scores from regulatory and customer audits",
                "Contamination prevention effectiveness": "Reduction in food safety incidents",
                "Recall management efficiency": "Speed and effectiveness of product recalls"
            }
        },

        "Customer Relationship Management": {
            "Increase Customer Satisfaction & Loyalty": {
                "Net Promoter Score (NPS)": "Percentage of promoters minus percentage of detractors",
                "Customer Satisfaction (CSAT) score": "Average satisfaction rating from customer surveys",
                "Customer Effort Score": "Ease of doing business with the farm",
                "Customer retention rate": "(Retained customers / Total customers) * 100"
            },
            "Improve Customer Service Quality": {
                "On-Time In-Full (OTIF) delivery rate": "(Orders delivered complete and on time / Total orders) * 100",
                "Customer query resolution time": "Average time to resolve customer inquiries",
                "Order accuracy rate": "(Accurate orders / Total orders) * 100",
                "Customer service cost per order": "Total service costs / Number of orders processed"
            },
            "Enhance Brand Image & Reputation": {
                "Brand awareness score": "Percentage of target market familiar with the brand",
                "Brand perception index": "Composite score of brand attributes perception",
                "Media sentiment analysis": "Positive vs negative media mentions ratio",
                "Brand advocacy mentions": "Number of unsolicited positive brand references"
            },
            "Optimize Pricing Perception": {
                "Price sensitivity meter": "Customer sensitivity to price changes",
                "Perceived value for money": "Customer rating of value proposition",
                "Competitive price positioning": "Price comparison with competitor offerings",
                "Promotion effectiveness": "Impact of promotional activities on sales"
            },
            "Develop Customer Insights": {
                "Customer feedback utilization": "Percentage of feedback implemented in improvements",
                "Market segmentation effectiveness": "Accuracy of customer segmentation",
                "Customer needs anticipation": "Ability to predict and meet emerging needs",
                "Loyalty program participation": "Engagement rate in customer loyalty programs"
            }
        },

        "Stakeholder & Community Relations": {
            "Strengthen Community Engagement": {
                "Community investment ratio": "(Community investment / Total profit) * 100",
                "Community partnership projects": "Number of active community development projects",
                "Local employment ratio": "(Local employees / Total employees) * 100",
                "Community perception score": "Results from community satisfaction surveys"
            },
            "Manage External Partnerships": {
                "Partner collaboration effectiveness": "Score from partnership performance assessments",
                "Joint project success rate": "(Successful joint projects / Total joint projects) * 100",
                "Revenue from partnerships": "Total revenue generated through collaborative efforts",
                "Strategic partner retention": "(Retained partners / Total partners) * 100"
            },
            "Enhance Citizen & Stakeholder Trust": {
                "Stakeholder trust index": "Composite measure of stakeholder confidence",
                "Transparency rating": "Score from transparency and disclosure assessments",
                "Stakeholder grievance resolution rate": "(Resolved grievances / Total grievances) * 100",
                "Multi-stakeholder platform participation": "Level of engagement in collaborative forums"
            },
            "Develop Community Partnerships": {
                "Local supplier development": "Percentage of procurement from local suppliers",
                "Community capacity building": "Number of community training programs conducted",
                "Shared value creation": "Economic and social benefits to local communities",
                "Stakeholder engagement depth": "Quality and frequency of stakeholder interactions"
            }
        }
    },

    "Internal Process Perspective": {
        "Agricultural Production Excellence: Crops": {
            "Maximize Crop Yields": {
                "Yield per hectare": "Total crop production / Total cultivated area",
                "Yield gap reduction": "((Potential yield - Actual yield) / Potential yield) * 100",
                "Yield stability index": "Consistency of yields across seasons and plots",
                "Target yield achievement rate": "(Fields achieving target yields / Total fields) * 100"
            },
            "Optimize Crop Management": {
                "Timeliness of operations": "(Operations completed on schedule / Total operations) * 100",
                "Crop rotation compliance": "(Area under proper rotation / Total area) * 100",
                "Planting density optimization": "(Area with optimal density / Total area) * 100",
                "Improved variety adoption": "(Area under improved varieties / Total area) * 100"
            },
            "Enhance Crop Health": {
                "Pest and disease incidence": "(Affected area / Total area) * 100",
                "Weed infestation level": "Weed density and coverage assessment",
                "Crop stress index": "Remote sensing-based stress indicators",
                "Pesticide application efficiency": "(Effective applications / Total applications) * 100"
            },
            "Improve Seed & Planting Material Quality": {
                "Germination rate": "(Germinated seeds / Total seeds planted) * 100",
                "Seed purity percentage": "(Pure seed / Total seed lot) * 100",
                "Certified seed adoption": "(Area under certified seed / Total area) * 100",
                "Seedling survival rate": "(Survived seedlings / Total planted seedlings) * 100"
            },
            "Optimize Harvesting Operations": {
                "Harvesting efficiency": "Area harvested per day / Target area",
                "Harvest quality preservation": "Percentage of quality maintained during harvest",
                "Harvest timing optimization": "Days to optimal harvest window",
                "Harvest labor productivity": "Output per harvest labor hour"
            }
        },

        "Agricultural Production Excellence: Livestock": {
            "Improve Livestock Productivity": {
                "Milk yield per cow": "Total milk production / Number of milking animals",
                "Feed conversion ratio": "Feed consumed / Live weight gain",
                "Reproductive performance": "(Successful conceptions / Breeding attempts) * 100",
                "Average daily gain": "Total weight gain / Number of days"
            },
            "Enhance Animal Health & Welfare": {
                "Animal mortality rate": "(Deaths / Total animals) * 100",
                "Disease incidence rate": "(Disease cases / Total animals) * 100",
                "Veterinary cost per animal": "Total vet costs / Number of animals",
                "Animal welfare assessment": "Score from welfare compliance audits"
            },
            "Optimize Breeding & Genetics": {
                "Conception rate": "(Successful conceptions / Breeding attempts) * 100",
                "Genetic merit index": "Average breeding value of stock",
                "Progeny performance": "Performance metrics of offspring",
                "Artificial insemination usage": "(AI breeding / Total breeding) * 100"
            },
            "Improve Feed & Forage Management": {
                "Feed cost per unit production": "Total feed cost / Production output",
                "Nutritional balance score": "Assessment of ration nutritional adequacy",
                "Home-grown forage yield": "Forage production per hectare",
                "Feed storage loss prevention": "Reduction in feed spoilage and waste"
            },
            "Enhance Livestock Housing & Environment": {
                "Housing facility adequacy": "Score from facility condition assessments",
                "Environmental control effectiveness": "Maintenance of optimal temperature and humidity",
                "Waste management efficiency": "Manure handling and utilization rate",
                "Biosecurity implementation": "Compliance with biosecurity protocols"
            }
        },

        "Resource Use Efficiency: Soil & Land": {
            "Improve Soil Health": {
                "Soil organic carbon level": "Percentage of organic carbon in soil",
                "Soil erosion rate": "Tons of soil lost per hectare per year",
                "Minimal soil disturbance area": "(Area under conservation tillage / Total area) * 100",
                "Soil biological activity": "Microbial and earthworm activity indicators"
            },
            "Enhance Nutrient Management": {
                "Nutrient use efficiency": "Crop uptake / Nutrient applied",
                "Soil nutrient balance": "Difference between inputs and outputs",
                "Organic fertilizer application": "(Nutrients from organic sources / Total nutrients) * 100",
                "Soil test-based recommendations": "(Area under tested recommendations / Total area) * 100"
            },
            "Optimize Land Utilization": {
                "Cropping intensity index": "(Total cropped area / Net sown area) * 100",
                "Cultivated land percentage": "(Cultivated area / Total farm area) * 100",
                "Land use change tracking": "Monitoring of land use changes over time",
                "Multi-story cropping adoption": "(Area under multi-story systems / Total area) * 100"
            },
            "Implement Soil Conservation": {
                "Conservation tillage adoption": "(Area under conservation tillage / Total area) * 100",
                "Cover crop adoption rate": "(Area with cover crops / Total area) * 100",
                "Contour farming implementation": "(Area under contour farming / Total area) * 100",
                "Windbreak establishment": "Length and effectiveness of windbreaks"
            },
            "Enhance Land Development": {
                "Land reclamation success": "Percentage of degraded land restored",
                "Terracing effectiveness": "Reduction in soil erosion from terraces",
                "Land leveling precision": "Accuracy of land leveling operations",
                "Drainage system efficiency": "Effectiveness of water drainage systems"
            }
        },

        "Resource Use Efficiency: Water & Irrigation": {
            "Optimize Water Management": {
                "Water use efficiency": "Crop yield / Total water used",
                "Irrigation system efficiency": "(Water used by crops / Water applied) * 100",
                "Water productivity": "Revenue generated / Water volume used",
                "Efficient irrigation coverage": "(Area under efficient irrigation / Total irrigated area) * 100"
            },
            "Enhance Irrigation Scheduling": {
                "Scientific scheduling adoption": "(Area under scientific scheduling / Total area) * 100",
                "Deficit irrigation implementation": "Appropriate use of deficit irrigation strategies",
                "Soil moisture sensor usage": "(Area monitored by sensors / Total area) * 100",
                "ET-based scheduling": "(Area under ET-based scheduling / Total area) * 100"
            },
            "Improve Irrigation Infrastructure Performance": {
                "System uniformity coefficient": "Measure of water application uniformity",
                "Conveyance efficiency": "(Water delivered / Water diverted) * 100",
                "Pumping plant efficiency": "Energy efficiency of pumping systems",
                "Maintenance backlog": "Outstanding maintenance tasks and costs"
            },
            "Develop Water Sources & Storage": {
                "Rainwater harvesting capacity": "Volume of rainwater captured and stored",
                "Groundwater recharge rate": "Rate of aquifer replenishment",
                "Storage efficiency": "(Water available / Water stored) * 100",
                "Water source diversification": "Number of different water sources utilized"
            },
            "Enhance Water Quality Management": {
                "Irrigation water quality": "Chemical and biological quality parameters",
                "Drainage water treatment": "Percentage of drainage water treated",
                "Salinity control effectiveness": "Maintenance of soil salinity levels",
                "Water recycling rate": "Percentage of water reused in operations"
            }
        },

        "Supply Chain & Logistics Management": {
            "Enhance Post-Harvest Management": {
                "Post-harvest loss reduction": "((Previous losses - Current losses) / Previous losses) * 100",
                "Storage facility efficiency": "(Properly stored produce / Total produce) * 100",
                "Cold chain compliance": "(Maintained cold chain / Required cold chain) * 100",
                "Processing efficiency improvement": "((Previous losses - Current losses) / Previous losses) * 100"
            },
            "Strengthen Logistics & Transportation": {
                "On-time delivery performance": "(On-time deliveries / Total deliveries) * 100",
                "Transportation cost efficiency": "Cost per tonne-kilometer of transport",
                "Vehicle utilization rate": "(Actual usage hours / Available hours) * 100",
                "Fuel efficiency": "Distance traveled per unit of fuel"
            },
            "Optimize Inventory Management": {
                "Inventory turnover ratio": "Cost of goods sold / Average inventory",
                "Days of inventory on hand": "Average inventory / Daily cost of goods sold",
                "Stock-out frequency": "Number of stock-out incidents per period",
                "Obsolete inventory reduction": "Reduction in worthless inventory value"
            },
            "Improve Procurement Operations": {
                "Input quality consistency": "Standard deviation of input quality measures",
                "Supplier delivery reliability": "(On-time deliveries / Total deliveries) * 100",
                "Procurement cycle time": "Time from requisition to delivery",
                "Supplier relationship depth": "Number of strategic supplier partnerships"
            },
            "Enhance Warehouse Management": {
                "Warehouse space utilization": "(Used space / Total available space) * 100",
                "Order picking accuracy": "(Accurate picks / Total picks) * 100",
                "Storage condition maintenance": "Compliance with storage requirements",
                "Inventory accuracy rate": "(Accurate records / Total inventory items) * 100"
            }
        },

        "Technology & Innovation Adoption": {
            "Implement Precision Agriculture": {
                "Precision farming adoption": "(Area under precision practices / Total area) * 100",
                "GPS guidance utilization": "(Operations using GPS / Total operations) * 100",
                "Variable rate technology adoption": "(Inputs applied with VRT / Total inputs) * 100",
                "Yield monitoring implementation": "(Area under yield monitoring / Total area) * 100"
            },
            "Adopt Digital Farming Solutions": {
                "Farm management software usage": "(Farmers using software / Total farmers) * 100",
                "IoT sensor deployment": "Number of sensors per unit area",
                "Remote sensing utilization": "(Area monitored remotely / Total area) * 100",
                "Automation level": "Percentage of operations automated"
            },
            "Enhance Mechanization": {
                "Mechanization level": "Percentage of operations mechanized",
                "Equipment efficiency improvement": "((Previous efficiency - Current efficiency) / Previous efficiency) * 100",
                "Custom hiring service utilization": "(Operations using custom hire / Total operations) * 100",
                "Equipment availability": "(Available time / Total time) * 100"
            },
            "Foster Production Innovation": {
                "New technology adoption rate": "(Adopted technologies / Available technologies) * 100",
                "Innovation implementation success": "(Successful innovations / Total innovations tried) * 100",
                "Research collaboration effectiveness": "Number of successful research partnerships",
                "Farmer-led innovation adoption": "Number of farmer-developed practices adopted"
            },
            "Develop Agricultural Engineering Solutions": {
                "Equipment customization rate": "Percentage of equipment adapted to local conditions",
                "Process engineering improvements": "Number of optimized production processes",
                "Infrastructure design efficiency": "Performance of designed agricultural structures",
                "Technical problem-solving rate": "Success rate in addressing technical challenges"
            }
        },

        "Quality Management & Control": {
            "Implement Quality Control Processes": {
                "In-process quality pass rate": "(Passed checks / Total checks) * 100",
                "Final inspection acceptance": "(Accepted products / Total inspected) * 100",
                "Non-conformance report rate": "Number of quality issues reported",
                "Cost of quality": "Total prevention, appraisal, and failure costs"
            },
            "Standardize Operating Procedures": {
                "SOP coverage rate": "(Processes with SOPs / Total processes) * 100",
                "SOP training completion": "(Trained staff / Total staff) * 100",
                "SOP adherence rate": "(Compliant operations / Total operations) * 100",
                "SOP update frequency": "Regularity of procedure reviews and updates"
            },
            "Enhance Process Control": {
                "Process capability index": "Statistical measure of process performance",
                "Control chart implementation": "Percentage of processes with statistical control",
                "Variation reduction": "Decrease in process variability over time",
                "Standard work development": "Extent of standardized work practices"
            }
        },

        "Compliance & Risk Management": {
            "Ensure Regulatory Compliance": {
                "Regulatory non-compliances": "Number of compliance violations",
                "Permit renewal timeliness": "(Renewed on time / Total permits) * 100",
                "Environmental regulation adherence": "Score from environmental compliance audits",
                "Labor law compliance": "Results from labor regulation inspections"
            },
            "Strengthen Biosecurity": {
                "Biosecurity protocol adherence": "Score from biosecurity audits",
                "Pest/disease outbreaks": "Number of disease incidents",
                "Quarantine effectiveness": "Prevention of disease spread",
                "Visitor logging compliance": "(Logged visits / Total visits) * 100"
            },
            "Manage Climate & Environmental Risk": {
                "Water stress index": "Assessment of water scarcity risk",
                "Soil degradation rate": "Rate of soil quality decline",
                "Biodiversity impact assessment": "Score from biodiversity evaluations",
                "Climate vulnerability index": "Composite climate risk assessment"
            },
            "Implement Safety Management": {
                "Safety incident rate": "Number of safety incidents per work hours",
                "Safety training completion": "(Trained staff / Total staff) * 100",
                "Emergency response readiness": "Score from emergency preparedness drills",
                "Safety inspection compliance": "(Addressed findings / Total findings) * 100"
            },
            "Enhance Operational Continuity": {
                "Business continuity planning": "Completeness of continuity plans",
                "Disaster recovery capability": "Time to restore operations after disruption",
                "Redundant system implementation": "Percentage of critical systems with backups",
                "Supply chain resilience": "Ability to maintain supply during disruptions"
            }
        },

        "Infrastructure Development & Maintenance": {
            "Optimize Farm Infrastructure": {
                "Infrastructure condition index": "Overall assessment of facility conditions",
                "Maintenance schedule compliance": "(Completed maintenance / Scheduled maintenance) * 100",
                "Infrastructure utilization rate": "(Actual usage / Design capacity) * 100",
                "Facility upgrade cycle": "Appropriateness of upgrade timing"
            },
            "Develop Production Facilities": {
                "Processing facility efficiency": "Output per facility operating hour",
                "Storage capacity optimization": "Utilization rate of storage facilities",
                "Packaging line performance": "Units packaged per hour",
                "Facility layout effectiveness": "Efficiency of material flow in facilities"
            },
            "Enhance Utility Systems": {
                "Energy system reliability": "Uptime percentage of energy systems",
                "Water system performance": "Efficiency of water distribution systems",
                "Waste management effectiveness": "Percentage of waste properly managed",
                "Utility cost control": "Cost per unit of utility services"
            }
        }
    },

    "Learning & Growth Perspective": {
        "Sustainable Resource Management": {
            "Promote Biodiversity": {
                "Crop and livestock variety count": "Number of different varieties maintained",
                "Habitat conservation area": "(Conserved habitat / Total area) * 100",
                "Pollinator habitat score": "Quality and quantity of pollinator habitats",
                "Integrated Pest Management adoption": "(Area under IPM / Total area) * 100"
            },
            "Implement Circular Economy Practices": {
                "Waste valorization rate": "(Waste converted to value / Total waste) * 100",
                "Resource recycling efficiency": "(Recycled resources / Total resources) * 100",
                "By-product utilization": "(Utilized by-products / Total by-products) * 100",
                "Closed-loop systems": "Number of circular production systems"
            },
            "Conserve Water Resources": {
                "Water footprint": "Total water consumed per unit output",
                "Groundwater level trend": "Change in groundwater levels over time",
                "Rainwater harvesting capacity": "Volume of rainwater captured annually",
                "Drought-tolerant crop adoption": "(Area under drought-tolerant crops / Total area) * 100"
            },
            "Enhance Ecosystem Services": {
                "Carbon sequestration rate": "Tonnes of carbon stored per hectare",
                "Pollination service value": "Economic value of natural pollination",
                "Soil formation rate": "Rate of natural soil development",
                "Water purification effectiveness": "Quality of water leaving the farm"
            }
        },

        "Climate Resilience & Adaptation": {
            "Build Climate Resilience": {
                "Climate-resilient practice adoption": "(Area under resilient practices / Total area) * 100",
                "Climate-smart agriculture implementation": "Extent of climate-smart practices adoption",
                "Crop diversification index": "Number of different crops grown",
                "Climate-adaptive infrastructure": "Investment in climate-resilient structures"
            },
            "Implement Mitigation Strategies": {
                "GHG emission reduction": "((Previous emissions - Current emissions) / Previous emissions) * 100",
                "Carbon sequestration rate": "Amount of carbon stored in soils and biomass",
                "Renewable energy adoption": "(Renewable energy used / Total energy) * 100",
                "Methane reduction achievements": "Reduction in livestock methane emissions"
            },
            "Enhance Weather Risk Management": {
                "Weather information service usage": "(Users of weather services / Total farmers) * 100",
                "Weather insurance coverage": "(Insured production / Total production) * 100",
                "Early warning system effectiveness": "Timeliness and accuracy of warnings",
                "Disaster preparedness drills": "Frequency and quality of preparedness exercises"
            },
            "Develop Adaptive Capacity": {
                "Climate adaptation planning": "Completeness of adaptation strategies",
                "Resilient variety adoption": "(Area under climate-resilient varieties / Total area) * 100",
                "Water storage capacity development": "Increase in water storage infrastructure",
                "Alternative livelihood development": "Number of climate-resilient income sources"
            }
        },

        "Farmer & Employee Capacity Development": {
            "Enhance Technical Skills": {
                "Training hours per person": "Total training hours / Number of participants",
                "Skills assessment pass rate": "(Passed assessments / Total assessments) * 100",
                "Practice adoption rate": "(Adopted practices / Taught practices) * 100",
                "Technical certifications": "Number of staff with professional certifications"
            },
            "Improve Digital Literacy": {
                "Digital skills proficiency": "(Proficient users / Total users) * 100",
                "Digital tool usage": "(Users of digital tools / Total staff) * 100",
                "Mobile technology utilization": "(Mobile app users / Total farmers) * 100",
                "E-learning completion": "(Completed courses / Enrolled courses) * 100"
            },
            "Strengthen Business Management": {
                "Business plan development": "(Farms with business plans / Total farms) * 100",
                "Financial record keeping": "(Farms maintaining records / Total farms) * 100",
                "Marketing skills assessment": "Score from marketing capability evaluations",
                "Strategic planning capability": "Assessment of planning and forecasting ability"
            },
            "Develop Irrigation Management Expertise": {
                "Certified irrigation managers": "Number of staff with irrigation certifications",
                "Modern irrigation training": "Hours of training on advanced irrigation methods",
                "Water policy knowledge": "Understanding of water rights and regulations",
                "Irrigation software proficiency": "Ability to use irrigation management software"
            },
            "Enhance Operational Skills": {
                "Equipment operation certification": "Percentage of operators with formal certification",
                "Maintenance skill level": "Score from maintenance competency assessments",
                "Process operation efficiency": "Performance in standard operating procedures",
                "Safety procedure compliance": "Adherence to safety protocols and procedures"
            }
        },

        "Research & Innovation Ecosystem": {
            "Strengthen Research Linkages": {
                "Research collaborations": "Number of active research partnerships",
                "Joint project funding": "Amount of co-funded research projects",
                "Co-authored publications": "Number of joint research publications",
                "Field trial success rate": "(Successful trials / Total trials) * 100"
            },
            "Enhance Technology Development": {
                "New technologies developed": "Number of innovations created annually",
                "R&D project completion": "(Completed projects / Total projects) * 100",
                "Intellectual property generation": "Number of patents and IP assets",
                "Technology readiness progression": "Advancement in technology maturity levels"
            },
            "Improve Knowledge Dissemination": {
                "Field demonstrations conducted": "Number of demonstration events held",
                "Farmer knowledge sharing": "Number of peer-to-peer learning events",
                "Extension material reach": "Number of farmers receiving extension materials",
                "Digital platform engagement": "Usage metrics of online knowledge platforms"
            },
            "Promote Research Utilization": {
                "Research adoption rate": "(Adopted research findings / Total applicable findings) * 100",
                "Technology transfer effectiveness": "(Successfully transferred technologies / Total technologies) * 100",
                "Knowledge dissemination reach": "Extent of knowledge sharing to end-users",
                "Research commercialization": "(Commercialized research / Total research) * 100"
            },
            "Foster Innovation Culture": {
                "Innovation proposal rate": "Number of improvement suggestions per employee",
                "Experiment implementation": "Number of controlled experiments conducted",
                "Cross-functional innovation": "Percentage of innovations from team collaborations",
                "Innovation recognition": "Number of innovations formally recognized"
            }
        },

        "Organizational Culture & Structure": {
            "Align Corporate Culture with Strategy": {
                "Strategic goal understanding": "Employee comprehension of organizational objectives",
                "Culture alignment score": "Results from cultural alignment assessments",
                "Values recognition rate": "Frequency of values-based recognition",
                "Cross-department collaboration": "Level of inter-departmental cooperation"
            },
            "Improve Communication & Teamwork": {
                "Internal communication effectiveness": "Score from communication satisfaction surveys",
                "Team performance metrics": "Performance indicators for team achievements",
                "Meeting effectiveness rating": "Evaluation of meeting productivity and outcomes",
                "Inter-departmental project success": "(Successful cross-team projects / Total projects) * 100"
            },
            "Enhance Organizational Agility": {
                "Change implementation speed": "Time to implement organizational changes",
                "Adaptation to market changes": "Speed of response to market shifts",
                "Employee empowerment index": "Level of decision-making authority at all levels",
                "Resource reallocation flexibility": "Ability to quickly redirect resources"
            },
            "Develop Organizational Learning": {
                "Lessons learned implementation": "Percentage of lessons incorporated into practices",
                "Best practice sharing": "Extent of sharing successful approaches",
                "Continuous improvement culture": "Employee engagement in improvement activities",
                "Knowledge retention rate": "Preservation of organizational knowledge"
            }
        },

        "Social Inclusion & Community Development": {
            "Promote Gender Equality": {
                "Gender leadership ratio": "(Women in leadership / Total leadership) * 100",
                "Gender pay equity": "Ratio of female to male compensation",
                "Women's resource access": "(Women with equal access / Total women) * 100",
                "Gender-sensitive training": "(Women in targeted programs / Total women) * 100"
            },
            "Enhance Youth Engagement": {
                "Youth workforce percentage": "(Workers under 35 / Total workforce) * 100",
                "Youth apprenticeship participation": "Number of youth in training programs",
                "Succession plan readiness": "Preparation level for leadership transitions",
                "Youth-led initiative support": "Number of youth-driven projects supported"
            },
            "Support Marginalized Groups": {
                "Marginalized group inclusion": "Participation rates of underrepresented communities",
                "Vulnerable group service access": "(Served vulnerable groups / Total vulnerable) * 100",
                "Cultural sensitivity implementation": "Adaptation of programs for cultural relevance",
                "Disability inclusion": "(Included persons with disabilities / Total with disabilities) * 100"
            },
            "Develop Citizen & Stakeholder Capabilities": {
                "Stakeholder training programs": "Number of capacity building initiatives",
                "Stakeholder development satisfaction": "Satisfaction scores from development programs",
                "Local institutional capacity": "Improvement in community organization capabilities",
                "Citizen planning participation": "Level of community involvement in agricultural planning"
            },
            "Enhance Community Development": {
                "Local economic development": "Growth in local business opportunities",
                "Community infrastructure improvement": "Investment in community facilities",
                "Social cohesion index": "Measure of community unity and cooperation",
                "Quality of life improvement": "Overall enhancement of community living standards"
            }
        },

        "Technology & Digital Capability": {
            "Enhance IT Infrastructure": {
                "System uptime reliability": "Percentage of time systems are operational",
                "Data security compliance": "Score from security audits and assessments",
                "IT help desk performance": "Average resolution time for technical issues",
                "IT infrastructure investment": "Level of spending on technology upgrades"
            },
            "Develop Data Analytics Capability": {
                "Predictive analytics usage": "Extent of analytics in decision-making processes",
                "Data quality score": "Assessment of data accuracy and completeness",
                "Analytics training completion": "Number of staff trained in data analysis",
                "Analytics project ROI": "Return on investment from data analytics initiatives"
            },
            "Improve Digital Connectivity": {
                "Internet speed and reliability": "Network performance metrics",
                "Mobile network coverage": "Percentage of area with reliable mobile service",
                "Digital communication adoption": "Usage rate of digital communication tools",
                "Rural broadband access": "Availability of high-speed internet in rural areas"
            },
            "Advance Agricultural Technology": {
                "AgTech research investment": "Funding allocated to agricultural technology R&D",
                "Technology integration success": "Effectiveness of integrating new technologies",
                "Digital platform development": "Creation and enhancement of digital tools",
                "Technology scalability": "Ability to scale technological solutions"
            }
        },

        "Employee Engagement & Performance": {
            "Increase Employee Engagement": {
                "Engagement survey score": "Results from employee engagement assessments",
                "Voluntary turnover rate": "(Voluntary departures / Total employees) * 100",
                "Employee Net Promoter Score": "Willingness to recommend as a workplace",
                "Absenteeism rate": "(Days absent / Total work days) * 100"
            },
            "Improve Performance Management": {
                "Goal achievement rate": "(Achieved goals / Total goals) * 100",
                "Performance review completion": "(Completed reviews / Total due reviews) * 100",
                "Feedback frequency": "Regularity of performance feedback sessions",
                "Development plan implementation": "(Implemented plans / Total plans) * 100"
            },
            "Strengthen Staff Retention": {
                "Overall retention rate": "(Retained employees / Total employees) * 100",
                "Top performer retention": "(Retained top performers / Total top performers) * 100",
                "Exit satisfaction score": "Feedback from departing employees",
                "Career development opportunities": "Number and quality of advancement paths"
            },
            "Build Knowledge Management Systems": {
                "Knowledge documentation": "(Documented critical knowledge / Total critical knowledge) * 100",
                "Knowledge repository usage": "Frequency and depth of system utilization",
                "Lessons learned application": "Implementation rate of captured insights",
                "Community of practice engagement": "Level of participation in knowledge sharing groups"
            },
            "Enhance Talent Development": {
                "Succession planning coverage": "Percentage of key roles with identified successors",
                "Leadership pipeline strength": "Quality and quantity of future leaders",
                "Skill gap reduction": "Progress in addressing competency deficiencies",
                "Professional development investment": "Resources allocated to employee growth"
            }
        },

        "Leadership & Governance": {
            "Develop Leadership Capacity": {
                "Leadership competency assessment": "Score from leadership capability evaluations",
                "Internal promotion rate": "(Internal promotions / Total promotions) * 100",
                "Leadership training hours": "Training investment in leadership development",
                "360-degree feedback scores": "Comprehensive leadership performance ratings"
            },
            "Strengthen Governance Systems": {
                "Board effectiveness score": "Assessment of governance body performance",
                "Policy compliance rate": "Adherence to organizational policies and procedures",
                "Ethical conduct assessment": "Evaluation of ethical standards compliance",
                "Stakeholder representation": "Inclusion of diverse stakeholder perspectives"
            },
            "Enhance Strategic Leadership": {
                "Strategic vision clarity": "Understanding and alignment with organizational vision",
                "Change leadership effectiveness": "Success in leading organizational transformations",
                "Innovation leadership": "Support and promotion of innovative initiatives",
                "Crisis management capability": "Effectiveness in handling emergency situations"
            }
        }
    }
}
