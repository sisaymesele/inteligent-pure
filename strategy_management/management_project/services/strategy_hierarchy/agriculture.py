from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE

AGRICULTURE_PERSPECTIVE = {

    "Financial Perspective": {
        **GENERIC_FINANCE_PERSPECTIVE['Financial Perspective'],
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

        **GENERIC_CUSTOMER_PERSPECTIVE['Customer Perspective'],
        # -------------------- Food Security & Nutrition --------------------
        "Food Security & Nutrition": {
            "Enhance Household Food Security": {
                "Household food security status (%)": "(Households meeting food security criteria / Total households) * 100",
                "Food self-sufficiency ratio (%)": "(Food produced for own consumption / Total food needs) * 100",
                "Dietary diversity improvement": "Increase in number of food groups consumed",
                "Food storage capacity (months)": "Average months of food storage per household"
            },
            "Improve Food Quality & Safety": {
                "Food safety compliance (%)": "(Products meeting safety standards / Total products) * 100",
                "Quality grade achievement (%)": "(Produce meeting quality standards / Total production) * 100",
                "Nutritional value enhancement": "Increase in nutrient content of food products",
                "Food contamination prevention (%)": "Reduction in food contamination incidents"
            },
            "Increase Food Affordability": {
                "Food price stability index": "Standard deviation of food prices over time",
                "Affordable diet coverage (%)": "(Population able to afford nutritious diet / Total population) * 100",
                "Food expenditure share reduction (%)": "((Previous share - Current) / Previous) * 100",
                "Local food availability index": "Availability of locally produced food in markets"
            },
            "Strengthen Food Distribution Systems": {
                "Distribution efficiency (%)": "(Food reaching consumers / Total production) * 100",
                "Market access for consumers (%)": "(Consumers with market access / Total population) * 100",
                "Food loss reduction (%)": "((Previous food loss - Current) / Previous) * 100",
                "Emergency reserve adequacy (%)": "(Available reserves / Required reserves) * 100"
            },
            "Promote Post-Harvest Management": {
                "Storage facility utilization (%)": "(Used storage capacity / Total capacity) * 100",
                "Post-harvest loss reduction (%)": "((Previous loss - Current) / Previous) * 100",
                "Cold chain adoption (%)": "(Farmers using cold storage / Total farmers) * 100",
                "Processing infrastructure coverage (%)": "(Farmers with access to processing facilities / Total farmers) * 100"
            },
            "Enhance Nutrition Outcomes": {
                "Micronutrient availability (%)": "Access to vitamin- and mineral-rich foods",
                "Food fortification reach (%)": "Population covered by fortified products",
                "Special dietary accommodation (%)": "Availability of specialized food products",
                "Nutrition education impact": "Improvement in nutritional knowledge and practices"
            },
            "Promote Agricultural Diversity": {
                "Crop diversification index": "Number of crop varieties grown per household",
                "Livestock diversity index": "Number of livestock types per household",
                "Agroforestry adoption (%)": "(Households practicing agroforestry / Total households) * 100",
                "Seed variety adoption (%)": "(Households using improved varieties / Total households) * 100"
            },
            "Ensure Food Security Resilience": {
                "Climate-resilient practice adoption (%)": "(Farmers using resilient practices / Total farmers) * 100",
                "Early warning system coverage (%)": "(Population covered by food security alerts / Total population) * 100",
                "Disaster preparedness (%)": "(Households prepared for shocks / Total households) * 100",
                "Emergency response effectiveness (%)": "Timeliness of response to food crises"
            }
        },

        # -------------------- Farmer Welfare & Livelihoods --------------------
        "Farmer Welfare & Livelihoods": {
            "Improve Farmer Incomes": {
                "Average household income growth (%)": "((Current income - Previous income) / Previous income) * 100",
                "Income diversification index": "Number of income sources per household",
                "Profit margin per enterprise (%)": "Net income per farming enterprise",
                "Debt-to-income ratio improvement (%)": "((Previous ratio - Current ratio) / Previous ratio) * 100"
            },
            "Enhance Social Protection": {
                "Social safety net coverage (%)": "(Farmers covered / Total farmers) * 100",
                "Health insurance access (%)": "(Farmers with health insurance / Total farmers) * 100",
                "Disaster relief timeliness (%)": "Speed of relief provision during disasters",
                "Old-age security provision (%)": "(Elderly farmers with security / Total elderly farmers) * 100"
            },
            "Promote Rural Livelihoods": {
                "Rural employment generation": "Number of rural jobs created",
                "Local economic multiplier": "Local economic impact per unit investment",
                "Rural enterprise development": "Number of new rural enterprises",
                "Income inequality reduction (%)": "Reduction in Gini coefficient for rural income"
            },
            "Strengthen Smallholder Resilience": {
                "Income diversification (%)": "(Farmers with multiple income sources / Total farmers) * 100",
                "Risk management adoption (%)": "(Farmers adopting risk strategies / Total farmers) * 100",
                "Emergency savings adequacy (%)": "(Households with adequate savings / Total households) * 100",
                "Climate adaptation adoption (%)": "(Area under adaptation practices / Total area) * 100"
            },
            "Access to Financial Services": {
                "Credit access (%)": "(Farmers with loans / Total farmers) * 100",
                "Savings account access (%)": "(Farmers with savings accounts / Total farmers) * 100",
                "Microinsurance coverage (%)": "(Farmers with crop/livestock insurance / Total farmers) * 100",
                "Financial literacy improvement": "Average financial knowledge score increase"
            },
            "Support Youth & Women Farmers": {
                "Youth participation (%)": "(Youth farmers / Total farmers) * 100",
                "Women participation (%)": "(Women farmers / Total farmers) * 100",
                "Youth-focused training (%)": "(Youth attending training / Total youth) * 100",
                "Women-focused training (%)": "(Women attending training / Total women) * 100"
            },
            "Promote Health & Safety": {
                "Access to protective equipment (%)": "(Farmers using PPE / Total farmers) * 100",
                "Occupational health training (%)": "(Farmers trained in safety / Total farmers) * 100",
                "Reduction in accidents (%)": "((Previous accidents - Current) / Previous) * 100",
                "Safe pesticide use compliance (%)": "(Farmers following safe use / Total farmers) * 100"
            },
            "Encourage Farmer Organizations": {
                "Farmer association membership (%)": "(Members / Total farmers) * 100",
                "Collective decision-making adoption (%)": "(Members participating in decisions / Total members) * 100",
                "Capacity building participation (%)": "(Members attending capacity programs / Total members) * 100",
                "Resource sharing initiatives": "Number of joint initiatives implemented"
            }
        },

        # -------------------- Market Access & Value Chain Development --------------------
        # -------------------- Cooperative Development --------------------
        "Cooperative Development": {
            "Increase Cooperative Membership": {
                "Farmer membership growth (%)": "(New members / Total farmers) * 100",
                "Member retention rate (%)": "(Retained members / Total members) * 100",
                "Youth participation (%)": "(Youth members / Total members) * 100",
                "Women participation (%)": "(Women members / Total members) * 100"
            },
            "Strengthen Cooperative Governance": {
                "Board election transparency (%)": "(Transparent elections / Total cooperatives) * 100",
                "Compliance with regulations (%)": "(Cooperatives in compliance / Total cooperatives) * 100",
                "Member satisfaction score": "Average member satisfaction rating",
                "Conflict resolution efficiency (%)": "(Conflicts resolved / Total conflicts) * 100"
            },
            "Enhance Financial Management": {
                "Financial audit coverage (%)": "(Cooperatives audited / Total cooperatives) * 100",
                "Loan repayment rate (%)": "(Loans repaid on time / Total loans) * 100",
                "Capital accumulation growth (%)": "Increase in cooperative funds",
                "Operational cost efficiency (%)": "(Budget used efficiently / Total budget) * 100"
            },
            "Promote Market Linkages": {
                "Volume sold via cooperative (%)": "(Sales through cooperative / Total production) * 100",
                "Revenue generated ($)": "Total revenue through cooperative marketing",
                "New market access (%)": "(Markets accessed via cooperative / Total potential markets) * 100",
                "Buyer satisfaction score": "Average rating of buyers linked to cooperative"
            },
            "Capacity Building & Training": {
                "Member training coverage (%)": "(Members trained / Total members) * 100",
                "Training effectiveness score": "Average score from post-training evaluation",
                "Leadership skill improvement (%)": "(Members demonstrating improved leadership / Total trained members) * 100",
                "Adoption of training practices (%)": "(Trained members applying knowledge / Total trained members) * 100"
            },
            "Foster Innovation & Entrepreneurship": {
                "New business initiatives (%)": "(Innovative projects / Total projects) * 100",
                "Agri-product development (%)": "(New products developed / Total products) * 100",
                "Revenue from innovation ($)": "Income generated from innovative activities",
                "Innovation adoption (%)": "(Members adopting innovations / Total members) * 100"
            },
            "Promote Cooperative Networking": {
                "Inter-cooperative collaboration (%)": "(Cooperatives collaborating / Total cooperatives) * 100",
                "Knowledge exchange events": "Number of joint events conducted",
                "Shared service initiatives (%)": "(Cooperatives sharing services / Total cooperatives) * 100",
                "Joint marketing success (%)": "(Successful joint sales initiatives / Total initiatives) * 100"
            },
            "Support Policy Advocacy": {
                "Participation in policy forums (%)": "(Cooperatives participating / Total cooperatives) * 100",
                "Policy influence effectiveness (%)": "Score of policy impact",
                "Advocacy campaigns conducted": "Number of advocacy initiatives",
                "Member awareness improvement (%)": "(Members aware of policies / Total members) * 100"
            }
        },

        # -------------------- Rural & Community Development --------------------
        "Rural & Community Development": {
            "Improve Rural Infrastructure Access": {
                "Road connectivity (%)": "(Households with road access / Total households) * 100",
                "Electricity access (%)": "(Households with reliable electricity / Total households) * 100",
                "Water access (%)": "(Households with improved water access / Total households) * 100",
                "Communication access (%)": "(Households with phone/internet / Total households) * 100"
            },
            "Promote Health & Sanitation": {
                "Health facility access (%)": "(Households with health access / Total households) * 100",
                "Sanitation coverage (%)": "(Households with improved sanitation / Total households) * 100",
                "Immunization rate (%)": "(Children vaccinated / Total children) * 100",
                "Hygiene education coverage (%)": "(Households receiving hygiene training / Total households) * 100"
            },
            "Support Education & Skills Development": {
                "School enrollment rate (%)": "(Children enrolled / Total school-age children) * 100",
                "Adult literacy improvement (%)": "Increase in adult literacy",
                "Vocational training coverage (%)": "(Individuals trained / Total target population) * 100",
                "Training adoption rate (%)": "(Trained individuals applying skills / Total trained) * 100"
            },
            "Enhance Social Cohesion & Governance": {
                "Community participation rate (%)": "(Active members / Total eligible members) * 100",
                "Local decision-making inclusivity (%)": "(Women & youth participation / Total participants) * 100",
                "Conflict resolution effectiveness (%)": "(Conflicts resolved / Total conflicts) * 100",
                "Community satisfaction score": "Average rating from community surveys"
            },
            "Promote Sustainable Livelihoods": {
                "Income diversification (%)": "(Households with multiple income sources / Total households) * 100",
                "Microenterprise development (%)": "(Households with microenterprises / Total households) * 100",
                "Access to finance (%)": "(Households accessing credit / Total households) * 100",
                "Employment generation": "Number of new rural jobs created"
            },
            "Support Women & Youth Empowerment": {
                "Women participation (%)": "(Women in programs / Total women) * 100",
                "Youth participation (%)": "(Youth in programs / Total youth) * 100",
                "Leadership skill improvement (%)": "Average leadership score improvement",
                "Program adoption rate (%)": "(Participants applying learned skills / Total participants) * 100"
            },
            "Encourage Environmental Stewardship": {
                "Community forest coverage (%)": "(Area under community forestry / Total land area) * 100",
                "Soil conservation adoption (%)": "(Households practicing soil conservation / Total households) * 100",
                "Water conservation initiatives (#)": "Number of community water projects implemented",
                "Renewable energy adoption (%)": "(Households using renewable energy / Total households) * 100"
            },
            "Promote Cultural & Social Heritage": {
                "Traditional knowledge integration (%)": "(Practices integrated / Total recommended practices) * 100",
                "Cultural event participation (%)": "(Population attending events / Total population) * 100",
                "Heritage site preservation (%)": "(Sites preserved / Total sites) * 100",
                "Community awareness improvement (%)": "(Population aware of cultural programs / Total population) * 100"
            }
        },

        "Subsidies & Input Support": {
            "Improve access to affordable inputs for smallholders": {
                "Average input cost reduction (%)": "((Previous input price - Current price) / Previous price) * 100",
                "Number of farmers receiving subsidized inputs": "Count of registered subsidy beneficiaries",
                "Distribution coverage (%)": "(Beneficiaries / Total smallholder farmers) * 100",
                "Input satisfaction score": "Survey-based satisfaction level with input quality"
            },
            "Enhance timely distribution of inputs": {
                "Input delivery timeliness (%)": "(On-time deliveries / Total deliveries) * 100",
                "Average distribution delay (days)": "Mean delay per delivery",
                "Farmer complaint rate (%)": "(Complaints / Total deliveries) * 100",
                "Input delivery coverage (%)": "(Regions served / Total regions) * 100"
            },
            "Promote local input production and distribution": {
                "Share of locally produced inputs (%)": "(Local inputs / Total inputs) * 100",
                "Number of certified local suppliers": "Registered and verified input producers",
                "Input quality compliance rate (%)": "(Compliant inputs / Total tested) * 100",
                "Input price volatility index": "Standard deviation of monthly input prices"
            },
            "Enhance targeting and efficiency of subsidies": {
                "Subsidy targeting accuracy (%)": "(Eligible beneficiaries / Total beneficiaries) * 100",
                "Leakage rate (%)": "(Non-eligible recipients / Total recipients) * 100",
                "Average subsidy utilization rate (%)": "(Inputs used / Inputs distributed) * 100",
                "Subsidy satisfaction level": "Survey rating from farmers"
            },
            "Increase mechanization adoption": {
                "Mechanized farming adoption rate (%)": "(Mechanized farms / Total farms) * 100",
                "Tractor hours per hectare": "Average mechanization usage per farm",
                "Machinery maintenance rate (%)": "(Maintained machinery / Total machinery) * 100",
                "Equipment ownership ratio": "(Equipment owners / Total farmers) * 100"
            },
            "Support input quality assurance systems": {
                "Certified input products (%)": "(Certified / Total inputs) * 100",
                "Inspection coverage (%)": "(Inspections done / Total input outlets) * 100",
                "Rejected input batches (%)": "(Rejected / Tested batches) * 100",
                "Farmer trust score": "Survey-based input trust level"
            },
            "Enhance fertilizer and seed usage efficiency": {
                "Optimal fertilizer usage rate (%)": "(Optimal users / Total users) * 100",
                "Seed germination success rate (%)": "(Successful germination / Total seeds planted) * 100",
                "Fertilizer response yield gain (%)": "Average yield increase due to fertilizer",
                "Soil nutrient balance index": "Soil test-based nutrient balance"
            },
            "Promote gender-inclusive input programs": {
                "Female beneficiary ratio (%)": "(Women recipients / Total recipients) * 100",
                "Women-led input cooperatives": "Count of active cooperatives led by women",
                "Gender gap in input access (%)": "(Male access - Female access) / Male access * 100",
                "Satisfaction gap index": "Difference in satisfaction between genders"
            }
        },

        "Technical Assistance & Extension Services": {
            "Enhance reach of extension services": {
                "Farmers reached (%)": "(Farmers served / Total farmers) * 100",
                "Extension officer-to-farmer ratio": "Number of farmers per extension officer",
                "Coverage of extension regions (%)": "(Regions covered / Total regions) * 100",
                "Satisfaction with extension services (%)": "Survey rating"
            },
            "Improve technical knowledge dissemination": {
                "Training sessions conducted": "Total number of extension-led training",
                "Knowledge retention rate (%)": "Post-training test score retention",
                "Digital advisory usage (%)": "(Digital advisory users / Total farmers) * 100",
                "Follow-up visit compliance (%)": "(Follow-up visits done / Scheduled visits) * 100"
            },
            "Promote climate-smart agriculture training": {
                "Farmers trained on CSA (%)": "(CSA trainees / Total trainees) * 100",
                "Adoption rate of CSA practices (%)": "(Adopters / Trained farmers) * 100",
                "Average yield change after CSA (%)": "((New yield - Old yield) / Old yield) * 100",
                "CSA satisfaction score": "Survey rating"
            },
            "Enhance ICT-based extension delivery": {
                "Digital advisory adoption rate (%)": "(ICT users / Total farmers) * 100",
                "SMS alert effectiveness (%)": "(Acted farmers / Recipients) * 100",
                "Online advisory uptime (%)": "(System uptime / Total time) * 100",
                "Mobile penetration rate (%)": "(Farmers with mobile access / Total farmers) * 100"
            },
            "Strengthen field visit programs": {
                "Extension visits per farm per year": "Average field visit frequency",
                "Response time to farmer request (days)": "Average delay to attend farmers",
                "Satisfaction with field visits (%)": "Survey-based rating",
                "Knowledge application rate (%)": "(Farmers applying advice / Farmers visited) * 100"
            },
            "Develop specialized expertise per crop": {
                "Crop-specific expert ratio": "(Specialized officers / Total officers) * 100",
                "Coverage of key crop regions (%)": "(Regions covered / Total key regions) * 100",
                "Farmer productivity increase (%)": "((Current yield - Previous yield)/Previous)*100",
                "Technical advice satisfaction (%)": "Survey-based rating"
            },
            "Encourage private sector participation in extension": {
                "Private advisory share (%)": "(Private providers / Total providers) * 100",
                "PPP extension programs (%)": "(Public-private programs / Total) * 100",
                "Private sector satisfaction index": "Survey from private partners",
                "Coverage expansion due to PPP (%)": "(Additional reach / Total farmers) * 100"
            },
            "Monitor and evaluate extension impact": {
                "Impact assessment frequency (per year)": "Number of evaluations conducted annually",
                "Farmer income change (%)": "((Current income - Previous) / Previous) * 100",
                "Knowledge adoption index": "Composite score of adoption metrics",
                "Yield variation due to advisory (%)": "((With advisory - Without) / Without) * 100"
            }
        },

        "Training & Capacity Building": {
            "Expand farmer training participation": {
                "Training attendance rate (%)": "(Participants / Total targeted) * 100",
                "Number of training sessions conducted": "Count of sessions completed",
                "Average hours per participant": "Total training hours / Total participants",
                "Satisfaction with training quality (%)": "Survey-based score"
            },
            "Enhance youth and women participation in training": {
                "Youth participation rate (%)": "(Youth trainees / Total trainees) * 100",
                "Female participation rate (%)": "(Women trainees / Total trainees) * 100",
                "Gender equality score": "Composite gender inclusion index",
                "Youth employment outcome rate (%)": "(Youth employed / Youth trained) * 100"
            },
            "Improve training relevance and impact": {
                "Post-training application rate (%)": "(Farmers applying skills / Total trained) * 100",
                "Yield improvement after training (%)": "((Post-training yield - Pre-training) / Pre-training) * 100",
                "Satisfaction with training content (%)": "Survey rating",
                "Retention rate after 6 months (%)": "(Still applying / Total trained) * 100"
            },
            "Develop trainer quality and expertise": {
                "Certified trainers (%)": "(Certified trainers / Total trainers) * 100",
                "Trainer-to-farmer ratio": "Trainers / Total participants",
                "Trainer evaluation score": "Average rating per trainer",
                "Refresher training frequency (per year)": "Sessions per trainer annually"
            },
            "Promote peer-to-peer learning networks": {
                "Active farmer field schools": "Number of ongoing peer learning groups",
                "Peer mentoring participation (%)": "(Participants / Total farmers) * 100",
                "Knowledge sharing sessions held": "Count per quarter",
                "Peer learning satisfaction (%)": "Survey-based feedback"
            },
            "Increase access to e-learning and digital capacity tools": {
                "Online training access rate (%)": "(Online trainees / Total trainees) * 100",
                "Completion rate (%)": "(Completed courses / Enrolled users) * 100",
                "Platform uptime (%)": "(Uptime hours / Total hours) * 100",
                "Knowledge retention test score": "Average post-test score"
            },
            "Enhance technical specialization in priority crops": {
                "Specialized training coverage (%)": "(Farmers trained in key crops / Total trained) * 100",
                "Crop productivity improvement (%)": "((New yield - Old yield)/Old yield) * 100",
                "Training cost efficiency (%)": "(Output gain / Training cost) * 100",
                "Specialized trainer certification rate (%)": "(Certified / Total trainers) * 100"
            },
            "Integrate business and entrepreneurship skills": {
                "Farmers trained in business planning (%)": "(Business trainees / Total trainees) * 100",
                "Enterprise startup rate (%)": "(New enterprises / Trained farmers) * 100",
                "Access to finance after training (%)": "(Financed farmers / Trained farmers) * 100",
                "Profitability improvement (%)": "((Post-training profit - Pre-training)/Pre-training)*100"
            }
        },

        "Access to Credit & Financial Services": {
            "Increase access to agricultural finance": {
                "Farmers with credit access (%)": "(Credit beneficiaries / Total farmers) * 100",
                "Total agricultural loan volume ($)": "Sum of disbursed agricultural loans",
                "Average loan size ($)": "Total loans / Number of borrowers",
                "Loan approval rate (%)": "(Approved / Applied) * 100"
            },
            "Promote inclusive rural financial systems": {
                "Rural financial institutions coverage (%)": "(Active institutions / Rural districts) * 100",
                "Female borrower ratio (%)": "(Women borrowers / Total borrowers) * 100",
                "Youth borrower ratio (%)": "(Youth borrowers / Total borrowers) * 100",
                "Average distance to nearest finance point (km)": "Mean distance from rural households"
            },
            "Improve agricultural credit repayment performance": {
                "Loan repayment rate (%)": "(Repaid loans / Total due loans) * 100",
                "Default rate (%)": "(Defaults / Total borrowers) * 100",
                "Average repayment period (months)": "Mean duration to settle loans",
                "Credit risk index": "Composite index of portfolio performance"
            },
            "Promote crop insurance adoption": {
                "Insured farmer coverage (%)": "(Farmers insured / Total farmers) * 100",
                "Claims settlement rate (%)": "(Claims paid / Claims filed) * 100",
                "Average premium per hectare ($)": "Total premiums / Hectares insured",
                "Insurance satisfaction index": "Survey-based rating"
            },
            "Expand mobile and digital financial access": {
                "Mobile wallet adoption rate (%)": "(Farmers using digital finance / Total farmers) * 100",
                "Transaction volume via mobile ($)": "Sum of mobile-based transactions",
                "Digital transaction success rate (%)": "(Successful / Total attempts) * 100",
                "Digital literacy score": "Survey-based index"
            },
            "Establish agricultural guarantee funds": {
                "Guarantee fund utilization (%)": "(Funds used / Total funds) * 100",
                "Number of loans guaranteed": "Loans backed by fund guarantees",
                "Recovery rate on guarantees (%)": "(Recovered / Guaranteed) * 100",
                "Leverage ratio": "Private capital mobilized / Guarantee fund value"
            },
            "Develop microfinance schemes for smallholders": {
                "Active microfinance beneficiaries": "Count of ongoing microfinance clients",
                "Microloan average repayment rate (%)": "(Repaid / Total disbursed) * 100",
                "Women-led group loan ratio (%)": "(Women group loans / Total group loans) * 100",
                "Loan usage productivity gain (%)": "((Post-loan yield - Pre-loan yield)/Pre-loan)*100"
            },
            "Integrate saving and investment programs": {
                "Farmer saving account penetration (%)": "(Farmers with savings / Total farmers) * 100",
                "Average saving growth rate (%)": "((Current - Previous)/Previous)*100",
                "Group saving participation (%)": "(Group savers / Total farmers) * 100",
                "Investment in farm improvements ($)": "Sum of reinvested capital"
            }
        },

        "Market Information & Linkages": {
            "Enhance access to real-time market information": {
                "Farmers accessing market data (%)": "(Users / Total farmers) * 100",
                "Market price accuracy (%)": "(Verified / Published) * 100",
                "Update frequency (per week)": "Number of updates",
                "User satisfaction index": "Survey-based score"
            },
            "Improve market infrastructure connectivity": {
                "Operational market centers": "Count of functional markets",
                "Distance to nearest market (km)": "Average travel distance",
                "Post-harvest loss reduction (%)": "((Previous - Current)/Previous)*100",
                "Market infrastructure coverage (%)": "(Markets with facilities / Total markets) * 100"
            },
            "Strengthen value chain coordination": {
                "Active producer-buyer contracts": "Number of active value chain contracts",
                "Producer organization participation (%)": "(Linked producers / Total producers) * 100",
                "Average farmgate-to-market margin (%)": "(Market price - Farmgate price)/Farmgate price * 100",
                "Supply chain efficiency index": "Composite logistics index"
            },
            "Promote farmer aggregation and collective marketing": {
                "Aggregated volume share (%)": "(Cooperative sales / Total sales) * 100",
                "Number of active cooperatives": "Registered and trading cooperatives",
                "Average price improvement (%)": "((Collective - Individual)/Individual)*100",
                "Cooperative member satisfaction (%)": "Survey-based score"
            },
            "Support export market diversification": {
                "Export product variety": "Number of exported products",
                "Export market destinations": "Count of export countries",
                "Export revenue growth (%)": "((Current - Previous)/Previous)*100",
                "Export quality compliance rate (%)": "(Compliant / Total shipments) * 100"
            },
            "Develop e-commerce and digital platforms for farmers": {
                "Online transaction volume ($)": "Total digital sales",
                "Registered digital traders": "Number of active e-commerce users",
                "Average delivery time (days)": "Mean time between order and delivery",
                "Digital market satisfaction (%)": "User survey rating"
            },
            "Facilitate contract farming schemes": {
                "Farmers under contract (%)": "(Contracted farmers / Total farmers) * 100",
                "Contract compliance rate (%)": "(Contracts honored / Total contracts) * 100",
                "Dispute occurrence rate (%)": "(Disputes / Contracts) * 100",
                "Average price stability (%)": "((Contract price - Market price)/Market price)*100"
            },
            "Enhance price transparency and fairness": {
                "Price spread ratio": "(Market price - Producer price) / Producer price * 100",
                "Farmer trust index": "Survey-based perception rating",
                "Complaints resolved (%)": "(Resolved / Reported) * 100",
                "Market regulation compliance (%)": "(Compliant traders / Total traders) * 100"
            }
        },

        "Infrastructure Development (irrigation, storage, roads)": {
            "Expand irrigation coverage and efficiency": {
                "Irrigated land area (ha)": "Total hectares under irrigation",
                "Irrigation system efficiency (%)": "(Water delivered / Water required) * 100",
                "Operational irrigation schemes (%)": "(Functional / Total schemes) * 100",
                "Water productivity (kg/m³)": "Crop output per unit of water used"
            },
            "Improve rural road accessibility for farmers": {
                "Rural road length improved (km)": "Kilometers of farm-to-market roads upgraded",
                "Transport time reduction (%)": "((Old time - New time) / Old time) * 100",
                "Market access improvement index": "Composite score of accessibility",
                "Freight cost reduction (%)": "((Previous - Current)/Previous)*100"
            },
            "Enhance post-harvest storage capacity": {
                "Storage capacity built (tons)": "New or improved storage volume",
                "Post-harvest loss reduction (%)": "((Before - After)/Before) * 100",
                "Utilization rate (%)": "(Used capacity / Total capacity) * 100",
                "Storage facility operational (%)": "(Operational / Total facilities) * 100"
            },
            "Increase access to cold chain logistics": {
                "Cold storage capacity (tons)": "Total cold storage available",
                "Perishable loss rate (%)": "(Lost produce / Total perishable) * 100",
                "Cold chain coverage (%)": "(Regions served / Total regions) * 100",
                "Energy efficiency of cold facilities (%)": "(Actual energy used / Standard use) * 100"
            },
            "Develop feeder roads and rural transport hubs": {
                "New feeder roads constructed (km)": "Kilometers built",
                "Travel cost reduction (%)": "((Previous - Current)/Previous)*100",
                "Average market trip time (minutes)": "Mean travel duration per trip",
                "Vehicle access ratio (%)": "(Accessible villages / Total villages) * 100"
            },
            "Upgrade processing and aggregation centers": {
                "Processing center utilization (%)": "(Used / Total capacity) * 100",
                "Processing output volume (tons)": "Total processed products",
                "Facility uptime (%)": "(Operational hours / Total hours) * 100",
                "Farmer access rate (%)": "(Farmers using / Total farmers) * 100"
            },
            "Promote water harvesting and small-scale infrastructure": {
                "Water harvesting systems installed": "Number of water collection units",
                "Water retention efficiency (%)": "(Stored / Rainfall) * 100",
                "Maintenance compliance rate (%)": "(Maintained / Total systems) * 100",
                "Beneficiary coverage (%)": "(Farmers served / Total farmers) * 100"
            },
            "Enhance climate-resilient infrastructure": {
                "Climate-proofed infrastructure (%)": "(Resilient facilities / Total) * 100",
                "Resilience investment ratio (%)": "(Resilient investment / Total investment) * 100",
                "Climate damage incidents (#)": "Number of infrastructure damage events",
                "Recovery time (days)": "Average days to restore functionality"
            }
        },

        "Social Safety Nets (cash transfers, food aid)": {
            "Expand coverage of agricultural social protection programs": {
                "Beneficiary households (#)": "Number of households receiving support",
                "Coverage rate (%)": "(Beneficiary households / Target households) * 100",
                "Targeting accuracy (%)": "(Eligible beneficiaries / Total beneficiaries) * 100",
                "Payment timeliness (%)": "(On-time payments / Total payments) * 100"
            },
            "Enhance efficiency of cash transfer delivery": {
                "Digital payment utilization (%)": "(Payments made digitally / Total payments) * 100",
                "Transaction cost per beneficiary ($)": "Total cost / Beneficiaries",
                "Delivery delay rate (%)": "(Delayed transfers / Total transfers) * 100",
                "Beneficiary satisfaction score": "Average satisfaction rating"
            },
            "Integrate safety nets with productive programs": {
                "Beneficiaries linked to livelihoods (%)": "(Linked / Total beneficiaries) * 100",
                "Graduation rate (%)": "(Beneficiaries exiting due to self-sufficiency / Total beneficiaries) * 100",
                "Complementary training provided (#)": "Training sessions conducted",
                "Income increase among beneficiaries (%)": "((After - Before)/Before)*100"
            },
            "Strengthen food assistance programs": {
                "Households receiving food aid (#)": "Count of supported households",
                "Food aid timeliness (%)": "(Delivered on time / Total distributions) * 100",
                "Food quality compliance (%)": "(Compliant rations / Total rations) * 100",
                "Beneficiary satisfaction (%)": "Feedback on adequacy and quality"
            },
            "Target vulnerable populations effectively": {
                "Vulnerability index coverage (%)": "(Registered vulnerable / Total target) * 100",
                "Female-headed household coverage (%)": "(Supported female-headed / Total supported) * 100",
                "Child nutrition support (%)": "(Children covered / Total children) * 100",
                "Support adequacy index": "Average sufficiency of aid"
            },
            "Enhance coordination with social welfare agencies": {
                "Joint coordination meetings (#)": "Meetings held per year",
                "Overlapping aid cases (%)": "(Duplicated beneficiaries / Total beneficiaries) * 100",
                "Unified database coverage (%)": "(Integrated records / Total records) * 100",
                "Agency satisfaction rate (%)": "Coordination rating from agencies"
            },
            "Promote financial inclusion through safety nets": {
                "Beneficiaries with bank accounts (%)": "(Accounts opened / Total beneficiaries) * 100",
                "Savings account activation (%)": "(Active accounts / Total accounts) * 100",
                "Mobile wallet utilization (%)": "(Users / Total beneficiaries) * 100",
                "Microinsurance uptake (%)": "(Insured beneficiaries / Total beneficiaries) * 100"
            },
            "Monitor social protection impacts on resilience": {
                "Income stability improvement (%)": "((After - Before)/Before)*100",
                "Poverty reduction rate (%)": "((Before poverty rate - After) / Before)*100",
                "Shock recovery rate (%)": "Speed of recovery post-crisis",
                "Household food consumption score": "Improvement in dietary adequacy"
            }
        },

        "Nutrition & Food Security Programs": {
            "Enhance access to nutritious food": {
                "Households with adequate diet (%)": "(Adequate diet households / Total) * 100",
                "Availability of fortified foods (%)": "(Fortified products / Total foods) * 100",
                "Household food consumption score": "Aggregate nutrition indicator",
                "Nutrient supply adequacy (%)": "(Available nutrients / Recommended levels) * 100"
            },
            "Strengthen nutrition-sensitive agriculture": {
                "Nutrition-linked projects (%)": "(Projects with nutrition focus / Total) * 100",
                "Biofortified crop adoption (%)": "(Biofortified area / Total cultivated) * 100",
                "Diversified crop production index": "Measure of crop diversity for nutrition",
                "Household dietary diversity score": "Average food group count"
            },
            "Improve maternal and child nutrition": {
                "Stunting prevalence (%)": "(Stunted children / Total children) * 100",
                "Exclusive breastfeeding rate (%)": "(Infants exclusively breastfed / Total infants) * 100",
                "Micronutrient supplementation coverage (%)": "(Children supplemented / Total children) * 100",
                "Nutrition education participation (%)": "(Mothers trained / Total mothers) * 100"
            },
            "Enhance school feeding and nutrition education": {
                "School feeding coverage (%)": "(Beneficiary schools / Total schools) * 100",
                "Local sourcing rate (%)": "(Local food sourced / Total food) * 100",
                "Meal quality compliance (%)": "(Compliant meals / Total meals) * 100",
                "Student nutrition awareness score": "Improvement in knowledge of nutrition"
            },
            "Strengthen food fortification programs": {
                "Fortified food production (%)": "(Fortified output / Total production) * 100",
                "Industry compliance rate (%)": "(Compliant producers / Total producers) * 100",
                "Micronutrient availability increase (%)": "((After - Before)/Before)*100",
                "Consumer awareness of fortification (%)": "(Aware population / Total population) * 100"
            },
            "Promote sustainable food systems": {
                "Sustainable sourcing rate (%)": "(Sustainably sourced food / Total food) * 100",
                "Food loss reduction (%)": "((Previous - Current loss)/Previous)*100",
                "Sustainable diet adoption (%)": "(Households following sustainable diets / Total) * 100",
                "Agroecology project share (%)": "(Agroecology projects / Total) * 100"
            },
            "Integrate food security monitoring systems": {
                "Early warning updates (per year)": "Frequency of FSN bulletins",
                "Food insecurity prevalence (%)": "(Insecure households / Total) * 100",
                "Data collection coverage (%)": "(Surveyed regions / Total regions) * 100",
                "Timeliness of reporting (%)": "(Reports on time / Total expected) * 100"
            },
            "Support national food security coordination": {
                "Multi-agency coordination score": "Effectiveness of inter-ministerial coordination",
                "Resource allocation efficiency (%)": "(Funds utilized / Funds allocated) * 100",
                "Program harmonization index": "Extent of aligned donor/partner projects",
                "National FSN policy implementation (%)": "(Implemented activities / Planned) * 100"
            }
        },

    },

    "Internal Process Perspective": {
        "Research & Development Results": {
            "Increase investment in agricultural R&D": {
                "R&D expenditure ratio (%)": "(R&D spend / Total budget) * 100",
                "Projects funded (#)": "Number of research projects supported",
                "Innovation index": "Composite score for innovation output",
                "Patents or technologies developed (#)": "Count of registered innovations"
            },
            "Enhance adoption of improved technologies": {
                "Adoption rate (%)": "(Users of new tech / Targeted farmers) * 100",
                "Yield increase (%)": "((After adoption - Before)/Before)*100",
                "Training sessions on new tech (#)": "Number of awareness activities",
                "Farmer satisfaction with new tech (%)": "Survey rating"
            },
            "Strengthen public-private R&D collaboration": {
                "Joint research projects (#)": "Collaborative initiatives",
                "Private investment share (%)": "(Private funds / Total R&D) * 100",
                "Research partnership retention (%)": "(Retained / Total partners) * 100",
                "Commercialized outputs (#)": "Research converted into market products"
            },
            "Promote climate-smart agricultural innovations": {
                "CSA technologies tested (#)": "Count of tested solutions",
                "CSA adoption rate (%)": "(CSA users / Total farmers) * 100",
                "GHG reduction (%)": "((Old emissions - New) / Old) * 100",
                "Yield under climate stress (%)": "(Output / Baseline yield) * 100"
            },
            "Improve research dissemination and extension linkage": {
                "Research briefs shared (#)": "Number distributed",
                "Extension adoption rate (%)": "(Adopted recommendations / Total shared) * 100",
                "Research-extension feedback sessions (#)": "Meetings held",
                "Knowledge uptake index": "Composite measure of practical adoption"
            },
            "Enhance data and evidence-based planning": {
                "Data-driven policy coverage (%)": "(Policies using data / Total policies) * 100",
                "Research citations in strategies (#)": "Number of references",
                "Monitoring data timeliness (%)": "(On-time updates / Total required) * 100",
                "Database completeness (%)": "(Updated records / Total datasets) * 100"
            },
            "Develop localized innovation hubs": {
                "Innovation centers established (#)": "Count of operational hubs",
                "Innovations transferred (#)": "Technologies moved to production",
                "Farmer innovators supported (#)": "Farmers trained in innovation use",
                "Community innovation rate (%)": "(Innovators / Total communities) * 100"
            },
            "Foster knowledge sharing and publication": {
                "Research publications (#)": "Papers and reports released",
                "Knowledge dissemination events (#)": "Workshops and expos held",
                "Stakeholder participation (%)": "(Participants / Invited) * 100",
                "Knowledge sharing satisfaction (%)": "Feedback survey result"
            }
        },

        "Policy Frameworks & Regulation": {
            "Strengthen agricultural policy implementation": {
                "Policy adoption rate (%)": "(Adopted / Proposed) * 100",
                "Implementation timeliness (%)": "(On-time actions / Total actions) * 100",
                "Stakeholder compliance rate (%)": "(Compliant entities / Total) * 100",
                "Policy impact index": "Composite effectiveness measure"
            },
            "Enhance regulatory oversight in agri-markets": {
                "Inspections conducted (#)": "Market compliance checks",
                "Non-compliance cases resolved (%)": "(Resolved / Reported) * 100",
                "Product quality certification rate (%)": "(Certified / Total products) * 100",
                "Enforcement action timeliness (%)": "(On-time / Total actions) * 100"
            },
            "Promote fair trade and pricing regulation": {
                "Price monitoring coverage (%)": "(Markets monitored / Total markets) * 100",
                "Farmgate-to-retail margin (%)": "(Retail - Farmgate)/Farmgate * 100",
                "Price volatility index": "Standard deviation of monthly price changes",
                "Complaints resolved (%)": "(Resolved / Filed) * 100"
            },
            "Enhance policy coordination across institutions": {
                "Inter-agency meetings held (#)": "Coordination forums conducted",
                "Joint programs implemented (#)": "Collaborative initiatives",
                "Policy coherence index": "Assessment score on alignment",
                "Duplication rate (%)": "(Overlaps / Total programs) * 100"
            },
            "Promote inclusive and participatory policymaking": {
                "Stakeholder consultations (#)": "Meetings and feedback sessions",
                "Stakeholder representation diversity (%)": "(Groups represented / Total invited) * 100",
                "Public policy awareness (%)": "(Aware citizens / Total population) * 100",
                "Policy satisfaction score": "Average stakeholder feedback rating"
            },
            "Simplify licensing and regulatory procedures": {
                "Average approval time (days)": "Mean time for licensing",
                "Digitalized services (%)": "(Online processes / Total services) * 100",
                "Client satisfaction (%)": "Survey score on ease of use",
                "Processing error rate (%)": "(Errors / Total processed) * 100"
            },
            "Enhance food safety and standards enforcement": {
                "Inspected facilities (%)": "(Inspected / Total facilities) * 100",
                "Compliance rate (%)": "(Compliant / Inspected) * 100",
                "Product recall incidents (#)": "Number of unsafe product recalls",
                "Testing coverage (%)": "(Tested samples / Total samples) * 100"
            },
            "Integrate environmental and climate policies": {
                "Climate policy integration rate (%)": "(Climate-integrated / Total policies) * 100",
                "Sustainability indicator tracking (%)": "(Tracked / Total indicators) * 100",
                "Deforestation reduction rate (%)": "((Old - New)/Old)*100",
                "Green investment ratio (%)": "(Green funds / Total investment) * 100"
            }
        },

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

        "Disaster Relief & Recovery Support": {
            "Improve agricultural disaster preparedness": {
                "Preparedness plan coverage (%)": "(Covered regions / Total regions) * 100",
                "Training sessions on DRR (#)": "Number of training sessions conducted",
                "Simulation exercises (#)": "Mock drills held annually",
                "Response readiness score": "Composite emergency preparedness score"
            },
            "Enhance early warning and risk communication": {
                "Early warning system coverage (%)": "(Regions with EWS / Total regions) * 100",
                "Lead time before disaster (days)": "Average warning period",
                "Information dissemination reach (%)": "(People informed / Total population) * 100",
                "Forecast accuracy (%)": "(Accurate alerts / Total alerts) * 100"
            },
            "Provide timely disaster response assistance": {
                "Response time (hours)": "Average time between alert and aid delivery",
                "Relief coverage (%)": "(Households assisted / Affected households) * 100",
                "Emergency supply adequacy (%)": "(Supplies delivered / Needed) * 100",
                "Beneficiary satisfaction (%)": "Average satisfaction rating"
            },
            "Rehabilitate damaged agricultural infrastructure": {
                "Infrastructure restored (%)": "(Repaired / Damaged) * 100",
                "Rehabilitation completion time (days)": "Average project duration",
                "Restoration investment ($)": "Total funds allocated",
                "Rehabilitation quality score": "Assessment of restoration effectiveness"
            },
            "Support affected farmers’ recovery": {
                "Compensation disbursed ($)": "Funds provided to affected farmers",
                "Recovery program participation (%)": "(Participating farmers / Affected farmers) * 100",
                "Crop replanting rate (%)": "(Replanted area / Affected area) * 100",
                "Livestock restocking ratio (%)": "(Restocked animals / Lost animals) * 100"
            },
            "Promote climate risk insurance mechanisms": {
                "Insurance coverage rate (%)": "(Insured farmers / Total farmers) * 100",
                "Claim processing time (days)": "Average time to settle claims",
                "Payout rate (%)": "(Claims paid / Claims filed) * 100",
                "Insurance awareness score": "Farmer understanding of products"
            },
            "Integrate disaster risk reduction in planning": {
                "Risk-informed plan coverage (%)": "(Plans integrating DRR / Total plans) * 100",
                "Budget allocated to DRR (%)": "(DRR budget / Total budget) * 100",
                "Hazard mapping coverage (%)": "(Mapped areas / Total regions) * 100",
                "Policy integration index": "Extent of DRR embedded in policies"
            },
            "Monitor post-disaster recovery outcomes": {
                "Recovery index": "Composite score measuring livelihood restoration",
                "Household resilience index": "Recovery and coping capacity metric",
                "Livelihood restoration rate (%)": "(Recovered households / Total affected) * 100",
                "Time to full recovery (months)": "Average recovery period"
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
