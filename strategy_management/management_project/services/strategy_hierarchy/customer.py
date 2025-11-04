class CustomerStrategyService:
    """Service class for Customer Perspective strategies"""

    def get_customer_hierarchy(self):
        return {

            "Customer Acquisition & Market Reach": {
                "Increase qualified lead generation": {
                    "Number of qualified leads per month": "Count of leads meeting qualification criteria per month",
                    "Lead generation cost per channel": "Total marketing spend per channel / Number of leads generated per channel",
                    "Lead-to-opportunity conversion rate": "(Leads converted to opportunities / Total leads) * 100",
                    "Marketing qualified lead volume growth": "((Current MQL volume - Previous MQL volume) / Previous MQL volume) * 100"
                },
                "Improve conversion rates across channels": {
                    "Conversion rate by channel": "(Leads converted / Total leads per channel) * 100",
                    "Sales funnel efficiency": "(Opportunities closed / Total leads) * 100",
                    "Cost per acquisition reduction": "((Previous acquisition cost - Current acquisition cost) / Previous acquisition cost) * 100",
                    "Revenue per channel growth": "((Current revenue per channel - Previous revenue per channel) / Previous revenue per channel) * 100"
                },
                "Enhance digital marketing effectiveness": {
                    "Digital marketing ROI": "((Revenue from digital campaigns - Campaign cost) / Campaign cost) * 100",
                    "Click-through rate improvement": "((Current CTR - Previous CTR) / Previous CTR) * 100",
                    "Cost per click reduction": "((Previous CPC - Current CPC) / Previous CPC) * 100",
                    "Digital campaign conversion rate": "(Conversions / Total clicks) * 100"
                },
                "Build strong brand awareness": {
                    "Brand awareness survey": "(Surveyed awareness level / Total surveyed) * 100",
                    "Unaided brand recall": "(Respondents recalling brand without prompts / Total respondents) * 100",
                    "Social media reach and engagement": "(Total interactions on social media / Total followers) * 100",
                    "Share of voice in market": "(Brand mentions / Total market mentions) * 100"
                },
                "Target new customer segments": {
                    "Revenue from new segments": "Revenue generated from newly targeted segments",
                    "Customer acquisition rate for new segments": "(New customers acquired / Total potential customers in segment) * 100",
                    "Market penetration rate for new segments": "(Customers acquired / Total potential customers in segment) * 100",
                    "Segment growth percentage": "((Current segment revenue - Previous segment revenue) / Previous segment revenue) * 100"
                },
                "Expand into underserved markets": {
                    "Revenue from underserved markets": "Total revenue generated in underserved areas",
                    "Customer acquisition cost in new markets": "Marketing & sales spend in new markets / New customers acquired",
                    "Market share in new areas": "(Sales in new area / Total market size) * 100",
                    "Customer satisfaction in new markets": "(Sum of satisfaction ratings from new market customers / Number of respondents) * 100"
                },
                "Optimize customer onboarding": {
                    "Onboarding completion rate": "(Customers completing onboarding / Total new customers) * 100",
                    "Time to first value reduction": "Previous time to first value - Current time to first value",
                    "New customer satisfaction score": "(Sum of satisfaction ratings from new customers / Number of respondents) * 100",
                    "Onboarding cost per customer": "Total onboarding cost / Number of onboarded customers"
                },
                "Leverage customer referral programs": {
                    "Referral rate": "(Referrals / Total customers) * 100",
                    "Cost per acquired referral": "Total referral program cost / Referrals acquired",
                    "Referral program ROI": "((Revenue from referrals - Program cost) / Program cost) * 100",
                    "Customer lifetime value from referrals": "Average CLV of customers acquired via referrals"
                },
                "Improve website conversion funnels": {
                    "Website conversion rate": "(Conversions / Total website visitors) * 100",
                    "Cart abandonment rate reduction": "((Previous abandonment rate - Current abandonment rate) / Previous abandonment rate) * 100",
                    "Bounce rate improvement": "((Previous bounce rate - Current bounce rate) / Previous bounce rate) * 100",
                    "Page views per session increase": "Current average page views per session - Previous average page views per session"
                },
                "Execute targeted acquisition campaigns": {
                    "Campaign ROI": "((Revenue from campaign - Campaign cost) / Campaign cost) * 100",
                    "Customer acquisition cost per campaign": "Total campaign cost / Customers acquired from campaign",
                    "Conversion rate per campaign": "(Conversions / Total leads generated from campaign) * 100",
                    "Revenue generated from campaigns": "Total revenue attributable to specific campaigns"
                }
            },
            "Customer Satisfaction & Experience": {
                "Improve service quality standards": {
                    "Customer satisfaction score (CSAT)": "(Sum of satisfaction ratings / Number of survey respondents) * 100",
                    "Service quality index score": "((Sum of service metrics scores) / Maximum possible score) * 100",
                    "First-contact resolution rate": "(Issues resolved at first contact / Total issues) * 100",
                    "Service level agreement compliance": "(SLAs met / Total SLAs) * 100"
                },
                "Enhance customer support responsiveness": {
                    "Average response time reduction": "Previous average response time - Current average response time",
                    "Support ticket backlog reduction": "Previous backlog - Current backlog",
                    "Customer satisfaction post-support": "(Sum of satisfaction ratings post-support / Number of respondents) * 100",
                    "Resolution time improvement": "Previous average resolution time - Current average resolution time"
                },
                "Personalize customer interactions": {
                    "Personalization effectiveness score": "((Number of personalized interactions leading to desired outcome) / Total personalized interactions) * 100",
                    "Customer engagement rate improvement": "((Current engagement rate - Previous engagement rate) / Previous engagement rate) * 100",
                    "Repeat purchase rate increase": "((Current repeat purchases - Previous repeat purchases) / Previous repeat purchases) * 100",
                    "Upsell conversion rate improvement": "((Current upsell conversions - Previous upsell conversions) / Previous upsell conversions) * 100"
                },
                "Streamline customer journey mapping": {
                    "Customer effort score reduction": "((Previous effort score - Current effort score) / Previous effort score) * 100",
                    "Journey completion rate improvement": "((Current journey completions - Previous journey completions) / Previous journey completions) * 100",
                    "Touchpoint satisfaction scores": "(Sum of touchpoint satisfaction ratings / Number of touchpoints) * 100",
                    "Process step reduction in journey": "Previous number of steps - Current number of steps"
                },
                "Improve complaint resolution processes": {
                    "Complaint resolution time reduction": "((Previous resolution time - Current resolution time) / Previous resolution time) * 100",
                    "First-contact resolution rate": "(Issues resolved at first contact / Total issues) * 100",
                    "Customer satisfaction post-complaint": "(Sum of satisfaction ratings post-complaint / Number of respondents) * 100",
                    "Complaint escalation rate reduction": "((Previous escalations - Current escalations) / Previous escalations) * 100"
                },
                "Enhance after-sales service": {
                    "After-sales satisfaction score": "(Sum of satisfaction ratings after service / Number of respondents) * 100",
                    "Service follow-up completion rate": "(Follow-ups completed / Total required follow-ups) * 100",
                    "Repeat purchase rate improvement": "((Current repeat purchases - Previous repeat purchases) / Previous repeat purchases) * 100",
                    "Warranty claim resolution time": "Average time to resolve warranty claims"
                },
                "Strengthen customer communication": {
                    "Communication open rate": "(Emails opened / Total emails sent) * 100",
                    "Click-through rate improvement": "((Current CTR - Previous CTR) / Previous CTR) * 100",
                    "Customer engagement score": "((Sum of interactions per customer) / Total customers) * 100",
                    "Response rate to outreach": "(Responses received / Total outreach attempts) * 100"
                },
                "Implement customer feedback systems": {
                    "Feedback collection rate": "(Feedback collected / Total customers solicited) * 100",
                    "Actionable insights implemented": "(Implemented insights / Total insights collected) * 100",
                    "Feedback response time reduction": "((Previous response time - Current response time) / Previous response time) * 100",
                    "Customer perception of being heard": "(Sum of survey scores on being heard / Number of respondents) * 100"
                },
                "Improve product usability": {
                    "Product usability score": "(Sum of usability ratings / Number of respondents) * 100",
                    "Customer training time reduction": "((Previous training hours - Current training hours) / Previous training hours) * 100",
                    "Support calls related to usability": "(Number of calls about usability / Total support calls) * 100",
                    "Feature adoption rate improvement": "((Current adoption rate - Previous adoption rate) / Previous adoption rate) * 100"
                },
                "Enhance digital experience": {
                    "Digital experience score": "(Sum of digital experience ratings / Number of respondents) * 100",
                    "Mobile app rating improvement": "((Current rating - Previous rating) / Previous rating) * 100",
                    "Website satisfaction score": "(Sum of website satisfaction ratings / Number of respondents) * 100",
                    "Digital channel engagement rate": "(Interactions via digital channels / Total users) * 100"
                }
            },
            "Customer Loyalty & Retention": {
                "Reduce customer churn rate": {
                    "Churn rate reduction": "((Previous churn rate - Current churn rate) / Previous churn rate) * 100",
                    "Customer lifetime value improvement": "((Current CLV - Previous CLV) / Previous CLV) * 100",
                    "Revenue retention percentage": "(Revenue retained from existing customers / Total revenue) * 100",
                    "Lost customer recovery rate": "(Recovered customers / Total lost customers) * 100"
                },
                "Increase customer retention percentage": {
                    "Customer retention rate by segment": "(Retained customers / Total customers in segment) * 100",
                    "Repeat purchase rate improvement": "((Current repeat purchase rate - Previous repeat purchase rate) / Previous repeat purchase rate) * 100",
                    "Loyalty program participation rate": "(Participants / Eligible customers) * 100",
                    "Customer tenure increase": "Average tenure current period - Previous period"
                },
                "Enhance loyalty program effectiveness": {
                    "Loyalty program enrollment rate": "(Enrolled customers / Total target customers) * 100",
                    "Points redemption rate": "(Redeemed points / Total points issued) * 100",
                    "Program engagement score": "(Sum of engagement actions in program / Total participants) * 100",
                    "Retention uplift from loyalty program": "((Retention of participants - Retention of non-participants) / Retention of non-participants) * 100"
                },
                "Improve net promoter score": {
                    "NPS score improvement": "Current NPS - Previous NPS",
                    "Promoter percentage increase": "((Current promoters / Total respondents) * 100) - Previous percentage",
                    "Detractor percentage reduction": "((Previous detractors - Current detractors) / Previous detractors) * 100",
                    "NPS trend over time": "Graphical trend analysis of NPS across periods"
                },
                "Strengthen customer engagement": {
                    "Active user percentage": "(Active users / Total users) * 100",
                    "Engagement score improvement": "((Current engagement actions per user - Previous) / Previous) * 100",
                    "Interaction frequency increase": "((Current interactions - Previous interactions) / Previous interactions) * 100",
                    "Product usage depth improvement": "((Current depth metrics - Previous depth metrics) / Previous depth metrics) * 100"
                },
                "Increase renewal rates": {
                    "Contract renewal rate": "(Contracts renewed / Contracts due for renewal) * 100",
                    "Renewal revenue retention": "(Revenue from renewed contracts / Revenue from contracts due) * 100",
                    "Auto-renewal rate improvement": "((Current auto-renewals - Previous auto-renewals) / Previous auto-renewals) * 100",
                    "Renewal process satisfaction": "(Sum of satisfaction ratings with renewal process / Number of respondents) * 100"
                },
                "Improve product stickiness": {
                    "Daily active users percentage": "(DAU / Total users) * 100",
                    "Feature usage frequency": "Average usage per feature / Total users",
                    "Product dependency index": "(Sum of reliance scores per feature / Number of features) * 100",
                    "Switching cost perception": "(Sum of survey scores on perceived switching cost / Number of respondents) * 100"
                },
                "Build customer communities": {
                    "Community participation rate": "(Active community members / Total members) * 100",
                    "User-generated content volume": "Total content contributions from users",
                    "Peer-to-peer support percentage": "(Resolved support issues by peers / Total support issues) * 100",
                    "Community satisfaction score": "(Sum of community satisfaction ratings / Number of respondents) * 100"
                },
                "Enhance proactive support": {
                    "Proactive issue resolution rate": "(Proactively resolved issues / Total issues) * 100",
                    "Preventative support incidents": "Number of incidents prevented via proactive actions",
                    "Customer satisfaction proactive support": "(Sum of satisfaction ratings for proactive support / Number of respondents) * 100",
                    "Reactive ticket reduction percentage": "((Previous reactive tickets - Current reactive tickets) / Previous reactive tickets) * 100"
                },
                "Personalize retention strategies": {
                    "Personalized offer acceptance rate": "(Accepted personalized offers / Total offers) * 100",
                    "Retention campaign effectiveness": "(Retention achieved via campaign / Total targeted) * 100",
                    "Customer segment retention rates": "(Retained customers per segment / Total segment customers) * 100",
                    "Lifetime value preservation rate": "(CLV preserved via retention actions / Total CLV) * 100"
                }
            },
            "Customer Value & Relationship Management": {
                "Increase customer lifetime value": {
                    "CLV amount improvement": "Current CLV - Previous CLV",
                    "Customer profitability score increase": "Current profitability score - Previous profitability score",
                    "Value per customer growth": "((Current value per customer - Previous value per customer) / Previous value per customer) * 100",
                    "Return on customer investment": "(Profit from customer / Cost to acquire & serve customer) * 100"
                },
                "Improve relationship management": {
                    "Account health score improvement": "Current health score - Previous health score",
                    "Relationship depth score": "(Sum of meaningful interactions per account / Total interactions) * 100",
                    "Strategic account retention rate": "(Strategic accounts retained / Total strategic accounts) * 100",
                    "Executive engagement frequency": "Average number of executive interactions per account"
                },
                "Enhance customer segmentation": {
                    "Segmentation accuracy percentage": "(Correctly segmented customers / Total customers) * 100",
                    "Targeting effectiveness score": "(Revenue or conversions from targeted segments / Total targeted segments) * 100",
                    "Segment-specific growth rates": "((Current segment revenue - Previous segment revenue) / Previous segment revenue) * 100",
                    "Personalization relevance score": "(Interactions meeting personalized needs / Total personalized interactions) * 100"
                },
                "Strengthen account management": {
                    "Account growth rate": "((Current account revenue - Previous account revenue) / Previous account revenue) * 100",
                    "Account penetration depth": "(Products/services used per account / Total offerings) * 100",
                    "Account manager effectiveness score": "(Sum of KPIs achieved by account manager / Total KPIs assigned) * 100",
                    "Strategic account satisfaction": "(Sum of satisfaction ratings from strategic accounts / Number of respondents) * 100"
                },
                "Develop customer success programs": {
                    "Customer success score improvement": "Current success score - Previous success score",
                    "Product adoption rate increase": "((Current adoption rate - Previous adoption rate) / Previous adoption rate) * 100",
                    "Success plan completion rate": "(Completed success plans / Total success plans) * 100",
                    "Business outcomes achieved": "(Number of outcomes achieved / Total improvement_needed outcomes) * 100"
                },
                "Improve upsell and cross-sell rates": {
                    "Upsell conversion rate": "(Upsell transactions / Eligible customers) * 100",
                    "Cross-sell revenue growth": "((Current cross-sell revenue - Previous cross-sell revenue) / Previous cross-sell revenue) * 100",
                    "Average revenue per account": "Total revenue / Total accounts",
                    "Solution adoption breadth": "(Number of solutions adopted per customer / Total solutions offered) * 100"
                },
                "Enhance customer education": {
                    "Training completion rate": "(Completed trainings / Total assigned trainings) * 100",
                    "Customer proficiency score": "(Sum of proficiency scores / Number of assessed customers) * 100",
                    "Self-service usage increase": "((Current usage - Previous usage) / Previous usage) * 100",
                    "Support ticket reduction percentage": "((Previous tickets - Current tickets) / Previous tickets) * 100"
                },
                "Build strategic customer partnerships": {
                    "Strategic partnership count": "Number of active strategic partnerships",
                    "Joint business value created": "Revenue or profit generated through partnerships",
                    "Partnership satisfaction score": "(Sum of satisfaction ratings from partners / Number of respondents) * 100",
                    "Co-innovation projects completed": "(Completed joint innovation projects / Total improvement_needed projects) * 100"
                },
                "Improve customer health scoring": {
                    "Health score accuracy percentage": "(Accurate health predictions / Total customers assessed) * 100",
                    "At-risk customer identification rate": "(Correctly identified at-risk customers / Total at-risk customers) * 100",
                    "Intervention effectiveness score": "(Revenue or retention preserved through interventions / Total interventions) * 100",
                    "Health score trend improvement": "Improvement of average health score over time"
                },
                "Develop customer advocacy programs": {
                    "Advocate identification rate": "(Identified advocates / Total customers) * 100",
                    "Referenceable customer percentage": "(Referenceable customers / Total customers) * 100",
                    "Case study completion rate": "(Completed case studies / Improvement Needed case studies) * 100",
                    "Advocate engagement score": "(Sum of engagement actions by advocates / Total advocates) * 100"
                }
            },
            "Customer Insights & Analytics": {
                "Enhance customer data collection": {
                    "Data completeness score": "(Complete customer profiles / Total customers) * 100",
                    "Data accuracy rate": "(Accurate data points / Total data points) * 100",
                    "Real-time data availability": "(Real-time data sources / Total data sources) * 100",
                    "Customer profile enrichment rate": "(Enriched profiles / Total profiles) * 100"
                },
                "Improve customer analytics capabilities": {
                    "Predictive model accuracy": "(Correct predictions / Total predictions) * 100",
                    "Customer segmentation effectiveness": "(Revenue from targeted segments / Total revenue) * 100",
                    "Behavioral pattern identification rate": "(Identified patterns / Total potential patterns) * 100",
                    "Analytics adoption by business units": "(Business units using analytics / Total units) * 100"
                },
                "Leverage customer feedback for improvement": {
                    "Feedback implementation rate": "(Implemented feedback items / Total feedback) * 100",
                    "Customer-suggested improvements implemented": "(Implemented customer suggestions / Total suggestions) * 100",
                    "Feedback response time": "Average time to respond to customer feedback",
                    "Customer perception of feedback utilization": "Survey score on how well feedback is used"
                },
                "Enhance customer journey analytics": {
                    "Journey mapping completeness": "(Mapped journey stages / Total stages) * 100",
                    "Drop-off point identification": "(Identified drop-off points / Total potential points) * 100",
                    "Journey optimization impact": "((Improved conversion rate - Baseline rate) / Baseline rate) * 100",
                    "Cross-channel journey visibility": "(Visible cross-channel interactions / Total interactions) * 100"
                },
                "Develop customer intelligence systems": {
                    "Customer intelligence platform adoption": "(Users adopting platform / Total potential users) * 100",
                    "Single customer view completeness": "(Complete customer views / Total customers) * 100",
                    "Real-time customer insights availability": "(Available real-time insights / Total improvement_needed insights) * 100",
                    "Customer intelligence ROI": "((Benefits from intelligence - System cost) / System cost) * 100"
                },
            },
            #
            # agriculture start
            # Agriculture - NGO & Development Context
            "Agriculture / NGO & Development Focus": {
                "Enhance Smallholder Farmer Resilience": {
                    "Smallholder income diversification": "(Farmers with multiple income sources / Total farmers) * 100",
                    "Climate resilience capacity score": "Composite score of adaptive capacity metrics",
                    "Food security index improvement": "((Current food security index - Previous) / Previous) * 100",
                    "Shock recovery time reduction": "((Previous recovery time - Current) / Previous) * 100"
                },
                "Promote Community-Led Development": {
                    "Community decision-making participation": "(Active community participants / Total community) * 100",
                    "Local resource mobilization effectiveness": "(Mobilized local resources / Total potential) * 100",
                    "Community ownership sustainability": "(Self-sustaining projects / Total projects) * 100",
                    "Traditional knowledge integration rate": "(Projects using traditional knowledge / Total projects) * 100"
                },
                "Strengthen Farmer Organizations": {
                    "Farmer group organizational capacity": "Score based on governance and management assessment",
                    "Collective marketing volume": "Percentage of produce sold collectively",
                    "Group savings mobilization": "Total savings mobilized per member",
                    "Leadership development completion": "(Trained leaders / Total target leaders) * 100"
                },
                "Expand Sustainable Livelihood Options": {
                    "Livelihood diversification index": "Average number of livelihood activities per household",
                    "Natural resource management adoption": "(Households practicing NRM / Total households) * 100",
                    "Value addition activities": "(Households engaged in value addition / Total households) * 100",
                    "Eco-enterprise development": "Number of successful eco-enterprises established"
                },
                "Improve Gender Equality in Agriculture": {
                    "Women's access to resources": "(Women with equal resource access / Total women) * 100",
                    "Women's decision-making power": "Score based on decision-making participation",
                    "Gender-based violence reduction": "((Previous incidents - Current) / Previous) * 100",
                    "Women's leadership representation": "(Women in leadership positions / Total positions) * 100"
                },
                "Enhance Disaster Risk Reduction": {
                    "Early warning system coverage": "(Covered households / Total households) * 100",
                    "Disaster preparedness plan adoption": "(Households with plans / Total households) * 100",
                    "Emergency response effectiveness": "Score based on response time and coverage",
                    "Risk reduction infrastructure": "(Protected assets / Total vulnerable assets) * 100"
                }
            },

            # Agriculture - Government & Policy Context
            "Agriculture / Government & Policy Focus": {
                "Strengthen Agricultural Extension Systems": {
                    "Extension worker to farmer ratio": "Number of farmers per extension worker",
                    "Extension service quality score": "Farmer satisfaction with extension services",
                    "Technology adoption rate": "(Adopted technologies / Recommended technologies) * 100",
                    "Knowledge transfer effectiveness": "(Farmers applying knowledge / Trained farmers) * 100"
                },
                "Enhance Food Security & Nutrition": {
                    "Food availability index": "Composite score of food availability metrics",
                    "Dietary diversity improvement": "((Current diversity - Previous) / Previous) * 100",
                    "Food price stability": "Percentage of time with stable food prices",
                    "Nutrition-sensitive agriculture adoption": "(Farmers practicing nutrition-sensitive agriculture / Total) * 100"
                },
                "Develop Robust Policy Frameworks": {
                    "Policy implementation rate": "(Implemented policies / Total policies) * 100",
                    "Stakeholder consultation effectiveness": "Score based on consultation quality",
                    "Policy impact assessment completion": "(Assessed policies / Total policies) * 100",
                    "Regulatory compliance rate": "(Compliant entities / Total entities) * 100"
                },
                "Invest in Rural Infrastructure": {
                    "Infrastructure accessibility index": "Composite score of infrastructure access",
                    "Maintenance system effectiveness": "(Well-maintained infrastructure / Total infrastructure) * 100",
                    "Public investment efficiency": "Output per infrastructure investment dollar",
                    "Community infrastructure ownership": "(Community-owned infrastructure / Total infrastructure) * 100"
                },
                "Promote Agricultural Research & Development": {
                    "Research-to-practice translation": "(Applied research findings / Total findings) * 100",
                    "Farmer participation in research": "(Participating farmers / Total farmers) * 100",
                    "Innovation adoption speed": "Average time from research to adoption",
                    "R&D investment impact": "Economic return on R&D investment"
                },
                "Enhance Market Regulation & Quality Control": {
                    "Quality standard compliance": "(Compliant products / Total products) * 100",
                    "Market information transparency": "(Transparent markets / Total markets) * 100",
                    "Consumer protection effectiveness": "Score based on protection mechanisms",
                    "Input quality assurance": "(Certified inputs / Total inputs) * 100"
                }
            },

            # Agriculture - Private Sector & Enterprise Context
            "Agriculture / Private Sector & Enterprise Focus": {
                "Develop Efficient Value Chains": {
                    "Value chain integration rate": "(Integrated farmers / Total farmers) * 100",
                    "Supply chain reliability": "(On-time deliveries / Total deliveries) * 100",
                    "Quality consistency achievement": "(Consistent quality batches / Total batches) * 100",
                    "Value addition profitability": "Profit margin from value-added products"
                },
                "Enhance Market-Driven Production": {
                    "Market-responsive cropping pattern": "(Area under market-driven crops / Total area) * 100",
                    "Demand forecasting accuracy": "(Accurate forecasts / Total forecasts) * 100",
                    "Customer satisfaction index": "Composite score of customer satisfaction metrics",
                    "Brand equity growth": "((Current brand value - Previous) / Previous) * 100"
                },
                "Optimize Agricultural Technology Solutions": {
                    "Agtech adoption ROI": "Return on agtech investments",
                    "Technology scalability achievement": "(Scalable technologies / Total technologies) * 100",
                    "Digital platform engagement": "(Active users / Total registered users) * 100",
                    "Innovation pipeline strength": "Number of viable innovations in pipeline"
                },
                "Strengthen Corporate Sustainability": {
                    "Sustainable sourcing percentage": "(Sustainably sourced products / Total products) * 100",
                    "Carbon footprint reduction": "((Previous emissions - Current) / Previous) * 100",
                    "Water stewardship performance": "Score based on water management metrics",
                    "Community investment impact": "Social return on community investments"
                },
                "Improve Supply Chain Efficiency": {
                    "Inventory turnover improvement": "((Current turnover - Previous) / Previous) * 100",
                    "Logistics cost optimization": "((Previous costs - Current) / Previous) * 100",
                    "Order fulfillment accuracy": "(Accurate orders / Total orders) * 100",
                    "Supply chain visibility": "(Visible supply chain segments / Total segments) * 100"
                },
                "Develop Strategic Partnerships": {
                    "Partnership value creation": "Economic value from partnerships",
                    "Knowledge sharing effectiveness": "(Shared knowledge utilized / Total shared) * 100",
                    "Risk sharing mechanism success": "(Successful risk sharing / Total mechanisms) * 100",
                    "Joint innovation outcomes": "Number of joint innovations developed"
                }
            },

            # Agriculture - Multi-stakeholder Collaboration Context
            "Agriculture / Multi-stakeholder Collaboration": {
                "Foster Effective Public-Private Partnerships": {
                    "PPP project success rate": "(Successful PPPs / Total PPPs) * 100",
                    "Co-investment mobilization": "Amount of leveraged investment",
                    "Risk sharing effectiveness": "Score based on risk distribution",
                    "Stakeholder satisfaction index": "Composite satisfaction score"
                },
                "Enhance Cross-Sector Coordination": {
                    "Policy coherence achievement": "(Aligned policies / Total policies) * 100",
                    "Resource complementarity utilization": "(Complementary resources used / Total available) * 100",
                    "Conflict resolution effectiveness": "(Resolved conflicts / Total conflicts) * 100",
                    "Coordinated action implementation": "(Coordinated actions / Total planned) * 100"
                },
                "Develop Agricultural Innovation Ecosystems": {
                    "Innovation ecosystem connectivity": "(Connected stakeholders / Total potential) * 100",
                    "Research commercialization rate": "(Commercialized research / Total research) * 100",
                    "Startup success rate": "(Successful startups / Total startups) * 100",
                    "Innovation funding accessibility": "(Accessible funding / Total needed funding) * 100"
                },
                "Strengthen Farmer-Industry Linkages": {
                    "Contract farming adoption": "(Farmers in contracts / Total farmers) * 100",
                    "Price premium achievement": "Average price premium over market rates",
                    "Quality standard compliance": "(Compliant farmers / Total farmers) * 100",
                    "Information sharing effectiveness": "(Shared information used / Total shared) * 100"
                },
                "Promote Knowledge Co-creation": {
                    "Joint research initiatives": "Number of collaborative research projects",
                    "Farmer-scientist interaction": "(Farmers interacting with scientists / Total farmers) * 100",
                    "Innovation adoption feedback": "(Feedback incorporated / Total feedback) * 100",
                    "Knowledge network density": "Number of active knowledge sharing connections"
                },
                "Enhance Stakeholder Governance": {
                    "Decision-making inclusivity": "(Inclusive decisions / Total decisions) * 100",
                    "Accountability mechanism effectiveness": "Score based on accountability systems",
                    "Transparency index": "Composite transparency score",
                    "Conflict of interest management": "(Managed conflicts / Total conflicts) * 100"
                }
            },

            # Agriculture - Digital Transformation Context
            "Agriculture / Digital & Technology Focus": {
                "Expand Digital Agriculture Platforms": {
                    "Platform adoption rate": "(Active users / Total target users) * 100",
                    "User retention rate": "(Retained users / Total users) * 100",
                    "Platform usability score": "User satisfaction with platform interface",
                    "Data-driven decision adoption": "(Decisions using platform data / Total decisions) * 100"
                },
                "Implement Precision Agriculture Technologies": {
                    "Precision input application": "(Area under precision application / Total area) * 100",
                    "Yield monitoring coverage": "(Monitored area / Total area) * 100",
                    "Automation level achievement": "Score based on automation implementation",
                    "Resource use efficiency": "((Previous resource use - Current) / Previous) * 100"
                },
                "Develop Agricultural Data Ecosystems": {
                    "Data interoperability achievement": "(Interoperable systems / Total systems) * 100",
                    "Data quality assurance": "(Quality data sets / Total data sets) * 100",
                    "Real-time monitoring coverage": "(Monitored parameters / Total parameters) * 100",
                    "Predictive analytics accuracy": "(Accurate predictions / Total predictions) * 100"
                },
                "Enhance E-Agriculture Services": {
                    "Digital transaction volume": "Value of digital agricultural transactions",
                    "Mobile service penetration": "(Farmers using mobile services / Total farmers) * 100",
                    "Digital literacy improvement": "((Current literacy - Previous) / Previous) * 100",
                    "Service accessibility score": "Score based on access across demographics"
                },
                "Strengthen Cybersecurity in Agriculture": {
                    "Security incident reduction": "((Previous incidents - Current) / Previous) * 100",
                    "Data protection compliance": "(Compliant systems / Total systems) * 100",
                    "Privacy assurance effectiveness": "Score based on privacy protection",
                    "Cyber resilience capacity": "Capacity to withstand cyber threats"
                },
                "Promote IoT & Smart Farming": {
                    "IoT device adoption": "(Farmers using IoT devices / Total farmers) * 100",
                    "Sensor network coverage": "(Covered area / Total area) * 100",
                    "Remote monitoring effectiveness": "(Effective remote monitoring / Total monitoring) * 100",
                    "Automated system reliability": "(Reliable automated systems / Total systems) * 100"
                }
            },

            # Agriculture - Climate & Sustainability Context
            "Agriculture / Climate & Sustainability Focus": {
                "Promote Climate-Smart Agriculture": {
                    "CSA practice adoption rate": "(Farmers adopting CSA / Total farmers) * 100",
                    "Carbon sequestration achievement": "Tons of carbon sequestered per hectare",
                    "Water use efficiency improvement": "((Previous water use - Current) / Previous) * 100",
                    "Climate risk management effectiveness": "Score based on risk reduction"
                },
                "Enhance Biodiversity Conservation": {
                    "Agrobiodiversity preservation": "Number of crop and livestock varieties conserved",
                    "Habitat restoration success": "(Restored habitat area / Total target area) * 100",
                    "Ecosystem service maintenance": "Score based on ecosystem service provision",
                    "Genetic resource protection": "Number of protected genetic resources"
                },
                "Implement Circular Economy Models": {
                    "Waste valorization rate": "(Valorized waste / Total waste) * 100",
                    "Circular business model adoption": "(Adopted circular models / Total models) * 100",
                    "Energy efficiency improvement": "((Previous energy use - Current) / Previous) * 100"
                },
                "Strengthen Environmental Governance": {
                    "Environmental compliance rate": "(Compliant operations / Total operations) * 100",
                    "Eco-certification adoption": "(Certified products / Total products) * 100",
                    "Environmental impact assessment": "(Assessed projects / Total projects) * 100",
                    "Sustainability reporting quality": "Score based on reporting standards"
                },
                "Develop Climate Resilience Strategies": {
                    "Adaptive capacity improvement": "((Current capacity - Previous) / Previous) * 100",
                    "Climate information utilization": "(Farmers using climate info / Total farmers) * 100",
                    "Resilient infrastructure development": "(Resilient infrastructure / Total infrastructure) * 100",
                    "Disaster risk financing coverage": "(Covered risks / Total risks) * 100"
                },
                "Promote Sustainable Intensification": {
                    "Yield gap reduction": "((Previous gap - Current gap) / Previous gap) * 100",
                    "Input use efficiency": "Output per unit of input",
                    "Land degradation neutrality": "Score based on land condition maintenance",
                    "Sustainable practice integration": "(Integrated practices / Total practices) * 100"
                }
            },

            # Agriculture - Social Inclusion Context
            "Agriculture / Social Inclusion & Equity": {
                "Enhance Youth Engagement in Agriculture": {
                    "Youth participation rate": "(Youth in agriculture / Total youth) * 100",
                    "Youth entrepreneurship development": "(Youth-led agribusinesses / Total businesses) * 100",
                    "Digital skills acquisition": "(Youth with digital skills / Total youth) * 100",
                    "Career pathway accessibility": "(Accessible pathways / Total pathways) * 100"
                },
                "Strengthen Indigenous Knowledge Systems": {
                    "Traditional knowledge documentation": "(Documented knowledge systems / Total systems) * 100",
                    "Intergenerational knowledge transfer": "(Transferred knowledge / Total knowledge) * 100",
                    "Cultural heritage preservation": "Score based on heritage maintenance",
                    "Indigenous innovation recognition": "(Recognized innovations / Total innovations) * 100"
                },
                "Improve Access for Marginalized Groups": {
                    "Resource access equity": "Score based on equitable resource distribution",
                    "Market inclusion rate": "(Included marginalized groups / Total groups) * 100",
                    "Capacity building effectiveness": "(Trained individuals / Total target) * 100",
                    "Social protection coverage": "(Covered individuals / Total vulnerable) * 100"
                },
                "Promote Inclusive Value Chains": {
                    "Smallholder inclusion rate": "(Included smallholders / Total smallholders) * 100",
                    "Gender-sensitive value chain development": "(Gender-sensitive chains / Total chains) * 100",
                    "Pro-poor business model adoption": "(Adopted pro-poor models / Total models) * 100",
                    "Inclusive market access": "(Accessible markets / Total markets) * 100"
                },
                "Enhance Social Cohesion": {
                    "Community trust index": "Score based on trust levels",
                    "Conflict resolution mechanism effectiveness": "(Resolved conflicts / Total conflicts) * 100",
                    "Social capital development": "Increase in social network strength",
                    "Collective action success": "(Successful collective actions / Total actions) * 100"
                },
                "Develop Inclusive Digital Solutions": {
                    "Digital divide reduction": "((Previous divide - Current) / Previous) * 100",
                    "Accessible technology design": "(Accessible technologies / Total technologies) * 100",
                    "Digital literacy equity": "Score based on literacy across demographics",
                    "Inclusive innovation development": "(Inclusive innovations / Total innovations) * 100"
                }
            },

            # agriculture end

            # health start
            "Health / Clinical Outcomes & Quality": {
                "Reduce disease incidence and prevalence": {
                    "Disease incidence rate": "(New cases / Population at risk) * 1000",
                    "Disease prevalence reduction": "((Previous prevalence - Current prevalence) / Previous prevalence) * 100",
                    "Mortality rate reduction": "((Previous mortality - Current mortality) / Previous mortality) * 100",
                    "Case fatality rate improvement": "((Previous CFR - Current CFR) / Previous CFR) * 100"
                },
                "Improve chronic disease management": {
                    "Disease control rate": "(Patients with controlled condition / Total patients) * 100",
                    "Hospital readmission reduction": "((Previous readmissions - Current readmissions) / Previous readmissions) * 100",
                    "Medication adherence rate": "(Patients adherent to treatment / Total patients) * 100",
                    "Complication prevention rate": "(Patients without complications / Total at-risk) * 100"
                },
                "Enhance maternal and child health outcomes": {
                    "Maternal mortality reduction": "((Previous MMR - Current MMR) / Previous MMR) * 100",
                    "Infant mortality improvement": "((Previous IMR - Current IMR) / Previous IMR) * 100",
                    "Low birth weight reduction": "((Previous rate - Current rate) / Previous rate) * 100",
                    "Child development milestone achievement": "(Children meeting milestones / Total children) * 100"
                },
                "Advance surgical and procedural outcomes": {
                    "Surgical success rate": "(Successful procedures / Total procedures) * 100",
                    "Surgical complication reduction": "((Previous complications - Current complications) / Previous complications) * 100",
                    "Post-operative recovery rate": "(Patients with optimal recovery / Total patients) * 100",
                    "Surgical site infection reduction": "((Previous SSI - Current SSI) / Previous SSI) * 100"
                },
                "Improve mental health outcomes": {
                    "Symptom reduction rate": "(Patients with improved symptoms / Total patients) * 100",
                    "Functional improvement score": "(Patients with functional improvement / Total patients) * 100",
                    "Crisis intervention success": "(Successful interventions / Total crises) * 100",
                    "Mental health recovery rate": "(Patients in recovery / Total patients) * 100"
                },
                "Optimize geriatric health outcomes": {
                    "Age-related condition management": "(Well-managed elderly / Total elderly) * 100",
                    "Functional independence maintenance": "(Independent elderly / Total elderly) * 100",
                    "Cognitive health preservation": "(Cognitively intact elderly / Total elderly) * 100",
                    "Multi-morbidity management success": "(Well-managed patients / Total multi-morbid) * 100"
                }
            },
            "Health / Preventive Health & Wellness": {
                "Expand immunization coverage": {
                    "Vaccination completion rate": "(Fully vaccinated / Total eligible) * 100",
                    "Vaccine-preventable disease reduction": "((Previous incidence - Current incidence) / Previous incidence) * 100",
                    "Immunization timeliness": "(Vaccines on schedule / Total vaccines) * 100",
                    "Herd immunity achievement": "(Population immune / Total population) * 100"
                },
                "Promote health screening and early detection": {
                    "Screening participation rate": "(Screened individuals / Total eligible) * 100",
                    "Early detection rate": "(Cases detected early / Total cases) * 100",
                    "Screening follow-up completion": "(Completed follow-ups / Total required) * 100",
                    "Risk factor identification rate": "(Identified risks / Total screened) * 100"
                },
                "Advance health education and literacy": {
                    "Health knowledge improvement": "(Individuals with improved knowledge / Total participants) * 100",
                    "Preventive behavior adoption": "(Adopting healthy behaviors / Total target) * 100",
                    "Health literacy score improvement": "((Current score - Previous score) / Previous score) * 100",
                    "Self-care capability development": "(Capable individuals / Total participants) * 100"
                },
                "Strengthen lifestyle medicine": {
                    "Nutrition improvement rate": "(Individuals with improved nutrition / Total participants) * 100",
                    "Physical activity adoption": "(Active individuals / Total target) * 100",
                    "Tobacco cessation success": "(Successful quitters / Total attempting) * 100",
                    "Substance use reduction": "((Previous use - Current use) / Previous use) * 100"
                },
                "Enhance occupational health": {
                    "Workplace health assessment rate": "(Assessed workplaces / Total workplaces) * 100",
                    "Occupational injury reduction": "((Previous injuries - Current injuries) / Previous injuries) * 100",
                    "Employee wellness participation": "(Participating employees / Total employees) * 100",
                    "Work-related illness prevention": "(Prevented cases / Total at-risk) * 100"
                },
                "Improve environmental health": {
                    "Environmental risk reduction": "((Previous risks - Current risks) / Previous risks) * 100",
                    "Sanitation coverage improvement": "((Current coverage - Previous coverage) / Previous coverage) * 100",
                    "Water safety compliance": "(Safe water sources / Total sources) * 100",
                    "Vector control effectiveness": "(Controlled areas / Total areas) * 100"
                }
            },
            "Health / Healthcare Access & Availability": {
                "Expand primary care access": {
                    "Primary care coverage": "(Population with access / Total population) * 100",
                    "First-contact availability": "(Available first contacts / Total needed) * 100",
                    "Geographic access equity": "(Equitable access points / Total access points) * 100",
                    "Continuity of care rate": "(Patients with continuous care / Total patients) * 100"
                },
                "Strengthen emergency care systems": {
                    "Emergency response timeliness": "(Timely responses / Total emergencies) * 100",
                    "Emergency department capacity": "(Available capacity / Total capacity) * 100",
                    "Critical care accessibility": "(Accessible critical care / Total needed) * 100",
                    "Trauma system effectiveness": "(Effective trauma care / Total trauma cases) * 100"
                },
                "Enhance specialty care access": {
                    "Specialist referral completion": "(Completed referrals / Total referrals) * 100",
                    "Specialty wait time reduction": "((Previous wait - Current wait) / Previous wait) * 100",
                    "Multi-disciplinary care availability": "(Available teams / Total needed) * 100",
                    "Complex condition management access": "(Accessible management / Total complex cases) * 100"
                },
                "Advance diagnostic service access": {
                    "Diagnostic test availability": "(Available tests / Total needed) * 100",
                    "Test result turnaround time": "(Timely results / Total tests) * 100",
                    "Imaging service accessibility": "(Accessible imaging / Total needed) * 100",
                    "Laboratory service coverage": "(Covered population / Total population) * 100"
                },
                "Improve medication access": {
                    "Essential medicine availability": "(Available medicines / Total essential) * 100",
                    "Prescription affordability": "(Affordable prescriptions / Total prescriptions) * 100",
                    "Medication supply continuity": "(Continuous supply / Total supply periods) * 100",
                    "Rational drug use compliance": "(Appropriate use / Total drug use) * 100"
                },
                "Expand digital health access": {
                    "Telehealth utilization rate": "(Telehealth users / Total eligible) * 100",
                    "Digital service availability": "(Available digital services / Total services) * 100",
                    "Health information access": "(Population with access / Total population) * 100",
                    "Remote monitoring coverage": "(Monitored patients / Total eligible) * 100"
                }
            },
            "Health / Patient Safety & Quality": {
                "Reduce healthcare-associated infections": {
                    "HAI incidence reduction": "((Previous HAI - Current HAI) / Previous HAI) * 100",
                    "Infection control compliance": "(Compliant facilities / Total facilities) * 100",
                    "Hand hygiene adherence": "(Adherent staff / Total staff) * 100",
                    "Sterilization effectiveness": "(Effective sterilization / Total procedures) * 100"
                },
                "Improve medication safety": {
                    "Medication error reduction": "((Previous errors - Current errors) / Previous errors) * 100",
                    "Adverse drug event prevention": "(Prevented events / Total at-risk) * 100",
                    "Prescription accuracy rate": "(Accurate prescriptions / Total prescriptions) * 100",
                    "Drug interaction screening": "(Screened patients / Total patients) * 100"
                },
                "Enhance surgical safety": {
                    "Surgical checklist compliance": "(Compliant surgeries / Total surgeries) * 100",
                    "Wrong-site surgery prevention": "(Prevented incidents / Total surgeries) * 100",
                    "Anesthesia safety improvement": "((Previous safety - Current safety) / Previous safety) * 100",
                    "Post-operative monitoring adequacy": "(Adequate monitoring / Total surgeries) * 100"
                },
                "Strengthen patient identification": {
                    "Correct identification rate": "(Correct identifications / Total identifications) * 100",
                    "Patient matching accuracy": "(Accurate matches / Total matches) * 100",
                    "Identification error reduction": "((Previous errors - Current errors) / Previous errors) * 100",
                    "Biometric verification usage": "(Verified patients / Total patients) * 100"
                },
                "Advance fall prevention": {
                    "Fall risk assessment rate": "(Assessed patients / Total patients) * 100",
                    "Fall incidence reduction": "((Previous falls - Current falls) / Previous falls) * 100",
                    "Prevention protocol adherence": "(Adherent units / Total units) * 100",
                    "Fall-related injury reduction": "((Previous injuries - Current injuries) / Previous injuries) * 100"
                },
                "Improve diagnostic accuracy": {
                    "Diagnostic error reduction": "((Previous errors - Current errors) / Previous errors) * 100",
                    "Test interpretation accuracy": "(Accurate interpretations / Total tests) * 100",
                    "Radiology reading accuracy": "(Accurate readings / Total readings) * 100",
                    "Pathology report accuracy": "(Accurate reports / Total reports) * 100"
                }
            },
            "Health / Patient Experience & Engagement": {
                "Enhance patient satisfaction": {
                    "Overall satisfaction rate": "(Satisfied patients / Total patients) * 100",
                    "Care experience improvement": "((Current rating - Previous rating) / Previous rating) * 100",
                    "Recommendation likelihood": "(Likely to recommend / Total surveyed) * 100",
                    "Service excellence recognition": "(Excellent ratings / Total ratings) * 100"
                },
                "Improve care coordination": {
                    "Care transition success": "(Successful transitions / Total transitions) * 100",
                    "Information sharing completeness": "(Complete sharing / Total required) * 100",
                    "Provider communication effectiveness": "(Effective communications / Total communications) * 100",
                    "Appointment coordination efficiency": "(Efficient coordination / Total appointments) * 100"
                },
                "Advance patient communication": {
                    "Health information understanding": "(Understanding patients / Total patients) * 100",
                    "Treatment explanation adequacy": "(Adequate explanations / Total treatments) * 100",
                    "Informed consent quality": "(Quality consents / Total consents) * 100",
                    "Language access availability": "(Available interpretation / Total needed) * 100"
                },
                "Strengthen patient empowerment": {
                    "Shared decision-making rate": "(Shared decisions / Total decisions) * 100",
                    "Self-management capability": "(Capable patients / Total patients) * 100",
                    "Health literacy improvement": "(Improved literacy / Total patients) * 100",
                    "Patient activation level": "(Activated patients / Total patients) * 100"
                },
                "Optimize wait time experience": {
                    "Wait time satisfaction": "(Satisfied with wait times / Total patients) * 100",
                    "Appointment punctuality": "(On-time appointments / Total appointments) * 100",
                    "Service delay reduction": "((Previous delays - Current delays) / Previous delays) * 100",
                    "Wait time communication effectiveness": "(Effective communications / Total waits) * 100"
                },
                "Enhance compassionate care": {
                    "Dignity and respect perception": "(Treated with dignity / Total patients) * 100",
                    "Emotional support adequacy": "(Adequately supported / Total patients) * 100",
                    "Cultural sensitivity rating": "(Culturally sensitive care / Total encounters) * 100",
                    "Privacy protection satisfaction": "(Satisfied with privacy / Total patients) * 100"
                }
            },
            "Health / Health Equity & Inclusion": {
                "Reduce health disparities": {
                    "Disparity reduction progress": "((Previous disparity - Current disparity) / Previous disparity) * 100",
                    "Equitable outcome achievement": "(Equitable outcomes / Total outcomes) * 100",
                    "Access equity improvement": "((Current equity - Previous equity) / Previous equity) * 100",
                    "Service distribution fairness": "(Fair distribution / Total services) * 100"
                },
                "Advance culturally competent care": {
                    "Cultural competence training completion": "(Trained staff / Total staff) * 100",
                    "Culturally appropriate service rate": "(Appropriate services / Total services) * 100",
                    "Language service availability": "(Available services / Total needed) * 100",
                    "Diverse patient satisfaction": "(Satisfied diverse patients / Total diverse) * 100"
                },
                "Improve vulnerable population access": {
                    "Vulnerable group coverage": "(Covered vulnerable / Total vulnerable) * 100",
                    "Barrier reduction achievement": "((Previous barriers - Current barriers) / Previous barriers) * 100",
                    "Targeted outreach effectiveness": "(Effective outreach / Total outreach) * 100",
                    "Inclusive service design": "(Inclusive services / Total services) * 100"
                },
                "Address social determinants of health": {
                    "SDOH screening rate": "(Screened patients / Total patients) * 100",
                    "Social need intervention": "(Addressed needs / Total identified) * 100",
                    "Community resource connection": "(Connected patients / Total needing) * 100",
                    "Cross-sector collaboration effectiveness": "(Effective collaborations / Total collaborations) * 100"
                },
                "Promote gender-sensitive care": {
                    "Gender-specific service availability": "(Available services / Total needed) * 100",
                    "Gender-based discrimination reduction": "((Previous incidents - Current incidents) / Previous incidents) * 100",
                    "Women's health service access": "(Accessible services / Total women) * 100",
                    "Gender equity in outcomes": "(Equitable outcomes / Total outcomes) * 100"
                },
                "Enhance disability inclusion": {
                    "Accessible facility rate": "(Accessible facilities / Total facilities) * 100",
                    "Disability accommodation provision": "(Provided accommodations / Total needed) * 100",
                    "Disability competency training": "(Trained staff / Total staff) * 100",
                    "Disabled patient satisfaction": "(Satisfied disabled patients / Total disabled) * 100"
                }
            },
            "Health / Healthcare Innovation & Technology": {
                "Advance digital health adoption": {
                    "EHR implementation rate": "(Implemented EHR / Total facilities) * 100",
                    "Telehealth service expansion": "((Current services - Previous services) / Previous services) * 100",
                    "Mobile health app utilization": "(Utilizing patients / Total eligible) * 100",
                    "Digital prescription adoption": "(Digital prescriptions / Total prescriptions) * 100"
                },
                "Improve health data analytics": {
                    "Data-driven decision making": "(Data-informed decisions / Total decisions) * 100",
                    "Predictive analytics utilization": "(Utilized analytics / Total opportunities) * 100",
                    "Clinical decision support usage": "(Used support tools / Total encounters) * 100",
                    "Population health management effectiveness": "(Effective management / Total populations) * 100"
                },
                "Enhance interoperability": {
                    "Health information exchange participation": "(Participating organizations / Total organizations) * 100",
                    "Data sharing capability": "(Shareable data / Total data) * 100",
                    "System integration success": "(Integrated systems / Total systems) * 100",
                    "Standardized data adoption": "(Adopted standards / Total standards) * 100"
                },
                "Promote clinical innovation": {
                    "New technology adoption rate": "(Adopted technologies / Total available) * 100",
                    "Clinical research participation": "(Participating patients / Total eligible) * 100",
                    "Innovation implementation success": "(Successful implementations / Total innovations) * 100",
                    "Evidence-based practice adoption": "(Adopted practices / Total recommended) * 100"
                },
                "Strengthen cybersecurity": {
                    "Security protocol compliance": "(Compliant systems / Total systems) * 100",
                    "Data breach prevention": "(Prevented breaches / Total attempts) * 100",
                    "Privacy protection effectiveness": "(Protected records / Total records) * 100",
                    "Security training completion": "(Trained staff / Total staff) * 100"
                },
                "Advance remote care technologies": {
                    "Remote monitoring implementation": "(Implemented monitoring / Total eligible) * 100",
                    "Virtual care effectiveness": "(Effective virtual visits / Total virtual visits) * 100",
                    "Wearable technology integration": "(Integrated wearables / Total available) * 100",
                    "Home health technology adoption": "(Adopting patients / Total eligible) * 100"
                }
            },
            "Health / Healthcare System Performance": {
                "Optimize resource utilization": {
                    "Bed occupancy optimization": "(Optimal occupancy / Total capacity) * 100",
                    "Staff productivity improvement": "((Current productivity - Previous) / Previous) * 100",
                    "Equipment utilization efficiency": "(Efficient utilization / Total capacity) * 100",
                    "Supply chain cost reduction": "((Previous costs - Current costs) / Previous costs) * 100"
                },
                "Improve operational efficiency": {
                    "Patient flow optimization": "(Optimized flow / Total patient journeys) * 100",
                    "Process standardization rate": "(Standardized processes / Total processes) * 100",
                    "Administrative cost reduction": "((Previous admin costs - Current) / Previous) * 100",
                    "Service delivery efficiency": "(Efficient deliveries / Total services) * 100"
                },
                "Enhance financial sustainability": {
                    "Cost-effectiveness improvement": "((Current effectiveness - Previous) / Previous) * 100",
                    "Revenue cycle optimization": "(Optimized cycles / Total cycles) * 100",
                    "Resource allocation efficiency": "(Efficient allocation / Total resources) * 100",
                    "Financial performance improvement": "((Current performance - Previous) / Previous) * 100"
                },
                "Strengthen workforce development": {
                    "Staff retention improvement": "((Current retention - Previous) / Previous) * 100",
                    "Training effectiveness rate": "(Effective training / Total training) * 100",
                    "Workforce satisfaction improvement": "((Current satisfaction - Previous) / Previous) * 100",
                    "Skill mix optimization": "(Optimized skill mix / Total opportunities) * 100"
                },
                "Advance quality improvement": {
                    "QI project success rate": "(Successful projects / Total projects) * 100",
                    "Benchmark achievement rate": "(Achieved benchmarks / Total benchmarks) * 100",
                    "Process improvement sustainability": "(Sustained improvements / Total improvements) * 100",
                    "Best practice implementation": "(Implemented practices / Total identified) * 100"
                },
                "Build organizational resilience": {
                    "Business continuity readiness": "(Ready systems / Total systems) * 100",
                    "Crisis response effectiveness": "(Effective responses / Total crises) * 100",
                    "Change management success": "(Successful changes / Total changes) * 100",
                    "Adaptive capacity improvement": "((Current capacity - Previous) / Previous) * 100"
                }
            },

            # health end
        }
