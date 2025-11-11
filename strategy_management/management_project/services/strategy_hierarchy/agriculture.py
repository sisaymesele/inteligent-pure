

from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE
from management_project.services.strategy_hierarchy.internal_process_perspective import GENERIC_INTERNAL_PROCESS_PERSPECTIVE
from management_project.services.strategy_hierarchy.learning_and_growth_perspective import GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE


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

        **GENERIC_INTERNAL_PROCESS_PERSPECTIVE['Internal Process Perspective'],

        # -------------------- 1. Soil Management --------------------
        "Soil Management": {
            "Enhance Soil Fertility": {
                "Soil nutrient index": "Composite index of NPK levels",
                "Organic matter content (%)": "Organic matter / Total soil mass * 100",
                "Soil pH compliance (%)": "Plots within optimal pH range / Total plots * 100",
                "Soil erosion reduction (%)": "(Baseline erosion - Current) / Baseline * 100"
            },
            "Optimize Soil Usage": {
                "Crop rotation adherence (%)": "Plots rotated properly / Total plots * 100",
                "Land productivity (kg/ha)": "Total yield / Area cultivated",
                "Fallow land management (%)": "Fallow land properly managed / Total fallow land",
                "Soil moisture utilization (%)": "Irrigation used / Soil water holding capacity * 100"
            },
            "Prevent Soil Degradation": {
                "Soil compaction reduction (%)": "(Previous - Current) / Previous * 100",
                "Erosion control structures implemented (#)": "Constructed / Planned",
                "Soil salinity levels (%)": "Plots within acceptable salinity range / Total plots",
                "Soil contamination incidents (#)": "Reported / Total area"
            },
            "Promote Sustainable Soil Practices": {
                "Use of organic fertilizers (%)": "Fields with organic fertilizer / Total fields * 100",
                "Conservation tillage adoption (%)": "Fields with reduced tillage / Total fields * 100",
                "Mulching coverage (%)": "Area mulched / Total area * 100",
                "Composting rate (%)": "Compost applied / Total crop residues * 100"
            },
            "Soil Monitoring & Analytics": {
                "Soil testing coverage (%)": "Tested plots / Total plots * 100",
                "Frequency of monitoring (#)": "Monitoring events / Planned events",
                "Data-driven soil interventions (%)": "Interventions based on soil data / Total interventions",
                "Soil health improvement (%)": "(Current soil health - Baseline) / Baseline * 100"
            },
            "Enhance Soil Water Retention": {
                "Moisture retention (%)": "Retained water / Total applied * 100",
                "Drought resilience index": "Composite measure of crop survival under low rainfall",
                "Irrigation water savings (%)": "(Previous - Current water used) / Previous * 100",
                "Rainwater harvesting adoption (%)": "Plots using harvested rainwater / Total plots * 100"
            }
        },

        # -------------------- 2. Irrigation Management --------------------
        "Irrigation Management": {
            "Improve Water Use Efficiency": {
                "Irrigation efficiency (%)": "Water delivered / Water required * 100",
                "Crop water productivity (kg/m³)": "Yield / Water applied",
                "Water loss reduction (%)": "(Previous losses - Current) / Previous * 100",
                "Irrigation coverage (%)": "Irrigated area / Total arable area * 100"
            },
            "Optimize Irrigation Scheduling": {
                "Timely irrigation compliance (%)": "Irrigation events on schedule / Total events",
                "Pump/equipment utilization (%)": "Operational hours / Total hours available",
                "Reduction in water stress incidents (%)": "(Previous incidents - Current) / Previous * 100",
                "Energy use per m³ of water (%)": "Energy consumed / Water delivered"
            },
            "Promote Efficient Irrigation Technology": {
                "Drip irrigation adoption (%)": "Fields with drip / Total irrigated fields * 100",
                "Sprinkler irrigation adoption (%)": "Fields with sprinklers / Total irrigated fields * 100",
                "Irrigation automation coverage (%)": "Automated systems / Total irrigated fields * 100",
                "Reduction in manual labor (%)": "(Previous - Current labor used) / Previous * 100"
            },
            "Enhance Water Storage & Distribution": {
                "Reservoir efficiency (%)": "Water stored / Total capacity * 100",
                "Canal network efficiency (%)": "Water delivered / Water released * 100",
                "Pipeline leakage reduction (%)": "(Previous - Current leaks) / Previous * 100",
                "Pump reliability (%)": "Operational pumps / Total pumps * 100"
            },
            "Monitor Water Quality": {
                "Water contamination incidents (#)": "Reported / Total monitored",
                "Compliance with water quality standards (%)": "Tests meeting standards / Total tests",
                "Chemical usage monitoring (%)": "Monitored fields / Total fields * 100",
                "Farmer awareness of water quality (%)": "Trained farmers / Total farmers * 100"
            },
            "Promote Water-Saving Practices": {
                "Mulching adoption (%)": "Area mulched / Total irrigated area * 100",
                "Rainwater harvesting coverage (%)": "Harvesting structures / Total farms * 100",
                "Soil moisture monitoring coverage (%)": "Monitored plots / Total plots * 100",
                "Reduction in water wastage (%)": "(Previous - Current) / Previous * 100"
            }
        },

        # -------------------- 3. Crop Management --------------------
        "Crop Management": {
            "Improve Crop Productivity": {
                "Yield per hectare": "Total yield / Area cultivated",
                "Crop survival rate (%)": "Survived seedlings / Total planted * 100",
                "Fertilizer use efficiency (%)": "Crop output per unit fertilizer applied",
                "Pest/disease incidence reduction (%)": "(Previous - Current) / Previous * 100"
            },
            "Enhance Crop Quality": {
                "Marketable crop proportion (%)": "Marketable produce / Total harvest * 100",
                "Post-harvest loss reduction (%)": "(Previous - Current) / Previous * 100",
                "Grain/fruit size compliance (%)": "Samples meeting standards / Total samples",
                "Storage quality compliance (%)": "Stored produce meeting quality standards / Total stored"
            },
            "Optimize Planting & Seeding": {
                "Timely planting rate (%)": "Planted on schedule / Total planned * 100",
                "Seed quality compliance (%)": "Certified seeds / Total seeds used * 100",
                "Optimal plant spacing adherence (%)": "Fields meeting spacing standards / Total fields",
                "Germination success rate (%)": "Seedlings emerged / Seeds planted * 100"
            },
            "Fertilizer & Nutrient Management": {
                "Correct fertilizer application (%)": "Fields with recommended rates / Total fields",
                "Soil nutrient balance achieved (%)": "Plots balanced / Total plots * 100",
                "Fertilizer use reduction (%)": "(Previous - Current) / Previous * 100",
                "Crop nutrient uptake efficiency (%)": "Nutrient absorbed / Nutrient applied * 100"
            },
            "Integrated Pest & Disease Management": {
                "IPM adoption (%)": "Fields using IPM / Total fields * 100",
                "Chemical pesticide reduction (%)": "(Previous - Current) / Previous * 100",
                "Pest monitoring frequency (%)": "Inspections conducted / Planned inspections * 100",
                "Crop protection success rate (%)": "Protected area / Total area * 100"
            },
            "Optimize Harvest Timing & Techniques": {
                "Harvest readiness adherence (%)": "Harvested on optimal date / Total planned",
                "Mechanized harvest utilization (%)": "Mechanized tools / Total tools available",
                "Harvest losses reduction (%)": "(Previous - Current) / Previous * 100",
                "Labor efficiency during harvest (kg/day)": "Yield per labor unit"
            }
        },

        # -------------------- 4. Harvest Management --------------------
        "Harvest Management": {
            "Timely Harvesting": {
                "Harvest schedule adherence (%)": "Harvest on planned dates / Total planned",
                "Labor allocation efficiency (%)": "Assigned labor / Required labor * 100",
                "Harvest machinery utilization (%)": "Used machinery / Total available",
                "Yield losses due to delay (%)": "(Previous - Current) / Previous * 100"
            },
            "Mechanized Harvest Adoption": {
                "Mechanized tools usage (%)": "Used tools / Total available",
                "Efficiency gain (%)": "(Output mechanized - Output manual) / Output manual * 100",
                "Reduction in manual labor (%)": "(Previous - Current labor used) / Previous * 100",
                "Harvest speed (ha/day)": "Area harvested / Day"
            },
            "Post-Harvest Handling": {
                "Storage loss reduction (%)": "(Previous - Current) / Previous * 100",
                "Proper drying compliance (%)": "Produce dried per standard / Total harvested",
                "Packaging quality compliance (%)": "Packaging meeting standards / Total packed",
                "Cold storage utilization (%)": "Cold storage used / Total capacity"
            },
            "Transport Efficiency": {
                "Timely transport (%)": "Crops delivered on schedule / Total harvest",
                "Transport loss reduction (%)": "(Previous - Current) / Previous * 100",
                "Fuel efficiency per ton (%)": "Fuel used / Ton delivered",
                "Load optimization (%)": "Optimal vs actual loads transported"
            },
            "Market Readiness": {
                "Market demand match (%)": "Supplied quantity matches demand / Total supply",
                "Price realization (%)": "Actual price / Expected market price * 100",
                "Quality grading compliance (%)": "Graded crops meeting standards / Total graded",
                "Market distribution coverage (%)": "Markets served / Planned markets * 100"
            },
            "Labor Safety & Compliance": {
                "Accidents during harvest (#)": "Reported accidents / Total harvest events",
                "PPE usage compliance (%)": "Workers using PPE / Total workers * 100",
                "Labor training coverage (%)": "Trained workers / Total workers * 100",
                "Adherence to labor regulations (%)": "Compliance checks passed / Total checks"
            }
        },

        # -------------------- 5. Pest Management --------------------
        "Pest Management": {
            "Pest Monitoring & Surveillance": {
                "Fields monitored (%)": "Monitored fields / Total fields * 100",
                "Frequency of monitoring (#)": "Monitoring events / Planned events",
                "Early pest detection rate (%)": "Pests detected early / Total detected",
                "Farmer reporting compliance (%)": "Reports submitted / Total farms"
            },
            "Integrated Pest Management (IPM)": {
                "IPM adoption (%)": "Fields using IPM / Total fields * 100",
                "Chemical pesticide reduction (%)": "(Previous - Current) / Previous * 100",
                "Biological control adoption (%)": "Fields with bio-control / Total fields * 100",
                "Success rate of pest control (%)": "Protected area / Total area * 100"
            },
            "Pesticide Use Optimization": {
                "Correct dosage compliance (%)": "Fields compliant / Total fields * 100",
                "Reduction in chemical use (%)": "(Previous - Current) / Previous * 100",
                "Safe pesticide storage compliance (%)": "Properly stored / Total stored",
                "Worker safety incidents (#)": "Accidents reported / Total applications"
            },
            "Crop Damage Minimization": {
                "Damage reduction (%)": "(Previous - Current) / Previous * 100",
                "Affected area (%)": "Infested area / Total area * 100",
                "Yield saved (%)": "Actual vs potential yield saved",
                "Economic loss reduction (%)": "(Previous - Current) / Previous * 100"
            },
            "Farmer Training & Awareness": {
                "Farmers trained (#)": "Farmers trained / Total target",
                "Training completion rate (%)": "Completed / Enrolled * 100",
                "Farmer adoption of IPM (%)": "Adopters / Total trained * 100",
                "Knowledge retention (%)": "Assessment score post-training"
            },
            "Pest Forecasting & Early Warning": {
                "Forecast accuracy (%)": "Correct predictions / Total forecasts * 100",
                "Time to alert (days)": "Average days from detection to alert",
                "Preventive actions taken (%)": "Actions taken / Recommended actions * 100",
                "Reduced outbreak frequency (%)": "(Previous - Current outbreaks) / Previous * 100"
            }
        },

        # -------------------- 6. Extension & Advisory --------------------
        "Extension & Advisory": {
            "Farmer Training Programs": {
                "Training coverage (%)": "Farmers trained / Total target",
                "Frequency of training (#)": "Events conducted / Planned events",
                "Knowledge uptake (%)": "Assessment score improvement / Max score * 100",
                "Adoption of practices (%)": "Farmers applying learned practices / Total trained"
            },
            "Field Advisory Services": {
                "Visits per farmer (#)": "Visits conducted / Farmers reached",
                "Response time to farmer queries (hrs)": "Average hours to respond",
                "Problem resolution rate (%)": "Resolved queries / Total queries * 100",
                "Advisory coverage (%)": "Farmers served / Total target * 100"
            },
            "Demonstration Plots": {
                "Number of plots established (#)": "Plots established / Planned plots",
                "Adoption of demonstrated techniques (%)": "Farmers applying demo practices / Total reached",
                "Yield improvement on demo plots (%)": "(Demo yield - Control yield) / Control yield * 100",
                "Farmer satisfaction (%)": "Survey score / Total responses * 100"
            },
            "Digital Advisory Tools": {
                "Mobile app adoption (%)": "Farmers using app / Total target * 100",
                "Information dissemination rate (%)": "Messages delivered / Total messages planned",
                "Feedback incorporation (%)": "Suggestions implemented / Total received",
                "Farmer engagement (%)": "Interactions / Total users * 100"
            },
            "Farmer Group Development": {
                "Groups formed (#)": "Farmer groups established / Planned",
                "Group meeting frequency (#)": "Meetings conducted / Planned meetings",
                "Collective adoption rate (%)": "Farmers in groups adopting practices / Total farmers",
                "Group productivity improvement (%)": "Average group yield increase (%)"
            },
            "Extension Staff Performance": {
                "Staff coverage (%)": "Farmers served / Total assigned",
                "Training completion rate (%)": "Staff completing training / Total staff * 100",
                "Advisory quality rating (%)": "Survey rating / Max score * 100",
                "Response time improvement (%)": "(Previous - Current) / Previous * 100"
            }
        },

        # -------------------- 7. Livestock Management --------------------
        "Livestock Management": {
            "Improve Animal Health": {
                "Vaccination coverage (%)": "Animals vaccinated / Total livestock * 100",
                "Disease incidence reduction (%)": "(Previous - Current) / Previous * 100",
                "Mortality rate (%)": "Deaths / Total livestock * 100",
                "Regular veterinary checkups (%)": "Checked / Total livestock * 100"
            },
            "Optimize Feeding & Nutrition": {
                "Feed conversion ratio": "Feed used / Weight gain",
                "Nutritional balance compliance (%)": "Animals receiving balanced diet / Total livestock * 100",
                "Feed cost per unit weight gain ($)": "Total feed cost / Weight gained",
                "Supplement adoption (%)": "Animals receiving supplements / Total livestock * 100"
            },
            "Breeding & Reproduction Management": {
                "Artificial insemination success (%)": "Successful AI / Total inseminations * 100",
                "Natural breeding efficiency (%)": "Pregnant animals / Total eligible",
                "Birth rate (%)": "Offspring born / Total breeding animals * 100",
                "Genetic improvement adoption (%)": "Improved breeds / Total animals * 100"
            },
            "Housing & Welfare": {
                "Adequate housing coverage (%)": "Livestock housed properly / Total livestock * 100",
                "Animal welfare compliance (%)": "Checks passed / Total checks * 100",
                "Disease-free housing (%)": "Clean housing / Total housing * 100",
                "Mortality due to poor housing (%)": "Deaths / Total livestock * 100"
            },
            "Milk & Meat Productivity": {
                "Milk yield per cow (L/day)": "Total milk / Number of cows",
                "Meat yield per animal (kg)": "Total meat / Number of animals slaughtered",
                "Product quality compliance (%)": "Products meeting standards / Total products",
                "Processing efficiency (%)": "Yield vs input ratio"
            },
            "Livestock Record Management": {
                "Record completeness (%)": "Animals recorded / Total livestock * 100",
                "Timely data entry (%)": "Data entered on time / Total required",
                "Traceability coverage (%)": "Animals traceable / Total livestock * 100",
                "Farmer record usage (%)": "Farmers using records for management / Total farmers * 100"
            }
        },

        # -------------------- 8. Horticulture --------------------
        "Horticulture": {
            "Improve Crop Variety Selection": {
                "High-yield variety adoption (%)": "Varieties adopted / Total area * 100",
                "Disease-resistant variety adoption (%)": "Varieties adopted / Total area * 100",
                "Exotic variety introduction (#)": "New varieties introduced / Total planned",
                "Variety performance compliance (%)": "Varieties meeting yield/quality standards / Total"
            },
            "Enhance Greenhouse & Protected Cultivation": {
                "Protected area coverage (%)": "Protected area / Total area * 100",
                "Yield improvement (%)": "(Protected yield - Open field yield) / Open field yield * 100",
                "Energy efficiency (%)": "(Previous - Current energy used) / Previous * 100",
                "Labor productivity (%)": "Yield per labor unit"
            },
            "Optimize Fertilizer & Irrigation": {
                "Fertilizer use efficiency (%)": "Yield per unit fertilizer",
                "Irrigation water use efficiency (%)": "Yield / Water used",
                "Nutrient deficiency incidents (#)": "Fields affected / Total fields",
                "Fertilizer cost reduction (%)": "(Previous - Current) / Previous * 100"
            },
            "Pest & Disease Management": {
                "IPM adoption (%)": "Protected area / Total area * 100",
                "Chemical reduction (%)": "(Previous - Current) / Previous * 100",
                "Disease monitoring frequency (#)": "Inspections conducted / Planned inspections",
                "Yield loss due to pests (%)": "(Previous - Current) / Previous * 100"
            },
            "Post-Harvest Handling": {
                "Storage loss reduction (%)": "(Previous - Current) / Previous * 100",
                "Packaging compliance (%)": "Compliant packages / Total packages * 100",
                "Cold chain maintenance (%)": "Maintained / Total harvested",
                "Marketable yield (%)": "Market-ready produce / Total harvested"
            },
            "Extension & Advisory": {
                "Farmer training coverage (%)": "Farmers trained / Total target",
                "Demonstration plot adoption (%)": "Farmers adopting demo practices / Total reached",
                "Knowledge retention (%)": "Assessment score improvement",
                "Satisfaction rate (%)": "Survey score / Max score * 100"
            }
        },

        # -------------------- 9. Forestry --------------------
        "Forestry": {
            "Tree Planting & Afforestation": {
                "Trees planted (#)": "Planned vs planted trees",
                "Survival rate (%)": "Survived trees / Total planted * 100",
                "Area afforested (ha)": "Total area afforested",
                "Community involvement (%)": "Participants / Target population * 100"
            },
            "Forest Protection & Fire Management": {
                "Fire incidents (#)": "Reported fires / Total area",
                "Fire control compliance (%)": "Fire checks passed / Total required",
                "Illegal logging reduction (%)": "(Previous - Current) / Previous * 100",
                "Patrolling coverage (%)": "Area patrolled / Total area * 100"
            },
            "Timber & Non-Timber Products Management": {
                "Sustainable harvest compliance (%)": "Harvested sustainably / Total harvest",
                "Product quality compliance (%)": "Products meeting standards / Total produced",
                "Processing efficiency (%)": "Yield vs input ratio",
                "Revenue from forest products ($)": "Total revenue collected"
            },
            "Biodiversity Conservation": {
                "Endangered species protected (#)": "Protected / Total endangered",
                "Habitat restoration coverage (%)": "Area restored / Planned area * 100",
                "Invasive species control (%)": "Area managed / Total affected area * 100",
                "Community awareness programs (#)": "Programs conducted / Planned"
            },
            "Carbon Sequestration & Climate Mitigation": {
                "CO2 absorbed (tons)": "Estimated carbon captured",
                "Forest cover change (%)": "Change vs baseline / Baseline * 100",
                "Carbon credits earned (#)": "Credits registered / Total potential",
                "Emission reduction from forest projects (%)": "Estimated reduction / Planned reduction * 100"
            },
            "Extension & Training": {
                "Forestry training sessions (#)": "Sessions conducted / Planned",
                "Farmer participation (%)": "Farmers attended / Target population * 100",
                "Adoption of sustainable practices (%)": "Farmers applying training / Total reached",
                "Satisfaction rate (%)": "Survey score / Max score * 100"
            }
        },

        # -------------------- 10. Aquaculture --------------------
        "Aquaculture": {
            "Improve Fish Stock Management": {
                "Stocking density compliance (%)": "Correct density / Total ponds * 100",
                "Survival rate (%)": "Survived fish / Stocked fish * 100",
                "Growth rate (g/day)": "Average daily weight gain",
                "Feed conversion ratio": "Feed consumed / Weight gain"
            },
            "Optimize Water Quality": {
                "Dissolved oxygen compliance (%)": "Ponds meeting DO standards / Total ponds",
                "pH compliance (%)": "Ponds within optimal pH / Total ponds",
                "Water temperature compliance (%)": "Ponds within temp range / Total ponds",
                "Turbidity control (%)": "Ponds meeting turbidity standard / Total ponds"
            },
            "Disease & Health Management": {
                "Disease incidence reduction (%)": "(Previous - Current) / Previous * 100",
                "Mortality reduction (%)": "(Previous - Current) / Previous * 100",
                "Vaccination coverage (%)": "Fish vaccinated / Total stock * 100",
                "Early detection compliance (%)": "Inspected ponds / Total ponds * 100"
            },
            "Feed & Nutrition Management": {
                "Feed efficiency (%)": "Weight gain / Feed consumed",
                "Optimal feed usage (%)": "Feed applied / Recommended feed * 100",
                "Cost per kg gain ($)": "Feed cost / Weight gain",
                "Nutritional balance compliance (%)": "Ponds meeting diet requirement / Total ponds * 100"
            },
            "Harvest & Market Readiness": {
                "Harvest schedule adherence (%)": "Harvest on planned date / Total harvest",
                "Yield per pond (kg)": "Total harvest / Pond area",
                "Product quality compliance (%)": "Fish meeting market standards / Total harvest",
                "Transport efficiency (%)": "On-time delivery / Total deliveries * 100"
            },
            "Extension & Advisory": {
                "Farmer training coverage (%)": "Farmers trained / Target farmers * 100",
                "Demonstration ponds (#)": "Ponds established / Planned",
                "Adoption of improved practices (%)": "Farmers adopting demo practices / Total trained",
                "Satisfaction rate (%)": "Survey score / Max score * 100"
            }
        },

        # -------------------- 11. Veterinary Services --------------------
        "Veterinary Services": {
            "Animal Health Monitoring": {
                "Regular check-up coverage (%)": "Animals checked / Total livestock * 100",
                "Disease incidence reduction (%)": "(Previous - Current) / Previous * 100",
                "Vaccination compliance (%)": "Vaccinated animals / Total eligible * 100",
                "Early detection rate (%)": "Diseases detected early / Total cases * 100"
            },
            "Preventive Healthcare": {
                "Vaccination coverage (%)": "Animals vaccinated / Total eligible * 100",
                "Deworming frequency compliance (%)": "Animals treated / Planned schedule * 100",
                "Parasite infestation reduction (%)": "(Previous - Current) / Previous * 100",
                "Farmer adherence to preventive protocols (%)": "Farmers following guidelines / Total farmers * 100"
            },
            "Disease Control & Treatment": {
                "Treatment success rate (%)": "Recovered animals / Total treated * 100",
                "Timely intervention (%)": "Interventions done within recommended time / Total cases",
                "Mortality reduction (%)": "(Previous - Current) / Previous * 100",
                "Medication compliance (%)": "Correct dosage applied / Total treatments * 100"
            },
            "Livestock Nutrition & Health Management": {
                "Balanced diet coverage (%)": "Animals receiving proper nutrition / Total livestock * 100",
                "Growth rate improvement (%)": "(Current - Previous) / Previous * 100",
                "Supplement adoption (%)": "Animals receiving supplements / Total livestock * 100",
                "Feed-related disease reduction (%)": "(Previous - Current) / Previous * 100"
            },
            "Emergency & Outbreak Response": {
                "Response time to outbreak (hrs)": "Average time to respond",
                "Affected area containment (%)": "Area contained / Total affected * 100",
                "Emergency vaccination coverage (%)": "Animals vaccinated / Total exposed * 100",
                "Mortality reduction during outbreak (%)": "(Previous - Current) / Previous * 100"
            },
            "Farmer Training & Advisory": {
                "Training coverage (%)": "Farmers trained / Target farmers * 100",
                "Adoption of veterinary practices (%)": "Farmers applying learned practices / Total trained",
                "Satisfaction rate (%)": "Survey score / Max score * 100",
                "Consultation frequency (#)": "Advice sessions conducted / Planned sessions"
            }
        },

        # 12. Post-Harvest & Storage Management
        "Post-Harvest & Storage Management": {
            "Cold Storage Utilization": {
                "Storage capacity utilization (%)": "Used storage capacity / Total capacity * 100",
                "Reduction in spoilage (%)": "(Previous losses - Current losses) / Previous losses * 100",
                "Energy efficiency of storage systems (%)": "Energy used per ton stored / Baseline * 100",
                "Temperature compliance rate (%)": "Hours within recommended temperature / Total hours * 100"
            },
            "Storage Loss Reduction": {
                "Post-harvest loss (%)": "Quantity lost / Total harvested * 100",
                "Inventory rotation efficiency (%)": "Items rotated / Total items * 100",
                "Packaging integrity (%)": "Intact packaging / Total packaging * 100",
                "Storage handling errors (#)": "Number of handling mistakes per month"
            },
            "Packaging & Handling Optimization": {
                "Packaging material utilization efficiency (%)": "Used / Planned * 100",
                "Reduction in damaged goods (%)": "(Previous damage - Current damage) / Previous damage * 100",
                "Standardized packaging adoption (%)": "Standard packages used / Total packages * 100",
                "Handling cost per ton ($)": "Total handling cost / Total tonnage handled"
            },
            "Transport to Market Timeliness": {
                "On-time delivery (%)": "Deliveries on schedule / Total deliveries * 100",
                "Average transit time (days)": "Total transit days / Number of shipments",
                "Delivery delay incidents (#)": "Number of late shipments",
                "Customer satisfaction with delivery (%)": "Survey score from customers"
            },
            "Inventory Management": {
                "Inventory accuracy (%)": "Correct stock / Total stock * 100",
                "Turnover rate (times/year)": "Total sales / Average inventory",
                "Stockout frequency (#)": "Number of times inventory ran out",
                "Obsolete stock reduction (%)": "(Previous obsolete - Current) / Previous * 100"
            },
            "Shelf-life Maximization": {
                "Average product shelf-life (days)": "Measured shelf-life per batch",
                "Reduction in expired products (%)": "(Previous expired - Current expired) / Previous * 100",
                "Improved storage practices adoption (%)": "Correct practices / Total storage events * 100",
                "Consumer complaints due to spoilage (#)": "Number of complaints related to quality"
            }
        },

        # 13. Agro-Processing & Value Addition
        "Agro-Processing & Value Addition": {
            "Processing Efficiency": {
                "Throughput per hour (tons/hr)": "Processed quantity / Processing time",
                "Equipment utilization rate (%)": "Actual usage / Available capacity * 100",
                "Process downtime (hrs)": "Total downtime per period",
                "Waste during processing (%)": "Wasted quantity / Total processed * 100"
            },
            "Quality Standards Compliance": {
                "Products meeting standards (%)": "Conforming products / Total products * 100",
                "Rejected product rate (%)": "Rejected quantity / Total quantity * 100",
                "ISO / HACCP certification adherence (%)": "Compliant processes / Total processes * 100",
                "Customer quality complaints (#)": "Number of quality-related complaints"
            },
            "Product Diversification": {
                "New products launched (#)": "Count of new products introduced",
                "Revenue from new products ($)": "Income from newly launched products",
                "Share of total revenue from new products (%)": "Revenue from new products / Total revenue * 100",
                "Market adoption rate (%)": "Customers using new products / Total customers * 100"
            },
            "Waste Reduction": {
                "Reduction in process waste (%)": "(Previous waste - Current waste) / Previous waste * 100",
                "Recycling / reusing rate (%)": "Quantity reused / Total waste * 100",
                "Loss reduction in storage (%)": "(Previous loss - Current loss) / Previous loss * 100",
                "Energy waste reduction (%)": "(Previous energy use - Current) / Previous * 100"
            },
            "Energy & Resource Efficiency": {
                "Energy consumption per ton ($/ton)": "Total energy / Processed quantity",
                "Water usage efficiency (m³/ton)": "Water used / Processed quantity",
                "Labor productivity (tons/employee)": "Processed quantity / Number of employees",
                "Input material utilization (%)": "Input used / Input required * 100"
            },
            "Marketable Product Yield": {
                "Marketable yield (%)": "Good product / Total processed * 100",
                "Loss during transport (%)": "Quantity lost / Total shipped * 100",
                "Time to market (days)": "Average days from processing to market",
                "Customer satisfaction with processed products (%)": "Survey score"
            }
        },

        # 14. Climate & Environmental Risk Management
        "Climate & Environmental Risk Management": {
            "Drought & Flood Preparedness": {
                "Irrigation buffer capacity (%)": "Available water reserve / Required reserve * 100",
                "Emergency response drills (#)": "Number of preparedness drills conducted",
                "Crop survival rate during drought (%)": "Survived crops / Total crops * 100",
                "Damage mitigation cost efficiency ($)": "Cost saved vs expected damage"
            },
            "Soil & Water Conservation": {
                "Erosion control implementation (%)": "Area with measures / Total area * 100",
                "Water retention improvement (%)": "Post-project retention - baseline retention / baseline * 100",
                "Farmer adoption of conservation practices (%)": "Adopting farmers / Total farmers * 100",
                "Reduction in sediment runoff (%)": "(Previous - Current runoff) / Previous * 100"
            },
            "Climate-Resilient Crop Adoption": {
                "Area under resilient crops (%)": "Resilient crop area / Total area * 100",
                "Yield stability index": "Variance of yields vs baseline",
                "Number of climate-resilient varieties introduced (#)": "Count of varieties",
                "Farmer adoption rate (%)": "Farmers planting resilient varieties / Total farmers * 100"
            },
            "Pest & Disease Risk Mitigation": {
                "Early warning system coverage (%)": "Area covered by monitoring / Total area * 100",
                "Reduction in outbreak incidence (%)": "(Previous outbreaks - Current) / Previous * 100",
                "Farmer training on risk mitigation (#)": "Number of trainings conducted",
                "Crop loss reduction (%)": "(Previous loss - Current) / Previous * 100"
            },
            "Environmental Compliance": {
                "Compliance with environmental laws (%)": "Audited compliant activities / Total activities * 100",
                "Wastewater discharge standards met (%)": "Compliant discharges / Total discharges * 100",
                "Chemical usage monitoring (%)": "Proper chemical use events / Total events * 100",
                "Environmental audit score": "Average audit rating"
            },
            "Sustainability Program Implementation": {
                "Green initiative projects (#)": "Number of environmental projects implemented",
                "Carbon footprint reduction (%)": "(Baseline emissions - Current) / Baseline * 100",
                "Renewable energy adoption (%)": "Energy from renewables / Total energy * 100",
                "Stakeholder engagement in sustainability (#)": "Participants in sustainability programs"
            }
        },

    },

    "Learning & Growth Perspective": {

        **GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE['Learning & Growth Perspective'],

    },
}
