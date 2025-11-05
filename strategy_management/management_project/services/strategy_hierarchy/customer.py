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

            "Community Engagement & Development": {
                "Strengthen Community Outreach and Participation": {
                    "Local Partnership Activation": "(Active community partnerships / Total potential partnerships) * 100",
                    "Community Program Engagement Growth": "((Current participants - Previous participants) / Previous participants) * 100",
                    "Local Brand Recognition": "Survey score measuring brand/service awareness in communities",
                    "Underserved Market Penetration": "(Services delivered to underserved areas / Total service areas) * 100"
                },
                "Build Community Member Loyalty": {
                    "Community Member Retention Rate": "(Retained active members / Total members) * 100",
                    "Consistent Community Participation": "(Regularly active members / Total members) * 100",
                    "Community Leadership Development": "(Emerging community leaders / Total active members) * 100",
                    "Perceived Community Value": "Survey score measuring value derived from community membership"
                },
                "Enhance Community Support Experience": {
                    "Community Support Satisfaction": "(Sum of community support ratings / Number of respondents) * 100",
                    "Peer Support Resolution Rate": "(Community-resolved issues / Total community support requests) * 100",
                    "Community Response Timeliness": "Average response time for community inquiries",
                    "Community Support Value Perception": "Survey score measuring value of community support resources"
                },
                "Leverage Community Value Generation": {
                    "Community Content Value Contribution": "Total value from community-generated content",
                    "Community Innovation Implementation": "(Implemented community ideas / Total ideas submitted) * 100",
                    "Community Support Cost Efficiency": "Reduction in formal support costs from community support",
                    "Community-driven Enhancement Rate": "(Community-inspired improvements / Total improvements) * 100"
                },
                "Strengthen Community Dialogue and Engagement": {
                    "Community Engagement Participation": "(Active engaged members / Total members) * 100",
                    "Community Meeting Effectiveness": "Score measuring impact of community meetings",
                    "Community Feedback Implementation": "(Implemented community feedback / Total feedback) * 100",
                    "Community Information Quality": "Survey score measuring usefulness of shared information"
                },
                "Cultivate Community Trust and Cohesion": {
                    "Community Trust Level": "Survey score measuring inter-member trust",
                    "Institutional Trust in Community": "Score measuring trust in community institutions",
                    "Community Conflict Resolution": "Score measuring effectiveness in resolving disputes",
                    "Social Capital Development Progress": "Score measuring growth of community networks"
                },
                "Develop Community Intelligence Capability": {
                    "Community Sentiment Analysis Accuracy": "(Accurate sentiment assessments / Total analyses) * 100",
                    "Real-time Community Monitoring Coverage": "Percentage of time with active community monitoring",
                    "Community Trend Prediction": "(Accurate trend predictions / Total predictions) * 100",
                    "Community Issue Early Detection": "(Early-detected issues / Total issues) * 100"
                }
            },

            "Citizen Services & Public Value": {
                "Expand Citizen Service Adoption": {
                    "Digital Service Registration Growth": "((Current registrations - Previous registrations) / Previous registrations) * 100",
                    "Multi-service Usage Rate": "(Citizens using multiple services / Total service users) * 100",
                    "Service Onboarding Completion": "(Completed onboarding journeys / Total new registrations) * 100",
                    "Service Awareness Penetration": "(Aware citizens / Total target population) * 100"
                },
                "Increase Citizen Service Loyalty": {
                    "Service Renewal and Continuation": "(Renewed services / Total services due for renewal) * 100",
                    "Long-term Citizen Engagement": "(Citizens engaged beyond 12 months / Total citizens) * 100",
                    "Service Upgrade Adoption": "(Citizens upgrading services / Total eligible citizens) * 100",
                    "Citizen Referral and Advocacy": "(Citizen referrals / Total engaged citizens) * 100"
                },
                "Improve Citizen Service Experience": {
                    "Citizen Service Satisfaction": "(Sum of citizen satisfaction ratings / Number of respondents) * 100",
                    "Service Request Resolution Time": "Average time to resolve citizen service requests",
                    "Service Accessibility Rating": "Survey score measuring ease of accessing services",
                    "Citizen Effort Reduction": "((Previous effort score - Current score) / Previous score) * 100"
                },
                "Enhance Citizen Value Creation": {
                    "Citizen Engagement Value Growth": "((Current citizen value - Previous) / Previous) * 100",
                    "Multi-service Citizen Value": "Average value of multi-service users vs single service",
                    "Citizen Interaction Depth": "Average service interactions per citizen per period",
                    "Long-term Citizen Contribution": "Total value from long-term engaged citizens"
                },
                "Deepen Citizen Behavior Understanding": {
                    "Citizen Service Pattern Identification": "(Identified usage patterns / Total citizen segments) * 100",
                    "Citizen Need Prediction Accuracy": "(Accurate need anticipations / Total predictions) * 100",
                    "Service Adoption Forecasting": "(Accurate adoption predictions / Total forecasts) * 100",
                    "Citizen Journey Mapping Coverage": "(Mapped journey stages / Total stages) * 100"
                },
                "Enhance Citizen Communication Experience": {
                    "Citizen Communication Satisfaction": "(Sum of communication satisfaction ratings / Respondents) * 100",
                    "Government Communication Clarity": "Survey score measuring clarity of official communications",
                    "Citizen Query Response Time": "Average response time to citizen communications",
                    "Public Information Accessibility": "(Easily accessible information / Total public information) * 100"
                },
                "Strengthen Citizen Confidence in Services": {
                    "Public Service Trust Level": "Survey score measuring citizen trust in public services",
                    "Government Transparency Index": "Composite score of information accessibility and clarity",
                    "Service Reliability Perception": "Survey score measuring perceived service dependability",
                    "Accountability System Effectiveness": "Score measuring effectiveness of accountability mechanisms"
                },
                "Advance Citizen-Centric Service Innovation": {
                    "Citizen Service Innovation Rate": "(New citizen services launched / Total planned) * 100",
                    "Service Modernization Impact": "Score measuring impact of service improvements",
                    "Process Automation Effectiveness": "(Automated processes / Total automatable) * 100",
                    "Service Design Excellence": "Score measuring quality of service design and UX"
                }
            },

            "Stakeholder Partnership & Collaboration": {
                "Excel in Multi-stakeholder Engagement": {
                    "Stakeholder Engagement Coverage": "(Active stakeholders / Total identified stakeholders) * 100",
                    "Strategic Dialogue Frequency": "Average number of meaningful dialogues per quarter",
                    "Engagement Diversity and Inclusion": "Score measuring diversity of engaged stakeholders",
                    "Stakeholder Input Implementation": "(Implemented stakeholder suggestions / Total suggestions) * 100"
                },
                "Build High-Impact Strategic Partnerships": {
                    "Partnership Satisfaction Level": "(Sum of satisfaction ratings / Number of partners) * 100",
                    "Joint Value Creation Performance": "Total value generated through partnership activities",
                    "Partnership Portfolio Diversity": "Score measuring variety of partnership types",
                    "Strategic Alignment Achievement": "Score measuring goal alignment with partners"
                },
                "Strengthen Donor and Investor Relations": {
                    "Donor Retention and Loyalty": "(Retained donors / Total donors) * 100",
                    "Reporting Excellence and Compliance": "(Reports delivered on standard / Total reports) * 100",
                    "Donor Satisfaction Performance": "Survey score measuring donor satisfaction",
                    "Fund Utilization Efficiency": "(Program impact / Total administrative costs) * 100"
                },
                "Optimize Inter-organizational Coordination": {
                    "Coordination Effectiveness Score": "Survey score measuring coordination success",
                    "Joint Initiative Success Rate": "(Successful joint initiatives / Total initiatives) * 100",
                    "Information Sharing Efficiency": "Score measuring effectiveness of knowledge sharing",
                    "Resource Sharing Optimization": "Score measuring efficiency of shared resource use"
                },
                "Enhance Collaborative Governance": {
                    "Governance Structure Effectiveness": "Score measuring effectiveness of governance frameworks",
                    "Collaborative Decision-making Efficiency": "Score measuring efficiency of joint decisions",
                    "Accountability in Partnerships": "Score measuring clarity of partnership accountability",
                    "Collaborative Leadership Impact": "Score measuring effectiveness of shared leadership"
                },
                "Excel in Stakeholder Communication": {
                    "Stakeholder Communication Satisfaction": "(Sum of satisfaction ratings / Number of stakeholders) * 100",
                    "Stakeholder Meeting Impact": "Score measuring effectiveness of stakeholder meetings",
                    "Stakeholder Response Timeliness": "(Communications responded within SLA / Total) * 100",
                    "Stakeholder Information Relevance": "Survey score measuring relevance of shared information"
                },
                "Enhance Stakeholder Trust and Confidence": {
                    "Stakeholder Trust Index": "Composite trust score from stakeholder surveys",
                    "Relationship Longevity and Strength": "Average duration and depth of stakeholder relationships",
                    "Collaboration Confidence Level": "Survey score measuring confidence in joint work",
                    "Transparency Perception Among Stakeholders": "Score measuring stakeholder view of organizational transparency"
                },
                "Strengthen Stakeholder Intelligence": {
                    "Stakeholder Data Completeness": "(Complete stakeholder profiles / Total stakeholders) * 100",
                    "Stakeholder Influence Mapping Accuracy": "(Accurate influence assessments / Total mappings) * 100",
                    "Stakeholder Need Prediction": "(Accurate need predictions / Total predictions) * 100",
                    "Stakeholder Network Analysis Depth": "Average connection levels mapped per stakeholder"
                }
            },

            "Product & Service Quality": {
                "Enhance product quality standards": {
                    "Product defect rate reduction": "((Previous defect rate - Current defect rate) / Previous defect rate) * 100",
                    "Quality compliance rate": "(Products meeting quality standards / Total products) * 100",
                    "Customer-reported quality issues": "Number of quality-related complaints per 1,000 customers",
                    "Product return rate reduction": "((Previous return rate - Current return rate) / Previous return rate) * 100"
                },
                "Improve service reliability": {
                    "Service uptime percentage": "(Uptime hours / Total operational hours) * 100",
                    "On-time delivery performance": "(Deliveries made on time / Total deliveries) * 100",
                    "Service consistency score": "Standard deviation of service performance metrics",
                    "Performance standard achievement rate": "(Performance standards met / Total standards) * 100"
                },
                "Strengthen quality assurance processes": {
                    "Quality audit pass rate": "(Passed quality audits / Total audits conducted) * 100",
                    "Preventive quality measure implementation": "(Implemented preventive measures / Total identified needs) * 100",
                    "Supplier quality compliance": "(Suppliers meeting quality standards / Total suppliers) * 100",
                    "Continuous improvement implementation rate": "(Quality improvements implemented / Total identified) * 100"
                }
            },
            "Customer Value & Profitability": {
                "Increase revenue per customer": {
                    "Average revenue per user growth": "((Current ARPU - Previous ARPU) / Previous ARPU) * 100",
                    "Customer profitability improvement": "((Current profit per customer - Previous) / Previous) * 100",
                    "Upsell conversion rate": "(Successful upsell transactions / Eligible customers) * 100",
                    "Cross-sell revenue growth": "((Current cross-sell revenue - Previous) / Previous) * 100"
                },
                "Optimize customer service costs": {
                    "Cost per service request reduction": "((Previous cost per request - Current cost) / Previous cost) * 100",
                    "Support cost per customer improvement": "((Previous support cost - Current cost) / Previous cost) * 100",
                    "Process efficiency savings": "Total cost savings from process improvements",
                    "Self-service cost reduction impact": "((Previous support costs - Current costs) / Previous costs) * 100"
                },
                "Enhance customer lifetime value": {
                    "CLV growth rate": "((Current CLV - Previous CLV) / Previous CLV) * 100",
                    "Customer value segmentation effectiveness": "(Revenue from targeted segments / Total revenue) * 100",
                    "High-value customer retention": "(Retained high-value customers / Total high-value customers) * 100",
                    "Customer investment return ratio": "(Customer-generated profit / Total customer investment) * 100"
                }
            },
            "Brand Awareness & Reputation": {
                "Increase brand recognition": {
                    "Brand awareness score improvement": "((Current awareness score - Previous score) / Previous score) * 100",
                    "Social media reach growth": "((Current reach - Previous reach) / Previous reach) * 100",
                    "Website traffic growth rate": "((Current visitors - Previous visitors) / Previous visitors) * 100",
                    "Brand recall accuracy": "(Correct brand identification / Total survey respondents) * 100"
                },
                "Build brand trust and reputation": {
                    "Net Promoter Score improvement": "Current NPS - Previous NPS",
                    "Positive media mention growth": "((Current positive mentions - Previous) / Previous) * 100",
                    "Industry award recognition": "Number of industry awards and certifications received",
                    "Brand trust index score": "Composite score from brand trust surveys"
                },
                "Strengthen brand positioning": {
                    "Competitive brand preference": "(Customers preferring brand over competitors / Total surveyed) * 100",
                    "Brand association strength": "Score measuring strength of desired brand associations",
                    "Market leadership perception": "Survey score measuring perception as market leader",
                    "Brand differentiation recognition": "(Customers recognizing unique value / Total surveyed) * 100"
                }
            },
            "Innovation & Customer Solutions": {
                "Accelerate new product development": {
                    "New product launch rate": "(New products launched / Total planned launches) * 100",
                    "Revenue from new products": "Percentage of total revenue from products launched in last 24 months",
                    "New product adoption rate": "(Customers adopting new products / Total target customers) * 100",
                    "Time-to-market improvement": "((Previous development time - Current time) / Previous time) * 100"
                },
                "Enhance solution customization": {
                    "Customized solution rate": "(Customized products/services delivered / Total deliveries) * 100",
                    "Customer satisfaction with tailored solutions": "Satisfaction score for customized offerings",
                    "Strategic customer retention through customization": "(Retained strategic customers / Total strategic customers) * 100",
                    "Customization implementation efficiency": "(Successfully implemented customizations / Total requests) * 100"
                },
                "Foster customer-driven innovation": {
                    "Customer idea implementation rate": "(Implemented customer suggestions / Total suggestions) * 100",
                    "Co-creation project success": "(Successful co-creation projects / Total projects) * 100",
                    "Innovation adoption speed": "Average time from ideation to customer adoption",
                    "Customer feedback in R&D": "(R&D decisions influenced by customer input / Total decisions) * 100"
                }
            },
            "Customer Feedback & Insights": {
                "Enhance feedback collection": {
                    "Survey response rate improvement": "((Current response rate - Previous rate) / Previous rate) * 100",
                    "Feedback channel utilization": "(Active feedback channels / Total available channels) * 100",
                    "Customer feedback volume growth": "((Current feedback volume - Previous) / Previous) * 100",
                    "Diverse feedback source coverage": "(Different customer segments providing feedback / Total segments) * 100"
                },
                "Improve insight implementation": {
                    "Actionable insight implementation rate": "(Implemented insights / Total insights generated) * 100",
                    "Product improvement from feedback": "(Improvements from customer feedback / Total improvements) * 100",
                    "Repeat complaint reduction": "((Previous repeat complaints - Current) / Previous) * 100",
                    "Customer perception of being heard": "Survey score on customer feeling heard and valued"
                },
                "Strengthen data-driven decision making": {
                    "Customer data accuracy rate": "(Accurate customer data points / Total data points) * 100",
                    "Analytics-driven improvements": "(Decisions using customer analytics / Total decisions) * 100",
                    "Customer insight ROI": "((Value from insights - Collection cost) / Collection cost) * 100",
                    "Real-time insight availability": "(Real-time insights available / Total needed insights) * 100"
                }
            },
            "Accessibility & Convenience": {
                "Improve service availability": {
                    "Product availability rate": "(Available products / Total product portfolio) * 100",
                    "Service coverage expansion": "((Current coverage - Previous coverage) / Previous coverage) * 100",
                    "Online accessibility uptime": "(Platform uptime hours / Total hours) * 100",
                    "Distribution network reach": "(Population covered / Total target population) * 100"
                },
                "Enhance customer convenience": {
                    "Ease-of-purchase score improvement": "((Current score - Previous score) / Previous score) * 100",
                    "Average transaction time reduction": "((Previous time - Current time) / Previous time) * 100",
                    "Multi-channel access rate": "(Customers using multiple channels / Total customers) * 100",
                    "24/7 service availability": "(Hours with full service / Total hours) * 100"
                },
                "Optimize physical and digital access": {
                    "Location accessibility score": "Score measuring physical location convenience",
                    "Digital platform accessibility": "(Platforms meeting accessibility standards / Total platforms) * 100",
                    "Mobile access performance": "Score measuring mobile platform effectiveness",
                    "Offline service capability": "(Services available offline / Total services) * 100"
                }
            },
            "Customer Engagement & Communication": {
                "Enhance communication effectiveness": {
                    "Response time improvement": "((Previous response time - Current time) / Previous time) * 100",
                    "Communication open rate growth": "((Current open rate - Previous rate) / Previous rate) * 100",
                    "Social media engagement rate": "(Total engagements / Total followers) * 100",
                    "Message clarity score": "Survey score measuring communication clarity"
                },
                "Increase customer engagement": {
                    "Event participation growth": "((Current participants - Previous participants) / Previous participants) * 100",
                    "Digital platform activity rate": "(Active platform users / Total users) * 100",
                    "Community interaction frequency": "Average interactions per user per period",
                    "Engagement depth score": "Composite score measuring engagement quality"
                },
                "Strengthen proactive communication": {
                    "Proactive outreach effectiveness": "(Positive responses to outreach / Total outreach) * 100",
                    "Educational content engagement": "(Customers using educational resources / Total customers) * 100",
                    "Personalized communication rate": "(Personalized communications / Total communications) * 100",
                    "Multi-language communication coverage": "(Languages supported / Total required languages) * 100"
                }
            },
            "Customer Support & Service": {
                "Improve support service quality": {
                    "First-contact resolution rate": "(Issues resolved initially / Total issues) * 100",
                    "Average resolution time reduction": "((Previous resolution time - Current time) / Previous time) * 100",
                    "Support satisfaction score": "Average satisfaction rating for support interactions",
                    "Support quality consistency": "Standard deviation of support quality scores"
                },
                "Enhance proactive service": {
                    "Proactive service implementation rate": "(Proactive services delivered / Total opportunities) * 100",
                    "Issues prevented through proactive measures": "Number of potential issues prevented",
                    "Customer satisfaction with proactive support": "Satisfaction score for proactive service interactions",
                    "Repeat service request reduction": "((Previous repeat requests - Current) / Previous) * 100"
                },
                "Optimize support channel efficiency": {
                    "Self-service adoption rate": "(Self-service completions / Total service requests) * 100",
                    "Support channel satisfaction": "Satisfaction score by support channel",
                    "Support cost efficiency": "((Previous support costs - Current costs) / Previous costs) * 100",
                    "Multi-channel support integration": "Score measuring seamless cross-channel support"
                }
            },
            "Trust, Compliance & Safety": {
                "Ensure regulatory compliance": {
                    "Compliance audit success rate": "(Successful compliance audits / Total audits) * 100",
                    "Compliance violation reduction": "((Previous violations - Current violations) / Previous violations) * 100",
                    "Regulatory training completion": "(Staff completing compliance training / Total staff) * 100",
                    "Compliance documentation accuracy": "(Accurate compliance documents / Total documents) * 100"
                },
                "Enhance safety and security": {
                    "Security incident reduction": "((Previous incidents - Current incidents) / Previous incidents) * 100",
                    "Safety compliance rate": "(Safety standards met / Total standards) * 100",
                    "Customer security satisfaction": "Survey score measuring perception of security",
                    "Data protection compliance": "(Data protection requirements met / Total requirements) * 100"
                },
                "Build customer trust": {
                    "Trust index score improvement": "((Current trust score - Previous score) / Previous score) * 100",
                    "Transparency perception score": "Survey score measuring perceived transparency",
                    "Ethical compliance rate": "(Ethical standards met / Total standards) * 100",
                    "Customer confidence index": "Composite score measuring customer confidence"
                }
            },
            "Digital & Online Experience": {
                "Enhance digital platform engagement": {
                    "Website usability score improvement": "((Current score - Previous score) / Previous score) * 100",
                    "Online transaction success rate": "(Successful transactions / Total transactions) * 100",
                    "Mobile app adoption growth": "((Current app users - Previous users) / Previous users) * 100",
                    "Digital platform satisfaction": "Average satisfaction score for digital platforms"
                },
                "Improve online self-service capabilities": {
                    "Self-service completion rate": "(Completed self-service requests / Total attempts) * 100",
                    "Support call reduction from self-service": "((Previous support calls - Current calls) / Previous calls) * 100",
                    "Digital tool satisfaction": "Satisfaction score with self-service tools",
                    "Online knowledge base utilization": "(Knowledge base accesses / Total support requests) * 100"
                },
                "Optimize digital customer journey": {
                    "Digital journey completion rate": "(Completed digital journeys / Total started) * 100",
                    "Online conversion rate improvement": "((Current conversion rate - Previous rate) / Previous rate) * 100",
                    "Digital experience consistency": "Score measuring consistent experience across digital touchpoints",
                    "Mobile experience quality": "Score measuring quality of mobile customer experience"
                }
            },
            "Pricing & Value Perception": {
                "Optimize price-value perception": {
                    "Price competitiveness index": "Score measuring competitive pricing position",
                    "Value perception score improvement": "((Current score - Previous score) / Previous score) * 100",
                    "Price sensitivity analysis accuracy": "(Accurate price sensitivity predictions / Total predictions) * 100",
                    "Customer willingness to pay": "Survey score measuring perceived value for price"
                },
                "Ensure pricing transparency and fairness": {
                    "Pricing complaint reduction": "((Previous pricing complaints - Current) / Previous) * 100",
                    "Discount program effectiveness": "(Successful discount redemptions / Total offers) * 100",
                    "Pricing transparency score": "Survey score measuring pricing clarity",
                    "Retention impact from pricing strategies": "((Retention with pricing strategy - Baseline) / Baseline) * 100"
                },
                "Enhance pricing strategy effectiveness": {
                    "Revenue optimization from pricing": "((Current revenue - Previous revenue) / Previous revenue) * 100",
                    "Customer segment pricing effectiveness": "(Revenue from segmented pricing / Total revenue) * 100",
                    "Dynamic pricing accuracy": "(Optimal pricing decisions / Total pricing decisions) * 100",
                    "Pricing model adoption rate": "(Customers on optimal pricing models / Total customers) * 100"
                }
            },
            "Strategic Partnerships & Alliances": {
                "Enhance customer co-creation partnerships": {
                    "Joint initiative success rate": "(Successful joint initiatives / Total initiatives) * 100",
                    "Partnership revenue growth": "((Current partnership revenue - Previous) / Previous) * 100",
                    "Customer satisfaction with partnerships": "Satisfaction score for partnership outcomes",
                    "Co-creation project completion": "(Completed co-creation projects / Total projects) * 100"
                },
                "Leverage strategic alliances for value creation": {
                    "Partner contribution to sales": "(Revenue from partner channels / Total revenue) * 100",
                    "New solutions via partnerships": "Number of new solutions developed through alliances",
                    "Co-created product retention": "(Retained customers using co-created products / Total users) * 100",
                    "Partnership value realization": "(Achieved partnership objectives / Total objectives) * 100"
                },
                "Strengthen alliance management": {
                    "Partner satisfaction score": "Average satisfaction rating from partners",
                    "Alliance performance improvement": "((Current performance - Previous) / Previous) * 100",
                    "Strategic alignment score": "Score measuring goal alignment with partners",
                    "Partnership innovation rate": "(Innovations from partnerships / Total innovations) * 100"
                }
            },

            #
            # agriculture start
            # Agriculture - NGO & Development Context
            # Area 1: Enhance Smallholder Farmer Resilience
            "Agriculture / Smallholder Farmer Resilience": {
                "Diversify Farmer Income": {
                    "% of farmers with multiple income sources": "(Farmers with multiple income sources / Total farmers) * 100",
                    "Average number of income streams per farmer": "Total income streams / Number of farmers",
                    "Growth rate of diversified farmer income": "((Current diversified income - Previous diversified income) / Previous diversified income) * 100",
                    "% of farmers moving above the poverty threshold": "(Farmers above poverty threshold / Total farmers) * 100"
                },
                "Strengthen Climate Resilience": {
                    "Climate resilience capacity index": "Composite score based on adaptive capacity metrics",
                    "% of farmers adopting climate-smart practices": "(Farmers adopting climate-smart practices / Total farmers) * 100",
                    "Reduction in crop losses due to climatic events": "((Previous crop losses - Current crop losses) / Previous crop losses) * 100",
                    "% of farmers accessing climate advisory services": "(Farmers accessing climate services / Total farmers) * 100"
                },
                "Improve Food Security": {
                    "Change in household food security index": "Current food security index - Previous food security index",
                    "% of households meeting minimum dietary requirements": "(Households meeting dietary requirements / Total households) * 100",
                    "Reduction in seasonal hunger periods": "Previous hunger periods - Current hunger periods",
                    "Crop yield stability index": "Standard deviation of crop yields over time"
                },
                "Reduce Recovery Time After Shocks": {
                    "Average recovery duration following climatic or economic shocks": "Total recovery days / Number of shock events",
                    "% of farmers regaining pre-shock income levels": "(Farmers regaining pre-shock income / Total affected farmers) * 100",
                    "Reduction in livestock mortality post-shock": "((Previous mortality - Current mortality) / Previous mortality) * 100",
                    "% of affected farmers receiving timely support": "(Farmers receiving timely support / Total affected farmers) * 100"
                }
            },

            # Area 2: Improve Access to Agricultural Inputs
            "Agriculture / Input Access": {
                "Ensure Seed Availability": {
                    "% of farmers accessing certified seeds": "(Farmers accessing certified seeds / Total farmers) * 100",
                    "Average lead time for seed delivery": "Total delivery days / Number of seed deliveries",
                    "% of farmers satisfied with seed quality": "(Satisfied farmers / Total farmers surveyed) * 100",
                    "Seed subsidy utilization rate": "(Subsidized seeds distributed / Total subsidized seeds available) * 100"
                },
                "Enhance Fertilizer Accessibility": {
                    "% of farmers with access to fertilizers": "(Farmers with fertilizer access / Total farmers) * 100",
                    "Average fertilizer cost per farmer": "Total fertilizer cost / Number of farmers",
                    "Reduction in fertilizer shortages": "((Previous shortage incidents - Current incidents) / Previous incidents) * 100",
                    "% of farmers applying recommended fertilizer doses": "(Farmers applying recommended doses / Total farmers) * 100"
                },
                "Promote Machinery Access": {
                    "% of farmers utilizing improved machinery": "(Farmers using improved machinery / Total farmers) * 100",
                    "Average farm equipment per farmer": "Total equipment units / Number of farmers",
                    "% reduction in labor time through mechanization": "((Previous labor hours - Current labor hours) / Previous labor hours) * 100",
                    "% of farmers accessing machinery financing": "(Farmers with machinery financing / Total farmers) * 100"
                },
                "Facilitate Subsidized Input Access for Vulnerable Farmers": {
                    "% of vulnerable farmers receiving subsidies": "(Vulnerable farmers receiving subsidies / Total vulnerable farmers) * 100",
                    "% of total input cost covered by subsidy": "(Subsidy amount / Total input cost) * 100",
                    "% of farmers reporting productivity improvement": "(Farmers reporting improvement / Total subsidized farmers) * 100",
                    "Timeliness of subsidy delivery": "(Subsidies delivered on time / Total subsidies) * 100"
                }
            },

            # Area 3: Enhance Knowledge & Advisory Services
            "Agriculture / Knowledge & Advisory Services": {
                "Increase Training Participation": {
                    "% of farmers attending training sessions": "(Farmers attending training / Total farmers) * 100",
                    "Number of training sessions per farmer": "Total training sessions / Number of farmers",
                    "% of trained farmers implementing recommended practices": "(Farmers implementing practices / Total trained farmers) * 100",
                    "Training satisfaction index": "Average satisfaction score from training evaluations"
                },
                "Expand Extension Service Coverage": {
                    "Average number of extension visits per farmer": "Total extension visits / Number of farmers",
                    "% of farmers receiving advisory services": "(Farmers receiving services / Total farmers) * 100",
                    "Satisfaction with extension support": "Average satisfaction score from farmer surveys",
                    "% of farm problems addressed through extension services": "(Problems addressed / Total problems reported) * 100"
                },
                "Improve Adoption of Recommended Practices": {
                    "% of farmers implementing recommended practices": "(Farmers implementing practices / Total farmers) * 100",
                    "Average yield increase from adoption": "Yield from adopters - Yield from non-adopters",
                    "Reduction in pest and disease incidents": "((Previous incidents - Current incidents) / Previous incidents) * 100",
                    "% increase in farm profitability due to adoption": "((Current profit - Previous profit) / Previous profit) * 100"
                },
                "Enhance Access to Agronomy Consultation": {
                    "% of farmers consulting experts annually": "(Farmers consulting experts / Total farmers) * 100",
                    "Average response time for advisory support": "Total response time / Number of consultations",
                    "% of recommendations implemented": "(Recommendations implemented / Total recommendations) * 100",
                    "Satisfaction with consultation quality": "Average satisfaction score from consultation feedback"
                }
            },

            # Area 4: Increase Market Access & Sales
            "Agriculture / Market Access & Sales": {
                "Expand Market Linkages": {
                    "% of farmers connected to formal markets": "(Farmers in formal markets / Total farmers) * 100",
                    "Average number of buyers per farmer": "Total buyers / Number of farmers",
                    "Volume of produce sold through organized channels": "Total volume sold through organized channels",
                    "% increase in market prices received": "((Current price - Previous price) / Previous price) * 100"
                },
                "Improve Average Price Received": {
                    "Weighted average farm-gate price": "Total sales value / Total quantity sold",
                    "Price stability index": "1 - (Standard deviation of prices / Average price)",
                    "% of farmers achieving minimum guaranteed prices": "(Farmers achieving guaranteed prices / Total farmers) * 100",
                    "% increase in prices compared to previous season": "((Current season price - Previous season price) / Previous season price) * 100"
                },
                "Increase Revenue per Farmer": {
                    "% growth in farmer revenue": "((Current revenue - Previous revenue) / Previous revenue) * 100",
                    "% of farmers achieving target revenue": "(Farmers achieving target revenue / Total farmers) * 100",
                    "Revenue contribution from diversified crops": "(Revenue from diversified crops / Total revenue) * 100",
                    "% of revenue from value-added products": "(Revenue from value-added products / Total revenue) * 100"
                },
                "Facilitate Access to Development/Fair-Trade Programs": {
                    "% of farmers enrolled in programs": "(Farmers enrolled / Total eligible farmers) * 100",
                    "Number of certifications obtained": "Total certifications achieved",
                    "% increase in sales through program channels": "((Current program sales - Previous program sales) / Previous program sales) * 100",
                    "Satisfaction with program support": "Average satisfaction score from program participants"
                }
            },

            # Area 5: Strengthen Cooperatives & Producer Organizations
            "Agriculture / Cooperatives & Producer Organizations": {
                "Grow Membership": {
                    "% increase in cooperative membership": "((Current members - Previous members) / Previous members) * 100",
                    "Retention rate of members": "(Retained members / Total members) * 100",
                    "Satisfaction of new members": "Average satisfaction score from new member surveys",
                    "Number of active members per cooperative": "Total active members / Number of cooperatives"
                },
                "Improve Cooperative Satisfaction": {
                    "Average satisfaction survey score": "Sum of satisfaction scores / Number of respondents",
                    "% of members benefiting from cooperative services": "(Members benefiting / Total members) * 100",
                    "Timeliness of service delivery": "(Services delivered on time / Total services) * 100",
                    "% of members participating in decision-making": "(Members participating in decisions / Total members) * 100"
                },
                "Expand Joint Marketing Initiatives": {
                    "Number of joint marketing initiatives per year": "Total joint marketing initiatives",
                    "% of products marketed jointly": "(Products jointly marketed / Total products) * 100",
                    "Revenue generated from joint marketing": "Total revenue from joint marketing",
                    "% increase in farmer income from joint marketing": "((Current joint marketing income - Previous) / Previous) * 100"
                },
                "Optimize Access to Shared Resources": {
                    "% of farmers using cooperative machinery or storage": "(Farmers using shared resources / Total members) * 100",
                    "Frequency of resource utilization": "Total resource uses / Number of resources",
                    "% of farmers reporting productivity improvements": "(Farmers reporting improvements / Total users) * 100",
                    "Cost savings per farmer through shared resources": "Total cost savings / Number of farmers"
                }
            },

            # Area 6: Promote Sustainable & Climate-Smart Practices
            "Agriculture / Sustainable & Climate-Smart Practices": {
                "Increase Adoption of Sustainable Practices": {
                    "% of farmers practicing sustainable agriculture": "(Farmers practicing sustainably / Total farmers) * 100",
                    "Area (hectares) under sustainable practices": "Total area under sustainable practices",
                    "% increase in soil fertility": "((Current fertility - Previous fertility) / Previous fertility) * 100",
                    "Farmer satisfaction with sustainable methods": "Average satisfaction score from farmer surveys"
                },
                "Improve Soil Health": {
                    "Soil organic matter improvement %": "((Current organic matter - Previous) / Previous) * 100",
                    "Reduction in soil erosion": "((Previous erosion - Current erosion) / Previous erosion) * 100",
                    "% of farmers practicing crop rotation": "(Farmers practicing rotation / Total farmers) * 100",
                    "Adoption of soil testing services": "(Farmers using soil testing / Total farmers) * 100"
                },
                "Reduce Chemical Input Usage": {
                    "% reduction in chemical fertilizers/pesticides": "((Previous usage - Current usage) / Previous usage) * 100",
                    "% of farmers adopting organic alternatives": "(Farmers using organic alternatives / Total farmers) * 100",
                    "Reduction in input costs": "((Previous costs - Current costs) / Previous costs) * 100",
                    "Environmental compliance score": "Average score from environmental compliance audits"
                },
                "Increase Adoption of Climate-Smart Interventions": {
                    "% of farmers using CSA techniques": "(Farmers using CSA techniques / Total farmers) * 100",
                    "Yield stability under climatic stress": "Coefficient of variation in yields during stress periods",
                    "% reduction in post-harvest loss": "((Previous losses - Current losses) / Previous losses) * 100",
                    "% of farmers accessing climate information services": "(Farmers accessing climate services / Total farmers) * 100"
                }
            },

            # Area 7: Improve Access to Finance & Credit
            "Agriculture / Finance & Credit Access": {
                "Increase Access to Loans/Credit": {
                    "% of farmers with access to loans": "(Farmers with loans / Total farmers) * 100",
                    "Average loan size": "Total loan amount / Number of loans",
                    "Loan approval rate": "(Approved loans / Total applications) * 100",
                    "% of farmers satisfied with financial services": "(Satisfied farmers / Total borrowers) * 100"
                },
                "Improve Loan Repayment Rate": {
                    "% of loans repaid on time": "(Loans repaid on time / Total loans) * 100",
                    "Reduction in default rate": "((Previous default rate - Current default rate) / Previous default rate) * 100",
                    "Average repayment period": "Total repayment days / Number of loans",
                    "Satisfaction with repayment terms": "Average satisfaction score from borrower surveys"
                },
                "Expand Microfinance/Grant Access": {
                    "% of farmers receiving grants/microloans": "(Farmers receiving grants/microloans / Total farmers) * 100",
                    "Average grant/loan per farmer": "Total grant/loan amount / Number of recipients",
                    "% of funds effectively used for farm improvement": "(Funds used for improvement / Total funds) * 100",
                    "Program satisfaction score": "Average satisfaction score from program participants"
                },
                "Increase Investment in Farm Infrastructure": {
                    "% of loan/grant funds invested in infrastructure": "(Funds invested in infrastructure / Total funds) * 100",
                    "Number of farms with new facilities": "Count of farms with new irrigation, storage facilities",
                    "% increase in productivity due to infrastructure": "((Current productivity - Previous) / Previous) * 100",
                    "Satisfaction with infrastructure improvements": "Average satisfaction score from beneficiary surveys"
                }
            },

            # Area 8: Enhance Post-Harvest Handling & Storage
            "Agriculture / Post-Harvest Handling & Storage": {
                "Reduce Post-Harvest Losses": {
                    "% reduction in post-harvest loss": "((Previous loss - Current loss) / Previous loss) * 100",
                    "% of farmers applying improved techniques": "(Farmers using improved techniques / Total farmers) * 100",
                    "Reduction in storage spoilage": "((Previous spoilage - Current spoilage) / Previous spoilage) * 100",
                    "Satisfaction with storage services": "Average satisfaction score from user surveys"
                },
                "Increase Storage Adoption": {
                    "% of farmers using improved storage": "(Farmers using improved storage / Total farmers) * 100",
                    "Storage capacity per farmer (kg)": "Total storage capacity / Number of farmers",
                    "Frequency of storage usage": "Total storage uses / Number of storage facilities",
                    "Cost savings due to storage": "Total cost savings from reduced losses"
                },
                "Expand Post-Harvest Training Coverage": {
                    "% of farmers trained in post-harvest management": "(Farmers trained / Total farmers) * 100",
                    "Average number of training sessions per farmer": "Total training sessions / Number of farmers",
                    "% of trained farmers implementing practices": "(Farmers implementing practices / Total trained) * 100",
                    "Training satisfaction index": "Average satisfaction score from training evaluations"
                },
                "Increase Cold-Chain Adoption": {
                    "% of farmers using cold storage": "(Farmers using cold storage / Total farmers) * 100",
                    "Volume of products preserved in cold storage": "Total volume in cold storage",
                    "% reduction in perishables loss": "((Previous perishable loss - Current loss) / Previous loss) * 100",
                    "Cost-benefit ratio of cold storage adoption": "Total benefits / Total costs"
                }
            },

            # Area 9: Improve Customer (Farmer) Satisfaction
            "Agriculture / Farmer Satisfaction": {
                "Increase Overall Satisfaction": {
                    "Average satisfaction survey score": "Sum of satisfaction scores / Number of respondents",
                    "% of farmers rating services as good/excellent": "(Farmers rating good/excellent / Total surveyed) * 100",
                    "% of complaints resolved timely": "(Complaints resolved on time / Total complaints) * 100",
                    "% of farmers willing to recommend services": "(Farmers willing to recommend / Total surveyed) * 100"
                },
                "Enhance Participation in Decision-Making": {
                    "% of farmers attending meetings": "(Farmers attending meetings / Total farmers) * 100",
                    "% of farmers influencing decisions": "(Farmers influencing decisions / Total farmers) * 100",
                    "Satisfaction with participation process": "Average satisfaction score from participant surveys",
                    "Number of active farmer committees": "Total active farmer committees"
                },
                "Improve Complaint Resolution": {
                    "% of complaints resolved": "(Resolved complaints / Total complaints) * 100",
                    "Average resolution time (days)": "Total resolution days / Number of complaints",
                    "Farmer satisfaction with resolution": "Average satisfaction score from complaint resolution surveys",
                    "% reduction in repeat complaints": "((Previous repeat complaints - Current) / Previous) * 100"
                },
                "Increase Loyalty & Retention": {
                    "% of repeat program participants": "(Repeat participants / Total participants) * 100",
                    "Duration of farmer engagement": "Average months of continuous participation",
                    "Renewal rate in cooperative membership": "(Renewed memberships / Total expiring memberships) * 100"
                }
            },

            # Area 10: Strengthen Nutrition & Food Security
            "Agriculture / Nutrition & Food Security": {
                "Improve Household Nutrition": {
                    "% of households meeting dietary diversity requirements": "(Households meeting requirements / Total households) * 100",
                    "% reduction in malnutrition rates": "((Previous malnutrition rate - Current rate) / Previous rate) * 100",
                    "% increase in consumption of protein-rich crops": "((Current consumption - Previous) / Previous) * 100",
                    "Household nutrition satisfaction score": "Average satisfaction score from household surveys"
                },
                "Promote Crop Diversification": {
                    "% of households cultivating multiple crop types": "(Households with multiple crops / Total households) * 100",
                    "Average number of crops per household": "Total crops cultivated / Number of households",
                    "% increase in income from diversified crops": "((Current diversified income - Previous) / Previous) * 100",
                    "Farmer satisfaction with crop variety": "Average satisfaction score from farmer surveys"
                },
                "Reduce Hunger Periods": {
                    "Number of months households experience food shortage": "Average shortage months per household",
                    "% decrease in hunger periods compared to previous year": "((Previous hunger periods - Current) / Previous) * 100",
                    "% of households maintaining food reserves": "(Households with food reserves / Total households) * 100",
                    "Participation rate in food security programs": "(Households in programs / Total eligible households) * 100"
                },
                "Increase Access to Fortified Crops": {
                    "% of households using fortified seeds": "(Households using fortified seeds / Total households) * 100",
                    "Improvement in nutritional content of household diets": "Average nutritional score improvement",
                    "% of farmers trained in fortified crop production": "(Farmers trained / Total farmers) * 100",
                    "Satisfaction with fortified crop programs": "Average satisfaction score from program participants"
                }
            },

            # Area 11: Expand Agri-Digital & Advisory Access
            "Agriculture / Agri-Digital & Advisory Access": {
                "Increase Digital Tool Adoption": {
                    "% of farmers using mobile or online agriculture tools": "(Farmers using digital tools / Total farmers) * 100",
                    "Number of digital interactions per farmer per month": "Total digital interactions / (Number of farmers * Months)",
                    "% of farmers reporting productivity improvements via digital tools": "(Farmers reporting improvements / Total digital users) * 100",
                    "Satisfaction with digital advisory platforms": "Average satisfaction score from user surveys"
                },
                "Improve Timeliness of Alerts": {
                    "% of alerts delivered on time": "(Alerts delivered on time / Total alerts) * 100",
                    "Average response time to alerts": "Total response time / Number of alerts",
                    "% of alerts acted upon successfully": "(Alerts acted upon / Total alerts) * 100",
                    "Farmer satisfaction with alert system": "Average satisfaction score from user feedback"
                },
                "Enhance Engagement with Platforms": {
                    "Average logins per farmer per month": "Total logins / (Number of farmers * Months)",
                    "% of farmers actively using advisory platforms": "(Active platform users / Total registered users) * 100",
                    "% of recommendations followed through the platform": "(Recommendations followed / Total recommendations) * 100",
                    "Satisfaction with platform usability": "Average usability satisfaction score"
                },
                "Increase Farm Management Software Usage": {
                    "% of farms using farm management software": "(Farms using software / Total farms) * 100",
                    "% of software features fully utilized": "(Features utilized / Total features) * 100",
                    "Increase in operational efficiency": "((Current efficiency - Previous efficiency) / Previous efficiency) * 100",
                    "Reduction in operational errors": "((Previous errors - Current errors) / Previous errors) * 100"
                }
            },

            # Area 12: Enhance Safety, Health & Labor Conditions
            "Agriculture / Safety, Health & Labor Conditions": {
                "Reduce Farm Accidents": {
                    "% reduction in farm-related accidents": "((Previous accidents - Current accidents) / Previous accidents) * 100",
                    "Number of reported injuries per 100 farmers": "(Total injuries / Total farmers) * 100",
                    "Severity index of accidents": "Weighted score based on accident severity levels",
                    "Satisfaction with safety measures": "Average satisfaction score from worker surveys"
                },
                "Expand Occupational Health Coverage": {
                    "% of farmers with access to health services": "(Farmers with health access / Total farmers) * 100",
                    "Number of health camps conducted annually": "Total health camps conducted",
                    "% reduction in farm-related illnesses": "((Previous illness rate - Current rate) / Previous rate) * 100",
                    "Satisfaction with health support": "Average satisfaction score from health service users"
                },
                "Improve Pesticide & Chemical Safety Compliance": {
                    "% of farmers following chemical safety guidelines": "(Farmers following guidelines / Total farmers) * 100",
                    "Reduction in chemical exposure incidents": "((Previous incidents - Current incidents) / Previous incidents) * 100",
                    "Number of trainings conducted on safe handling": "Total safety trainings conducted",
                    "Compliance rate after inspections": "(Compliant farms / Total inspected farms) * 100"
                },
                "Strengthen Labor Rights Compliance": {
                    "% of workers adhering to labor standards": "(Workers adhering to standards / Total workers) * 100",
                    "Number of labor violations reported": "Total labor violations identified",
                    "% of corrective actions implemented": "(Corrective actions implemented / Total required) * 100",
                    "Worker satisfaction with labor compliance": "Average satisfaction score from worker surveys"
                }
            },

            # Area 13: Improve Product & Service Quality
            "Agriculture / Product & Service Quality": {
                "Increase Quality Compliance": {
                    "% of products meeting quality standards": "(Products meeting standards / Total products) * 100",
                    "Number of quality audits passed": "Total successful quality audits",
                    "% of products rejected at market": "(Rejected products / Total products sold) * 100",
                    "Satisfaction with quality programs": "Average satisfaction score from program participants"
                },
                "Reduce Customer Complaints About Quality": {
                    "Number of complaints per 1,000 products": "(Total complaints / Total products) * 1000",
                    "Average resolution time per complaint": "Total resolution time / Number of complaints",
                    "% reduction in repeat complaints": "((Previous repeat complaints - Current) / Previous) * 100",
                    "Satisfaction with complaint handling": "Average satisfaction score from complainant surveys"
                },
                "Reduce Product Returns": {
                    "% reduction in returned products": "((Previous returns - Current returns) / Previous returns) * 100",
                    "% of farmers trained in quality standards": "(Farmers trained / Total farmers) * 100",
                    "% decrease in defective products": "((Previous defect rate - Current rate) / Previous rate) * 100",
                    "Satisfaction with product support services": "Average satisfaction score from user surveys"
                },
                "Enhance Traceability & Certification": {
                    "% of products with traceability": "(Traceable products / Total products) * 100",
                    "Number of certified products/farms": "Total certified products or farms",
                    "% of farmers participating in certification programs": "(Farmers in certification programs / Total farmers) * 100",
                    "Market acceptance of certified products": "(Certified products sold / Total certified products) * 100"
                }
            },

            # Area 14: Strengthen Community & Social Capital
            "Agriculture / Community & Social Capital": {
                "Increase Participation in Farmer Groups": {
                    "% of farmers in active groups": "(Farmers in active groups / Total farmers) * 100",
                    "Number of group meetings held annually": "Total group meetings conducted",
                    "% of farmers engaged in group activities": "(Farmers engaged in activities / Total group members) * 100",
                    "Satisfaction with group participation": "Average satisfaction score from member surveys"
                },
                "Implement Community-Led Projects": {
                    "Number of community projects implemented per year": "Total community projects implemented",
                    "% of community members actively involved": "(Active members / Total community members) * 100",
                    "% of projects completed on schedule": "(Projects completed on schedule / Total projects) * 100",
                    "Satisfaction with project outcomes": "Average satisfaction score from community surveys"
                },
                "Improve Collaboration & Trust": {
                    "Trust index based on survey results": "Average trust score from community surveys",
                    "% increase in cooperative initiatives": "((Current initiatives - Previous initiatives) / Previous initiatives) * 100",
                    "% of conflicts resolved amicably": "(Conflicts resolved amicably / Total conflicts) * 100",
                    "Satisfaction with collaborative processes": "Average satisfaction score from participant surveys"
                },
                "Enhance Social Cohesion": {
                    "Survey-based social cohesion score": "Average cohesion score from community surveys",
                    "Number of community events organized annually": "Total community events organized",
                    "% of farmers participating in social initiatives": "(Farmers in social initiatives / Total farmers) * 100",
                    "% increase in volunteer activities": "((Current volunteer activities - Previous) / Previous) * 100"
                }
            },

            # Area 15: Promote Gender Equity & Inclusion
            "Agriculture / Gender Equity & Inclusion": {
                "Increase Female Farmer Participation": {
                    "% of female farmers": "(Female farmers / Total farmers) * 100",
                    "% of female farmers in leadership roles": "(Female leaders / Total leadership positions) * 100",
                    "Female participation in training programs": "(Female participants / Total training participants) * 100",
                    "Satisfaction of female farmers with support services": "Average satisfaction score from female farmer surveys"
                },
                "Expand Access to Resources for Marginalized Groups": {
                    "% of marginalized farmers accessing services": "(Marginalized farmers accessing services / Total marginalized farmers) * 100",
                    "Number of targeted support programs": "Total programs for marginalized groups",
                    "% of resources effectively allocated": "(Resources allocated to target groups / Total resources) * 100",
                    "Satisfaction survey score for marginalized groups": "Average satisfaction score from marginalized group surveys"
                },
                "Strengthen Leadership & Decision-Making Roles": {
                    "% of women in cooperative leadership positions": "(Women leaders / Total leadership positions) * 100",
                    "Number of women-led initiatives implemented": "Total initiatives led by women",
                    "% of women attending decision-making meetings": "(Women attending meetings / Total women members) * 100",
                    "Satisfaction with leadership support": "Average satisfaction score from women leader surveys"
                },
                "Improve Training for Women & Youth": {
                    "% of women and youth trained": "(Women and youth trained / Total women and youth) * 100",
                    "Number of skill-building sessions conducted": "Total training sessions for women and youth",
                    "% adoption of learned techniques": "(Techniques adopted / Total techniques taught) * 100",
                    "Training satisfaction score": "Average satisfaction score from training evaluations"
                }
            },

            # Area 16: Infrastructure & Rural Development
            "Agriculture / Infrastructure & Rural Development": {
                "Expand Irrigation Facility Access": {
                    "% of farmers with irrigation access": "(Farmers with irrigation / Total farmers) * 100",
                    "Area under irrigation per farm": "Total irrigated area / Number of farms",
                    "% increase in yield due to irrigation": "((Irrigated yield - Non-irrigated yield) / Non-irrigated yield) * 100",
                    "Satisfaction with irrigation infrastructure": "Average satisfaction score from user surveys"
                },
                "Improve Rural Roads & Transport": {
                    "% of farmers with road access": "(Farmers with road access / Total farmers) * 100",
                    "Average travel time to markets": "Total travel time / Number of market trips",
                    "% of produce transported safely": "(Produce transported safely / Total produce transported) * 100",
                    "Satisfaction with transport access": "Average satisfaction score from farmer surveys"
                },
                "Increase Electricity Access": {
                    "% of farms with electricity": "(Farms with electricity / Total farms) * 100",
                    "Average hours of electricity available per day": "Total electricity hours / Number of days",
                    "% of farm operations powered by electricity": "(Electric-powered operations / Total operations) * 100",
                    "Satisfaction with electricity service": "Average satisfaction score from user surveys"
                },
                "Improve Access to Clean Water": {
                    "% of households/farms with clean water": "(Households/farms with clean water / Total) * 100",
                    "Water quality index": "Average score from water quality tests",
                    "Average daily water availability": "Total water available / Number of days",
                    "Satisfaction with water services": "Average satisfaction score from user surveys"
                },
                "Enhance Storage & Warehouse Facilities": {
                    "% of farmers with access to storage/warehouse": "(Farmers with storage access / Total farmers) * 100",
                    "Storage capacity per farm": "Total storage capacity / Number of farms",
                    "% reduction in post-harvest losses": "((Previous losses - Current losses) / Previous losses) * 100",
                    "Satisfaction with storage facilities": "Average satisfaction score from user surveys"
                },
                "Increase Participation in Infrastructure Development Programs": {
                    "% of farmers/communities benefiting": "(Beneficiaries / Total eligible) * 100",
                    "Number of infrastructure projects completed": "Total projects completed",
                    "% of infrastructure effectively utilized": "(Infrastructure utilized / Total infrastructure) * 100",
                    "Satisfaction with infrastructure programs": "Average satisfaction score from beneficiary surveys"
                },
                "Improve Farm-to-Market Logistics Support": {
                    "% of farms using logistics services": "(Farms using logistics / Total farms) * 100",
                    "Average transport cost per unit": "Total transport cost / Total units transported",
                    "% reduction in spoilage during transport": "((Previous spoilage - Current spoilage) / Previous spoilage) * 100",
                    "Satisfaction with logistics support": "Average satisfaction score from user surveys"
                }
            },


            # agriculture end

            #health start
            # Area 1: Improve Patient Access to Services
            "Health / Patient Access to Services": {
                "Increase Service Coverage": {
                    "% of population with access to essential health services": "(Population with access / Total population) * 100",
                    "Average distance/travel time to health facilities": "Total travel time / Number of patients",
                    "% of underserved areas receiving outreach services": "(Underserved areas served / Total underserved areas) * 100",
                    "Patient satisfaction with accessibility": "Average satisfaction score from patient surveys"
                },
                "Reduce Appointment Waiting Time": {
                    "Average waiting time for consultations": "Total waiting time / Number of consultations",
                    "% of patients seen within target time": "(Patients seen on time / Total patients) * 100",
                    "% reduction in missed appointments": "((Previous missed appointments - Current missed) / Previous missed) * 100",
                    "Patient satisfaction with scheduling efficiency": "Average satisfaction score from scheduling feedback"
                },
                "Expand Telehealth & Digital Services": {
                    "% of patients using telehealth services": "(Patients using telehealth / Total patients) * 100",
                    "Number of virtual consultations per month": "Total virtual consultations per month",
                    "% of successful remote diagnoses": "(Successful remote diagnoses / Total remote consultations) * 100",
                    "Patient satisfaction with digital health services": "Average satisfaction score from digital service users"
                },
                "Improve Emergency Service Accessibility": {
                    "% of population covered by emergency response": "(Population covered / Total population) * 100",
                    "Average response time for emergencies": "Total response time / Number of emergencies",
                    "% of emergencies stabilized within target timeframe": "(Emergencies stabilized on time / Total emergencies) * 100",
                    "Patient satisfaction with emergency services": "Average satisfaction score from emergency service users"
                }
            },

            # Area 2: Enhance Quality of Care
            "Health / Quality of Care": {
                "Improve Clinical Outcomes": {
                    "% of patients achieving treatment targets": "(Patients achieving targets / Total patients) * 100",
                    "Readmission rate reduction": "((Previous readmission rate - Current rate) / Previous rate) * 100",
                    "% of complications prevented": "(Complications prevented / Expected complications) * 100",
                    "Patient recovery satisfaction score": "Average satisfaction score from recovered patients"
                },
                "Ensure Evidence-Based Practice": {
                    "% of treatments aligned with clinical guidelines": "(Guideline-aligned treatments / Total treatments) * 100",
                    "Number of audits performed for compliance": "Total compliance audits conducted",
                    "% of staff trained in updated clinical protocols": "(Staff trained / Total staff) * 100",
                    "Compliance satisfaction score": "Average satisfaction score from compliance assessments"
                },
                "Reduce Medical Errors": {
                    "Number of adverse events per 1,000 patients": "(Total adverse events / Total patients) * 1000",
                    "% reduction in medication errors": "((Previous errors - Current errors) / Previous errors) * 100",
                    "Number of safety audits conducted": "Total safety audits performed",
                    "Staff and patient satisfaction with safety measures": "Average satisfaction score from safety surveys"
                },
                "Improve Patient-Centered Care": {
                    "Patient satisfaction survey score": "Average score from patient satisfaction surveys",
                    "% of patients involved in care decisions": "(Patients involved in decisions / Total patients) * 100",
                    "% of patients reporting improved care experience": "(Patients reporting improvement / Total surveyed) * 100",
                    "% of complaints addressed promptly": "(Complaints addressed promptly / Total complaints) * 100"
                }
            },

            # Area 3: Strengthen Preventive Health Programs
            "Health / Preventive Health Programs": {
                "Increase Immunization Coverage": {
                    "% of children fully immunized": "(Children fully immunized / Total children) * 100",
                    "% of target population receiving seasonal vaccines": "(Population vaccinated / Target population) * 100",
                    "Immunization dropout rate": "(Dropout children / Total enrolled children) * 100",
                    "Satisfaction with vaccination services": "Average satisfaction score from vaccination services"
                },
                "Promote Health Education": {
                    "% of population reached through awareness campaigns": "(Population reached / Total population) * 100",
                    "Number of health education sessions conducted": "Total education sessions held",
                    "% of participants adopting healthy behaviors": "(Participants adopting behaviors / Total participants) * 100",
                    "Satisfaction with health education programs": "Average satisfaction score from program participants"
                },
                "Expand Screening & Early Detection": {
                    "% of target population screened for key diseases": "(Population screened / Target population) * 100",
                    "Average time from screening to diagnosis": "Total diagnosis time / Number of screenings",
                    "% of early detections leading to successful treatment": "(Successful treatments / Early detections) * 100",
                    "Patient satisfaction with screening services": "Average satisfaction score from screening services"
                },
                "Improve Disease Surveillance & Reporting": {
                    "Timeliness of case reporting": "(Reports submitted on time / Total reports) * 100",
                    "% of outbreaks detected early": "(Early detections / Total outbreaks) * 100",
                    "% of response actions completed within targets": "(Actions completed on time / Total actions) * 100",
                    "Stakeholder satisfaction with surveillance system": "Average satisfaction score from stakeholders"
                }
            },

            # Area 4: Enhance Patient Satisfaction & Experience
            "Health / Patient Satisfaction & Experience": {
                "Improve Overall Patient Satisfaction": {
                    "Average satisfaction survey score": "Sum of satisfaction scores / Number of respondents",
                    "% of patients rating services as good/excellent": "(Patients rating good/excellent / Total surveyed) * 100",
                    "% reduction in complaints": "((Previous complaints - Current complaints) / Previous complaints) * 100",
                    "% of patients recommending the facility": "(Patients recommending / Total surveyed) * 100"
                },
                "Reduce Waiting Times for Services": {
                    "Average waiting time at clinics": "Total waiting time / Number of clinic visits",
                    "% of patients seen within target time": "(Patients seen on time / Total patients) * 100",
                    "Reduction in service delays": "((Previous delays - Current delays) / Previous delays) * 100",
                    "Patient satisfaction with waiting experience": "Average satisfaction score from waiting experience surveys"
                },
                "Increase Communication & Information Sharing": {
                    "% of patients receiving clear treatment instructions": "(Patients receiving clear instructions / Total patients) * 100",
                    "% of patients aware of follow-up schedules": "(Patients aware of schedules / Total patients) * 100",
                    "% of patients reporting effective communication": "(Patients reporting effective communication / Total surveyed) * 100",
                    "Patient satisfaction with information provision": "Average satisfaction score from information surveys"
                },
                "Improve Patient Privacy & Dignity": {
                    "% of patients satisfied with privacy standards": "(Satisfied patients / Total surveyed) * 100",
                    "Number of reported privacy breaches": "Total privacy breach incidents",
                    "Compliance with confidentiality protocols": "(Compliant instances / Total instances) * 100",
                    "Patient satisfaction with respectful treatment": "Average satisfaction score from dignity surveys"
                }
            },

            # Area 5: Strengthen Healthcare Workforce Competency
            "Health / Healthcare Workforce Competency": {
                "Increase Staff Training & Development": {
                    "% of staff completing continuing education programs": "(Staff completing programs / Total staff) * 100",
                    "Number of training hours per staff": "Total training hours / Number of staff",
                    "% of trained staff applying learned skills": "(Staff applying skills / Total trained staff) * 100",
                    "Staff satisfaction with professional development": "Average satisfaction score from staff development surveys"
                },
                "Improve Clinical Competency": {
                    "% of staff meeting competency assessment targets": "(Staff meeting targets / Total staff) * 100",
                    "% of staff certified in essential skills": "(Certified staff / Total staff) * 100",
                    "Reduction in clinical errors due to skill gaps": "((Previous skill-related errors - Current errors) / Previous errors) * 100",
                    "Satisfaction with competency improvement programs": "Average satisfaction score from competency programs"
                },
                "Enhance Staff Retention & Engagement": {
                    "Staff turnover rate": "(Staff leaving / Total staff) * 100",
                    "Employee satisfaction score": "Average score from employee satisfaction surveys",
                    "% of staff participating in engagement programs": "(Staff participating / Total staff) * 100",
                    "Reduction in absenteeism": "((Previous absenteeism - Current absenteeism) / Previous absenteeism) * 100"
                },
                "Increase Workforce Coverage": {
                    "Ratio of healthcare providers to population": "Population / Number of providers",
                    "% of underserved areas staffed adequately": "(Adequately staffed areas / Total underserved areas) * 100",
                    "Average time to fill vacancies": "Total days to fill vacancies / Number of vacancies",
                    "Satisfaction with workforce availability": "Average satisfaction score from workforce availability surveys"
                }
            },

            # Area 6: Strengthen Health Infrastructure & Facilities
            "Health / Health Infrastructure & Facilities": {
                "Expand Facility Coverage": {
                    "% of population with access to primary care facilities": "(Population with access / Total population) * 100",
                    "Number of functional health centers per region": "Total functional centers / Number of regions",
                    "Average distance to nearest facility": "Total distance / Number of communities",
                    "Patient satisfaction with facility access": "Average satisfaction score from facility access surveys"
                },
                "Upgrade Medical Equipment": {
                    "% of facilities with functional essential equipment": "(Facilities with functional equipment / Total facilities) * 100",
                    "Number of equipment upgrades completed annually": "Total equipment upgrades completed",
                    "% of equipment downtime reduced": "((Previous downtime - Current downtime) / Previous downtime) * 100",
                    "Staff satisfaction with equipment availability": "Average satisfaction score from equipment surveys"
                },
                "Ensure Facility Safety & Cleanliness": {
                    "% of facilities passing hygiene audits": "(Facilities passing audits / Total facilities) * 100",
                    "Number of safety incidents per facility": "Total safety incidents / Number of facilities",
                    "Compliance with infection prevention protocols": "(Compliant facilities / Total facilities) * 100",
                    "Patient satisfaction with cleanliness and safety": "Average satisfaction score from cleanliness surveys"
                },
                "Improve Infrastructure for Specialized Services": {
                    "% of facilities with specialty units operational": "(Facilities with specialty units / Total facilities) * 100",
                    "Average service availability per specialty": "Total service availability / Number of specialties",
                    "Reduction in patient referrals outside region": "((Previous referrals - Current referrals) / Previous referrals) * 100",
                    "Patient satisfaction with specialized services": "Average satisfaction score from specialty service users"
                }
            },

            # Area 7: Increase Access to Medicines & Supplies
            "Health / Access to Medicines & Supplies": {
                "Improve Medicine Availability": {
                    "% of essential medicines in stock": "(Medicines in stock / Total essential medicines) * 100",
                    "Frequency of stock-outs": "Number of stock-out incidents per period",
                    "Average lead time for restocking": "Total restocking time / Number of restocking events",
                    "Patient satisfaction with medicine availability": "Average satisfaction score from medicine availability surveys"
                },
                "Ensure Affordable Medicines": {
                    "Average cost of essential medicines": "Total medicine cost / Number of medicines",
                    "% of patients able to afford prescribed medications": "(Patients able to afford / Total patients) * 100",
                    "Reduction in out-of-pocket spending": "((Previous spending - Current spending) / Previous spending) * 100",
                    "Patient satisfaction with medicine affordability": "Average satisfaction score from affordability surveys"
                },
                "Enhance Supply Chain Efficiency": {
                    "% of deliveries received on time": "(On-time deliveries / Total deliveries) * 100",
                    "% reduction in supply shortages": "((Previous shortages - Current shortages) / Previous shortages) * 100",
                    "Inventory accuracy rate": "(Accurate inventory records / Total inventory records) * 100",
                    "Satisfaction with supply management": "Average satisfaction score from supply management surveys"
                },
                "Improve Access to Specialized Medical Supplies": {
                    "% of facilities with required specialized supplies": "(Facilities with supplies / Total facilities) * 100",
                    "Number of patients receiving critical supplies on time": "Total patients receiving supplies on time",
                    "Reduction in treatment delays due to supply gaps": "((Previous delays - Current delays) / Previous delays) * 100",
                    "Satisfaction with supply availability": "Average satisfaction score from supply availability surveys"
                }
            },

            # Area 8: Strengthen Patient Safety
            "Health / Patient Safety": {
                "Reduce Medical Errors": {
                    "Number of adverse events per 1,000 patients": "(Total adverse events / Total patients) * 1000",
                    "% reduction in medication errors": "((Previous medication errors - Current errors) / Previous errors) * 100",
                    "% of staff trained in patient safety protocols": "(Staff trained / Total staff) * 100",
                    "Patient satisfaction with safety measures": "Average satisfaction score from patient safety surveys"
                },
                "Improve Infection Prevention & Control": {
                    "% of facilities compliant with IPC standards": "(Compliant facilities / Total facilities) * 100",
                    "Number of hospital-acquired infections per 1,000 patients": "(Total HAIs / Total patients) * 1000",
                    "% reduction in infection rates year-over-year": "((Previous infection rate - Current rate) / Previous rate) * 100",
                    "Patient satisfaction with hygiene practices": "Average satisfaction score from hygiene surveys"
                },
                "Enhance Medication Safety": {
                    "% of prescriptions verified for accuracy": "(Verified prescriptions / Total prescriptions) * 100",
                    "Number of adverse drug events reported": "Total adverse drug events reported",
                    "% of patients receiving correct dosage instructions": "(Patients receiving correct instructions / Total patients) * 100",
                    "Staff satisfaction with medication safety procedures": "Average satisfaction score from medication safety surveys"
                },
                "Increase Reporting & Response": {
                    "% of safety incidents reported promptly": "(Incidents reported promptly / Total incidents) * 100",
                    "Average response time to reported incidents": "Total response time / Number of incidents",
                    "% of corrective actions implemented": "(Actions implemented / Total required actions) * 100",
                    "Stakeholder satisfaction with reporting system": "Average satisfaction score from reporting system surveys"
                }
            },

            # Area 9: Promote Community & Public Health
            "Health / Community & Public Health": {
                "Expand Preventive Health Programs": {
                    "% of target population reached by public health campaigns": "(Population reached / Target population) * 100",
                    "Number of vaccination campaigns conducted": "Total vaccination campaigns conducted",
                    "% of population adopting preventive practices": "(Population adopting practices / Total population) * 100",
                    "Community satisfaction with health programs": "Average satisfaction score from community health surveys"
                },
                "Increase Health Awareness": {
                    "Number of health education sessions conducted": "Total education sessions conducted",
                    "% of population aware of key health risks": "(Aware population / Total population) * 100",
                    "% of community members demonstrating improved health knowledge": "(Members with improved knowledge / Total members) * 100",
                    "Satisfaction with awareness programs": "Average satisfaction score from awareness program surveys"
                },
                "Improve Disease Surveillance": {
                    "% of disease cases reported timely": "(Cases reported timely / Total cases) * 100",
                    "Number of outbreaks detected early": "Total outbreaks detected early",
                    "% of response actions completed within target": "(Actions completed on time / Total actions) * 100",
                    "Stakeholder satisfaction with surveillance system": "Average satisfaction score from surveillance system surveys"
                },
                "Promote Environmental Health Initiatives": {
                    "% of communities with access to safe water": "(Communities with safe water / Total communities) * 100",
                    "% of households practicing proper sanitation": "(Households with proper sanitation / Total households) * 100",
                    "Number of environmental health inspections conducted": "Total environmental inspections conducted",
                    "Community satisfaction with environmental health services": "Average satisfaction score from environmental health surveys"
                }
            },

            # Area 10: Improve Emergency & Critical Care Services
            "Health / Emergency & Critical Care Services": {
                "Enhance Emergency Response": {
                    "Average response time to emergencies": "Total response time / Number of emergencies",
                    "% of emergencies stabilized within target timeframe": "(Emergencies stabilized on time / Total emergencies) * 100",
                    "% of population covered by emergency services": "(Population covered / Total population) * 100",
                    "Patient satisfaction with emergency response": "Average satisfaction score from emergency response surveys"
                },
                "Improve Critical Care Quality": {
                    "% of ICU patients achieving treatment targets": "(ICU patients achieving targets / Total ICU patients) * 100",
                    "Reduction in ICU mortality rate": "((Previous mortality rate - Current rate) / Previous rate) * 100",
                    "Compliance with critical care protocols": "(Compliant instances / Total instances) * 100",
                    "Patient satisfaction with critical care services": "Average satisfaction score from critical care surveys"
                },
                "Increase Availability of Emergency Resources": {
                    "% of facilities with functional emergency equipment": "(Facilities with functional equipment / Total facilities) * 100",
                    "Average time to replenish critical supplies": "Total replenishment time / Number of replenishment events",
                    "% of emergencies managed without delay due to resource gaps": "(Emergencies without delay / Total emergencies) * 100",
                    "Staff satisfaction with emergency preparedness": "Average satisfaction score from emergency preparedness surveys"
                },
                "Strengthen Trauma & Disaster Response": {
                    "% of trauma patients stabilized within target time": "(Trauma patients stabilized on time / Total trauma patients) * 100",
                    "Number of disaster response drills conducted annually": "Total disaster drills conducted",
                    "% of emergency protocols tested successfully": "(Protocols tested successfully / Total protocols) * 100",
                    "Stakeholder satisfaction with disaster preparedness": "Average satisfaction score from disaster preparedness surveys"
                }
            },

            # Area 11: Enhance Healthcare Quality & Accreditation
            "Health / Healthcare Quality & Accreditation": {
                "Increase Facility Accreditation": {
                    "% of facilities accredited nationally/internationally": "(Accredited facilities / Total facilities) * 100",
                    "Number of accreditation audits conducted": "Total accreditation audits conducted",
                    "% of compliance with quality standards": "(Compliant standards / Total standards) * 100",
                    "Staff satisfaction with accreditation process": "Average satisfaction score from accreditation process surveys"
                },
                "Strengthen Clinical Governance": {
                    "Number of clinical audits conducted": "Total clinical audits conducted",
                    "% of staff complying with clinical protocols": "(Staff complying / Total staff) * 100",
                    "% reduction in adverse clinical events": "((Previous adverse events - Current events) / Previous events) * 100",
                    "Patient satisfaction with clinical governance": "Average satisfaction score from clinical governance surveys"
                },
                "Implement Continuous Quality Improvement": {
                    "Number of quality improvement initiatives completed": "Total quality initiatives completed",
                    "% of identified improvements implemented": "(Improvements implemented / Total identified) * 100",
                    "Reduction in service errors": "((Previous service errors - Current errors) / Previous errors) * 100",
                    "Stakeholder satisfaction with quality programs": "Average satisfaction score from quality program surveys"
                },
                "Increase Patient Feedback Integration": {
                    "% of feedback collected from patients": "(Feedback collected / Target feedback) * 100",
                    "% of feedback acted upon": "(Feedback acted upon / Total feedback) * 100",
                    "Average time to address feedback": "Total response time / Number of feedback items",
                    "Patient satisfaction with responsiveness": "Average satisfaction score from responsiveness surveys"
                }
            },

            # Area 12: Promote Equity & Inclusion in Healthcare
            "Health / Equity & Inclusion in Healthcare": {
                "Improve Access for Vulnerable Populations": {
                    "% of vulnerable populations accessing services": "(Vulnerable population accessing services / Total vulnerable population) * 100",
                    "Reduction in service access disparities": "((Previous disparity - Current disparity) / Previous disparity) * 100",
                    "Number of targeted outreach programs": "Total outreach programs conducted",
                    "Satisfaction of vulnerable populations with services": "Average satisfaction score from vulnerable population surveys"
                },
                "Reduce Gender Inequalities in Health": {
                    "% of female patients accessing maternal/child services": "(Female patients accessing services / Total female patients) * 100",
                    "% of health programs targeting gender-specific needs": "(Gender-specific programs / Total programs) * 100",
                    "% improvement in maternal and child health indicators": "((Current indicators - Previous indicators) / Previous indicators) * 100",
                    "Patient satisfaction with gender-focused services": "Average satisfaction score from gender-focused service surveys"
                },
                "Increase Accessibility for Persons with Disabilities": {
                    "% of facilities compliant with accessibility standards": "(Compliant facilities / Total facilities) * 100",
                    "Number of disability-friendly health programs implemented": "Total disability-friendly programs implemented",
                    "% of disabled patients receiving timely care": "(Disabled patients receiving timely care / Total disabled patients) * 100",
                    "Satisfaction of patients with disabilities": "Average satisfaction score from patients with disabilities"
                },
                "Strengthen Community Engagement for Equity": {
                    "% of community members involved in health planning": "(Community members involved / Total community members) * 100",
                    "Number of equity-focused community initiatives": "Total equity initiatives conducted",
                    "% of initiatives completed on schedule": "(Initiatives completed on schedule / Total initiatives) * 100",
                    "Satisfaction with equity engagement programs": "Average satisfaction score from equity engagement surveys"
                }
            },

            # Area 13: Strengthen Digital Health & Innovation
            "Health / Digital Health & Innovation": {
                "Expand E-Health Services": {
                    "% of patients using electronic health records": "(Patients using EHR / Total patients) * 100",
                    "% of consultations conducted digitally": "(Digital consultations / Total consultations) * 100",
                    "Reduction in documentation errors": "((Previous documentation errors - Current errors) / Previous errors) * 100",
                    "Patient satisfaction with digital services": "Average satisfaction score from digital service surveys"
                },
                "Improve Health Data Management": {
                    "% of facilities with reliable data reporting systems": "(Facilities with reliable systems / Total facilities) * 100",
                    "Timeliness of health data submission": "(Data submitted on time / Total data submissions) * 100",
                    "Accuracy of collected health data": "(Accurate data / Total data collected) * 100",
                    "Staff satisfaction with data systems": "Average satisfaction score from data system surveys"
                },
                "Increase Telemedicine Adoption": {
                    "% of patients utilizing telemedicine services": "(Patients using telemedicine / Total patients) * 100",
                    "Number of telemedicine consultations per month": "Total telemedicine consultations per month",
                    "% of patients reporting successful outcomes": "(Patients reporting success / Total telemedicine users) * 100",
                    "Satisfaction with telemedicine quality": "Average satisfaction score from telemedicine quality surveys"
                },
                "Promote Health Technology Innovation": {
                    "Number of digital health innovations implemented": "Total innovations implemented",
                    "% of staff trained on new technology": "(Staff trained / Total staff) * 100",
                    "Improvement in operational efficiency from technology": "((Current efficiency - Previous efficiency) / Previous efficiency) * 100",
                    "Stakeholder satisfaction with health technology initiatives": "Average satisfaction score from technology initiative surveys"
                }
            },

            # Area 14: Improve Research & Evidence-Based Practice
            "Health / Research & Evidence-Based Practice": {
                "Increase Health Research Output": {
                    "Number of research studies conducted annually": "Total research studies conducted",
                    "% of research projects completed on time": "(Projects completed on time / Total projects) * 100",
                    "Number of publications in peer-reviewed journals": "Total publications in peer-reviewed journals",
                    "Stakeholder satisfaction with research quality": "Average satisfaction score from research quality surveys"
                },
                "Promote Evidence-Based Clinical Decisions": {
                    "% of clinical decisions aligned with research evidence": "(Evidence-based decisions / Total decisions) * 100",
                    "% of staff trained in evidence-based practice": "(Staff trained / Total staff) * 100",
                    "% reduction in non-evidence-based treatments": "((Previous non-evidence treatments - Current) / Previous) * 100",
                    "Patient satisfaction with clinical decisions": "Average satisfaction score from clinical decision surveys"
                },
                "Enhance Data Utilization for Policy": {
                    "Number of policies informed by research data": "Total policies using research data",
                    "% of management decisions using evidence": "(Evidence-based decisions / Total decisions) * 100",
                    "Timeliness of research reports for decision-making": "(Reports delivered on time / Total reports) * 100",
                    "Stakeholder satisfaction with policy support": "Average satisfaction score from policy support surveys"
                },
                "Increase Collaboration in Research": {
                    "Number of collaborative research projects": "Total collaborative projects",
                    "% of projects with multi-institutional participation": "(Multi-institutional projects / Total projects) * 100",
                    "% of research findings implemented in practice": "(Findings implemented / Total findings) * 100",
                    "Satisfaction with research partnerships": "Average satisfaction score from research partnership surveys"
                }
            },

            # Area 15: Enhance Patient & Staff Satisfaction
            "Health / Patient & Staff Satisfaction": {
                "Improve Patient Experience": {
                    "Average patient satisfaction survey score": "Sum of patient satisfaction scores / Number of respondents",
                    "% of patients rating services as excellent": "(Patients rating excellent / Total surveyed) * 100",
                    "% of patient complaints resolved promptly": "(Complaints resolved promptly / Total complaints) * 100",
                    "% of patients willing to recommend the facility": "(Patients willing to recommend / Total surveyed) * 100"
                },
                "Increase Staff Engagement & Satisfaction": {
                    "Staff satisfaction survey score": "Sum of staff satisfaction scores / Number of respondents",
                    "% of staff participating in engagement programs": "(Staff participating / Total staff) * 100",
                    "Staff retention rate": "(Staff retained / Total staff) * 100",
                    "Reduction in absenteeism": "((Previous absenteeism - Current absenteeism) / Previous absenteeism) * 100"
                },
                "Strengthen Communication & Feedback Loops": {
                    "% of patients and staff providing feedback": "(Feedback providers / Total patients and staff) * 100",
                    "Average time to respond to feedback": "Total response time / Number of feedback items",
                    "% of feedback addressed effectively": "(Feedback addressed effectively / Total feedback) * 100",
                    "Satisfaction with communication processes": "Average satisfaction score from communication process surveys"
                },
                "Promote a Positive Work & Care Environment": {
                    "Number of initiatives to improve workplace culture": "Total culture improvement initiatives",
                    "% of staff reporting improved work conditions": "(Staff reporting improvement / Total staff) * 100",
                    "% of patients reporting positive environment": "(Patients reporting positive environment / Total surveyed) * 100",
                    "Stakeholder satisfaction with organizational culture": "Average satisfaction score from organizational culture surveys"
                }
            },

            # Area 16: Strengthen Health Infrastructure & Logistics
            "Health / Health Infrastructure & Logistics": {
                "Expand Facility Capacity": {
                    "Number of new health facilities established": "Total new facilities established",
                    "% increase in bed capacity": "((Current capacity - Previous capacity) / Previous capacity) * 100",
                    "% of facilities operating at optimal capacity": "(Facilities at optimal capacity / Total facilities) * 100",
                    "Patient satisfaction with infrastructure": "Average satisfaction score from infrastructure surveys"
                },
                "Improve Medical Equipment Availability": {
                    "% of facilities with functional essential equipment": "(Facilities with functional equipment / Total facilities) * 100",
                    "Average downtime of critical equipment": "Total downtime / Number of equipment units",
                    "% of equipment meeting operational standards": "(Equipment meeting standards / Total equipment) * 100",
                    "Staff satisfaction with equipment availability": "Average satisfaction score from equipment availability surveys"
                },
                "Strengthen Supply Chain & Logistics": {
                    "% of medicines and supplies delivered on time": "(Deliveries on time / Total deliveries) * 100",
                    "Reduction in stock-outs": "((Previous stock-outs - Current stock-outs) / Previous stock-outs) * 100",
                    "Average lead time for essential supplies": "Total lead time / Number of supply orders",
                    "Satisfaction with logistics management": "Average satisfaction score from logistics management surveys"
                },
                "Upgrade ICT & Health Information Systems": {
                    "% of facilities with functional ICT infrastructure": "(Facilities with functional ICT / Total facilities) * 100",
                    "Timeliness and accuracy of health data reporting": "(Accurate timely reports / Total reports) * 100",
                    "Number of ICT upgrades implemented annually": "Total ICT upgrades implemented",
                    "Staff and patient satisfaction with ICT systems": "Average satisfaction score from ICT system surveys"
                }
            },

            #health end

            #manufacturing start
            # Area 1: Enhance Product/Service Quality
            "Manufacturing / Product Quality": {
                "Ensure consistent product quality": {
                    "% of products meeting quality standards consistently": "(Products meeting standards / Total products) * 100",
                    "Number of quality audits successfully completed": "Total quality audits passed",
                    "% reduction in defective products": "((Previous defects - Current defects) / Previous defects) * 100",
                    "Customer satisfaction with product quality": "Average satisfaction score from quality surveys"
                },
                "Minimize customer complaints": {
                    "Number of complaints received per period": "Total customer complaints received",
                    "Average time to resolve customer complaints": "Total resolution time / Number of complaints",
                    "% reduction in repeat complaints": "((Previous repeat complaints - Current) / Previous) * 100",
                    "Customer satisfaction with complaint handling process": "Average satisfaction score from complaint handling surveys"
                },
                "Improve reliability and performance": {
                    "% of products passing reliability and performance tests": "(Products passing tests / Total tested) * 100",
                    "Number of warranty claims filed": "Total warranty claims received",
                    "Number of product recalls executed": "Total product recalls conducted",
                    "Customer satisfaction with product reliability": "Average satisfaction score from reliability surveys"
                },
                "Strengthen traceability and certification compliance": {
                    "% of products with complete traceability from origin": "(Traceable products / Total products) * 100",
                    "Number of industry-standard certifications achieved": "Total certifications obtained",
                    "% compliance with certification audits": "(Compliant audits / Total audits) * 100",
                    "Customer satisfaction with certified products": "Average satisfaction score from certified product surveys"
                }
            },

            # Area 2: Improve Customer Access & Delivery
            "Manufacturing / Customer Access & Delivery": {
                "Reduce delivery lead time": {
                    "Average production-to-delivery cycle time": "Total cycle time / Number of orders",
                    "% of orders delivered on or before promised date": "(Orders delivered on time / Total orders) * 100",
                    "Reduction in late shipment incidents": "((Previous late shipments - Current) / Previous) * 100",
                    "Customer satisfaction with delivery timeliness": "Average satisfaction score from delivery surveys"
                },
                "Improve production and scheduling accuracy": {
                    "% of orders completed according to schedule": "(Orders completed on schedule / Total orders) * 100",
                    "Average delay per production batch": "Total delay time / Number of batches",
                    "Number of on-time deliveries per period": "Total on-time deliveries",
                    "Customer satisfaction with scheduling reliability": "Average satisfaction score from scheduling surveys"
                },
                "Enhance logistics and transportation efficiency": {
                    "% of shipments delivered without damage": "(Undamaged shipments / Total shipments) * 100",
                    "Average transportation time per order": "Total transport time / Number of orders",
                    "% reduction in logistics-related delays": "((Previous delays - Current delays) / Previous delays) * 100",
                    "Customer satisfaction with logistics service": "Average satisfaction score from logistics surveys"
                },
                "Strengthen order tracking and communication": {
                    "% of orders tracked in real-time": "(Real-time tracked orders / Total orders) * 100",
                    "Number of customer updates provided per order": "Total updates / Number of orders",
                    "Average response time to customer inquiries": "Total response time / Number of inquiries",
                    "Customer satisfaction with order communication": "Average satisfaction score from communication surveys"
                }
            },

            # Area 3: Strengthen Customer Service & Support
            "Manufacturing / Customer Service & Support": {
                "Improve responsiveness to customer inquiries": {
                    "Average response time to customer inquiries": "Total response time / Number of inquiries",
                    "% of inquiries resolved within SLA": "(Inquiries resolved within SLA / Total inquiries) * 100",
                    "Number of support tickets handled per month": "Total support tickets handled",
                    "Customer satisfaction with responsiveness": "Average satisfaction score from responsiveness surveys"
                },
                "Enhance after-sales support services": {
                    "% of issues resolved within service level agreements": "(Issues resolved within SLA / Total issues) * 100",
                    "Average resolution time for after-sales issues": "Total resolution time / Number of after-sales issues",
                    "Reduction in recurring after-sales issues": "((Previous recurring issues - Current) / Previous) * 100",
                    "Customer satisfaction with after-sales support": "Average satisfaction score from after-sales surveys"
                },
                "Increase customer engagement and feedback utilization": {
                    "% of customers providing actionable feedback": "(Customers providing feedback / Total customers) * 100",
                    "% of feedback implemented into operations": "(Feedback implemented / Total feedback) * 100",
                    "Number of customer satisfaction surveys conducted": "Total satisfaction surveys conducted",
                    "Customer satisfaction with engagement efforts": "Average satisfaction score from engagement surveys"
                },
                "Strengthen customer retention and loyalty": {
                    "Customer retention rate": "(Customers retained / Total customers) * 100",
                    "% of repeat orders": "(Repeat orders / Total orders) * 100",
                    "Number of customers participating in loyalty programs": "Total loyalty program participants",
                    "Customer satisfaction with loyalty initiatives": "Average satisfaction score from loyalty program surveys"
                }
            },

            # Area 4: Promote Innovation & New Offerings
            "Manufacturing / Innovation & New Offerings": {
                "Increase development of new products": {
                    "Number of new products launched annually": "Total new products launched",
                    "% of new products meeting customer expectations": "(New products meeting expectations / Total new products) * 100",
                    "Average time-to-market for new offerings": "Total development time / Number of new products",
                    "Customer satisfaction with new products": "Average satisfaction score from new product surveys"
                },
                "Improve R&D effectiveness and innovation impact": {
                    "% of R&D projects completed on schedule": "(Projects completed on schedule / Total projects) * 100",
                    "% of projects achieving intended outcomes": "(Projects achieving outcomes / Total projects) * 100",
                    "Number of patents or innovations registered": "Total patents or innovations registered",
                    "Stakeholder satisfaction with R&D performance": "Average satisfaction score from R&D performance surveys"
                },
                "Enhance customization and personalization": {
                    "% of products customized per customer request": "(Customized products / Total products) * 100",
                    "Number of personalized solutions successfully delivered": "Total personalized solutions delivered",
                    "% of repeat orders for customized products": "(Repeat custom orders / Total custom orders) * 100",
                    "Customer satisfaction with personalization options": "Average satisfaction score from customization surveys"
                },
                "Strengthen market research and customer insight": {
                    "Number of market research studies conducted": "Total market research studies",
                    "% of product decisions informed by insights": "(Decisions using insights / Total decisions) * 100",
                    "% of offerings adapted based on customer feedback": "(Offerings adapted / Total offerings) * 100",
                    "Customer satisfaction with responsiveness to market needs": "Average satisfaction score from market responsiveness surveys"
                }
            },

            # Area 5: Improve Operational Efficiency
            "Manufacturing / Operational Efficiency": {
                "Reduce production waste": {
                    "% reduction in material or resource waste": "((Previous waste - Current waste) / Previous waste) * 100",
                    "Cost savings achieved from waste reduction": "Total cost savings from waste reduction",
                    "% of production processes optimized": "(Optimized processes / Total processes) * 100",
                    "Customer satisfaction with operational efficiency": "Average satisfaction score from efficiency surveys"
                },
                "Improve capacity utilization": {
                    "% of production capacity utilized": "(Actual output / Maximum capacity) * 100",
                    "Reduction in idle machine or resource hours": "((Previous idle hours - Current) / Previous) * 100",
                    "Increase in output per production unit": "((Current output - Previous output) / Previous output) * 100",
                    "Customer satisfaction with order fulfillment": "Average satisfaction score from fulfillment surveys"
                },
                "Enhance supply chain efficiency": {
                    "% of suppliers meeting delivery and quality targets": "(Suppliers meeting targets / Total suppliers) * 100",
                    "% reduction in supply chain disruptions": "((Previous disruptions - Current) / Previous) * 100",
                    "Average lead time from supplier to production": "Total lead time / Number of supplier orders",
                    "Customer satisfaction with supply reliability": "Average satisfaction score from supply reliability surveys"
                },
                "Strengthen equipment/process reliability": {
                    "% of equipment operating at optimal performance": "(Optimal equipment / Total equipment) * 100",
                    "Reduction in unplanned downtime": "((Previous downtime - Current downtime) / Previous downtime) * 100",
                    "Number of preventive maintenance tasks completed": "Total preventive maintenance tasks completed",
                    "Customer satisfaction with production reliability": "Average satisfaction score from production reliability surveys"
                }
            },

            # Area 6: Enhance Sustainability & Environmental Responsibility
            "Manufacturing / Sustainability & Environmental Responsibility": {
                "Reduce energy consumption and improve efficiency": {
                    "% reduction in energy consumption per unit produced": "((Previous consumption - Current) / Previous) * 100",
                    "% of energy sourced from renewable sources": "(Renewable energy / Total energy) * 100",
                    "Cost savings from energy efficiency initiatives": "Total cost savings from energy efficiency",
                    "Stakeholder satisfaction with sustainability practices": "Average satisfaction score from sustainability surveys"
                },
                "Minimize waste and emissions": {
                    "% reduction in emissions per production unit": "((Previous emissions - Current) / Previous) * 100",
                    "% of waste recycled or reused": "(Waste recycled / Total waste) * 100",
                    "Number of environmental incidents reported": "Total environmental incidents",
                    "Stakeholder satisfaction with environmental compliance": "Average satisfaction score from environmental compliance surveys"
                },
                "Promote sustainable operations": {
                    "% of operations certified as sustainable": "(Certified operations / Total operations) * 100",
                    "Number of sustainability initiatives implemented": "Total sustainability initiatives implemented",
                    "Improvement in ESG performance ratings": "((Current rating - Previous rating) / Previous rating) * 100",
                    "Customer/stakeholder satisfaction with sustainability efforts": "Average satisfaction score from sustainability effort surveys"
                },
                "Increase sustainability awareness and training": {
                    "% of employees trained in environmental best practices": "(Employees trained / Total employees) * 100",
                    "Number of sustainability awareness sessions conducted": "Total awareness sessions conducted",
                    "% of employees applying sustainable practices": "(Employees applying practices / Total employees) * 100",
                    "Employee satisfaction with sustainability training": "Average satisfaction score from sustainability training surveys"
                }
            },

            # Area 7: Strengthen Workforce Competency & Engagement
            "Manufacturing / Workforce Competency & Engagement": {
                "Improve employee skills and training": {
                    "% of employees completing training programs": "(Employees completing training / Total employees) * 100",
                    "Average training hours per employee": "Total training hours / Number of employees",
                    "% of employees applying new skills on the job": "(Employees applying skills / Total trained) * 100",
                    "Employee satisfaction with training effectiveness": "Average satisfaction score from training effectiveness surveys"
                },
                "Enhance leadership and management capability": {
                    "% of supervisors/managers completing leadership training": "(Leaders trained / Total leaders) * 100",
                    "Number of leadership programs conducted": "Total leadership programs conducted",
                    "% of leadership positions filled internally": "(Internal promotions / Total leadership positions) * 100",
                    "Staff satisfaction with management support": "Average satisfaction score from management support surveys"
                },
                "Increase employee engagement and retention": {
                    "Employee engagement survey score": "Average score from engagement surveys",
                    "Employee turnover rate": "(Employees leaving / Total employees) * 100",
                    "% of employees participating in engagement programs": "(Employees participating / Total employees) * 100",
                    "Reduction in absenteeism rate": "((Previous absenteeism - Current) / Previous) * 100"
                },
                "Promote safety and positive workplace culture": {
                    "% of employees adhering to safety protocols": "(Employees following protocols / Total employees) * 100",
                    "Number of workplace culture initiatives": "Total culture initiatives implemented",
                    "Reduction in workplace incidents and accidents": "((Previous incidents - Current) / Previous) * 100",
                    "Employee satisfaction with work environment": "Average satisfaction score from work environment surveys"
                }
            },

            # Area 8: Increase Customer Satisfaction & Loyalty
            "Manufacturing / Customer Satisfaction & Loyalty": {
                "Strengthen customer relationships": {
                    "Customer retention rate (%)": "(Customers retained / Total customers) * 100",
                    "% of repeat orders per customer": "(Repeat orders / Total orders) * 100",
                    "% of customers rating service as excellent": "(Customers rating excellent / Total surveyed) * 100",
                    "Loyalty program participation rate (%)": "(Loyalty participants / Total customers) * 100"
                },
                "Improve communication with customers": {
                    "% of inquiries responded to within SLA": "(Inquiries responded within SLA / Total inquiries) * 100",
                    "Average response time to customer questions": "Total response time / Number of questions",
                    "% of customer feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Customer satisfaction with communication effectiveness": "Average satisfaction score from communication effectiveness surveys"
                },
                "Enhance service responsiveness": {
                    "% of complaints resolved within target timeframe": "(Complaints resolved on time / Total complaints) * 100",
                    "Average resolution time for customer issues": "Total resolution time / Number of issues",
                    "% reduction in repeat complaints": "((Previous repeat complaints - Current) / Previous) * 100",
                    "Customer satisfaction with support services": "Average satisfaction score from support service surveys"
                },
                "Promote superior customer experience": {
                    "Customer satisfaction survey score": "Average score from customer satisfaction surveys",
                    "Net Promoter Score (NPS)": "Percentage of promoters minus percentage of detractors",
                    "Number of positive customer testimonials": "Total positive testimonials received",
                    "% improvement in overall customer experience": "((Current experience score - Previous) / Previous) * 100"
                }
            },

            # Area 9: Improve Product Safety & Compliance
            "Manufacturing / Product Safety & Compliance": {
                "Ensure regulatory compliance": {
                    "% of audits passed without violations": "(Audits passed / Total audits) * 100",
                    "Number of non-compliance incidents reported": "Total non-compliance incidents",
                    "% of corrective actions implemented on time": "(Actions implemented on time / Total actions) * 100",
                    "Customer/stakeholder satisfaction with compliance": "Average satisfaction score from compliance surveys"
                },
                "Strengthen product safety testing": {
                    "% of products meeting safety standards": "(Products meeting standards / Total products) * 100",
                    "Number of safety incidents per period": "Total safety incidents",
                    "% of product recalls successfully executed": "(Successful recalls / Total recalls) * 100",
                    "Customer satisfaction with product safety": "Average satisfaction score from product safety surveys"
                },
                "Increase recall preparedness and responsiveness": {
                    "% of products traceable for recall": "(Traceable products / Total products) * 100",
                    "Number of recalls executed efficiently": "Total efficient recalls conducted",
                    "Average response time during recalls": "Total response time / Number of recalls",
                    "Customer satisfaction with recall handling": "Average satisfaction score from recall handling surveys"
                },
                "Enhance supplier compliance": {
                    "% of suppliers compliant with safety and quality standards": "(Compliant suppliers / Total suppliers) * 100",
                    "Number of supplier audits conducted": "Total supplier audits conducted",
                    "% of non-compliance issues resolved": "(Issues resolved / Total issues) * 100",
                    "Customer satisfaction with supplier reliability": "Average satisfaction score from supplier reliability surveys"
                }
            },

            # Area 10: Strengthen Supply Chain & Logistics
            "Manufacturing / Supply Chain & Logistics": {
                "Improve supplier performance": {
                    "% of suppliers meeting delivery and quality targets": "(Suppliers meeting targets / Total suppliers) * 100",
                    "Number of supplier audits conducted": "Total supplier audits conducted",
                    "% of supplier non-compliance issues resolved": "(Issues resolved / Total issues) * 100",
                    "Customer satisfaction with supplier reliability": "Average satisfaction score from supplier reliability surveys"
                },
                "Optimize inventory management": {
                    "% of inventory turnover per period": "(Cost of goods sold / Average inventory) * 100",
                    "Reduction in stock-outs or excess inventory": "((Previous issues - Current issues) / Previous issues) * 100",
                    "% inventory accuracy in system": "(Accurate inventory records / Total records) * 100",
                    "Customer satisfaction with product availability": "Average satisfaction score from product availability surveys"
                },
                "Enhance transportation and delivery efficiency": {
                    "% of orders delivered on time": "(Orders delivered on time / Total orders) * 100",
                    "Average delivery lead time": "Total delivery time / Number of orders",
                    "% of deliveries received without damage": "(Undamaged deliveries / Total deliveries) * 100",
                    "Customer satisfaction with delivery performance": "Average satisfaction score from delivery performance surveys"
                },
                "Strengthen supply chain transparency": {
                    "% of supply chain data traceable from origin to customer": "(Traceable data / Total data) * 100",
                    "Number of supply chain reports shared with stakeholders": "Total reports shared",
                    "% of corrective actions implemented": "(Actions implemented / Total actions) * 100",
                    "Customer satisfaction with supply chain transparency": "Average satisfaction score from transparency surveys"
                }
            },

            # Area 11: Promote Operational Innovation
            "Manufacturing / Operational Innovation": {
                "Increase process automation": {
                    "% of production processes automated": "(Automated processes / Total processes) * 100",
                    "% reduction in manual errors": "((Previous manual errors - Current) / Previous) * 100",
                    "% improvement in operational speed": "((Current speed - Previous speed) / Previous speed) * 100",
                    "Stakeholder satisfaction with operational efficiency": "Average satisfaction score from operational efficiency surveys"
                },
                "Strengthen R&D for process improvement": {
                    "Number of process improvement projects implemented": "Total improvement projects implemented",
                    "% of projects achieving targeted results": "(Projects achieving results / Total projects) * 100",
                    "% reduction in operational costs due to process innovation": "((Previous costs - Current costs) / Previous costs) * 100",
                    "Stakeholder satisfaction with innovation outcomes": "Average satisfaction score from innovation outcome surveys"
                },
                "Enhance product innovation": {
                    "Number of new or improved products launched": "Total new/improved products launched",
                    "% of innovations meeting customer expectations": "(Innovations meeting expectations / Total innovations) * 100",
                    "Market adoption rate of new products": "(Market adoption / Target market) * 100",
                    "Customer satisfaction with innovation": "Average satisfaction score from innovation surveys"
                },
                "Promote knowledge sharing and best practices": {
                    "Number of knowledge-sharing sessions conducted": "Total knowledge-sharing sessions",
                    "% of employees applying best practices": "(Employees applying practices / Total employees) * 100",
                    "% reduction in process inefficiencies": "((Previous inefficiencies - Current) / Previous) * 100",
                    "Staff satisfaction with training and knowledge sharing": "Average satisfaction score from knowledge sharing surveys"
                }
            },

            # Area 12: Improve Digital Transformation
            "Manufacturing / Digital Transformation": {
                "Increase adoption of digital tools": {
                    "% of operations using digital systems": "(Digital operations / Total operations) * 100",
                    "% reduction in manual documentation errors": "((Previous manual errors - Current) / Previous) * 100",
                    "% improvement in operational efficiency": "((Current efficiency - Previous efficiency) / Previous efficiency) * 100",
                    "Stakeholder satisfaction with digital operations": "Average satisfaction score from digital operation surveys"
                },
                "Strengthen data management and analytics": {
                    "% of operational data accurately captured and analyzed": "(Accurate data / Total data) * 100",
                    "Number of actionable insights generated": "Total actionable insights produced",
                    "% of decisions supported by data-driven insights": "(Decisions using insights / Total decisions) * 100",
                    "Customer satisfaction with timely information": "Average satisfaction score from information timeliness surveys"
                },
                "Enhance digital customer experience": {
                    "% of orders tracked digitally": "(Digitally tracked orders / Total orders) * 100",
                    "Average response time to digital customer queries": "Total response time / Number of digital queries",
                    "% of issues resolved through digital channels": "(Issues resolved digitally / Total issues) * 100",
                    "Customer satisfaction with digital service": "Average satisfaction score from digital service surveys"
                },
                "Promote cybersecurity and data protection": {
                    "% of systems compliant with cybersecurity standards": "(Compliant systems / Total systems) * 100",
                    "Number of cybersecurity incidents per period": "Total cybersecurity incidents",
                    "% of incidents resolved promptly": "(Incidents resolved promptly / Total incidents) * 100",
                    "Stakeholder confidence in data security": "Average confidence score from data security surveys"
                }
            },

            # Area 13: Strengthen Workforce & Employee Engagement
            "Manufacturing / Workforce & Employee Engagement": {
                "Improve employee training and competence": {
                    "% of employees completing training programs": "(Employees completing training / Total employees) * 100",
                    "Average training hours per employee": "Total training hours / Number of employees",
                    "% of employees applying new skills": "(Employees applying skills / Total trained) * 100",
                    "Employee satisfaction with training programs": "Average satisfaction score from training program surveys"
                },
                "Increase engagement and motivation": {
                    "Employee engagement survey score": "Average score from engagement surveys",
                    "% of staff participating in engagement programs": "(Staff participating / Total staff) * 100",
                    "Employee turnover rate": "(Employees leaving / Total employees) * 100",
                    "Reduction in absenteeism": "((Previous absenteeism - Current) / Previous) * 100"
                },
                "Enhance workplace safety and culture": {
                    "% of employees adhering to safety protocols": "(Employees following protocols / Total employees) * 100",
                    "Number of workplace culture initiatives implemented": "Total culture initiatives implemented",
                    "Reduction in workplace incidents and accidents": "((Previous incidents - Current) / Previous) * 100",
                    "Employee satisfaction with workplace environment": "Average satisfaction score from workplace environment surveys"
                },
                "Promote leadership and career development": {
                    "% of supervisors/managers trained in leadership": "(Leaders trained / Total leaders) * 100",
                    "Number of leadership development programs conducted": "Total leadership programs conducted",
                    "% of leadership positions filled internally": "(Internal promotions / Total leadership positions) * 100",
                    "Staff satisfaction with career growth opportunities": "Average satisfaction score from career growth surveys"
                }
            },

            # Area 14: Improve Customer Satisfaction with Delivery
            "Manufacturing / Customer Satisfaction with Delivery": {
                "Ensure timely delivery": {
                    "% of orders delivered on time": "(Orders delivered on time / Total orders) * 100",
                    "Average delivery lead time": "Total delivery time / Number of orders",
                    "Reduction in late shipments": "((Previous late shipments - Current) / Previous) * 100",
                    "Customer satisfaction with delivery timeliness": "Average satisfaction score from delivery timeliness surveys"
                },
                "Improve product reliability": {
                    "% of products meeting specifications": "(Products meeting specs / Total products) * 100",
                    "Reduction in defects per period": "((Previous defects - Current defects) / Previous defects) * 100",
                    "Number of warranty claims": "Total warranty claims filed",
                    "Customer satisfaction with product reliability": "Average satisfaction score from product reliability surveys"
                },
                "Optimize packaging and handling": {
                    "% of shipments received without damage": "(Undamaged shipments / Total shipments) * 100",
                    "Number of complaints related to packaging": "Total packaging complaints received",
                    "Reduction in shipment losses": "((Previous losses - Current losses) / Previous losses) * 100",
                    "Customer satisfaction with packaging quality": "Average satisfaction score from packaging quality surveys"
                },
                "Strengthen customer support for delivery": {
                    "% of delivery-related inquiries resolved promptly": "(Inquiries resolved promptly / Total inquiries) * 100",
                    "Average response time to delivery issues": "Total response time / Number of delivery issues",
                    "% of repeat delivery complaints": "(Repeat delivery complaints / Total complaints) * 100",
                    "Customer satisfaction with support services": "Average satisfaction score from support service surveys"
                }
            },

            # Area 15: Strengthen Risk Management & Crisis Response
            "Manufacturing / Risk Management & Crisis Response": {
                "Identify and assess operational risks": {
                    "Number of operational risks identified": "Total operational risks identified",
                    "% of risks assessed for impact and likelihood": "(Risks assessed / Total risks) * 100",
                    "Reduction in operational incidents": "((Previous incidents - Current incidents) / Previous incidents) * 100",
                    "Stakeholder satisfaction with risk management": "Average satisfaction score from risk management surveys"
                },
                "Enhance crisis preparedness": {
                    "Number of emergency drills conducted": "Total emergency drills performed",
                    "Average response time during crises": "Total response time / Number of crises",
                    "% of contingency plans updated regularly": "(Plans updated / Total plans) * 100",
                    "Stakeholder confidence in crisis readiness": "Average confidence score from crisis readiness surveys"
                },
                "Minimize operational and financial losses": {
                    "% reduction in losses from operational incidents": "((Previous losses - Current losses) / Previous losses) * 100",
                    "Number of claims settled successfully": "Total claims successfully settled",
                    "% of incidents mitigated effectively": "(Incidents mitigated / Total incidents) * 100",
                    "Stakeholder satisfaction with loss prevention": "Average satisfaction score from loss prevention surveys"
                },
                "Improve crisis communication": {
                    "% of stakeholders updated promptly": "(Stakeholders updated / Total stakeholders) * 100",
                    "Reduction in misinformation or miscommunication": "((Previous misinformation - Current) / Previous) * 100",
                    "Completeness of crisis documentation": "(Complete documentation / Total crises) * 100",
                    "Stakeholder satisfaction with communication during crises": "Average satisfaction score from crisis communication surveys"
                }
            },

            # Area 16: Strengthen Corporate Governance & Ethical Practices
            "Manufacturing / Corporate Governance & Ethical Practices": {
                "Promote transparency and accountability": {
                    "% of reports shared with stakeholders and board": "(Reports shared / Total reports) * 100",
                    "Number of audits conducted annually": "Total audits conducted",
                    "% of corrective actions implemented on time": "(Actions implemented on time / Total actions) * 100",
                    "Stakeholder satisfaction with transparency": "Average satisfaction score from transparency surveys"
                },
                "Strengthen ethical standards and behavior": {
                    "% of employees trained on ethics and compliance": "(Employees trained / Total employees) * 100",
                    "Number of ethical violations reported": "Total ethical violations reported",
                    "% of violations resolved promptly": "(Violations resolved promptly / Total violations) * 100",
                    "Stakeholder perception of organizational ethics": "Average perception score from ethics surveys"
                },
                "Enhance decision-making and oversight": {
                    "% of strategic decisions reviewed by governance bodies": "(Decisions reviewed / Total decisions) * 100",
                    "Number of internal audits completed": "Total internal audits completed",
                    "% of corrective actions implemented successfully": "(Actions implemented successfully / Total actions) * 100",
                    "Stakeholder satisfaction with governance": "Average satisfaction score from governance surveys"
                },
                "Increase corporate reputation and stakeholder confidence": {
                    "Corporate reputation index": "Composite score from reputation assessments",
                    "Number of positive media mentions annually": "Total positive media mentions",
                    "% improvement in external evaluations": "((Current evaluation - Previous) / Previous) * 100",
                    "Stakeholder confidence in leadership and governance": "Average confidence score from leadership surveys"
                }
            },

            #manufacturing end

            #construction start
            # Area 1: Client Satisfaction & Experience
            "Construction / Client Satisfaction & Experience": {
                "Enhance client satisfaction": {
                    "Client satisfaction survey score": "Average score from client satisfaction surveys",
                    "% of projects meeting client expectations": "(Projects meeting expectations / Total projects) * 100",
                    "% of repeat clients": "(Repeat clients / Total clients) * 100",
                    "Number of positive client testimonials": "Total positive testimonials received"
                },
                "Strengthen client relationships": {
                    "% of projects with proactive client engagement": "(Projects with proactive engagement / Total projects) * 100",
                    "Number of follow-up meetings with clients": "Total follow-up meetings conducted",
                    "Client retention rate": "(Clients retained / Total clients) * 100",
                    "Stakeholder satisfaction with relationship management": "Average satisfaction score from relationship management surveys"
                },
                "Improve responsiveness to client inquiries": {
                    "Average response time to client questions": "Total response time / Number of inquiries",
                    "% of inquiries resolved within SLA": "(Inquiries resolved within SLA / Total inquiries) * 100",
                    "Number of client complaints addressed promptly": "Total complaints addressed promptly",
                    "Client satisfaction with responsiveness": "Average satisfaction score from responsiveness surveys"
                },
                "Increase trust and credibility": {
                    "Corporate reputation index among clients": "Composite score from client reputation assessments",
                    "% of projects delivered as promised": "(Projects delivered as promised / Total projects) * 100",
                    "Number of projects recognized for excellence": "Total projects receiving awards or recognition",
                    "Stakeholder confidence in organization": "Average confidence score from stakeholder surveys"
                },
                "Improve contract clarity and communication": {
                    "% of contracts delivered without errors": "(Error-free contracts / Total contracts) * 100",
                    "Number of contract clarifications requested": "Total clarification requests received",
                    "Average time to resolve contract issues": "Total resolution time / Number of contract issues",
                    "Client perception of contract transparency": "Average transparency score from client surveys"
                },
                "Enhance post-project evaluation": {
                    "Number of project evaluation reports shared": "Total evaluation reports shared with clients",
                    "% of client feedback incorporated into future projects": "(Feedback incorporated / Total feedback) * 100",
                    "Reduction in recurring project complaints": "((Previous recurring complaints - Current) / Previous) * 100",
                    "Client satisfaction with post-project evaluation": "Average satisfaction score from post-project evaluation surveys"
                },
                "Foster long-term client partnerships": {
                    "Number of multi-year projects signed": "Total multi-year project agreements",
                    "% of clients participating in advisory councils": "(Clients in advisory roles / Total clients) * 100",
                    "Number of joint improvement initiatives": "Total joint initiatives with clients",
                    "Client trust index": "Composite trust score from client surveys"
                },
                "Promote innovative client solutions": {
                    "Number of tailored solutions implemented per project": "Total tailored solutions implemented",
                    "% of client requests for innovation fulfilled": "(Innovation requests fulfilled / Total requests) * 100",
                    "Number of project process improvements suggested by clients": "Total client-suggested improvements",
                    "Stakeholder perception of client-focused innovation": "Average perception score from innovation surveys"
                }
            },

            # Area 2: Community & Citizen Engagement
            "Construction / Community & Citizen Engagement": {
                "Increase community involvement in projects": {
                    "Number of community engagement sessions per project": "Total engagement sessions / Number of projects",
                    "% of community feedback addressed": "(Feedback addressed / Total feedback) * 100",
                    "Participation rate of community members in consultations": "(Participants / Total community) * 100",
                    "Community satisfaction with engagement": "Average satisfaction score from community surveys"
                },
                "Enhance transparency for citizens and stakeholders": {
                    "% of project updates communicated to community and authorities": "(Updates communicated / Total updates) * 100",
                    "Number of public reports or briefings shared": "Total public reports shared",
                    "Stakeholder understanding of project scope and impact": "Average understanding score from stakeholder surveys",
                    "Citizen and stakeholder satisfaction with transparency": "Average satisfaction score from transparency surveys"
                },
                "Minimize negative impact on community": {
                    "Number of community complaints related to project operations": "Total community complaints received",
                    "% of complaints resolved within agreed timeframe": "(Complaints resolved on time / Total complaints) * 100",
                    "Reduction in repeat complaints": "((Previous repeat complaints - Current) / Previous) * 100",
                    "Community perception of project impact": "Average perception score from community impact surveys"
                },
                "Promote community development & local benefits": {
                    "Number of local infrastructure improvements linked to projects": "Total local improvements implemented",
                    "% of projects creating local employment opportunities": "(Projects with local employment / Total projects) * 100",
                    "Number of skills development initiatives for local community": "Total skills development initiatives",
                    "Stakeholder satisfaction with developmental impact": "Average satisfaction score from developmental impact surveys"
                },
                "Encourage local participation in planning": {
                    "Number of local planning meetings held": "Total planning meetings conducted",
                    "% of community suggestions implemented": "(Suggestions implemented / Total suggestions) * 100",
                    "Stakeholder perception of participatory planning": "Average perception score from planning surveys",
                    "Number of joint initiatives with community": "Total joint initiatives with community"
                },
                "Strengthen communication channels": {
                    "Number of community newsletters distributed": "Total newsletters distributed",
                    "% of inquiries responded to within timeframe": "(Inquiries responded on time / Total inquiries) * 100",
                    "Community satisfaction with communication clarity": "Average satisfaction score from communication surveys",
                    "Reduction in miscommunication complaints": "((Previous miscommunication complaints - Current) / Previous) * 100"
                },
                "Enhance social awareness programs": {
                    "Number of social programs conducted per project": "Total social programs / Number of projects",
                    "% of population reached by programs": "(Population reached / Total population) * 100",
                    "Stakeholder perception of social impact": "Average perception score from social impact surveys",
                    "Community engagement satisfaction index": "Composite satisfaction score from engagement surveys"
                },
                "Promote equity and inclusiveness": {
                    "% of projects benefiting marginalized groups": "(Projects benefiting marginalized groups / Total projects) * 100",
                    "Number of initiatives supporting vulnerable populations": "Total initiatives for vulnerable populations",
                    "Stakeholder perception of equitable benefits": "Average perception score from equity surveys",
                    "Improvement in accessibility to project resources": "((Current accessibility - Previous) / Previous) * 100"
                }
            },

            # Area 3: Housing & Residential Development
            "Construction / Housing & Residential Development": {
                "Increase access to safe housing": {
                    "Number of housing units delivered on schedule": "Total housing units delivered on time",
                    "% of housing units meeting quality and safety standards": "(Units meeting standards / Total units) * 100",
                    "Stakeholder satisfaction with housing quality": "Average satisfaction score from housing quality surveys",
                    "% of low-income households benefitting": "(Low-income households benefitting / Total households) * 100"
                },
                "Enhance housing affordability": {
                    "% of housing units affordable to target population": "(Affordable units / Total units) * 100",
                    "Number of housing subsidies or support programs delivered": "Total subsidy programs delivered",
                    "Stakeholder perception of affordability": "Average perception score from affordability surveys",
                    "% reduction in complaints about housing cost": "((Previous cost complaints - Current) / Previous) * 100"
                },
                "Promote sustainable and safe living environments": {
                    "% of housing projects with green/sustainable features": "(Sustainable projects / Total projects) * 100",
                    "Number of safety inspections passed per project": "Total safety inspections passed / Number of projects",
                    "Stakeholder satisfaction with environmental standards": "Average satisfaction score from environmental surveys",
                    "Number of houses with access to basic utilities (water, electricity)": "Total houses with utility access"
                },
                "Foster community engagement in housing projects": {
                    "Number of community consultations conducted": "Total community consultations held",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Satisfaction with participation in planning": "Average satisfaction score from participation surveys",
                    "Number of local jobs created through housing projects": "Total local jobs created"
                },
                "Improve construction quality and standards": {
                    "% of housing projects meeting international construction standards": "(Projects meeting standards / Total projects) * 100",
                    "Number of defects reported and resolved": "Total defects resolved",
                    "Average construction inspection score": "Average score from construction inspections",
                    "Reduction in safety violations": "((Previous violations - Current violations) / Previous violations) * 100"
                },
                "Increase housing project efficiency": {
                    "Average project completion time": "Total completion time / Number of projects",
                    "% of projects delivered within budget": "(Projects within budget / Total projects) * 100",
                    "Number of delays caused by resource constraints": "Total delays due to resource constraints",
                    "Stakeholder satisfaction with project efficiency": "Average satisfaction score from efficiency surveys"
                },
                "Promote housing innovation": {
                    "Number of innovative housing designs implemented": "Total innovative designs implemented",
                    "% of energy-efficient housing units delivered": "(Energy-efficient units / Total units) * 100",
                    "Stakeholder perception of innovative features": "Average perception score from innovation surveys",
                    "Number of projects using smart home technologies": "Total projects with smart technologies"
                },
                "Support community capacity building": {
                    "Number of training sessions for local workforce": "Total training sessions conducted",
                    "% of housing projects employing local labor": "(Projects with local labor / Total projects) * 100",
                    "Stakeholder perception of skill development": "Average perception score from skill development surveys",
                    "Number of partnerships with local suppliers": "Total local supplier partnerships"
                }
            },

            # Area 4: Roads & Connectivity
            "Construction / Roads & Connectivity": {
                "Improve road network coverage": {
                    "Kilometers of new roads constructed": "Total kilometers of new roads built",
                    "% of planned roads completed on schedule": "(Roads completed on schedule / Total planned) * 100",
                    "Stakeholder satisfaction with road coverage": "Average satisfaction score from road coverage surveys",
                    "Reduction in travel time due to new roads": "((Previous travel time - Current) / Previous) * 100"
                },
                "Enhance access for remote or underserved areas": {
                    "% of previously inaccessible areas connected": "(Areas connected / Total inaccessible areas) * 100",
                    "Number of new transport links established": "Total new transport links created",
                    "Stakeholder satisfaction with accessibility improvements": "Average satisfaction score from accessibility surveys",
                    "Number of local businesses benefiting from road improvements": "Total businesses benefiting"
                },
                "Strengthen road project management": {
                    "% of projects delivered within planned budget": "(Projects within budget / Total projects) * 100",
                    "Average project completion time": "Total completion time / Number of projects",
                    "Number of delays caused by resource constraints": "Total delays due to resource constraints",
                    "Stakeholder satisfaction with project management": "Average satisfaction score from project management surveys"
                },
                "Improve traffic and mobility solutions": {
                    "% reduction in congestion after project completion": "((Previous congestion - Current) / Previous) * 100",
                    "Number of traffic management initiatives implemented": "Total traffic initiatives implemented",
                    "Stakeholder perception of mobility improvement": "Average perception score from mobility surveys",
                    "Average reduction in travel time for citizens": "((Previous travel time - Current) / Previous) * 100"
                },
                "Promote local economic benefits from road projects": {
                    "Number of local contractors engaged": "Total local contractors involved",
                    "% of materials sourced locally": "(Local materials / Total materials) * 100",
                    "Jobs created in local communities": "Total jobs created in local communities",
                    "Stakeholder satisfaction with local economic impact": "Average satisfaction score from economic impact surveys"
                },
                "Enhance stakeholder communication in road projects": {
                    "Number of community consultations held": "Total community consultations conducted",
                    "% of feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with updates": "Average satisfaction score from update surveys",
                    "Number of awareness campaigns conducted": "Total awareness campaigns conducted"
                },
                "Promote environmentally sustainable road construction": {
                    "% of roads with eco-friendly materials": "(Eco-friendly roads / Total roads) * 100",
                    "Number of green initiatives implemented": "Total green initiatives implemented",
                    "Reduction in environmental complaints": "((Previous complaints - Current) / Previous) * 100",
                    "Stakeholder perception of sustainable infrastructure": "Average perception score from sustainability surveys"
                },
                "Increase road quality and safety": {
                    "% of roads passing quality inspections": "(Roads passing inspections / Total roads) * 100",
                    "Number of road accident reductions": "((Previous accidents - Current) / Previous) * 100",
                    "Stakeholder perception of road safety": "Average perception score from safety surveys",
                    "Number of maintenance works completed on schedule": "Total maintenance works completed on time"
                }
            },

            # Area 5: Transport Infrastructure & Public Mobility
            "Construction / Transport Infrastructure & Public Mobility": {
                "Enhance public transport accessibility": {
                    "Number of new public transport routes implemented": "Total new transport routes created",
                    "% of population with access to public transport within 2 km": "(Population with access / Total population) * 100",
                    "Stakeholder satisfaction with accessibility improvements": "Average satisfaction score from accessibility surveys",
                    "Increase in public transport usage": "((Current usage - Previous) / Previous) * 100"
                },
                "Improve transport infrastructure quality": {
                    "% of transport infrastructure passing quality inspections": "(Infrastructure passing inspections / Total) * 100",
                    "Number of maintenance works completed on schedule": "Total maintenance works completed on time",
                    "Stakeholder satisfaction with infrastructure quality": "Average satisfaction score from quality surveys",
                    "Reduction in service disruptions": "((Previous disruptions - Current) / Previous) * 100"
                },
                "Promote sustainable transport solutions": {
                    "% of transport projects using green technology": "(Green technology projects / Total projects) * 100",
                    "Number of bike lanes and pedestrian paths created": "Total bike lanes and paths created",
                    "Reduction in emissions from transport projects": "((Previous emissions - Current) / Previous) * 100",
                    "Stakeholder perception of sustainable mobility": "Average perception score from sustainability surveys"
                },
                "Increase connectivity with other regions": {
                    "Number of new intercity transport links established": "Total intercity links created",
                    "Reduction in average travel time between regions": "((Previous travel time - Current) / Previous) * 100",
                    "Stakeholder perception of improved connectivity": "Average perception score from connectivity surveys",
                    "Increase in regional trade facilitated by transport projects": "((Current trade - Previous) / Previous) * 100"
                },
                "Enhance safety in transport systems": {
                    "Number of safety audits conducted": "Total safety audits performed",
                    "Reduction in transport-related accidents": "((Previous accidents - Current) / Previous) * 100",
                    "Stakeholder perception of safety": "Average perception score from safety surveys",
                    "% of projects meeting transport safety standards": "(Projects meeting standards / Total projects) * 100"
                },
                "Foster stakeholder engagement in transport projects": {
                    "Number of transport planning consultations conducted": "Total planning consultations held",
                    "% of stakeholder feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participation": "Average satisfaction score from participation surveys",
                    "Number of joint initiatives with local authorities": "Total joint initiatives with authorities"
                },
                "Increase efficiency in transport operations": {
                    "% of transport infrastructure projects delivered on time": "(Projects delivered on time / Total projects) * 100",
                    "Average operational downtime reduction": "((Previous downtime - Current) / Previous) * 100",
                    "Stakeholder satisfaction with project delivery": "Average satisfaction score from delivery surveys",
                    "Reduction in operational bottlenecks": "((Previous bottlenecks - Current) / Previous) * 100"
                },
                "Support socio-economic development through transport": {
                    "Number of jobs created through transport projects": "Total jobs created",
                    "% of materials sourced locally": "(Local materials / Total materials) * 100",
                    "Number of small business beneficiaries from transport infrastructure": "Total small business beneficiaries",
                    "Stakeholder satisfaction with local economic impact": "Average satisfaction score from economic impact surveys"
                }
            },

            # Area 6: Water & Sanitation
            "Construction / Water & Sanitation": {
                "Increase access to safe water": {
                    "Number of households with access to clean water": "Total households with water access",
                    "% of water supply projects completed on schedule": "(Projects completed on time / Total projects) * 100",
                    "Stakeholder satisfaction with water quality": "Average satisfaction score from water quality surveys",
                    "Reduction in water-borne disease cases": "((Previous cases - Current) / Previous) * 100"
                },
                "Improve sanitation infrastructure": {
                    "Number of sanitation facilities constructed": "Total sanitation facilities built",
                    "% of projects meeting health and safety standards": "(Projects meeting standards / Total projects) * 100",
                    "Stakeholder satisfaction with sanitation services": "Average satisfaction score from sanitation surveys",
                    "Number of community awareness programs on sanitation": "Total awareness programs conducted"
                },
                "Promote water sustainability and efficiency": {
                    "% of projects with water recycling/conservation features": "(Projects with water features / Total projects) * 100",
                    "Reduction in water loss or leakage": "((Previous loss - Current) / Previous) * 100",
                    "Stakeholder perception of water sustainability": "Average perception score from sustainability surveys",
                    "Number of local water committees supported": "Total water committees supported"
                },
                "Foster community engagement in water & sanitation projects": {
                    "Number of community consultations": "Total community consultations held",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participation": "Average satisfaction score from participation surveys",
                    "Number of local jobs created through water projects": "Total local jobs created"
                },
                "Enhance water quality monitoring": {
                    "% of water samples meeting quality standards": "(Samples meeting standards / Total samples) * 100",
                    "Number of water quality inspections conducted": "Total water inspections conducted",
                    "Reduction in water contamination incidents": "((Previous incidents - Current) / Previous) * 100",
                    "Stakeholder perception of water safety": "Average perception score from water safety surveys"
                },
                "Promote sanitation education": {
                    "Number of hygiene awareness programs conducted": "Total hygiene programs conducted",
                    "% of community participation in programs": "(Participants / Total community) * 100",
                    "Reduction in sanitation-related complaints": "((Previous complaints - Current) / Previous) * 100",
                    "Stakeholder satisfaction with educational initiatives": "Average satisfaction score from education surveys"
                },
                "Improve wastewater management": {
                    "Number of wastewater treatment projects implemented": "Total wastewater projects implemented",
                    "% of wastewater safely treated before release": "(Treated wastewater / Total wastewater) * 100",
                    "Reduction in environmental pollution from wastewater": "((Previous pollution - Current) / Previous) * 100",
                    "Stakeholder perception of wastewater management effectiveness": "Average perception score from wastewater management surveys"
                },
                "Support sustainable water infrastructure development": {
                    "Number of water storage or distribution improvements": "Total water infrastructure improvements",
                    "% of projects integrating sustainable technology": "(Projects with sustainable tech / Total projects) * 100",
                    "Stakeholder satisfaction with infrastructure reliability": "Average satisfaction score from reliability surveys",
                    "Reduction in service disruptions": "((Previous disruptions - Current) / Previous) * 100"
                }
            },

            # Area 7: Public Facilities & Urban Infrastructure
            "Construction / Public Facilities & Urban Infrastructure": {
                "Expand access to schools and educational facilities": {
                    "Number of schools built or renovated": "Total schools constructed or upgraded",
                    "% of projects meeting quality and safety standards": "(Projects meeting standards / Total projects) * 100",
                    "Stakeholder satisfaction with education infrastructure": "Average satisfaction score from education infrastructure surveys",
                    "Number of students benefiting": "Total students served by new facilities"
                },
                "Expand access to healthcare facilities": {
                    "Number of hospitals/clinics constructed or upgraded": "Total healthcare facilities built or upgraded",
                    "% of projects meeting healthcare standards": "(Projects meeting standards / Total projects) * 100",
                    "Stakeholder satisfaction with healthcare facilities": "Average satisfaction score from healthcare facility surveys",
                    "Reduction in patient travel time to healthcare": "((Previous travel time - Current) / Previous) * 100"
                },
                "Improve public amenities and social infrastructure": {
                    "Number of parks, recreational areas, or community centers built": "Total public amenities constructed",
                    "% of projects completed on time": "(Projects completed on time / Total projects) * 100",
                    "Stakeholder satisfaction with amenities": "Average satisfaction score from amenity surveys",
                    "Number of community programs hosted": "Total community programs conducted"
                },
                "Strengthen urban resilience and accessibility": {
                    "Number of bridges or pedestrian pathways built": "Total bridges and pathways constructed",
                    "% of projects improving mobility for vulnerable groups": "(Projects improving mobility / Total projects) * 100",
                    "Stakeholder perception of urban accessibility": "Average perception score from accessibility surveys",
                    "Reduction in urban congestion or accessibility complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Enhance urban safety and emergency preparedness": {
                    "Number of emergency facilities built or upgraded": "Total emergency facilities constructed or upgraded",
                    "% of projects with safety protocols implemented": "(Projects with safety protocols / Total projects) * 100",
                    "Stakeholder perception of urban safety": "Average perception score from safety surveys",
                    "Reduction in emergency response times": "((Previous response time - Current) / Previous) * 100"
                },
                "Promote citizen engagement in urban planning": {
                    "Number of community planning sessions held": "Total planning sessions conducted",
                    "% of feedback implemented into urban projects": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder perception of participatory planning": "Average perception score from planning surveys",
                    "Number of citizen advisory boards created": "Total advisory boards established"
                },
                "Increase efficiency in public facility management": {
                    "% of facilities maintained within budget": "(Facilities within budget / Total facilities) * 100",
                    "Reduction in facility downtime or disruptions": "((Previous downtime - Current) / Previous) * 100",
                    "Stakeholder satisfaction with facility management": "Average satisfaction score from facility management surveys",
                    "Number of maintenance programs completed on schedule": "Total maintenance programs completed on time"
                },
                "Foster sustainable urban development": {
                    "% of projects meeting green building standards": "(Projects meeting green standards / Total projects) * 100",
                    "Number of projects integrating renewable energy": "Total projects with renewable energy",
                    "Reduction in urban carbon footprint": "((Previous carbon footprint - Current) / Previous) * 100",
                    "Stakeholder perception of sustainability impact": "Average perception score from sustainability impact surveys"
                }
            },

            # Area 8: Energy & Utilities
            "Construction / Energy & Utilities": {
                "Expand access to electricity and renewable energy": {
                    "Number of households connected to electricity": "Total households with electricity access",
                    "% of projects completed on schedule": "(Projects completed on time / Total projects) * 100",
                    "Stakeholder satisfaction with energy access": "Average satisfaction score from energy access surveys",
                    "% of renewable energy integration in projects": "(Renewable energy projects / Total projects) * 100"
                },
                "Improve reliability and efficiency of utilities": {
                    "% reduction in power outages or disruptions": "((Previous outages - Current) / Previous) * 100",
                    "Number of maintenance programs completed": "Total maintenance programs completed",
                    "Stakeholder perception of utility reliability": "Average perception score from reliability surveys",
                    "% of utilities operating at optimal capacity": "(Utilities at optimal capacity / Total utilities) * 100"
                },
                "Promote sustainable energy use": {
                    "% of projects implementing energy-saving measures": "(Projects with energy savings / Total projects) * 100",
                    "Reduction in carbon emissions from projects": "((Previous emissions - Current) / Previous) * 100",
                    "Stakeholder perception of sustainable energy initiatives": "Average perception score from sustainable energy surveys",
                    "Number of awareness programs on energy conservation": "Total awareness programs conducted"
                },
                "Foster community engagement in energy projects": {
                    "Number of consultations with local communities": "Total community consultations held",
                    "% of feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participation": "Average satisfaction score from participation surveys",
                    "Number of local jobs created through energy projects": "Total local jobs created"
                },
                "Enhance utility infrastructure planning": {
                    "% of energy infrastructure projects completed on schedule": "(Projects completed on time / Total projects) * 100",
                    "Reduction in system downtime": "((Previous downtime - Current) / Previous) * 100",
                    "Stakeholder satisfaction with infrastructure planning": "Average satisfaction score from planning surveys",
                    "Number of new energy distribution points installed": "Total distribution points installed"
                },
                "Promote energy safety and compliance": {
                    "Number of safety inspections conducted": "Total safety inspections performed",
                    "% of projects meeting regulatory compliance": "(Projects meeting compliance / Total projects) * 100",
                    "Reduction in energy-related incidents": "((Previous incidents - Current) / Previous) * 100",
                    "Stakeholder perception of safety measures": "Average perception score from safety surveys"
                },
                "Improve utility customer service": {
                    "Average response time to service requests": "Total response time / Number of requests",
                    "% of complaints resolved within SLA": "(Complaints resolved within SLA / Total complaints) * 100",
                    "Stakeholder satisfaction with service delivery": "Average satisfaction score from service delivery surveys",
                    "Number of customer support initiatives conducted": "Total customer support initiatives"
                },
                "Encourage innovative energy solutions": {
                    "Number of renewable energy pilot projects implemented": "Total pilot projects implemented",
                    "% of projects using smart energy management systems": "(Projects with smart systems / Total projects) * 100",
                    "Stakeholder perception of energy innovation": "Average perception score from innovation surveys",
                    "Number of new technologies adopted in projects": "Total new technologies adopted"
                }
            },

            # Area 9: Environmental Management & Sustainability
            "Construction / Environmental Management & Sustainability": {
                "Minimize environmental impact of projects": {
                    "% of projects with environmental assessments completed": "(Projects with assessments / Total projects) * 100",
                    "Reduction in carbon emissions per project": "((Previous emissions - Current) / Previous) * 100",
                    "Number of environmental incidents reported": "Total environmental incidents",
                    "Stakeholder perception of environmental stewardship": "Average perception score from environmental stewardship surveys"
                },
                "Promote green construction practices": {
                    "% of projects using eco-friendly materials": "(Projects with eco-materials / Total projects) * 100",
                    "Number of sustainable building certifications received": "Total sustainability certifications obtained",
                    "Reduction in construction waste": "((Previous waste - Current) / Previous) * 100",
                    "Stakeholder satisfaction with sustainability practices": "Average satisfaction score from sustainability practice surveys"
                },
                "Enhance biodiversity and ecosystem protection": {
                    "Number of conservation initiatives implemented": "Total conservation initiatives",
                    "% of projects avoiding critical habitats": "(Projects avoiding habitats / Total projects) * 100",
                    "Reduction in environmental complaints": "((Previous complaints - Current) / Previous) * 100",
                    "Stakeholder perception of ecological impact": "Average perception score from ecological impact surveys"
                },
                "Improve waste management": {
                    "% of waste recycled or reused": "(Waste recycled / Total waste) * 100",
                    "Number of waste management plans implemented": "Total waste management plans implemented",
                    "Reduction in landfill contributions": "((Previous landfill waste - Current) / Previous) * 100",
                    "Stakeholder satisfaction with waste handling": "Average satisfaction score from waste handling surveys"
                },
                "Foster community environmental awareness": {
                    "Number of environmental education programs conducted": "Total environmental education programs",
                    "% of population reached through campaigns": "(Population reached / Total population) * 100",
                    "Stakeholder perception of awareness initiatives": "Average perception score from awareness surveys",
                    "Number of local environmental committees established": "Total environmental committees established"
                },
                "Ensure regulatory compliance": {
                    "% of projects compliant with environmental laws": "(Compliant projects / Total projects) * 100",
                    "Number of audits conducted": "Total environmental audits conducted",
                    "Reduction in non-compliance incidents": "((Previous non-compliance - Current) / Previous) * 100",
                    "Stakeholder perception of adherence to regulations": "Average perception score from regulatory compliance surveys"
                },
                "Promote water and energy conservation": {
                    "% reduction in water usage in projects": "((Previous water usage - Current) / Previous) * 100",
                    "% reduction in energy consumption per project": "((Previous energy consumption - Current) / Previous) * 100",
                    "Number of conservation initiatives implemented": "Total conservation initiatives",
                    "Stakeholder perception of resource efficiency": "Average perception score from resource efficiency surveys"
                },
                "Support sustainable urban planning": {
                    "% of projects integrating green infrastructure": "(Projects with green infrastructure / Total projects) * 100",
                    "Number of eco-friendly urban projects completed": "Total eco-friendly urban projects",
                    "Stakeholder perception of urban sustainability": "Average perception score from urban sustainability surveys",
                    "Reduction in environmental complaints from citizens": "((Previous complaints - Current) / Previous) * 100"
                }
            },

            # Area 10: Disaster Resilience & Safety
            "Construction / Disaster Resilience & Safety": {
                "Enhance structural safety of buildings": {
                    "% of projects meeting structural safety standards": "(Projects meeting standards / Total projects) * 100",
                    "Number of safety inspections conducted": "Total safety inspections performed",
                    "Reduction in structural failures": "((Previous failures - Current) / Previous) * 100",
                    "Stakeholder perception of building safety": "Average perception score from building safety surveys"
                },
                "Improve disaster preparedness": {
                    "Number of emergency drills conducted": "Total emergency drills performed",
                    "% of staff trained in disaster response": "(Staff trained / Total staff) * 100",
                    "Reduction in response time during emergencies": "((Previous response time - Current) / Previous) * 100",
                    "Stakeholder satisfaction with preparedness": "Average satisfaction score from preparedness surveys"
                },
                "Strengthen early warning systems": {
                    "Number of warning systems installed per community": "Total warning systems installed",
                    "% of population covered by early warning systems": "(Population covered / Total population) * 100",
                    "Reduction in disaster-related damages": "((Previous damages - Current) / Previous) * 100",
                    "Stakeholder perception of warning effectiveness": "Average perception score from warning system surveys"
                },
                "Promote resilient infrastructure": {
                    "% of infrastructure designed to withstand natural hazards": "(Resilient infrastructure / Total infrastructure) * 100",
                    "Number of retrofitting projects completed": "Total retrofitting projects completed",
                    "Reduction in damage from natural events": "((Previous damage - Current) / Previous) * 100",
                    "Stakeholder satisfaction with resilience measures": "Average satisfaction score from resilience surveys"
                },
                "Enhance community disaster awareness": {
                    "Number of public awareness campaigns conducted": "Total awareness campaigns conducted",
                    "% of community participation in training programs": "(Participants / Total community) * 100",
                    "Stakeholder perception of disaster knowledge": "Average perception score from disaster knowledge surveys",
                    "Reduction in preventable disaster-related incidents": "((Previous incidents - Current) / Previous) * 100"
                },
                "Improve emergency response capacity": {
                    "Average emergency response time": "Total response time / Number of emergencies",
                    "Number of emergency facilities upgraded": "Total emergency facilities upgraded",
                    "Reduction in casualties or property loss": "((Previous losses - Current) / Previous) * 100",
                    "Stakeholder perception of response efficiency": "Average perception score from response efficiency surveys"
                },
                "Ensure regulatory compliance in safety": {
                    "% of projects compliant with safety and disaster regulations": "(Compliant projects / Total projects) * 100",
                    "Number of safety audits conducted": "Total safety audits performed",
                    "Reduction in non-compliance incidents": "((Previous non-compliance - Current) / Previous) * 100",
                    "Stakeholder perception of adherence to standards": "Average perception score from safety standard surveys"
                },
                "Promote collaboration with safety agencies": {
                    "Number of joint initiatives with disaster management authorities": "Total joint initiatives with authorities",
                    "% of projects coordinated with emergency agencies": "(Projects coordinated / Total projects) * 100",
                    "Reduction in response gaps during disasters": "((Previous gaps - Current) / Previous) * 100",
                    "Stakeholder perception of collaboration effectiveness": "Average perception score from collaboration surveys"
                }
            },

            # Area 11: ICT & Smart Infrastructure
            "Construction / ICT & Smart Infrastructure": {
                "Increase ICT integration in projects": {
                    "% of projects using smart technologies": "(Projects with smart tech / Total projects) * 100",
                    "Number of ICT-enabled infrastructure solutions implemented": "Total ICT solutions implemented",
                    "Stakeholder satisfaction with ICT features": "Average satisfaction score from ICT feature surveys",
                    "Reduction in operational inefficiencies through technology": "((Previous inefficiencies - Current) / Previous) * 100"
                },
                "Enhance data management and analytics": {
                    "Number of infrastructure projects using data analytics": "Total projects using data analytics",
                    "% of projects with real-time monitoring systems": "(Projects with monitoring / Total projects) * 100",
                    "Stakeholder perception of data transparency": "Average perception score from data transparency surveys",
                    "Reduction in decision-making delays": "((Previous delays - Current) / Previous) * 100"
                },
                "Improve digital citizen services": {
                    "Number of smart services available to citizens": "Total smart services available",
                    "% of population using digital infrastructure services": "(Population using services / Total population) * 100",
                    "Stakeholder satisfaction with digital access": "Average satisfaction score from digital access surveys",
                    "Number of online support or complaint resolutions": "Total online resolutions"
                },
                "Promote cybersecurity in infrastructure": {
                    "Number of cybersecurity audits conducted": "Total cybersecurity audits performed",
                    "% of ICT projects compliant with security standards": "(Compliant projects / Total projects) * 100",
                    "Reduction in security incidents": "((Previous incidents - Current) / Previous) * 100",
                    "Stakeholder perception of digital safety": "Average perception score from digital safety surveys"
                },
                "Enhance connectivity and network infrastructure": {
                    "Kilometers of fiber optic or broadband networks installed": "Total network kilometers installed",
                    "% of population with access to high-speed internet": "(Population with access / Total population) * 100",
                    "Stakeholder satisfaction with connectivity": "Average satisfaction score from connectivity surveys",
                    "Number of ICT infrastructure projects completed on schedule": "Total ICT projects completed on time"
                },
                "Foster innovation in smart infrastructure": {
                    "Number of pilot smart infrastructure projects implemented": "Total pilot projects implemented",
                    "% of projects adopting innovative technology solutions": "(Projects with innovative tech / Total projects) * 100",
                    "Stakeholder perception of innovation": "Average perception score from innovation surveys",
                    "Number of technology partnerships formed": "Total technology partnerships"
                },
                "Support operational efficiency through ICT": {
                    "% reduction in operational downtime through ICT solutions": "((Previous downtime - Current) / Previous) * 100",
                    "Number of automated monitoring systems deployed": "Total automated systems deployed",
                    "Stakeholder satisfaction with operational efficiency": "Average satisfaction score from operational efficiency surveys",
                    "Reduction in manual process errors": "((Previous errors - Current) / Previous) * 100"
                },
                "Promote ICT training and community engagement": {
                    "Number of ICT training sessions for staff and citizens": "Total ICT training sessions conducted",
                    "% of population trained on smart infrastructure usage": "(Population trained / Total population) * 100",
                    "Stakeholder satisfaction with training programs": "Average satisfaction score from training program surveys",
                    "Number of community ICT initiatives implemented": "Total community ICT initiatives"
                }
            },

            # Area 12: Parks, Recreation & Social Amenities
            "Construction / Parks, Recreation & Social Amenities": {
                "Expand public green spaces": {
                    "Number of parks constructed or upgraded": "Total parks built or upgraded",
                    "% of parks meeting quality standards": "(Parks meeting standards / Total parks) * 100",
                    "Stakeholder satisfaction with green spaces": "Average satisfaction score from green space surveys",
                    "Number of community events hosted in parks": "Total community events hosted"
                },
                "Promote recreational facilities accessibility": {
                    "% of population with access to recreational facilities": "(Population with access / Total population) * 100",
                    "Number of new sports or leisure facilities built": "Total recreational facilities built",
                    "Stakeholder perception of facility accessibility": "Average perception score from accessibility surveys",
                    "Participation rate in recreational programs": "(Participants / Total population) * 100"
                },
                "Enhance safety in recreational areas": {
                    "Number of safety inspections conducted": "Total safety inspections performed",
                    "% of facilities meeting safety standards": "(Facilities meeting standards / Total facilities) * 100",
                    "Reduction in accident incidents in recreational areas": "((Previous accidents - Current) / Previous) * 100",
                    "Stakeholder perception of safety in public spaces": "Average perception score from public safety surveys"
                },
                "Foster community engagement in amenities planning": {
                    "Number of community consultation sessions held": "Total consultation sessions conducted",
                    "% of feedback implemented into project design": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder perception of participation": "Average perception score from participation surveys",
                    "Number of joint initiatives with local groups": "Total joint initiatives with local groups"
                },
                "Promote environmental sustainability in parks": {
                    "% of parks with green and eco-friendly features": "(Parks with green features / Total parks) * 100",
                    "Number of tree planting or biodiversity projects conducted": "Total environmental projects conducted",
                    "Stakeholder satisfaction with environmental impact": "Average satisfaction score from environmental impact surveys",
                    "Reduction in environmental complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Improve maintenance and operations": {
                    "% of parks maintained within budget": "(Parks within budget / Total parks) * 100",
                    "Number of maintenance works completed on schedule": "Total maintenance works completed on time",
                    "Stakeholder satisfaction with facility upkeep": "Average satisfaction score from upkeep surveys",
                    "Reduction in service disruptions": "((Previous disruptions - Current) / Previous) * 100"
                },
                "Support inclusive recreational initiatives": {
                    "% of facilities accessible to persons with disabilities": "(Accessible facilities / Total facilities) * 100",
                    "Number of inclusive community programs conducted": "Total inclusive programs conducted",
                    "Stakeholder perception of inclusivity": "Average perception score from inclusivity surveys",
                    "Participation rate of marginalized groups": "(Marginalized group participants / Total participants) * 100"
                },
                "Encourage socio-cultural programs in amenities": {
                    "Number of cultural or educational events hosted": "Total cultural events hosted",
                    "Stakeholder satisfaction with community programs": "Average satisfaction score from community program surveys",
                    "Participation rate of local communities": "(Local participants / Total participants) * 100",
                    "Number of partnerships with cultural organizations": "Total cultural partnerships"
                }
            },

            # Area 13: Industrial & Commercial Infrastructure
            "Construction / Industrial & Commercial Infrastructure": {
                "Expand industrial zones and facilities": {
                    "Number of industrial units constructed or upgraded": "Total industrial units built or upgraded",
                    "% of projects meeting quality and safety standards": "(Projects meeting standards / Total projects) * 100",
                    "Stakeholder satisfaction with industrial facilities": "Average satisfaction score from industrial facility surveys",
                    "Number of businesses benefitting from new infrastructure": "Total businesses benefitting"
                },
                "Improve commercial building quality": {
                    "% of commercial projects meeting design and safety standards": "(Projects meeting standards / Total projects) * 100",
                    "Number of defect reports resolved": "Total defect reports resolved",
                    "Stakeholder perception of quality": "Average perception score from quality surveys",
                    "Number of certifications obtained": "Total quality certifications obtained"
                },
                "Enhance energy efficiency in industrial projects": {
                    "% of projects using energy-saving systems": "(Projects with energy systems / Total projects) * 100",
                    "Reduction in energy consumption per facility": "((Previous consumption - Current) / Previous) * 100",
                    "Stakeholder perception of efficiency": "Average perception score from efficiency surveys",
                    "Number of sustainable energy certifications": "Total energy certifications obtained"
                },
                "Promote access to industrial utilities": {
                    "% of industrial facilities connected to power, water, and ICT": "(Facilities connected / Total facilities) * 100",
                    "Number of utility upgrades completed": "Total utility upgrades completed",
                    "Stakeholder satisfaction with utility access": "Average satisfaction score from utility access surveys",
                    "Reduction in service disruptions": "((Previous disruptions - Current) / Previous) * 100"
                },
                "Foster industrial community engagement": {
                    "Number of consultations with local businesses": "Total business consultations held",
                    "% of feedback implemented in project design": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participation": "Average satisfaction score from participation surveys",
                    "Number of joint development initiatives": "Total joint development initiatives"
                },
                "Strengthen safety and compliance in industrial infrastructure": {
                    "% of projects compliant with industrial safety standards": "(Compliant projects / Total projects) * 100",
                    "Number of safety inspections conducted": "Total safety inspections performed",
                    "Reduction in accidents/incidents": "((Previous accidents - Current) / Previous) * 100",
                    "Stakeholder perception of compliance": "Average perception score from compliance surveys"
                },
                "Improve operational efficiency in industrial zones": {
                    "% reduction in downtime due to infrastructure issues": "((Previous downtime - Current) / Previous) * 100",
                    "Number of process automation initiatives": "Total automation initiatives implemented",
                    "Stakeholder satisfaction with operational efficiency": "Average satisfaction score from operational efficiency surveys",
                    "Number of operational improvements implemented": "Total operational improvements"
                },
                "Encourage innovation and industrial growth": {
                    "Number of pilot industrial technology projects": "Total pilot technology projects",
                    "% of projects adopting innovative industrial solutions": "(Projects with innovative solutions / Total projects) * 100",
                    "Stakeholder perception of innovation impact": "Average perception score from innovation impact surveys",
                    "Number of new industrial partnerships formed": "Total new industrial partnerships"
                }
            },

            # Area 14: Housing & Residential Infrastructure
            "Construction / Housing & Residential Infrastructure": {
                "Increase access to affordable housing": {
                    "Number of housing units delivered on schedule": "Total housing units delivered on time",
                    "% of units affordable to target population": "(Affordable units / Total units) * 100",
                    "Stakeholder satisfaction with housing availability": "Average satisfaction score from housing availability surveys",
                    "Reduction in complaints about housing cost": "((Previous cost complaints - Current) / Previous) * 100"
                },
                "Improve housing quality and safety": {
                    "% of housing units meeting quality and safety standards": "(Units meeting standards / Total units) * 100",
                    "Number of safety inspections conducted": "Total safety inspections performed",
                    "Reduction in construction defects": "((Previous defects - Current) / Previous) * 100",
                    "Stakeholder perception of housing quality": "Average perception score from housing quality surveys"
                },
                "Promote sustainable and energy-efficient housing": {
                    "% of units with green or energy-saving features": "(Units with green features / Total units) * 100",
                    "Reduction in household energy consumption": "((Previous consumption - Current) / Previous) * 100",
                    "Stakeholder satisfaction with sustainability features": "Average satisfaction score from sustainability feature surveys",
                    "Number of sustainable building certifications obtained": "Total sustainability certifications"
                },
                "Enhance community participation in housing projects": {
                    "Number of community consultations conducted": "Total community consultations held",
                    "% of feedback incorporated into design": "(Feedback incorporated / Total feedback) * 100",
                    "Stakeholder perception of participatory planning": "Average perception score from planning surveys",
                    "Number of local jobs created through housing projects": "Total local jobs created"
                },
                "Foster social inclusion in housing initiatives": {
                    "% of housing units allocated to low-income or marginalized groups": "(Units for marginalized groups / Total units) * 100",
                    "Number of inclusive housing programs implemented": "Total inclusive housing programs",
                    "Stakeholder perception of equity in housing allocation": "Average perception score from equity surveys",
                    "Reduction in complaints related to housing access": "((Previous access complaints - Current) / Previous) * 100"
                },
                "Promote housing maintenance and management": {
                    "% of housing units maintained within schedule": "(Units maintained on schedule / Total units) * 100",
                    "Number of maintenance requests resolved": "Total maintenance requests resolved",
                    "Stakeholder satisfaction with housing management": "Average satisfaction score from housing management surveys",
                    "Reduction in recurring maintenance issues": "((Previous recurring issues - Current) / Previous) * 100"
                },
                "Support housing financing and subsidies": {
                    "Number of housing loans or subsidies provided": "Total housing financial supports provided",
                    "% of target population accessing financing options": "(Population accessing financing / Target population) * 100",
                    "Stakeholder satisfaction with financial support programs": "Average satisfaction score from financial support surveys",
                    "Reduction in financial barriers for housing": "((Previous barriers - Current) / Previous) * 100"
                },
                "Encourage innovation in residential development": {
                    "Number of pilot housing technology projects": "Total pilot housing projects",
                    "% of units using innovative construction methods": "(Units with innovative methods / Total units) * 100",
                    "Stakeholder perception of innovative housing solutions": "Average perception score from housing innovation surveys",
                    "Number of new partnerships for housing development": "Total new housing partnerships"
                }
            },

            # Area 15: Roads & Transport Infrastructure – Urban Mobility
            "Construction / Roads & Transport Infrastructure – Urban Mobility": {
                "Improve urban road network connectivity": {
                    "Kilometers of new roads constructed in urban areas": "Total urban road kilometers built",
                    "% of planned urban roads completed on schedule": "(Urban roads completed on time / Total planned) * 100",
                    "Stakeholder satisfaction with urban connectivity": "Average satisfaction score from urban connectivity surveys",
                    "Reduction in travel time in urban zones": "((Previous travel time - Current) / Previous) * 100"
                },
                "Ensure road safety and quality in cities": {
                    "% of urban roads passing quality inspections": "(Urban roads passing inspections / Total urban roads) * 100",
                    "Number of accident reductions due to road improvements": "((Previous accidents - Current) / Previous) * 100",
                    "Stakeholder perception of urban road safety": "Average perception score from urban safety surveys",
                    "Number of maintenance works completed on schedule": "Total maintenance works completed on time"
                },
                "Enhance accessibility for vulnerable groups": {
                    "% of urban roads adapted for persons with disabilities": "(Accessible urban roads / Total urban roads) * 100",
                    "Number of pedestrian pathways and crossings built": "Total pedestrian infrastructure built",
                    "Stakeholder satisfaction with accessibility improvements": "Average satisfaction score from accessibility surveys",
                    "Reduction in mobility-related complaints": "((Previous mobility complaints - Current) / Previous) * 100"
                },
                "Promote public transport infrastructure": {
                    "Number of public transport hubs constructed or upgraded": "Total transport hubs built or upgraded",
                    "% of projects improving transit efficiency": "(Projects improving efficiency / Total projects) * 100",
                    "Stakeholder satisfaction with public transport access": "Average satisfaction score from public transport surveys",
                    "Reduction in public transport delays": "((Previous delays - Current) / Previous) * 100"
                },
                "Integrate smart transport solutions": {
                    "Number of smart traffic management systems implemented": "Total smart traffic systems implemented",
                    "% of traffic systems operating optimally": "(Optimal traffic systems / Total systems) * 100",
                    "Stakeholder perception of traffic efficiency": "Average perception score from traffic efficiency surveys",
                    "Reduction in traffic congestion": "((Previous congestion - Current) / Previous) * 100"
                },
                "Enhance environmental sustainability of transport projects": {
                    "% of roads with eco-friendly materials": "(Eco-friendly urban roads / Total urban roads) * 100",
                    "Number of green transport initiatives implemented": "Total green transport initiatives",
                    "Reduction in vehicular emissions": "((Previous emissions - Current) / Previous) * 100",
                    "Stakeholder perception of sustainable transport": "Average perception score from sustainable transport surveys"
                },
                "Foster community engagement in transport planning": {
                    "Number of community consultations on transport projects": "Total transport consultations held",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with planning process": "Average satisfaction score from planning process surveys",
                    "Number of joint transport development initiatives": "Total joint transport initiatives"
                },
                "Improve project delivery and timeliness": {
                    "% of urban road projects delivered on schedule": "(Urban projects delivered on time / Total projects) * 100",
                    "Average delay per project": "Total delay time / Number of projects",
                    "Stakeholder satisfaction with project timeliness": "Average satisfaction score from timeliness surveys",
                    "Number of milestones achieved on time": "Total milestones achieved on schedule"
                }
            },

            # Area 16: Roads & Transport Infrastructure – Rural Connectivity
            "Construction / Roads & Transport Infrastructure – Rural Connectivity": {
                "Expand rural road network": {
                    "Kilometers of rural roads constructed": "Total rural road kilometers built",
                    "% of planned rural roads completed": "(Rural roads completed / Total planned) * 100",
                    "Stakeholder satisfaction with rural connectivity": "Average satisfaction score from rural connectivity surveys",
                    "Reduction in travel time for rural communities": "((Previous travel time - Current) / Previous) * 100"
                },
                "Ensure rural road quality and safety": {
                    "% of rural roads passing quality inspections": "(Rural roads passing inspections / Total rural roads) * 100",
                    "Number of accident reductions in rural areas": "((Previous rural accidents - Current) / Previous) * 100",
                    "Stakeholder perception of rural road safety": "Average perception score from rural safety surveys",
                    "Number of maintenance works completed on schedule": "Total rural maintenance works completed on time"
                },
                "Enhance access to remote communities": {
                    "% of previously inaccessible areas connected": "(Inaccessible areas connected / Total inaccessible) * 100",
                    "Number of new transport links established": "Total new rural transport links",
                    "Stakeholder satisfaction with rural accessibility": "Average satisfaction score from rural accessibility surveys",
                    "Number of local businesses benefiting from improved transport": "Total rural businesses benefiting"
                },
                "Promote sustainable rural transport": {
                    "% of rural roads using eco-friendly materials": "(Eco-friendly rural roads / Total rural roads) * 100",
                    "Number of green transport initiatives implemented": "Total rural green initiatives",
                    "Reduction in environmental complaints": "((Previous rural complaints - Current) / Previous) * 100",
                    "Stakeholder perception of sustainability": "Average perception score from rural sustainability surveys"
                },
                "Foster community engagement in rural projects": {
                    "Number of community consultations conducted": "Total rural consultations held",
                    "% of feedback incorporated into rural road planning": "(Feedback incorporated / Total feedback) * 100",
                    "Stakeholder satisfaction with participation": "Average satisfaction score from rural participation surveys",
                    "Number of local jobs created through projects": "Total rural jobs created"
                },
                "Support maintenance and reliability of rural roads": {
                    "% of maintenance projects completed on schedule": "(Rural maintenance projects on time / Total) * 100",
                    "Number of repairs conducted per year": "Total rural repairs conducted",
                    "Stakeholder satisfaction with road reliability": "Average satisfaction score from rural reliability surveys",
                    "Reduction in road-related disruptions": "((Previous rural disruptions - Current) / Previous) * 100"
                },
                "Improve connectivity for economic development": {
                    "Number of rural communities connected to markets": "Total rural communities connected",
                    "% increase in transport of goods due to new roads": "((Current goods transport - Previous) / Previous) * 100",
                    "Stakeholder satisfaction with economic impact": "Average satisfaction score from rural economic impact surveys",
                    "Number of businesses benefitting from connectivity": "Total rural businesses benefitting"
                },
                "Strengthen disaster resilience of rural roads": {
                    "% of rural roads designed to withstand natural hazards": "(Resilient rural roads / Total rural roads) * 100",
                    "Number of retrofitting projects completed": "Total rural retrofitting projects",
                    "Reduction in road closures during disasters": "((Previous rural closures - Current) / Previous) * 100",
                    "Stakeholder perception of rural road resilience": "Average perception score from rural resilience surveys"
                }
            },

            # Area 17: Social, Health & Community Infrastructure
            "Construction / Social, Health & Community Infrastructure": {
                "Expand access to healthcare facilities": {
                    "Number of hospitals/clinics constructed or upgraded": "Total healthcare facilities built or upgraded",
                    "% of projects meeting healthcare standards": "(Projects meeting standards / Total projects) * 100",
                    "Stakeholder satisfaction with healthcare services": "Average satisfaction score from healthcare service surveys",
                    "Reduction in patient travel time": "((Previous travel time - Current) / Previous) * 100"
                },
                "Improve community health programs": {
                    "Number of public health campaigns conducted": "Total health campaigns conducted",
                    "% of target population reached": "(Population reached / Target population) * 100",
                    "Stakeholder satisfaction with program effectiveness": "Average satisfaction score from program effectiveness surveys",
                    "Reduction in disease incidence": "((Previous disease incidence - Current) / Previous) * 100"
                },
                "Enhance educational infrastructure": {
                    "Number of schools and educational facilities built/renovated": "Total educational facilities built or renovated",
                    "% of projects meeting quality standards": "(Projects meeting standards / Total projects) * 100",
                    "Stakeholder satisfaction with education infrastructure": "Average satisfaction score from education infrastructure surveys",
                    "Number of students benefiting": "Total students served"
                },
                "Strengthen social and cultural facilities": {
                    "Number of community centers, libraries, or cultural facilities built": "Total social facilities built",
                    "% of projects completed on schedule": "(Projects completed on time / Total projects) * 100",
                    "Stakeholder satisfaction with amenities": "Average satisfaction score from amenity surveys",
                    "Number of community programs hosted": "Total community programs hosted"
                },
                "Promote community engagement & participation": {
                    "Number of community consultations conducted": "Total community consultations held",
                    "% of community feedback incorporated": "(Feedback incorporated / Total feedback) * 100",
                    "Stakeholder satisfaction with participation": "Average satisfaction score from participation surveys",
                    "Number of local jobs created through social projects": "Total social project jobs created"
                },
                "Ensure sustainability in social infrastructure": {
                    "% of projects with eco-friendly design": "(Projects with eco-design / Total projects) * 100",
                    "Number of renewable energy integrations in social facilities": "Total renewable energy integrations",
                    "Stakeholder satisfaction with sustainable initiatives": "Average satisfaction score from sustainability surveys",
                    "Reduction in environmental complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Improve accessibility and inclusivity": {
                    "% of facilities accessible to persons with disabilities": "(Accessible facilities / Total facilities) * 100",
                    "Number of inclusive programs conducted": "Total inclusive programs conducted",
                    "Stakeholder perception of accessibility and equity": "Average perception score from accessibility surveys",
                    "Participation rate of marginalized groups": "(Marginalized group participants / Total participants) * 100"
                },
                "Promote health, safety, and welfare standards": {
                    "% of projects compliant with health and safety regulations": "(Compliant projects / Total projects) * 100",
                    "Number of inspections conducted": "Total health and safety inspections",
                    "Reduction in incidents or accidents": "((Previous incidents - Current) / Previous) * 100",
                    "Stakeholder perception of safety and welfare": "Average perception score from safety and welfare surveys"
                }
            },

            #construction end

            #energy start
            # Area 1: Renewable Energy Projects
            "Energy / Renewable Energy Projects": {
                "Increase renewable energy capacity": {
                    "% increase in renewable energy contribution": "((Current renewable capacity - Previous capacity) / Previous capacity) * 100",
                    "Stakeholder satisfaction with renewable projects": "Average satisfaction score from stakeholder surveys",
                    "Reduction in fossil fuel dependency": "((Previous fossil fuel use - Current use) / Previous use) * 100",
                    "Number of local jobs created through projects": "Total local jobs created from renewable projects"
                },
                "Foster community involvement in renewable projects": {
                    "Number of community-led renewable initiatives": "Total community-led renewable projects",
                    "% of community feedback implemented": "(Community feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Number of local jobs created": "Total local jobs created from community projects"
                },
                "Promote environmental sustainability": {
                    "% of renewable projects with minimal environmental impact": "(Projects with minimal impact / Total projects) * 100",
                    "Stakeholder perception of environmental responsibility": "Average perception score from environmental surveys",
                    "Reduction in carbon emissions": "((Previous emissions - Current emissions) / Previous emissions) * 100",
                    "Number of environmental awareness programs conducted": "Total environmental awareness programs"
                },
                "Encourage innovation with stakeholder participation": {
                    "Number of pilot renewable projects involving local communities": "Total pilot projects with community involvement",
                    "% of projects using new technologies with public benefit": "(Projects with beneficial tech / Total projects) * 100",
                    "Stakeholder perception of innovation": "Average perception score from innovation surveys",
                    "Number of successful technology deployments benefiting local areas": "Total successful tech deployments"
                }
            },

            # Area 2: Energy Efficiency & Conservation
            "Energy / Energy Efficiency & Conservation": {
                "Promote energy-saving initiatives for households and communities": {
                    "Number of energy efficiency programs targeting households/communities": "Total efficiency programs implemented",
                    "% reduction in community energy consumption": "((Previous consumption - Current consumption) / Previous consumption) * 100",
                    "Stakeholder perception of efficiency improvements": "Average perception score from efficiency surveys",
                    "Reduction in energy costs for community": "((Previous costs - Current costs) / Previous costs) * 100"
                },
                "Increase awareness and training for citizens": {
                    "Number of workshops or awareness campaigns conducted": "Total workshops and campaigns conducted",
                    "% of community reached through programs": "(Population reached / Total population) * 100",
                    "Stakeholder satisfaction with awareness campaigns": "Average satisfaction score from awareness surveys",
                    "Reduction in energy misuse incidents": "((Previous misuse incidents - Current) / Previous) * 100"
                },
                "Implement community-focused energy management": {
                    "% of local facilities with digital monitoring for public benefit": "(Facilities with monitoring / Total facilities) * 100",
                    "Stakeholder satisfaction with energy management support": "Average satisfaction score from management surveys",
                    "Reduction in peak load issues affecting community": "((Previous peak load issues - Current) / Previous) * 100",
                    "Number of local stakeholders trained in energy management": "Total stakeholders trained in energy management"
                },
                "Promote equitable access to energy efficiency programs": {
                    "% of marginalized groups participating": "(Marginalized participants / Total participants) * 100",
                    "Stakeholder satisfaction with access": "Average satisfaction score from access surveys",
                    "Number of local community incentives delivered": "Total community incentives provided",
                    "Reduction in complaints about unequal energy services": "((Previous inequality complaints - Current) / Previous) * 100"
                }
            },

            # Area 3: Off-grid & Rural Energy Solutions
            "Energy / Off-grid & Rural Energy Solutions": {
                "Expand rural electrification": {
                    "% increase in rural population with energy access": "((Current access - Previous access) / Previous access) * 100",
                    "Stakeholder satisfaction with accessibility": "Average satisfaction score from accessibility surveys",
                    "Reduction in energy poverty": "((Previous energy poverty rate - Current) / Previous) * 100",
                    "Number of local jobs created": "Total local jobs created from rural projects"
                },
                "Foster community engagement in rural energy projects": {
                    "Number of local training programs": "Total training programs conducted",
                    "% of community participation in energy management": "(Community participants / Total community) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Number of skills development initiatives": "Total skills development initiatives"
                },
                "Promote sustainability and environmental protection": {
                    "% of projects using eco-friendly technology": "(Projects with eco-tech / Total projects) * 100",
                    "Stakeholder perception of sustainability": "Average perception score from sustainability surveys",
                    "Reduction in local pollution": "((Previous pollution levels - Current) / Previous) * 100",
                    "Number of awareness campaigns": "Total awareness campaigns conducted"
                },
                "Increase affordability of off-grid solutions": {
                    "% of rural households benefiting from subsidized solutions": "(Households with subsidies / Total households) * 100",
                    "Stakeholder satisfaction with pricing": "Average satisfaction score from pricing surveys",
                    "Number of financing options provided to communities": "Total financing options available",
                    "Reduction in energy cost complaints": "((Previous cost complaints - Current) / Previous) * 100"
                }
            },

            # Area 4: Community Development & Stakeholder Engagement
            "Energy / Community Development & Stakeholder Engagement": {
                "Enhance community awareness programs": {
                    "Number of energy education campaigns": "Total education campaigns conducted",
                    "% of community reached": "(Population reached / Total population) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Reduction in energy misuse": "((Previous misuse - Current) / Previous) * 100"
                },
                "Promote local employment through energy projects": {
                    "Number of local jobs created per project": "Total local jobs / Number of projects",
                    "% of workforce sourced locally": "(Local workers / Total workers) * 100",
                    "Stakeholder satisfaction with employment impact": "Average satisfaction score from employment surveys",
                    "Reduction in unemployment complaints": "((Previous unemployment complaints - Current) / Previous) * 100"
                },
                "Foster skills development and training": {
                    "Number of training programs conducted": "Total training programs offered",
                    "% of participants completing training": "(Participants completing / Total participants) * 100",
                    "Stakeholder satisfaction with skill development": "Average satisfaction score from skill development surveys",
                    "Number of energy-related jobs generated": "Total energy jobs created"
                },
                "Increase stakeholder collaboration in energy planning": {
                    "Number of collaborative initiatives with local authorities": "Total collaborative initiatives",
                    "% of projects incorporating stakeholder feedback": "(Projects with feedback / Total projects) * 100",
                    "Stakeholder satisfaction with collaboration": "Average satisfaction score from collaboration surveys",
                    "Number of successful joint projects": "Total successful joint projects"
                },
                "Promote social responsibility initiatives": {
                    "Number of community development programs implemented": "Total community development programs",
                    "% of initiatives meeting intended outcomes": "(Initiatives meeting outcomes / Total initiatives) * 100",
                    "Stakeholder perception of social impact": "Average perception score from social impact surveys",
                    "Number of recognitions or awards received": "Total awards and recognitions"
                },
                "Improve transparency and trust": {
                    "Number of public reports shared with stakeholders": "Total public reports issued",
                    "% of stakeholder concerns addressed": "(Concerns addressed / Total concerns) * 100",
                    "Stakeholder confidence score": "Average confidence score from stakeholder surveys",
                    "Number of community briefings conducted": "Total community briefings held"
                },
                "Support equitable energy access": {
                    "% of projects benefitting marginalized groups": "(Projects benefiting marginalized / Total projects) * 100",
                    "Number of programs targeting vulnerable populations": "Total programs for vulnerable populations",
                    "Stakeholder satisfaction with equity initiatives": "Average satisfaction score from equity surveys",
                    "Reduction in complaints related to inequality": "((Previous inequality complaints - Current) / Previous) * 100"
                },
                "Foster innovation in community engagement": {
                    "Number of pilot community engagement programs": "Total pilot engagement programs",
                    "% of feedback implemented in projects": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder perception of innovation": "Average perception score from innovation surveys",
                    "Number of successful engagement outcomes": "Total successful engagement outcomes"
                }
            },

            # Area 5: Disaster Resilience & Community Preparedness
            "Energy / Disaster Resilience & Community Preparedness": {
                "Strengthen energy infrastructure to benefit communities": {
                    "% of facilities designed for hazard resistance impacting citizens": "(Resilient facilities / Total facilities) * 100",
                    "Stakeholder perception of preparedness": "Average perception score from preparedness surveys",
                    "Reduction in outage duration affecting public services": "((Previous outage duration - Current) / Previous) * 100",
                    "Number of community awareness campaigns on disaster readiness": "Total disaster awareness campaigns"
                },
                "Develop emergency power solutions for essential services": {
                    "Number of critical facilities with backup systems": "Total facilities with backup power",
                    "Stakeholder satisfaction with emergency readiness": "Average satisfaction score from emergency surveys",
                    "% of rural/urban population benefiting": "(Population benefiting / Total population) * 100",
                    "Reduction in service interruptions to citizens": "((Previous interruptions - Current) / Previous) * 100"
                },
                "Foster collaborative disaster response with stakeholders": {
                    "Number of joint initiatives with local authorities": "Total joint initiatives with authorities",
                    "% of community engagement in planning": "(Community engaged in planning / Total community) * 100",
                    "Stakeholder satisfaction with coordination": "Average satisfaction score from coordination surveys",
                    "Number of successful disaster responses": "Total successful disaster responses"
                },
                "Promote community resilience and adaptation": {
                    "Number of energy projects supporting local climate adaptation": "Total adaptation-supporting projects",
                    "% of projects meeting resilience standards": "(Projects meeting standards / Total projects) * 100",
                    "Stakeholder perception of community protection": "Average perception score from protection surveys",
                    "Reduction in disaster vulnerability": "((Previous vulnerability - Current) / Previous) * 100"
                }
            },

            # Area 6: Grid Modernization & Smart Networks (Community & Stakeholder Focus)
            "Energy / Grid Modernization & Smart Networks": {
                "Expand access to underserved communities": {
                    "% of previously unconnected areas receiving electricity": "(Areas connected / Total unconnected) * 100",
                    "Stakeholder satisfaction with network reach": "Average satisfaction score from network reach surveys",
                    "Number of households gaining access to energy": "Total households gaining energy access",
                    "Reduction in energy poverty": "((Previous energy poverty - Current) / Previous) * 100"
                },
                "Promote stakeholder participation in network planning": {
                    "Number of consultations with local communities": "Total community consultations held",
                    "% of feedback incorporated into planning": "(Feedback incorporated / Total feedback) * 100",
                    "Stakeholder perception of inclusivity": "Average perception score from inclusivity surveys",
                    "Number of successful joint projects": "Total successful joint projects"
                },
                "Enhance reliability for community services": {
                    "% of network improvements benefiting schools, hospitals, or public facilities": "(Improvements benefiting facilities / Total improvements) * 100",
                    "Stakeholder satisfaction with service continuity": "Average satisfaction score from continuity surveys",
                    "Reduction in service interruptions impacting communities": "((Previous interruptions - Current) / Previous) * 100",
                    "Number of infrastructure resilience upgrades completed": "Total resilience upgrades completed"
                },
                "Foster renewable integration with community benefit": {
                    "% of renewable energy contributing to local supply": "(Renewable energy / Total energy) * 100",
                    "Number of hybrid or community renewable projects": "Total hybrid/community renewable projects",
                    "Stakeholder satisfaction with sustainable energy access": "Average satisfaction score from sustainable access surveys",
                    "Reduction in reliance on fossil fuels": "((Previous fossil fuel reliance - Current) / Previous) * 100"
                },
                "Promote transparency in network development": {
                    "Number of public briefings or reports issued": "Total briefings and reports issued",
                    "% of stakeholder concerns addressed": "(Concerns addressed / Total concerns) * 100",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Number of local awareness sessions conducted": "Total awareness sessions conducted"
                },
                "Enhance equitable energy access": {
                    "% of projects targeting marginalized populations": "(Projects targeting marginalized / Total projects) * 100",
                    "Stakeholder satisfaction with equity initiatives": "Average satisfaction score from equity surveys",
                    "Number of programs providing subsidized or affordable energy": "Total subsidized energy programs",
                    "Reduction in complaints regarding unequal access": "((Previous access complaints - Current) / Previous) * 100"
                },
                "Foster local employment through modernization projects": {
                    "Number of local jobs created through grid projects": "Total local jobs from grid projects",
                    "% of workforce sourced locally": "(Local workers / Total workers) * 100",
                    "Stakeholder satisfaction with employment impact": "Average satisfaction score from employment surveys",
                    "Number of skills development initiatives": "Total skills development initiatives"
                },
                "Promote community awareness of smart energy usage": {
                    "Number of educational programs conducted": "Total educational programs conducted",
                    "% of community participating": "(Community participants / Total community) * 100",
                    "Stakeholder satisfaction with awareness campaigns": "Average satisfaction score from awareness surveys",
                    "Reduction in energy misuse incidents": "((Previous misuse incidents - Current) / Previous) * 100"
                }
            },

            # Area 7: Customer Satisfaction & Service Quality
            "Energy / Customer Satisfaction & Service Quality": {
                "Improve overall customer satisfaction": {
                    "Customer satisfaction survey scores": "Average score from customer satisfaction surveys",
                    "Stakeholder satisfaction with service quality": "Average satisfaction score from service quality surveys",
                    "Number of positive testimonials from community/citizens": "Total positive testimonials received",
                    "% of repeat users or customers": "(Repeat customers / Total customers) * 100"
                },
                "Enhance responsiveness to inquiries and complaints": {
                    "% of community and citizen complaints resolved promptly": "(Complaints resolved promptly / Total complaints) * 100",
                    "Average response time for public inquiries": "Total response time / Number of inquiries",
                    "Stakeholder perception of service quality": "Average perception score from service quality surveys",
                    "Reduction in recurring complaints": "((Previous recurring complaints - Current) / Previous) * 100"
                },
                "Promote transparency in billing and service delivery": {
                    "% of bills accurately issued to customers": "(Accurate bills / Total bills) * 100",
                    "Stakeholder perception of fairness and transparency": "Average perception score from transparency surveys",
                    "Number of public billing workshops or info sessions": "Total billing workshops conducted",
                    "Reduction in complaints regarding billing": "((Previous billing complaints - Current) / Previous) * 100"
                },
                "Support equitable access for vulnerable groups": {
                    "% of projects benefiting marginalized or underserved populations": "(Projects benefiting marginalized / Total projects) * 100",
                    "Number of targeted programs implemented": "Total targeted programs implemented",
                    "Stakeholder satisfaction with inclusion": "Average satisfaction score from inclusion surveys",
                    "Reduction in energy access disparities": "((Previous disparities - Current) / Previous) * 100"
                },
                "Foster innovation in service delivery for public benefit": {
                    "Number of new service delivery programs implemented": "Total new service programs",
                    "% of stakeholder feedback integrated": "(Feedback integrated / Total feedback) * 100",
                    "Stakeholder satisfaction with innovative services": "Average satisfaction score from innovation surveys",
                    "Reduction in service inefficiencies": "((Previous inefficiencies - Current) / Previous) * 100"
                },
                "Promote community engagement in service improvements": {
                    "Number of community consultations conducted": "Total community consultations held",
                    "% of feedback incorporated into service design": "(Feedback incorporated / Total feedback) * 100",
                    "Stakeholder perception of participation": "Average perception score from participation surveys",
                    "Number of successful improvements implemented": "Total successful improvements"
                },
                "Strengthen trust and credibility among stakeholders": {
                    "Stakeholder confidence score": "Average confidence score from stakeholder surveys",
                    "Number of public recognitions or awards for service quality": "Total awards and recognitions",
                    "% of projects delivered meeting community expectations": "(Projects meeting expectations / Total projects) * 100",
                    "Number of positive media mentions or recognitions": "Total positive media mentions"
                },
                "Enhance social and environmental responsibility": {
                    "Number of community development programs supported": "Total community programs supported",
                    "% of projects contributing to local public good": "(Projects contributing to public good / Total projects) * 100",
                    "Stakeholder perception of social/environmental impact": "Average perception score from impact surveys",
                    "Reduction in negative social/environmental incidents": "((Previous incidents - Current) / Previous) * 100"
                }
            },

            # Area 8: Disaster Resilience & Emergency Preparedness
            "Energy / Disaster Resilience & Emergency Preparedness": {
                "Strengthen energy infrastructure for community safety": {
                    "% of facilities built/resilient against hazards affecting citizens": "(Resilient facilities / Total facilities) * 100",
                    "Stakeholder satisfaction with safety preparedness": "Average satisfaction score from safety surveys",
                    "Reduction in outages during disasters": "((Previous disaster outages - Current) / Previous) * 100",
                    "Number of community resilience programs": "Total community resilience programs"
                },
                "Ensure emergency energy access for critical services": {
                    "Number of hospitals, schools, and shelters with backup power": "Total critical facilities with backup",
                    "Stakeholder satisfaction with emergency readiness": "Average satisfaction score from emergency surveys",
                    "% of affected population covered": "(Population covered / Total population) * 100",
                    "Reduction in service interruptions for public facilities": "((Previous interruptions - Current) / Previous) * 100"
                },
                "Promote community awareness of disaster preparedness": {
                    "Number of awareness campaigns conducted": "Total awareness campaigns conducted",
                    "% of community participation": "(Community participants / Total community) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Reduction in disaster-related incidents": "((Previous incidents - Current) / Previous) * 100"
                },
                "Foster collaborative emergency response": {
                    "Number of joint initiatives with local authorities": "Total joint initiatives with authorities",
                    "% of community involvement in planning": "(Community involved in planning / Total community) * 100",
                    "Stakeholder perception of coordination effectiveness": "Average perception score from coordination surveys",
                    "Number of successful disaster response actions": "Total successful disaster responses"
                },
                "Increase resilience of renewable energy sources": {
                    "% of renewable installations designed to withstand hazards": "(Resilient renewables / Total renewables) * 100",
                    "Number of retrofitted systems": "Total systems retrofitted for resilience",
                    "Stakeholder satisfaction with resilience": "Average satisfaction score from resilience surveys",
                    "Reduction in downtime of renewable energy sources": "((Previous downtime - Current) / Previous) * 100"
                },
                "Ensure equitable disaster preparedness": {
                    "% of programs targeting vulnerable populations": "(Programs targeting vulnerable / Total programs) * 100",
                    "Stakeholder satisfaction with inclusion": "Average satisfaction score from inclusion surveys",
                    "Number of training sessions for at-risk communities": "Total training sessions for at-risk communities",
                    "Reduction in disaster impact disparities": "((Previous impact disparities - Current) / Previous) * 100"
                },
                "Strengthen regulatory and community compliance": {
                    "% of disaster preparedness projects compliant with regulations": "(Compliant projects / Total projects) * 100",
                    "Number of audits and inspections": "Total audits and inspections conducted",
                    "Stakeholder perception of compliance": "Average perception score from compliance surveys",
                    "Reduction in non-compliance incidents": "((Previous non-compliance - Current) / Previous) * 100"
                },
                "Encourage innovation in community resilience": {
                    "Number of pilot projects for disaster-resilient energy": "Total pilot resilience projects",
                    "% of innovative approaches implemented": "(Innovative approaches / Total approaches) * 100",
                    "Stakeholder satisfaction with innovation": "Average satisfaction score from innovation surveys",
                    "Reduction in vulnerability to disruptions": "((Previous vulnerability - Current) / Previous) * 100"
                }
            },

            # Area 9: Access & Affordability of Energy
            "Energy / Access & Affordability of Energy": {
                "Increase access for underserved populations": {
                    "% of households gaining electricity access": "(Households gaining access / Total households) * 100",
                    "Stakeholder satisfaction with energy accessibility": "Average satisfaction score from accessibility surveys",
                    "Number of community energy programs implemented": "Total community energy programs",
                    "Reduction in energy poverty": "((Previous energy poverty - Current) / Previous) * 100"
                },
                "Enhance affordability of energy services": {
                    "% of energy bills reduced for low-income households": "(Households with reduced bills / Total low-income) * 100",
                    "Number of subsidized energy programs delivered": "Total subsidized programs delivered",
                    "Stakeholder perception of fairness in pricing": "Average perception score from pricing surveys",
                    "Reduction in complaints about energy cost": "((Previous cost complaints - Current) / Previous) * 100"
                },
                "Promote equitable distribution of energy resources": {
                    "% of projects benefiting marginalized groups": "(Projects benefiting marginalized / Total projects) * 100",
                    "Number of energy distribution projects targeting rural areas": "Total rural distribution projects",
                    "Stakeholder satisfaction with equity in access": "Average satisfaction score from equity surveys",
                    "Reduction in service gaps across regions": "((Previous service gaps - Current) / Previous) * 100"
                },
                "Foster community engagement in energy planning": {
                    "Number of public consultations conducted": "Total public consultations held",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder perception of participation": "Average perception score from participation surveys",
                    "Number of projects co-designed with local communities": "Total co-designed projects"
                },
                "Increase adoption of renewable energy at household/community level": {
                    "Number of households with solar panels or mini-grids": "Total households with renewables",
                    "Stakeholder satisfaction with renewable energy programs": "Average satisfaction score from renewable surveys",
                    "% of local energy demand met with renewables": "(Renewable energy / Total energy demand) * 100",
                    "Reduction in fossil fuel dependence": "((Previous fossil fuel use - Current) / Previous) * 100"
                },
                "Promote energy literacy among citizens": {
                    "Number of awareness programs conducted": "Total awareness programs conducted",
                    "% of population reached": "(Population reached / Total population) * 100",
                    "Stakeholder satisfaction with educational impact": "Average satisfaction score from education surveys",
                    "Reduction in energy misuse or wastage": "((Previous misuse - Current) / Previous) * 100"
                },
                "Support local job creation through energy projects": {
                    "Number of jobs created through energy access projects": "Total jobs from energy access projects",
                    "% of workforce sourced locally": "(Local workers / Total workers) * 100",
                    "Stakeholder perception of employment impact": "Average perception score from employment surveys",
                    "Number of training programs provided": "Total training programs provided"
                },
                "Strengthen monitoring and accountability for access programs": {
                    "Number of public reports issued on access programs": "Total public reports issued",
                    "% of stakeholder concerns addressed": "(Concerns addressed / Total concerns) * 100",
                    "Stakeholder confidence in program delivery": "Average confidence score from program surveys",
                    "Reduction in complaints about accessibility": "((Previous accessibility complaints - Current) / Previous) * 100"
                }
            },

            # Area 10: Energy Reliability & Service Continuity
            "Energy / Energy Reliability & Service Continuity": {
                "Ensure continuous power supply to public services": {
                    "% of hospitals, schools, and public facilities with uninterrupted power": "(Facilities with uninterrupted power / Total facilities) * 100",
                    "Stakeholder satisfaction with reliability": "Average satisfaction score from reliability surveys",
                    "Number of backup systems installed": "Total backup systems installed",
                    "Reduction in outages affecting citizens": "((Previous citizen outages - Current) / Previous) * 100"
                },
                "Minimize disruptions for communities": {
                    "% reduction in energy interruptions": "((Previous interruptions - Current) / Previous) * 100",
                    "Number of maintenance programs benefiting public services": "Total maintenance programs for public services",
                    "Stakeholder perception of service reliability": "Average perception score from reliability surveys",
                    "Reduction in citizen complaints": "((Previous citizen complaints - Current) / Previous) * 100"
                },
                "Foster stakeholder participation in reliability planning": {
                    "Number of consultations conducted": "Total reliability consultations held",
                    "% of feedback integrated into network planning": "(Feedback integrated / Total feedback) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Number of collaborative projects completed": "Total collaborative reliability projects"
                },
                "Enhance resilience of energy supply to climate or hazards": {
                    "% of infrastructure climate-resilient": "(Climate-resilient infrastructure / Total infrastructure) * 100",
                    "Number of upgrades or retrofits completed": "Total upgrades and retrofits completed",
                    "Stakeholder perception of resilience": "Average perception score from resilience surveys",
                    "Reduction in hazard-related outages": "((Previous hazard outages - Current) / Previous) * 100"
                },
                "Promote community-focused maintenance programs": {
                    "Number of local maintenance teams trained": "Total local maintenance teams trained",
                    "% of community-involved monitoring initiatives": "(Community monitoring initiatives / Total initiatives) * 100",
                    "Stakeholder satisfaction with maintenance": "Average satisfaction score from maintenance surveys",
                    "Reduction in localized outages": "((Previous localized outages - Current) / Previous) * 100"
                },
                "Support equitable reliability for all communities": {
                    "% of projects benefitting marginalized or rural populations": "(Projects benefiting marginalized/rural / Total projects) * 100",
                    "Stakeholder satisfaction with equitable supply": "Average satisfaction score from equity surveys",
                    "Number of programs addressing service gaps": "Total programs addressing service gaps",
                    "Reduction in service inequities": "((Previous service inequities - Current) / Previous) * 100"
                },
                "Improve transparency in reliability metrics": {
                    "Number of reports shared with stakeholders": "Total reliability reports shared",
                    "% of community concerns addressed": "(Community concerns addressed / Total concerns) * 100",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Number of briefings conducted": "Total reliability briefings conducted"
                },
                "Encourage innovative solutions for service continuity": {
                    "Number of pilot projects for reliability improvements": "Total pilot reliability projects",
                    "% of innovative solutions adopted": "(Innovative solutions adopted / Total solutions) * 100",
                    "Stakeholder satisfaction with innovation": "Average satisfaction score from innovation surveys",
                    "Reduction in service interruptions": "((Previous service interruptions - Current) / Previous) * 100"
                }
            },

            # Area 11: Community & Stakeholder Engagement
            "Energy / Community & Stakeholder Engagement": {
                "Increase community participation in energy initiatives": {
                    "Number of engagement sessions held": "Total engagement sessions conducted",
                    "% of feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Number of projects co-created with local communities": "Total co-created projects"
                },
                "Promote transparency and trust among stakeholders": {
                    "Number of public reports issued": "Total public reports issued",
                    "% of concerns addressed": "(Concerns addressed / Total concerns) * 100",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Number of briefings conducted": "Total stakeholder briefings conducted"
                },
                "Foster local economic development": {
                    "Number of jobs created through energy projects": "Total jobs from energy projects",
                    "% of workforce sourced locally": "(Local workers / Total workers) * 100",
                    "Stakeholder satisfaction with economic impact": "Average satisfaction score from economic surveys",
                    "Reduction in local unemployment complaints": "((Previous unemployment complaints - Current) / Previous) * 100"
                },
                "Encourage social and environmental responsibility": {
                    "Number of community development programs supported": "Total community programs supported",
                    "% of projects contributing to social or environmental benefits": "(Projects with benefits / Total projects) * 100",
                    "Stakeholder perception of impact": "Average perception score from impact surveys",
                    "Number of local awareness campaigns": "Total local awareness campaigns"
                },
                "Strengthen collaboration with local authorities": {
                    "Number of joint planning initiatives": "Total joint planning initiatives",
                    "% of community input incorporated": "(Community input incorporated / Total input) * 100",
                    "Stakeholder satisfaction with collaboration": "Average satisfaction score from collaboration surveys",
                    "Number of successful joint projects": "Total successful joint projects"
                },
                "Enhance participation in policy and planning": {
                    "Number of consultations with stakeholders": "Total stakeholder consultations held",
                    "% of feedback incorporated into decision-making": "(Feedback incorporated / Total feedback) * 100",
                    "Stakeholder perception of inclusion": "Average perception score from inclusion surveys",
                    "Number of energy policies influenced": "Total policies influenced"
                },
                "Foster innovation in community engagement": {
                    "Number of pilot engagement programs": "Total pilot engagement programs",
                    "% of feedback integrated into projects": "(Feedback integrated / Total feedback) * 100",
                    "Stakeholder satisfaction with innovative approaches": "Average satisfaction score from innovation surveys",
                    "Number of successful outcomes from pilot programs": "Total successful pilot outcomes"
                },
                "Promote equitable access to engagement opportunities": {
                    "% of marginalized populations involved": "(Marginalized participants / Total participants) * 100",
                    "Number of programs targeting underrepresented groups": "Total programs for underrepresented groups",
                    "Stakeholder satisfaction with inclusion": "Average satisfaction score from inclusion surveys",
                    "Reduction in complaints about participation inequity": "((Previous participation complaints - Current) / Previous) * 100"
                }
            },

            # Area 12: Sustainable Energy & Climate Impact
            "Energy / Sustainable Energy & Climate Impact": {
                "Reduce environmental footprint of energy projects": {
                    "Reduction in CO₂ emissions": "((Previous emissions - Current emissions) / Previous emissions) * 100",
                    "% of projects implementing eco-friendly practices": "(Projects with eco-practices / Total projects) * 100",
                    "Stakeholder perception of environmental responsibility": "Average perception score from environmental surveys",
                    "Number of environmental awareness campaigns": "Total environmental awareness campaigns"
                },
                "Promote renewable energy adoption": {
                    "% of energy generated from renewables": "(Renewable energy / Total energy) * 100",
                    "Stakeholder satisfaction with sustainable energy access": "Average satisfaction score from sustainable access surveys",
                    "Number of renewable energy initiatives": "Total renewable energy initiatives",
                    "Reduction in fossil fuel dependence": "((Previous fossil fuel use - Current) / Previous) * 100"
                },
                "Enhance energy efficiency across communities": {
                    "% reduction in energy intensity": "((Previous energy intensity - Current) / Previous) * 100",
                    "Number of energy efficiency programs implemented": "Total efficiency programs implemented",
                    "Stakeholder perception of impact": "Average perception score from impact surveys",
                    "Reduction in energy costs for citizens": "((Previous citizen energy costs - Current) / Previous) * 100"
                },
                "Foster climate-resilient infrastructure": {
                    "% of projects designed to withstand climate hazards": "(Climate-resilient projects / Total projects) * 100",
                    "Number of resilient upgrades completed": "Total resilient upgrades completed",
                    "Stakeholder satisfaction with resilience": "Average satisfaction score from resilience surveys",
                    "Reduction in climate-related service disruptions": "((Previous climate disruptions - Current) / Previous) * 100"
                },
                "Support community-based climate adaptation initiatives": {
                    "Number of adaptation projects implemented": "Total adaptation projects implemented",
                    "% of community participation": "(Community participants / Total community) * 100",
                    "Stakeholder perception of adaptation effectiveness": "Average perception score from adaptation surveys",
                    "Reduction in climate vulnerability": "((Previous vulnerability - Current) / Previous) * 100"
                },
                "Promote sustainable resource management": {
                    "% of projects implementing sustainable practices": "(Projects with sustainable practices / Total projects) * 100",
                    "Number of environmental protection initiatives": "Total environmental protection initiatives",
                    "Stakeholder perception of resource stewardship": "Average perception score from stewardship surveys",
                    "Reduction in natural resource depletion": "((Previous resource depletion - Current) / Previous) * 100"
                },
                "Improve transparency and reporting on sustainability": {
                    "Number of sustainability reports published": "Total sustainability reports published",
                    "% of stakeholder concerns addressed": "(Concerns addressed / Total concerns) * 100",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Number of recognitions or awards received": "Total sustainability awards and recognitions"
                },
                "Encourage innovation in sustainable energy solutions": {
                    "Number of sustainability-focused innovations": "Total sustainability innovations",
                    "% of projects adopting green technologies": "(Projects with green tech / Total projects) * 100",
                    "Stakeholder satisfaction with innovation": "Average satisfaction score from innovation surveys",
                    "Reduction in environmental impact": "((Previous environmental impact - Current) / Previous) * 100"
                }
            },

            # Area 13: Innovation & Community-Focused Technology
            "Energy / Innovation & Community-Focused Technology": {
                "Promote innovative energy solutions for public benefit": {
                    "Number of community-oriented pilot projects implemented": "Total community pilot projects",
                    "Stakeholder satisfaction with innovative solutions": "Average satisfaction score from innovation surveys",
                    "% of projects demonstrating measurable public benefits": "(Projects with public benefits / Total projects) * 100",
                    "Number of successful technology deployments benefiting citizens": "Total successful tech deployments"
                },
                "Foster collaboration with communities in energy innovation": {
                    "Number of joint innovation initiatives with local stakeholders": "Total joint innovation initiatives",
                    "% of community feedback integrated into projects": "(Feedback integrated / Total feedback) * 100",
                    "Stakeholder perception of inclusivity": "Average perception score from inclusivity surveys",
                    "Number of projects co-designed with communities": "Total co-designed innovation projects"
                },
                "Encourage adoption of new technologies in underserved areas": {
                    "% of rural or marginalized communities using new energy technologies": "(Communities using new tech / Total communities) * 100",
                    "Stakeholder satisfaction with technology access": "Average satisfaction score from technology access surveys",
                    "Number of local training programs for technology adoption": "Total technology training programs",
                    "Reduction in energy access gaps": "((Previous access gaps - Current) / Previous) * 100"
                },
                "Enhance sustainability through innovative approaches": {
                    "% of projects implementing eco-friendly or energy-saving innovations": "(Projects with eco-innovations / Total projects) * 100",
                    "Stakeholder perception of environmental impact": "Average perception score from environmental surveys",
                    "Number of awareness campaigns on innovative sustainable solutions": "Total sustainability awareness campaigns",
                    "Reduction in carbon emissions or resource usage": "((Previous emissions/usage - Current) / Previous) * 100"
                },
                "Promote skills development in energy technology": {
                    "Number of community training programs delivered": "Total technology training programs delivered",
                    "% of participants successfully trained": "(Participants trained / Total participants) * 100",
                    "Stakeholder satisfaction with skill-building outcomes": "Average satisfaction score from skill-building surveys",
                    "Number of new local jobs created through technology adoption": "Total new local tech jobs"
                },
                "Improve transparency in technology deployment": {
                    "Number of public briefings or reports shared": "Total technology briefings and reports",
                    "% of stakeholder concerns addressed": "(Concerns addressed / Total concerns) * 100",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Reduction in complaints about technology rollout": "((Previous rollout complaints - Current) / Previous) * 100"
                },
                "Foster equitable access to energy innovation": {
                    "% of projects targeting underserved communities": "(Projects targeting underserved / Total projects) * 100",
                    "Stakeholder satisfaction with inclusion initiatives": "Average satisfaction score from inclusion surveys",
                    "Number of affordable technology programs implemented": "Total affordable tech programs",
                    "Reduction in complaints about unequal access": "((Previous access complaints - Current) / Previous) * 100"
                },
                "Promote recognition of successful community-focused innovations": {
                    "Number of awards or recognitions received for innovation": "Total innovation awards and recognitions",
                    "Stakeholder perception of organizational credibility": "Average perception score from credibility surveys",
                    "Number of case studies shared publicly": "Total public case studies shared",
                    "Increase in community adoption of innovative solutions": "((Current adoption - Previous) / Previous) * 100"
                }
            },

            # Area 14: Public Health & Safety in Energy Projects
            "Energy / Public Health & Safety in Energy Projects": {
                "Reduce health risks associated with energy infrastructure": {
                    "Number of safety inspections conducted in community areas": "Total safety inspections in communities",
                    "Stakeholder satisfaction with safety measures": "Average satisfaction score from safety surveys",
                    "% of projects compliant with safety standards": "(Compliant projects / Total projects) * 100",
                    "Reduction in accidents or incidents": "((Previous accidents - Current) / Previous) * 100"
                },
                "Promote safe energy usage among citizens": {
                    "Number of awareness programs on safe energy use": "Total safety awareness programs",
                    "% of community reached through campaigns": "(Community reached / Total community) * 100",
                    "Stakeholder satisfaction with safety awareness": "Average satisfaction score from awareness surveys",
                    "Reduction in safety-related complaints": "((Previous safety complaints - Current) / Previous) * 100"
                },
                "Improve emergency preparedness for energy hazards": {
                    "Number of community drills or preparedness programs": "Total community emergency drills",
                    "Stakeholder perception of readiness": "Average perception score from readiness surveys",
                    "% of at-risk areas covered by emergency plans": "(At-risk areas covered / Total at-risk) * 100",
                    "Reduction in impact of energy-related hazards": "((Previous hazard impact - Current) / Previous) * 100"
                },
                "Foster stakeholder collaboration in safety initiatives": {
                    "Number of joint safety projects with local authorities": "Total joint safety projects",
                    "% of community feedback integrated": "(Feedback integrated / Total feedback) * 100",
                    "Stakeholder satisfaction with collaboration": "Average satisfaction score from collaboration surveys",
                    "Number of successful hazard mitigation programs": "Total successful hazard mitigation programs"
                },
                "Ensure equitable access to safety resources": {
                    "% of marginalized communities benefiting from safety programs": "(Marginalized communities benefiting / Total marginalized) * 100",
                    "Stakeholder satisfaction with inclusive safety initiatives": "Average satisfaction score from inclusion surveys",
                    "Number of safety kits or resources distributed": "Total safety resources distributed",
                    "Reduction in complaints regarding unequal safety measures": "((Previous safety inequality complaints - Current) / Previous) * 100"
                },
                "Enhance monitoring and reporting of safety issues": {
                    "Number of safety reports issued publicly": "Total public safety reports issued",
                    "% of safety concerns addressed": "(Safety concerns addressed / Total concerns) * 100",
                    "Stakeholder perception of accountability": "Average perception score from accountability surveys",
                    "Reduction in unreported incidents": "((Previous unreported incidents - Current) / Previous) * 100"
                },
                "Promote innovation in energy safety solutions": {
                    "Number of pilot safety technologies implemented": "Total pilot safety technologies",
                    "Stakeholder satisfaction with innovation": "Average satisfaction score from innovation surveys",
                    "% of successful safety interventions": "(Successful interventions / Total interventions) * 100",
                    "Reduction in hazard-related risks": "((Previous hazard risks - Current) / Previous) * 100"
                },
                "Strengthen social responsibility in energy safety": {
                    "Number of community health and safety programs supported": "Total community health/safety programs",
                    "Stakeholder perception of social impact": "Average perception score from social impact surveys",
                    "% of projects contributing to local health and safety": "(Projects contributing to health/safety / Total projects) * 100",
                    "Number of recognitions or awards received": "Total safety awards and recognitions"
                }
            },

            # Area 15: Socio-Economic Development & Local Impact
            "Energy / Socio-Economic Development & Local Impact": {
                "Increase local employment opportunities through energy projects": {
                    "Number of jobs created in local communities": "Total local jobs created",
                    "% of workforce sourced locally": "(Local workers / Total workers) * 100",
                    "Stakeholder satisfaction with economic impact": "Average satisfaction score from economic impact surveys",
                    "Reduction in local unemployment": "((Previous unemployment - Current) / Previous) * 100"
                },
                "Promote skills development for citizens": {
                    "Number of training programs conducted": "Total training programs conducted",
                    "% of participants completing programs": "(Participants completing / Total participants) * 100",
                    "Stakeholder perception of skill-building effectiveness": "Average perception score from skill-building surveys",
                    "Number of new local energy-related jobs created": "Total new local energy jobs"
                },
                "Enhance community economic benefits": {
                    "Number of projects supporting local suppliers or businesses": "Total projects supporting local businesses",
                    "Stakeholder satisfaction with economic impact": "Average satisfaction score from economic surveys",
                    "% of local content in energy projects": "(Local content / Total content) * 100",
                    "Number of community income-generating initiatives": "Total community income initiatives"
                },
                "Foster equitable socio-economic development": {
                    "% of projects targeting marginalized groups": "(Projects targeting marginalized / Total projects) * 100",
                    "Stakeholder perception of equity in economic benefits": "Average perception score from equity surveys",
                    "Number of programs addressing socio-economic disparities": "Total disparity programs",
                    "Reduction in local complaints about inequity": "((Previous inequity complaints - Current) / Previous) * 100"
                },
                "Support local entrepreneurship": {
                    "Number of energy-related local startups supported": "Total local energy startups supported",
                    "% of programs providing financial or technical assistance": "(Programs with assistance / Total programs) * 100",
                    "Stakeholder satisfaction with entrepreneurship support": "Average satisfaction score from entrepreneurship surveys",
                    "Number of new businesses established": "Total new businesses established"
                },
                "Promote community engagement in economic initiatives": {
                    "Number of consultations held with local stakeholders": "Total economic consultations held",
                    "% of feedback implemented in project design": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participation": "Average satisfaction score from participation surveys",
                    "Number of co-created initiatives benefiting the community": "Total co-created economic initiatives"
                },
                "Enhance transparency in socio-economic outcomes": {
                    "Number of public reports shared on local economic impact": "Total economic impact reports shared",
                    "% of stakeholder concerns addressed": "(Concerns addressed / Total concerns) * 100",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Reduction in complaints related to project benefits": "((Previous benefit complaints - Current) / Previous) * 100"
                },
                "Encourage recognition of developmental impact": {
                    "Number of awards or recognitions received": "Total developmental awards and recognitions",
                    "Stakeholder perception of organizational contribution": "Average perception score from contribution surveys",
                    "Number of public case studies or reports issued": "Total developmental case studies",
                    "Increase in community adoption of developmental programs": "((Current adoption - Previous) / Previous) * 100"
                }
            },

            # Area 16: Stakeholder Trust, Governance & Transparency
            "Energy / Stakeholder Trust, Governance & Transparency": {
                "Strengthen trust among communities and citizens": {
                    "Stakeholder satisfaction survey score": "Average satisfaction score from stakeholder surveys",
                    "Number of consultations conducted": "Total stakeholder consultations held",
                    "% of feedback incorporated into projects": "(Feedback incorporated / Total feedback) * 100",
                    "Number of successful joint initiatives": "Total successful joint initiatives"
                },
                "Promote transparency in project planning and reporting": {
                    "Number of public reports issued": "Total public reports issued",
                    "% of stakeholder concerns addressed": "(Concerns addressed / Total concerns) * 100",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Number of community briefings conducted": "Total community briefings held"
                },
                "Foster ethical and accountable practices": {
                    "% of projects compliant with ethical standards": "(Compliant projects / Total projects) * 100",
                    "Number of ethical complaints resolved": "Total ethical complaints resolved",
                    "Stakeholder perception of organizational integrity": "Average perception score from integrity surveys",
                    "Reduction in incidents of misconduct": "((Previous misconduct incidents - Current) / Previous) * 100"
                },
                "Enhance stakeholder participation in governance": {
                    "Number of participatory decision-making sessions held": "Total participatory sessions held",
                    "% of stakeholder input integrated": "(Stakeholder input integrated / Total input) * 100",
                    "Stakeholder satisfaction with governance participation": "Average satisfaction score from governance surveys",
                    "Number of joint governance initiatives": "Total joint governance initiatives"
                },
                "Promote social responsibility through stakeholder engagement": {
                    "Number of community programs supported": "Total community programs supported",
                    "% of projects contributing to public benefit": "(Projects with public benefit / Total projects) * 100",
                    "Stakeholder perception of social impact": "Average perception score from social impact surveys",
                    "Number of recognitions or awards received": "Total social responsibility awards"
                },
                "Ensure equitable engagement for all stakeholder groups": {
                    "% of marginalized groups actively involved": "(Marginalized groups involved / Total marginalized) * 100",
                    "Stakeholder satisfaction with inclusivity": "Average satisfaction score from inclusivity surveys",
                    "Number of initiatives specifically targeting vulnerable populations": "Total initiatives for vulnerable populations",
                    "Reduction in complaints regarding exclusion": "((Previous exclusion complaints - Current) / Previous) * 100"
                },
                "Encourage innovation in stakeholder engagement": {
                    "Number of pilot initiatives for engagement": "Total pilot engagement initiatives",
                    "% of feedback integrated into projects": "(Feedback integrated / Total feedback) * 100",
                    "Stakeholder satisfaction with innovative approaches": "Average satisfaction score from innovation surveys",
                    "Number of successful outcomes from pilots": "Total successful pilot outcomes"
                },
                "Strengthen organizational reputation and credibility": {
                    "Corporate reputation index among stakeholders": "Composite reputation score from stakeholder surveys",
                    "Number of positive media mentions or public recognitions": "Total positive media mentions and recognitions",
                    "Stakeholder confidence improvement": "((Current confidence - Previous) / Previous) * 100",
                    "Number of awards received for transparency and social responsibility": "Total transparency and social responsibility awards"
                }
            },

            #energy end


            #education start
            # Area 1: Access to Education
            "Education / Access to Education": {
                "Increase enrollment for all children": {
                    "% of school-age children enrolled": "(Enrolled children / Total school-age children) * 100",
                    "Number of new students admitted": "Total new student admissions",
                    "Stakeholder satisfaction with enrollment process": "Average satisfaction score from enrollment surveys",
                    "Reduction in out-of-school children": "((Previous out-of-school - Current) / Previous) * 100"
                },
                "Improve access for marginalized groups": {
                    "% of enrollment among girls, minorities, or low-income groups": "(Marginalized group enrollment / Total marginalized population) * 100",
                    "Number of scholarship or support programs delivered": "Total scholarship/support programs implemented",
                    "Stakeholder perception of inclusion": "Average perception score from inclusion surveys",
                    "Reduction in educational disparities": "((Previous disparity rate - Current) / Previous) * 100"
                },
                "Expand early childhood education coverage": {
                    "% of children attending pre-primary programs": "(Children in pre-primary / Total pre-primary age) * 100",
                    "Number of early learning centers established": "Total early learning centers created",
                    "Stakeholder satisfaction with early learning access": "Average satisfaction score from early education surveys",
                    "Increase in literacy readiness among children": "((Current readiness - Previous) / Previous) * 100"
                },
                "Promote equitable geographical access": {
                    "Number of rural or underserved areas served by schools": "Total underserved areas with school access",
                    "Stakeholder satisfaction with school distribution": "Average satisfaction score from distribution surveys",
                    "% of new facilities in underserved regions": "(New facilities in underserved / Total new facilities) * 100",
                    "Reduction in travel time for students": "((Previous travel time - Current) / Previous) * 100"
                },
                "Enhance access to inclusive education": {
                    "Number of students with special needs supported": "Total special needs students supported",
                    "Stakeholder perception of inclusivity": "Average perception score from inclusivity surveys",
                    "% of schools implementing inclusive programs": "(Schools with inclusive programs / Total schools) * 100",
                    "Reduction in barriers to learning for special needs students": "((Previous barriers - Current) / Previous) * 100"
                },
                "Improve access to vocational and technical education": {
                    "Number of vocational/technical programs available": "Total vocational/technical programs",
                    "% of youth enrolled in skills programs": "(Youth in skills programs / Total youth) * 100",
                    "Stakeholder satisfaction with skills access": "Average satisfaction score from skills access surveys",
                    "Increase in employability of graduates": "((Current employability - Previous) / Previous) * 100"
                },
                "Strengthen adult and lifelong learning programs": {
                    "Number of adult education programs conducted": "Total adult education programs",
                    "% of participants completing programs": "(Participants completing / Total participants) * 100",
                    "Stakeholder satisfaction with adult learning": "Average satisfaction score from adult learning surveys",
                    "Increase in literacy and skills among adults": "((Current literacy - Previous) / Previous) * 100"
                },
                "Promote community awareness of educational opportunities": {
                    "Number of public outreach programs conducted": "Total outreach programs conducted",
                    "% of community participating": "(Community participants / Total community) * 100",
                    "Stakeholder satisfaction with awareness": "Average satisfaction score from awareness surveys",
                    "Increase in knowledge of educational programs": "((Current knowledge - Previous) / Previous) * 100"
                }
            },

            # Area 2: Quality of Teaching & Learning
            "Education / Quality of Teaching & Learning": {
                "Enhance teacher competence and training": {
                    "Number of teacher training programs conducted": "Total teacher training programs",
                    "% of teachers completing professional development": "(Teachers completing PD / Total teachers) * 100",
                    "Stakeholder satisfaction with teacher quality": "Average satisfaction score from quality surveys",
                    "Improvement in student learning outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Promote student-centered learning approaches": {
                    "% of classrooms implementing interactive/active learning": "(Interactive classrooms / Total classrooms) * 100",
                    "Number of teaching resources provided": "Total teaching resources distributed",
                    "Stakeholder satisfaction with learning experience": "Average satisfaction score from learning experience surveys",
                    "Improvement in student engagement scores": "((Current engagement - Previous) / Previous) * 100"
                },
                "Strengthen curriculum relevance": {
                    "% of schools implementing updated curriculum": "(Schools with updated curriculum / Total schools) * 100",
                    "Stakeholder satisfaction with curriculum content": "Average satisfaction score from curriculum surveys",
                    "Number of curriculum reviews conducted": "Total curriculum reviews completed",
                    "Increase in student performance in key subjects": "((Current performance - Previous) / Previous) * 100"
                },
                "Improve assessment and evaluation practices": {
                    "Number of schools adopting modern assessment methods": "Total schools with modern assessments",
                    "% of students receiving timely feedback": "(Students receiving feedback / Total students) * 100",
                    "Stakeholder perception of assessment fairness": "Average perception score from assessment surveys",
                    "Increase in measurable learning outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Foster teacher-student engagement": {
                    "Number of teacher-student interaction programs": "Total teacher-student programs",
                    "% of students reporting positive engagement": "(Students with positive engagement / Total students) * 100",
                    "Stakeholder satisfaction with teacher support": "Average satisfaction score from support surveys",
                    "Reduction in student dropout rates": "((Previous dropout rate - Current) / Previous) * 100"
                },
                "Promote professional learning communities": {
                    "Number of collaborative teacher initiatives": "Total collaborative initiatives",
                    "% of teachers participating in peer learning": "(Teachers in peer learning / Total teachers) * 100",
                    "Stakeholder perception of teaching effectiveness": "Average perception score from effectiveness surveys",
                    "Increase in innovative teaching practices": "((Current innovations - Previous) / Previous) * 100"
                },
                "Enhance use of educational technology": {
                    "% of schools equipped with ICT resources": "(Schools with ICT / Total schools) * 100",
                    "Number of teachers trained in digital tools": "Total teachers trained in digital tools",
                    "Stakeholder satisfaction with technology integration": "Average satisfaction score from technology surveys",
                    "Improvement in digital literacy among students": "((Current digital literacy - Previous) / Previous) * 100"
                },
                "Ensure quality assurance and accountability": {
                    "Number of schools undergoing quality audits": "Total schools audited",
                    "% of quality standards met": "(Standards met / Total standards) * 100",
                    "Stakeholder perception of accountability": "Average perception score from accountability surveys",
                    "Reduction in complaints about teaching quality": "((Previous complaints - Current) / Previous) * 100"
                }
            },

            # Area 3: Infrastructure & Learning Environment
            "Education / Infrastructure & Learning Environment": {
                "Expand physical school infrastructure": {
                    "Number of new classrooms constructed": "Total new classrooms built",
                    "% of planned school facilities completed": "(Completed facilities / Planned facilities) * 100",
                    "Stakeholder satisfaction with school facilities": "Average satisfaction score from facility surveys",
                    "Reduction in classroom overcrowding": "((Previous overcrowding - Current) / Previous) * 100"
                },
                "Improve access to basic utilities": {
                    "% of schools with clean water, sanitation, and electricity": "(Schools with utilities / Total schools) * 100",
                    "Number of schools with functional facilities": "Total schools with functional facilities",
                    "Stakeholder perception of safety and comfort": "Average perception score from safety surveys",
                    "Reduction in student absenteeism due to poor facilities": "((Previous absenteeism - Current) / Previous) * 100"
                },
                "Promote inclusive and safe learning spaces": {
                    "% of schools with accessible facilities for disabled students": "(Accessible schools / Total schools) * 100",
                    "Stakeholder satisfaction with inclusivity": "Average satisfaction score from inclusivity surveys",
                    "Number of safety inspections passed": "Total safety inspections passed",
                    "Reduction in safety incidents": "((Previous incidents - Current) / Previous) * 100"
                },
                "Enhance ICT infrastructure": {
                    "Number of schools equipped with computers and internet": "Total schools with ICT infrastructure",
                    "% of students accessing digital resources": "(Students accessing digital resources / Total students) * 100",
                    "Stakeholder satisfaction with ICT access": "Average satisfaction score from ICT access surveys",
                    "Improvement in digital literacy outcomes": "((Current digital literacy - Previous) / Previous) * 100"
                },
                "Foster community involvement in school infrastructure": {
                    "Number of community consultation sessions": "Total community consultations",
                    "% of feedback implemented in infrastructure projects": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participation": "Average satisfaction score from participation surveys",
                    "Number of co-created community initiatives": "Total co-created initiatives"
                },
                "Promote green and sustainable school facilities": {
                    "% of schools implementing eco-friendly infrastructure": "(Schools with eco-infrastructure / Total schools) * 100",
                    "Stakeholder perception of environmental initiatives": "Average perception score from environmental surveys",
                    "Number of awareness campaigns on sustainability": "Total sustainability campaigns",
                    "Reduction in school energy consumption": "((Previous consumption - Current) / Previous) * 100"
                },
                "Improve maintenance of school facilities": {
                    "Number of maintenance programs conducted": "Total maintenance programs",
                    "% of schools meeting safety and functionality standards": "(Schools meeting standards / Total schools) * 100",
                    "Stakeholder satisfaction with upkeep": "Average satisfaction score from upkeep surveys",
                    "Reduction in facility-related complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Ensure equitable infrastructure development": {
                    "% of new infrastructure in underserved areas": "(New infrastructure in underserved / Total new infrastructure) * 100",
                    "Stakeholder satisfaction with equity": "Average satisfaction score from equity surveys",
                    "Number of programs targeting marginalized populations": "Total targeted programs",
                    "Reduction in infrastructure disparity across regions": "((Previous disparity - Current) / Previous) * 100"
                }
            },

            # Area 4: Curriculum & Learning Outcomes
            "Education / Curriculum & Learning Outcomes": {
                "Improve student literacy and numeracy": {
                    "% of students meeting grade-level literacy standards": "(Students meeting standards / Total students) * 100",
                    "% of students meeting numeracy benchmarks": "(Students meeting benchmarks / Total students) * 100",
                    "Stakeholder satisfaction with student learning outcomes": "Average satisfaction score from learning outcome surveys",
                    "Reduction in learning gaps": "((Previous learning gaps - Current) / Previous) * 100"
                },
                "Enhance critical thinking and problem-solving skills": {
                    "Number of programs fostering critical thinking": "Total critical thinking programs",
                    "% of students demonstrating improved problem-solving": "(Students improving / Total students) * 100",
                    "Stakeholder perception of skill development": "Average perception score from skill development surveys",
                    "Improvement in standardized assessment scores": "((Current scores - Previous) / Previous) * 100"
                },
                "Promote STEM education participation": {
                    "% of students enrolled in STEM subjects": "(STEM students / Total students) * 100",
                    "Number of STEM extracurricular programs conducted": "Total STEM extracurricular programs",
                    "Stakeholder satisfaction with STEM opportunities": "Average satisfaction score from STEM opportunity surveys",
                    "Increase in STEM-related student achievements": "((Current achievements - Previous) / Previous) * 100"
                },
                "Encourage arts, culture, and creative learning": {
                    "Number of arts and cultural programs conducted": "Total arts and cultural programs",
                    "% of students participating in creative initiatives": "(Participating students / Total students) * 100",
                    "Stakeholder satisfaction with cultural education": "Average satisfaction score from cultural education surveys",
                    "Increase in student creativity and engagement scores": "((Current scores - Previous) / Previous) * 100"
                },
                "Strengthen vocational and technical learning outcomes": {
                    "% of students completing vocational programs": "(Students completing vocational / Total vocational students) * 100",
                    "Number of certifications issued": "Total certifications awarded",
                    "Stakeholder perception of employability": "Average perception score from employability surveys",
                    "Increase in graduate employment rates": "((Current employment - Previous) / Previous) * 100"
                },
                "Ensure alignment of curriculum with developmental needs": {
                    "% of schools implementing updated curriculum standards": "(Schools with updated standards / Total schools) * 100",
                    "Stakeholder satisfaction with curriculum relevance": "Average satisfaction score from curriculum relevance surveys",
                    "Number of curriculum reviews conducted": "Total curriculum reviews",
                    "Improvement in developmental skill outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Promote assessment-driven learning improvement": {
                    "Number of schools implementing continuous assessment practices": "Total schools with continuous assessment",
                    "% of students receiving timely performance feedback": "(Students receiving feedback / Total students) * 100",
                    "Stakeholder perception of fair evaluation": "Average perception score from evaluation surveys",
                    "Reduction in learning deficiencies": "((Previous deficiencies - Current) / Previous) * 100"
                },
                "Foster community involvement in learning outcomes": {
                    "Number of parent-teacher engagement sessions": "Total parent-teacher sessions",
                    "% of parental/community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with learning support": "Average satisfaction score from support surveys",
                    "Increase in student academic performance": "((Current performance - Previous) / Previous) * 100"
                }
            },

            # Area 5: Teacher Development & Support
            "Education / Teacher Development & Support": {
                "Enhance teacher recruitment and retention": {
                    "Number of qualified teachers recruited": "Total qualified teachers recruited",
                    "% of teacher retention year-over-year": "(Retained teachers / Previous year teachers) * 100",
                    "Stakeholder satisfaction with teaching staff availability": "Average satisfaction score from staff availability surveys",
                    "Reduction in teacher shortages": "((Previous shortages - Current) / Previous) * 100"
                },
                "Strengthen professional development": {
                    "Number of training programs conducted": "Total teacher training programs",
                    "% of teachers completing professional development": "(Teachers completing PD / Total teachers) * 100",
                    "Stakeholder perception of teacher competence": "Average perception score from competence surveys",
                    "Improvement in teaching quality scores": "((Current quality scores - Previous) / Previous) * 100"
                },
                "Promote mentorship and peer learning": {
                    "Number of mentorship programs implemented": "Total mentorship programs",
                    "% of teachers participating in peer learning": "(Teachers in peer learning / Total teachers) * 100",
                    "Stakeholder satisfaction with teacher support": "Average satisfaction score from support surveys",
                    "Increase in adoption of best teaching practices": "((Current adoption - Previous) / Previous) * 100"
                },
                "Enhance teacher motivation and engagement": {
                    "Teacher satisfaction survey score": "Average teacher satisfaction score",
                    "% of teachers receiving recognition or incentives": "(Teachers recognized / Total teachers) * 100",
                    "Stakeholder perception of teacher commitment": "Average perception score from commitment surveys",
                    "Reduction in absenteeism": "((Previous absenteeism - Current) / Previous) * 100"
                },
                "Foster innovative teaching practices": {
                    "Number of pilot teaching innovation programs": "Total pilot innovation programs",
                    "% of teachers adopting new teaching methods": "(Teachers adopting new methods / Total teachers) * 100",
                    "Stakeholder satisfaction with innovation in teaching": "Average satisfaction score from innovation surveys",
                    "Improvement in student learning outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Promote equitable teacher distribution": {
                    "% of teachers placed in underserved areas": "(Teachers in underserved / Total teachers) * 100",
                    "Stakeholder satisfaction with teacher allocation": "Average satisfaction score from allocation surveys",
                    "Number of support programs for remote teachers": "Total support programs for remote teachers",
                    "Reduction in disparities across regions": "((Previous disparities - Current) / Previous) * 100"
                },
                "Strengthen accountability and performance monitoring": {
                    "Number of teacher performance evaluations conducted": "Total teacher evaluations",
                    "% of performance targets met": "(Targets met / Total targets) * 100",
                    "Stakeholder perception of accountability": "Average perception score from accountability surveys",
                    "Improvement in classroom learning outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Encourage community involvement in teacher support": {
                    "Number of parent/community programs for teacher support": "Total community support programs",
                    "% of feedback implemented in teaching improvements": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with teacher-community engagement": "Average satisfaction score from engagement surveys",
                    "Increase in student satisfaction with teaching": "((Current satisfaction - Previous) / Previous) * 100"
                }
            },

            # Area 6: Student Engagement & Wellbeing
            "Education / Student Engagement & Wellbeing": {
                "Promote attendance and reduce dropout rates": {
                    "% of students with regular attendance": "(Regular attendees / Total students) * 100",
                    "Number of dropout cases reduced": "Total reduction in dropout cases",
                    "Stakeholder satisfaction with student retention efforts": "Average satisfaction score from retention surveys",
                    "Improvement in enrollment continuity": "((Current continuity - Previous) / Previous) * 100"
                },
                "Support student mental health and wellbeing": {
                    "Number of counseling or wellbeing programs conducted": "Total wellbeing programs",
                    "% of students accessing support services": "(Students accessing support / Total students) * 100",
                    "Stakeholder perception of student wellbeing": "Average perception score from wellbeing surveys",
                    "Reduction in mental health-related absenteeism": "((Previous absenteeism - Current) / Previous) * 100"
                },
                "Enhance student participation in school governance": {
                    "Number of student councils or leadership programs": "Total student governance programs",
                    "% of students participating in governance": "(Students in governance / Total students) * 100",
                    "Stakeholder satisfaction with student engagement": "Average satisfaction score from engagement surveys",
                    "Increase in student-led initiatives": "((Current initiatives - Previous) / Previous) * 100"
                },
                "Encourage extracurricular and co-curricular activities": {
                    "Number of extracurricular programs conducted": "Total extracurricular programs",
                    "% of student participation in activities": "(Participating students / Total students) * 100",
                    "Stakeholder satisfaction with holistic development": "Average satisfaction score from development surveys",
                    "Improvement in student skills and creativity": "((Current skill levels - Previous) / Previous) * 100"
                },
                "Foster community and parental engagement": {
                    "Number of parent-student engagement events": "Total parent-student events",
                    "% of parental feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with engagement efforts": "Average satisfaction score from engagement surveys",
                    "Improvement in student learning outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Promote safe and inclusive school environments": {
                    "% of schools meeting safety and inclusivity standards": "(Schools meeting standards / Total schools) * 100",
                    "Number of anti-bullying or inclusion programs": "Total anti-bullying/inclusion programs",
                    "Stakeholder perception of safe environment": "Average perception score from safety surveys",
                    "Reduction in safety incidents": "((Previous incidents - Current) / Previous) * 100"
                },
                "Enhance student recognition and reward systems": {
                    "Number of student awards or recognition programs": "Total recognition programs",
                    "% of students recognized for achievements": "(Students recognized / Total students) * 100",
                    "Stakeholder satisfaction with recognition systems": "Average satisfaction score from recognition surveys",
                    "Increase in student motivation and performance": "((Current motivation - Previous) / Previous) * 100"
                },
                "Strengthen career guidance and future readiness": {
                    "Number of career guidance sessions conducted": "Total career guidance sessions",
                    "% of students receiving counseling on career paths": "(Students receiving counseling / Total students) * 100",
                    "Stakeholder satisfaction with guidance programs": "Average satisfaction score from guidance surveys",
                    "Increase in successful transitions to higher education or employment": "((Current transitions - Previous) / Previous) * 100"
                }
            },

            # Area 7: Educational Infrastructure
            "Education / Educational Infrastructure": {
                "Expand school facilities to underserved areas": {
                    "Number of new classrooms or schools constructed": "Total new classrooms/schools built",
                    "% of planned facilities completed": "(Completed facilities / Planned facilities) * 100",
                    "Stakeholder satisfaction with infrastructure distribution": "Average satisfaction score from distribution surveys",
                    "Reduction in overcrowded classrooms": "((Previous overcrowding - Current) / Previous) * 100"
                },
                "Improve access to clean water, sanitation, and electricity": {
                    "% of schools with functional water, sanitation, and electricity": "(Schools with utilities / Total schools) * 100",
                    "Number of schools passing safety and hygiene inspections": "Total schools passing inspections",
                    "Stakeholder perception of facility adequacy": "Average perception score from adequacy surveys",
                    "Reduction in health-related absenteeism": "((Previous absenteeism - Current) / Previous) * 100"
                },
                "Promote safe and inclusive school environments": {
                    "% of schools with accessible facilities for students with disabilities": "(Accessible schools / Total schools) * 100",
                    "Stakeholder satisfaction with safety and inclusivity": "Average satisfaction score from safety surveys",
                    "Number of safety drills conducted": "Total safety drills conducted",
                    "Reduction in accidents or safety incidents": "((Previous incidents - Current) / Previous) * 100"
                },
                "Enhance ICT and digital learning infrastructure": {
                    "Number of schools equipped with computers and internet access": "Total schools with ICT access",
                    "% of students accessing digital learning resources": "(Students accessing digital resources / Total students) * 100",
                    "Stakeholder satisfaction with ICT integration": "Average satisfaction score from ICT surveys",
                    "Improvement in student digital literacy": "((Current digital literacy - Previous) / Previous) * 100"
                },
                "Foster community participation in infrastructure development": {
                    "Number of community consultations for school infrastructure projects": "Total community consultations",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participatory processes": "Average satisfaction score from participation surveys",
                    "Number of joint initiatives completed": "Total joint initiatives completed"
                },
                "Promote sustainable and green infrastructure": {
                    "% of schools with eco-friendly or energy-efficient facilities": "(Schools with eco-facilities / Total schools) * 100",
                    "Stakeholder perception of environmental sustainability": "Average perception score from sustainability surveys",
                    "Number of awareness campaigns on green practices": "Total green awareness campaigns",
                    "Reduction in energy and resource consumption": "((Previous consumption - Current) / Previous) * 100"
                },
                "Ensure equitable allocation of educational resources": {
                    "% of facilities provided to marginalized or remote areas": "(Facilities in marginalized areas / Total facilities) * 100",
                    "Stakeholder satisfaction with equity of access": "Average satisfaction score from equity surveys",
                    "Number of targeted support programs implemented": "Total targeted support programs",
                    "Reduction in regional disparities in infrastructure": "((Previous disparities - Current) / Previous) * 100"
                },
                "Strengthen maintenance and facility management": {
                    "Number of regular maintenance programs conducted": "Total maintenance programs",
                    "% of schools meeting operational standards": "(Schools meeting standards / Total schools) * 100",
                    "Stakeholder satisfaction with facility upkeep": "Average satisfaction score from upkeep surveys",
                    "Reduction in facility-related complaints": "((Previous complaints - Current) / Previous) * 100"
                }
            },

            # Area 8: Educational Technology & Digital Learning
            "Education / Educational Technology & Digital Learning": {
                "Expand access to digital learning tools": {
                    "Number of schools equipped with digital learning resources": "Total schools with digital resources",
                    "% of students using digital tools effectively": "(Students using tools effectively / Total students) * 100",
                    "Stakeholder satisfaction with technology access": "Average satisfaction score from technology access surveys",
                    "Improvement in student digital competencies": "((Current competencies - Previous) / Previous) * 100"
                },
                "Promote teacher training in digital pedagogy": {
                    "Number of teachers trained in ICT integration": "Total teachers trained in ICT",
                    "% of trained teachers implementing digital tools": "(Teachers implementing tools / Trained teachers) * 100",
                    "Stakeholder perception of teaching effectiveness": "Average perception score from teaching effectiveness surveys",
                    "Increase in student engagement via technology": "((Current engagement - Previous) / Previous) * 100"
                },
                "Enhance online and blended learning opportunities": {
                    "Number of blended/online learning programs offered": "Total blended/online programs",
                    "% of students participating in digital learning": "(Students in digital learning / Total students) * 100",
                    "Stakeholder satisfaction with learning accessibility": "Average satisfaction score from accessibility surveys",
                    "Improvement in learning outcomes via digital methods": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Encourage community and parental engagement in digital learning": {
                    "Number of workshops or awareness sessions for parents": "Total parent workshops",
                    "% of community feedback implemented in digital learning initiatives": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Increase in parent/community support for e-learning": "((Current support - Previous) / Previous) * 100"
                },
                "Foster innovation in educational technology": {
                    "Number of pilot digital tools or learning platforms implemented": "Total pilot digital tools",
                    "% of successful technology interventions": "(Successful interventions / Total interventions) * 100",
                    "Stakeholder satisfaction with innovative solutions": "Average satisfaction score from innovation surveys",
                    "Improvement in learning outcomes via innovative technologies": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Ensure equitable access to technology": {
                    "% of marginalized students accessing digital resources": "(Marginalized students with access / Total marginalized) * 100",
                    "Stakeholder satisfaction with technology inclusion": "Average satisfaction score from inclusion surveys",
                    "Number of targeted programs for underserved communities": "Total targeted technology programs",
                    "Reduction in digital divide": "((Previous divide - Current) / Previous) * 100"
                },
                "Promote safe and responsible use of technology": {
                    "Number of digital safety awareness programs": "Total digital safety programs",
                    "% of students adhering to online safety guidelines": "(Students adhering to guidelines / Total students) * 100",
                    "Stakeholder perception of responsible technology use": "Average perception score from responsible use surveys",
                    "Reduction in digital misuse incidents": "((Previous misuse - Current) / Previous) * 100"
                },
                "Monitor and evaluate digital learning impact": {
                    "Number of assessments of digital learning effectiveness": "Total digital learning assessments",
                    "% of projects meeting digital learning objectives": "(Projects meeting objectives / Total projects) * 100",
                    "Stakeholder satisfaction with impact measurement": "Average satisfaction score from impact surveys",
                    "Improvement in student digital competency scores": "((Current scores - Previous) / Previous) * 100"
                }
            },

            # Area 9: Community & Stakeholder Engagement
            "Education / Community & Stakeholder Engagement": {
                "Increase community participation in school governance": {
                    "Number of community consultation meetings": "Total community consultations",
                    "% of feedback implemented in decision-making": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participation": "Average satisfaction score from participation surveys",
                    "Number of joint initiatives completed": "Total joint community-school initiatives"
                },
                "Strengthen parental involvement in education": {
                    "Number of parent-teacher engagement sessions": "Total parent-teacher sessions",
                    "% of parents actively participating": "(Active parents / Total parents) * 100",
                    "Stakeholder satisfaction with parental engagement": "Average satisfaction score from engagement surveys",
                    "Improvement in student performance linked to parent involvement": "((Current performance - Previous) / Previous) * 100"
                },
                "Promote student voice and leadership": {
                    "Number of student councils or leadership programs": "Total student leadership programs",
                    "% of students participating in governance": "(Students in governance / Total students) * 100",
                    "Stakeholder satisfaction with student involvement": "Average satisfaction score from involvement surveys",
                    "Increase in student-led initiatives": "((Current initiatives - Previous) / Previous) * 100"
                },
                "Enhance collaboration with local authorities": {
                    "Number of partnerships with local government or agencies": "Total local authority partnerships",
                    "% of joint programs successfully implemented": "(Successful joint programs / Total joint programs) * 100",
                    "Stakeholder satisfaction with authority collaboration": "Average satisfaction score from collaboration surveys",
                    "Number of local policy improvements influenced": "Total policy improvements influenced"
                },
                "Foster partnerships with NGOs and community groups": {
                    "Number of partnerships established": "Total NGO/community partnerships",
                    "% of joint programs achieving objectives": "(Programs achieving objectives / Total programs) * 100",
                    "Stakeholder satisfaction with NGO collaboration": "Average satisfaction score from collaboration surveys",
                    "Number of community-beneficial projects implemented": "Total community-beneficial projects"
                },
                "Promote transparency and accountability in schools": {
                    "Number of public reports issued": "Total public reports issued",
                    "% of stakeholder concerns addressed": "(Concerns addressed / Total concerns) * 100",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Reduction in complaints or conflicts": "((Previous complaints - Current) / Previous) * 100"
                },
                "Encourage equitable engagement across all communities": {
                    "% of marginalized groups actively involved": "(Marginalized groups involved / Total marginalized) * 100",
                    "Stakeholder satisfaction with inclusivity": "Average satisfaction score from inclusivity surveys",
                    "Number of initiatives targeting vulnerable populations": "Total initiatives for vulnerable populations",
                    "Reduction in disparities in stakeholder participation": "((Previous disparities - Current) / Previous) * 100"
                },
                "Recognize and reward community engagement efforts": {
                    "Number of awards or recognitions given": "Total awards and recognitions",
                    "Stakeholder perception of organizational credibility": "Average perception score from credibility surveys",
                    "Number of case studies shared publicly": "Total public case studies shared",
                    "Increase in community adoption of engagement programs": "((Current adoption - Previous) / Previous) * 100"
                }
            },

            # Area 10: Teacher Performance & Accountability
            "Education / Teacher Performance & Accountability": {
                "Implement teacher performance monitoring": {
                    "Number of teacher evaluations conducted": "Total teacher evaluations",
                    "% of teachers meeting performance standards": "(Teachers meeting standards / Total teachers) * 100",
                    "Stakeholder satisfaction with teaching quality": "Average satisfaction score from quality surveys",
                    "Improvement in student learning outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Promote accountability in teaching": {
                    "Number of performance improvement plans implemented": "Total improvement plans",
                    "% of teachers adhering to standards": "(Teachers adhering to standards / Total teachers) * 100",
                    "Stakeholder perception of accountability": "Average perception score from accountability surveys",
                    "Reduction in classroom performance gaps": "((Previous gaps - Current) / Previous) * 100"
                },
                "Encourage continuous professional growth": {
                    "Number of continuous professional development programs": "Total continuous PD programs",
                    "% of teachers participating": "(Teachers participating / Total teachers) * 100",
                    "Stakeholder satisfaction with teacher growth": "Average satisfaction score from growth surveys",
                    "Increase in teacher skill competencies": "((Current competencies - Previous) / Previous) * 100"
                },
                "Recognize high-performing teachers": {
                    "Number of awards or recognitions given": "Total teacher awards",
                    "% of teachers recognized annually": "(Teachers recognized / Total teachers) * 100",
                    "Stakeholder perception of teacher motivation": "Average perception score from motivation surveys",
                    "Improvement in student learning outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Support underperforming teachers": {
                    "Number of mentorship programs for underperforming teachers": "Total mentorship programs",
                    "% of teachers showing performance improvement": "(Teachers improving / Total underperforming) * 100",
                    "Stakeholder satisfaction with support programs": "Average satisfaction score from support surveys",
                    "Reduction in classroom performance issues": "((Previous issues - Current) / Previous) * 100"
                },
                "Promote equitable distribution of skilled teachers": {
                    "% of schools in underserved areas with qualified teachers": "(Schools with qualified teachers / Total underserved schools) * 100",
                    "Stakeholder perception of teacher allocation equity": "Average perception score from equity surveys",
                    "Number of targeted support programs": "Total targeted support programs",
                    "Reduction in regional disparities": "((Previous disparities - Current) / Previous) * 100"
                },
                "Enhance teacher engagement and retention": {
                    "Teacher satisfaction survey score": "Average teacher satisfaction score",
                    "% reduction in teacher turnover": "((Previous turnover - Current) / Previous) * 100",
                    "Stakeholder satisfaction with teaching staff stability": "Average satisfaction score from stability surveys",
                    "Improvement in classroom learning continuity": "((Current continuity - Previous) / Previous) * 100"
                },
                "Strengthen collaboration among teaching staff": {
                    "Number of collaborative teaching initiatives": "Total collaborative initiatives",
                    "% of teachers participating in peer learning": "(Teachers in peer learning / Total teachers) * 100",
                    "Stakeholder satisfaction with collaboration": "Average satisfaction score from collaboration surveys",
                    "Improvement in adoption of best practices": "((Current adoption - Previous) / Previous) * 100"
                }
            },

            # Area 11: Curriculum Development & Relevance
            "Education / Curriculum Development & Relevance": {
                "Ensure curriculum alignment with developmental needs": {
                    "% of schools implementing updated curriculum": "(Schools with updated curriculum / Total schools) * 100",
                    "Stakeholder satisfaction with curriculum relevance": "Average satisfaction score from relevance surveys",
                    "Number of curriculum reviews conducted": "Total curriculum reviews",
                    "Improvement in student learning outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Promote STEM and technical skills": {
                    "% of students enrolled in STEM programs": "(STEM students / Total students) * 100",
                    "Number of STEM extracurricular initiatives": "Total STEM extracurricular initiatives",
                    "Stakeholder satisfaction with STEM opportunities": "Average satisfaction score from STEM surveys",
                    "Improvement in student STEM competency": "((Current competency - Previous) / Previous) * 100"
                },
                "Encourage arts, culture, and creative learning": {
                    "Number of arts and cultural programs implemented": "Total arts/cultural programs",
                    "% of student participation": "(Students participating / Total students) * 100",
                    "Stakeholder perception of holistic education": "Average perception score from holistic education surveys",
                    "Increase in student creativity scores": "((Current creativity - Previous) / Previous) * 100"
                },
                "Strengthen life skills and social-emotional learning": {
                    "Number of life skills programs conducted": "Total life skills programs",
                    "% of students showing improvement in social-emotional learning": "(Students improving / Total students) * 100",
                    "Stakeholder satisfaction with student development": "Average satisfaction score from development surveys",
                    "Reduction in behavioral or social issues": "((Previous issues - Current) / Previous) * 100"
                },
                "Foster vocational and career-focused learning": {
                    "% of students completing vocational courses": "(Students completing vocational / Total vocational students) * 100",
                    "Number of certifications awarded": "Total certifications awarded",
                    "Stakeholder satisfaction with employability": "Average satisfaction score from employability surveys",
                    "Increase in successful transitions to employment": "((Current transitions - Previous) / Previous) * 100"
                },
                "Promote assessment-driven improvement": {
                    "Number of schools implementing modern assessments": "Total schools with modern assessments",
                    "% of students receiving timely feedback": "(Students receiving feedback / Total students) * 100",
                    "Stakeholder satisfaction with assessment fairness": "Average satisfaction score from fairness surveys",
                    "Improvement in learning outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Encourage community involvement in curriculum design": {
                    "Number of community consultations": "Total community consultations",
                    "% of feedback incorporated": "(Feedback incorporated / Total feedback) * 100",
                    "Stakeholder satisfaction with participatory curriculum development": "Average satisfaction score from participatory surveys",
                    "Number of co-created learning materials": "Total co-created materials"
                },
                "Monitor and evaluate curriculum effectiveness": {
                    "Number of curriculum impact studies conducted": "Total curriculum studies",
                    "% of curriculum objectives met": "(Objectives met / Total objectives) * 100",
                    "Stakeholder satisfaction with evaluation processes": "Average satisfaction score from evaluation surveys",
                    "Improvement in student competency scores": "((Current scores - Previous) / Previous) * 100"
                }
            },

            # Area 12: Student Wellbeing & Inclusion
            "Education / Student Wellbeing & Inclusion": {
                "Improve mental health support": {
                    "Number of counseling programs conducted": "Total counseling programs",
                    "% of students accessing support": "(Students accessing support / Total students) * 100",
                    "Stakeholder satisfaction with mental health initiatives": "Average satisfaction score from mental health surveys",
                    "Reduction in mental health-related absenteeism": "((Previous absenteeism - Current) / Previous) * 100"
                },
                "Promote inclusive education": {
                    "% of students with special needs supported": "(Special needs students supported / Total special needs) * 100",
                    "Number of accessibility programs implemented": "Total accessibility programs",
                    "Stakeholder perception of inclusivity": "Average perception score from inclusivity surveys",
                    "Reduction in learning barriers": "((Previous barriers - Current) / Previous) * 100"
                },
                "Enhance safety and protection measures": {
                    "Number of safety and anti-bullying programs": "Total safety/anti-bullying programs",
                    "% of schools meeting safety standards": "(Schools meeting standards / Total schools) * 100",
                    "Stakeholder satisfaction with safety measures": "Average satisfaction score from safety surveys",
                    "Reduction in incidents at school": "((Previous incidents - Current) / Previous) * 100"
                },
                "Foster student engagement and participation": {
                    "Number of student councils or leadership programs": "Total student leadership programs",
                    "% of students participating": "(Students participating / Total students) * 100",
                    "Stakeholder satisfaction with student voice": "Average satisfaction score from student voice surveys",
                    "Increase in student-led initiatives": "((Current initiatives - Previous) / Previous) * 100"
                },
                "Support physical health and nutrition": {
                    "Number of school health programs implemented": "Total health programs",
                    "% of students benefiting from nutrition programs": "(Students benefiting / Total students) * 100",
                    "Stakeholder satisfaction with health initiatives": "Average satisfaction score from health surveys",
                    "Improvement in student physical health indicators": "((Current health - Previous) / Previous) * 100"
                },
                "Promote equity in learning opportunities": {
                    "% of marginalized students accessing education": "(Marginalized students accessing / Total marginalized) * 100",
                    "Number of targeted support programs": "Total targeted support programs",
                    "Stakeholder satisfaction with equity initiatives": "Average satisfaction score from equity surveys",
                    "Reduction in performance gaps": "((Previous gaps - Current) / Previous) * 100"
                },
                "Encourage parental and community involvement": {
                    "Number of engagement sessions with parents/community": "Total engagement sessions",
                    "% of feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Improvement in student outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Recognize student achievements": {
                    "Number of awards or recognition programs": "Total recognition programs",
                    "% of students recognized": "(Students recognized / Total students) * 100",
                    "Stakeholder perception of reward systems": "Average perception score from reward surveys",
                    "Improvement in student motivation and performance": "((Current motivation - Previous) / Previous) * 100"
                }
            },

            # Area 13: Policy, Governance & Accountability
            "Education / Policy, Governance & Accountability": {
                "Strengthen school governance structures": {
                    "Number of governance committees established": "Total governance committees",
                    "% of schools with active governance bodies": "(Schools with governance / Total schools) * 100",
                    "Stakeholder satisfaction with governance": "Average satisfaction score from governance surveys",
                    "Improvement in decision-making transparency": "((Current transparency - Previous) / Previous) * 100"
                },
                "Promote accountability in school management": {
                    "Number of performance reports issued": "Total performance reports",
                    "% of issues resolved promptly": "(Issues resolved / Total issues) * 100",
                    "Stakeholder perception of accountability": "Average perception score from accountability surveys",
                    "Reduction in complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Ensure policy compliance and standards": {
                    "% of schools compliant with national education standards": "(Compliant schools / Total schools) * 100",
                    "Number of audits conducted": "Total compliance audits",
                    "Stakeholder satisfaction with compliance": "Average satisfaction score from compliance surveys",
                    "Improvement in overall quality": "((Current quality - Previous) / Previous) * 100"
                },
                "Foster community and parental oversight": {
                    "Number of oversight meetings conducted": "Total oversight meetings",
                    "% of feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with oversight processes": "Average satisfaction score from oversight surveys",
                    "Increase in participatory governance": "((Current participation - Previous) / Previous) * 100"
                },
                "Encourage evidence-based decision making": {
                    "Number of data collection and monitoring programs": "Total data collection programs",
                    "% of decisions based on evidence": "(Evidence-based decisions / Total decisions) * 100",
                    "Stakeholder satisfaction with decision-making quality": "Average satisfaction score from decision-making surveys",
                    "Improvement in school performance indicators": "((Current performance - Previous) / Previous) * 100"
                },
                "Strengthen financial management transparency": {
                    "Number of budget reports shared publicly": "Total budget reports shared",
                    "% of funds used according to plan": "(Funds used as planned / Total funds) * 100",
                    "Stakeholder perception of financial integrity": "Average perception score from financial surveys",
                    "Reduction in financial mismanagement issues": "((Previous issues - Current) / Previous) * 100"
                },
                "Promote policy innovation and reform": {
                    "Number of policy improvement initiatives implemented": "Total policy initiatives",
                    "Stakeholder satisfaction with reforms": "Average satisfaction score from reform surveys",
                    "% of schools adopting new policies": "(Schools adopting new policies / Total schools) * 100",
                    "Improvement in educational outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Enhance regulatory compliance monitoring": {
                    "Number of inspections conducted": "Total inspections conducted",
                    "% of corrective actions implemented": "(Corrective actions implemented / Total required) * 100",
                    "Stakeholder satisfaction with monitoring": "Average satisfaction score from monitoring surveys",
                    "Reduction in policy violations": "((Previous violations - Current) / Previous) * 100"
                }
            },

            # Area 14: Sustainability & Environmental Education
            "Education / Sustainability & Environmental Education": {
                "Promote environmental awareness among students": {
                    "Number of environmental education programs conducted": "Total environmental programs",
                    "% of students participating in sustainability initiatives": "(Students in sustainability / Total students) * 100",
                    "Stakeholder satisfaction with environmental learning": "Average satisfaction score from environmental learning surveys",
                    "Increase in student environmental knowledge scores": "((Current knowledge - Previous) / Previous) * 100"
                },
                "Foster green practices in schools": {
                    "% of schools implementing energy-efficient measures": "(Schools with efficiency / Total schools) * 100",
                    "Number of waste reduction or recycling programs": "Total waste reduction programs",
                    "Stakeholder perception of environmental responsibility": "Average perception score from environmental responsibility surveys",
                    "Reduction in school resource consumption": "((Previous consumption - Current) / Previous) * 100"
                },
                "Encourage student-led environmental projects": {
                    "Number of student sustainability projects implemented": "Total student sustainability projects",
                    "% of projects achieving objectives": "(Successful projects / Total projects) * 100",
                    "Stakeholder satisfaction with student initiatives": "Average satisfaction score from student initiative surveys",
                    "Increase in community environmental impact": "((Current impact - Previous) / Previous) * 100"
                },
                "Integrate sustainability into curriculum": {
                    "% of subjects including sustainability topics": "(Subjects with sustainability / Total subjects) * 100",
                    "Number of curriculum modules updated with environmental content": "Total updated curriculum modules",
                    "Stakeholder satisfaction with curriculum relevance": "Average satisfaction score from curriculum relevance surveys",
                    "Improvement in student sustainability competency": "((Current competency - Previous) / Previous) * 100"
                },
                "Enhance school-community environmental collaboration": {
                    "Number of joint community-school environmental projects": "Total joint environmental projects",
                    "% of community feedback incorporated": "(Feedback incorporated / Total feedback) * 100",
                    "Stakeholder satisfaction with collaboration": "Average satisfaction score from collaboration surveys",
                    "Improvement in local environmental outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Promote responsible resource management": {
                    "Reduction in water, energy, and material waste in schools": "((Previous waste - Current) / Previous) * 100",
                    "Number of resource management programs conducted": "Total resource management programs",
                    "Stakeholder perception of sustainability practices": "Average perception score from sustainability surveys",
                    "% of schools achieving green certification or standards": "(Schools with certification / Total schools) * 100"
                },
                "Increase awareness of climate change and resilience": {
                    "Number of climate education programs": "Total climate education programs",
                    "% of students demonstrating knowledge of climate issues": "(Students with climate knowledge / Total students) * 100",
                    "Stakeholder satisfaction with climate education": "Average satisfaction score from climate education surveys",
                    "Number of climate adaptation projects in schools": "Total climate adaptation projects"
                },
                "Recognize and reward sustainability initiatives": {
                    "Number of awards or recognitions for environmental projects": "Total environmental awards",
                    "% of schools/students recognized for sustainability efforts": "(Recognized entities / Total entities) * 100",
                    "Stakeholder perception of organizational commitment to sustainability": "Average perception score from commitment surveys",
                    "Improvement in school and community sustainability indicators": "((Current indicators - Previous) / Previous) * 100"
                }
            },

            # Area 15: Equity, Inclusion & Social Development
            "Education / Equity, Inclusion & Social Development": {
                "Ensure access to education for marginalized groups": {
                    "% of marginalized or disadvantaged students enrolled": "(Marginalized students enrolled / Total marginalized) * 100",
                    "Number of targeted programs for inclusion": "Total inclusion programs",
                    "Stakeholder satisfaction with equity initiatives": "Average satisfaction score from equity surveys",
                    "Reduction in disparities in educational access": "((Previous disparities - Current) / Previous) * 100"
                },
                "Promote gender equality in education": {
                    "% of female students in schools and programs": "(Female students / Total students) * 100",
                    "Number of initiatives addressing gender gaps": "Total gender equality initiatives",
                    "Stakeholder perception of gender equity": "Average perception score from gender equity surveys",
                    "Improvement in gender parity indicators": "((Current parity - Previous) / Previous) * 100"
                },
                "Support students with special needs": {
                    "% of schools with inclusive facilities": "(Inclusive schools / Total schools) * 100",
                    "Number of programs supporting students with disabilities": "Total special needs programs",
                    "Stakeholder satisfaction with inclusion programs": "Average satisfaction score from inclusion surveys",
                    "Reduction in barriers to learning": "((Previous barriers - Current) / Previous) * 100"
                },
                "Foster cultural diversity and inclusion": {
                    "Number of programs celebrating cultural diversity": "Total diversity programs",
                    "% of students participating in inclusive activities": "(Students in inclusive activities / Total students) * 100",
                    "Stakeholder satisfaction with diversity initiatives": "Average satisfaction score from diversity surveys",
                    "Improvement in cultural awareness and social cohesion": "((Current awareness - Previous) / Previous) * 100"
                },
                "Strengthen community engagement for social development": {
                    "Number of community projects linked to schools": "Total community-school projects",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with social development outcomes": "Average satisfaction score from social development surveys",
                    "Number of students benefiting from community initiatives": "Total students benefiting"
                },
                "Promote equitable access to learning resources": {
                    "% of schools providing resources to underserved students": "(Schools providing resources / Total schools) * 100",
                    "Number of programs ensuring learning equity": "Total equity programs",
                    "Stakeholder satisfaction with resource distribution": "Average satisfaction score from distribution surveys",
                    "Reduction in performance gaps": "((Previous gaps - Current) / Previous) * 100"
                },
                "Encourage civic responsibility and participation": {
                    "Number of programs promoting civic education": "Total civic education programs",
                    "% of students participating in civic initiatives": "(Students in civic initiatives / Total students) * 100",
                    "Stakeholder satisfaction with civic engagement": "Average satisfaction score from civic engagement surveys",
                    "Increase in student civic awareness and participation": "((Current participation - Previous) / Previous) * 100"
                },
                "Recognize achievements in equity and inclusion": {
                    "Number of awards or recognition programs for inclusive practices": "Total inclusion awards",
                    "% of students and schools recognized": "(Recognized entities / Total entities) * 100",
                    "Stakeholder perception of inclusion effectiveness": "Average perception score from inclusion effectiveness surveys",
                    "Improvement in equitable learning outcomes": "((Current outcomes - Previous) / Previous) * 100"
                }
            },

            # Area 16: Socio-Economic Development & Employability
            "Education / Socio-Economic Development & Employability": {
                "Enhance career guidance and employability skills": {
                    "Number of career counseling sessions conducted": "Total career counseling sessions",
                    "% of students receiving employability training": "(Students with training / Total students) * 100",
                    "Stakeholder satisfaction with career guidance": "Average satisfaction score from career guidance surveys",
                    "Increase in successful transitions to employment or higher education": "((Current transitions - Previous) / Previous) * 100"
                },
                "Promote vocational and technical skills development": {
                    "% of students completing vocational programs": "(Students completing vocational / Total vocational students) * 100",
                    "Number of certifications issued": "Total certifications awarded",
                    "Stakeholder perception of employability": "Average perception score from employability surveys",
                    "Improvement in graduate job placement rates": "((Current placement - Previous) / Previous) * 100"
                },
                "Strengthen entrepreneurship and innovation programs": {
                    "Number of entrepreneurship initiatives implemented": "Total entrepreneurship initiatives",
                    "% of students participating in innovation projects": "(Students in innovation / Total students) * 100",
                    "Stakeholder satisfaction with entrepreneurial programs": "Average satisfaction score from entrepreneurship surveys",
                    "Number of startups or student projects successfully launched": "Total successful student ventures"
                },
                "Foster partnerships with industries and employers": {
                    "Number of school-industry partnership programs": "Total industry partnerships",
                    "% of students accessing internship or apprenticeship opportunities": "(Students with internships / Total students) * 100",
                    "Stakeholder satisfaction with industry collaboration": "Average satisfaction score from collaboration surveys",
                    "Improvement in workforce readiness": "((Current readiness - Previous) / Previous) * 100"
                },
                "Support socio-economic mobility through education": {
                    "Number of scholarships or financial aid programs provided": "Total scholarship programs",
                    "% of disadvantaged students benefiting": "(Disadvantaged students benefiting / Total disadvantaged) * 100",
                    "Stakeholder satisfaction with socio-economic support": "Average satisfaction score from socio-economic surveys",
                    "Increase in graduation rates among target populations": "((Current graduation - Previous) / Previous) * 100"
                },
                "Promote community-based economic development": {
                    "Number of school-community development projects": "Total community development projects",
                    "% of projects benefiting local economy": "(Projects benefiting economy / Total projects) * 100",
                    "Stakeholder perception of socio-economic impact": "Average perception score from socio-economic impact surveys",
                    "Increase in community employment opportunities": "((Current opportunities - Previous) / Previous) * 100"
                },
                "Enhance student entrepreneurship and employability recognition": {
                    "Number of student awards or recognition for employability skills": "Total employability awards",
                    "% of students achieving measurable career milestones": "(Students achieving milestones / Total students) * 100",
                    "Stakeholder satisfaction with recognition programs": "Average satisfaction score from recognition surveys",
                    "Improvement in student career readiness": "((Current readiness - Previous) / Previous) * 100"
                },
                "Monitor and evaluate socio-economic impact": {
                    "Number of socio-economic impact assessments conducted": "Total impact assessments",
                    "% of objectives achieved in development programs": "(Objectives achieved / Total objectives) * 100",
                    "Stakeholder satisfaction with monitoring outcomes": "Average satisfaction score from monitoring surveys",
                    "Improvement in socio-economic indicators linked to education": "((Current indicators - Previous) / Previous) * 100"
                }
            },

            #education end

            #transport start
            # Area 1: Passenger Satisfaction & Experience
            "Transport / Passenger Satisfaction & Experience": {
                "Enhance overall passenger satisfaction": {
                    "Passenger satisfaction survey score": "Average score from passenger satisfaction surveys",
                    "% of complaints resolved within service standards": "(Complaints resolved within SLA / Total complaints) * 100",
                    "% of repeat passengers or subscribers": "(Repeat passengers / Total passengers) * 100",
                    "Number of positive passenger testimonials": "Total positive testimonials received"
                },
                "Improve service reliability": {
                    "% of services operating on schedule": "(On-time services / Total services) * 100",
                    "Average delay per route": "Total delay minutes / Number of routes",
                    "Passenger perception of punctuality": "Average perception score from punctuality surveys",
                    "Number of service disruptions addressed promptly": "Total disruptions resolved within SLA"
                },
                "Strengthen passenger engagement": {
                    "Number of customer feedback sessions conducted": "Total feedback sessions held",
                    "% of feedback incorporated into service improvements": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with engagement mechanisms": "Average satisfaction score from engagement surveys",
                    "Increase in passenger participation in surveys": "((Current participation - Previous) / Previous) * 100"
                },
                "Ensure passenger safety and security": {
                    "Number of safety incidents reported": "Total safety incidents reported",
                    "% of incidents addressed within SLA": "(Incidents resolved within SLA / Total incidents) * 100",
                    "Passenger perception of safety": "Average perception score from safety surveys",
                    "Number of safety awareness programs conducted": "Total safety awareness programs"
                },
                "Enhance service accessibility": {
                    "% of routes accessible to disabled or vulnerable passengers": "(Accessible routes / Total routes) * 100",
                    "Number of accessible facilities and vehicles": "Total accessible facilities and vehicles",
                    "Stakeholder satisfaction with accessibility": "Average satisfaction score from accessibility surveys",
                    "Increase in usage by previously underserved passenger groups": "((Current usage - Previous) / Previous) * 100"
                },
                "Improve ticketing and customer service efficiency": {
                    "Average ticketing transaction time": "Total transaction time / Number of transactions",
                    "% of ticketing issues resolved on first contact": "(Issues resolved first contact / Total issues) * 100",
                    "Passenger satisfaction with service counters or apps": "Average satisfaction score from ticketing surveys",
                    "Number of complaints related to ticketing": "Total ticketing-related complaints"
                },
                "Strengthen passenger communication": {
                    "% of real-time updates provided to passengers": "(Updates provided / Total required updates) * 100",
                    "Number of communication channels utilized": "Total communication channels available",
                    "Stakeholder perception of information clarity": "Average perception score from communication surveys",
                    "Reduction in passenger complaints due to misinformation": "((Previous misinformation complaints - Current) / Previous) * 100"
                },
                "Build trust and credibility with passengers": {
                    "Passenger trust index": "Composite trust score from passenger surveys",
                    "% of services delivered as promised": "(Services delivered as promised / Total services) * 100",
                    "Number of awards or recognitions for service excellence": "Total awards and recognitions received",
                    "Stakeholder confidence in organization integrity": "Average confidence score from stakeholder surveys"
                }
            },

            # Area 2: Infrastructure Development & Maintenance
            "Transport / Infrastructure Development & Maintenance": {
                "Expand transport network coverage": {
                    "Kilometers of new roads, rail, or transit lines constructed": "Total kilometers of new infrastructure",
                    "% of planned network completed on schedule": "(Completed network / Planned network) * 100",
                    "Stakeholder satisfaction with network expansion": "Average satisfaction score from expansion surveys",
                    "Reduction in travel time for users": "((Previous travel time - Current) / Previous) * 100"
                },
                "Maintain existing infrastructure quality": {
                    "% of infrastructure passing quality inspections": "(Infrastructure passing / Total inspected) * 100",
                    "Number of maintenance programs completed on time": "Total maintenance programs completed within schedule",
                    "Stakeholder perception of reliability": "Average perception score from reliability surveys",
                    "Reduction in service disruptions due to infrastructure failure": "((Previous disruptions - Current) / Previous) * 100"
                },
                "Promote sustainable and resilient infrastructure": {
                    "% of projects with sustainable design features": "(Sustainable projects / Total projects) * 100",
                    "Number of climate-resilient projects implemented": "Total climate-resilient projects completed",
                    "Stakeholder satisfaction with sustainability efforts": "Average satisfaction score from sustainability surveys",
                    "Reduction in environmental complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Ensure accessibility and inclusivity": {
                    "% of infrastructure accessible to persons with disabilities": "(Accessible infrastructure / Total infrastructure) * 100",
                    "Number of transport hubs with universal design features": "Total hubs with universal design",
                    "Stakeholder satisfaction with accessibility improvements": "Average satisfaction score from accessibility surveys",
                    "Increase in usage by vulnerable groups": "((Current usage - Previous) / Previous) * 100"
                },
                "Strengthen connectivity in underserved areas": {
                    "% of previously unserved areas connected": "(Connected areas / Previously unserved areas) * 100",
                    "Number of new routes or links established": "Total new routes/links created",
                    "Stakeholder satisfaction with connectivity": "Average satisfaction score from connectivity surveys",
                    "Increase in economic activity or access in newly connected areas": "((Current activity - Previous) / Previous) * 100"
                },
                "Promote multimodal integration": {
                    "Number of hubs integrating multiple transport modes": "Total multimodal hubs",
                    "% of passengers using multimodal services": "(Multimodal passengers / Total passengers) * 100",
                    "Stakeholder satisfaction with integration efficiency": "Average satisfaction score from integration surveys",
                    "Reduction in transfer/waiting times": "((Previous transfer time - Current) / Previous) * 100"
                },
                "Enhance community engagement in infrastructure planning": {
                    "Number of public consultation sessions conducted": "Total consultation sessions",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participatory planning": "Average satisfaction score from planning surveys",
                    "Number of co-created solutions implemented": "Total co-created solutions"
                },
                "Monitor and evaluate infrastructure impact": {
                    "Number of infrastructure performance assessments": "Total performance assessments conducted",
                    "% of objectives achieved": "(Objectives achieved / Total objectives) * 100",
                    "Stakeholder satisfaction with evaluation processes": "Average satisfaction score from evaluation surveys",
                    "Improvement in travel efficiency and user satisfaction": "((Current efficiency - Previous) / Previous) * 100"
                }
            },

            # Area 3: Road Safety & Traffic Management
            "Transport / Road Safety & Traffic Management": {
                "Reduce traffic accidents and fatalities": {
                    "Number of traffic accidents reported": "Total accidents reported",
                    "% reduction in accident rate compared to previous year": "((Previous accidents - Current) / Previous) * 100",
                    "Stakeholder perception of road safety": "Average perception score from safety surveys",
                    "Number of road safety awareness campaigns conducted": "Total safety campaigns conducted"
                },
                "Improve traffic flow and congestion management": {
                    "Average travel time on major routes": "Total travel time / Number of routes monitored",
                    "% reduction in congestion hotspots": "((Previous hotspots - Current) / Previous) * 100",
                    "Stakeholder satisfaction with traffic management": "Average satisfaction score from traffic management surveys",
                    "Number of congestion mitigation initiatives implemented": "Total congestion initiatives"
                },
                "Strengthen enforcement of traffic regulations": {
                    "Number of traffic violations detected and addressed": "Total violations addressed",
                    "% of compliance with road safety rules": "(Compliant observations / Total observations) * 100",
                    "Stakeholder perception of regulatory effectiveness": "Average perception score from regulatory surveys",
                    "Reduction in repeat offenses": "((Previous repeat offenses - Current) / Previous) * 100"
                },
                "Promote pedestrian and cyclist safety": {
                    "Number of pedestrian/cyclist accidents reported": "Total pedestrian/cyclist accidents",
                    "% of safe pedestrian and cycling pathways": "(Safe pathways / Total pathways) * 100",
                    "Stakeholder satisfaction with non-motorized transport safety": "Average satisfaction score from non-motorized transport surveys",
                    "Increase in pedestrian/cyclist usage of safe routes": "((Current usage - Previous) / Previous) * 100"
                },
                "Enhance public awareness of traffic rules": {
                    "Number of traffic education campaigns": "Total education campaigns conducted",
                    "% of target population reached": "(Population reached / Target population) * 100",
                    "Stakeholder perception of awareness effectiveness": "Average perception score from awareness surveys",
                    "Reduction in preventable accidents": "((Previous preventable accidents - Current) / Previous) * 100"
                },
                "Improve emergency response for traffic incidents": {
                    "Average response time to accidents": "Total response time / Number of incidents",
                    "% of incidents resolved within SLA": "(Incidents resolved within SLA / Total incidents) * 100",
                    "Stakeholder satisfaction with emergency services": "Average satisfaction score from emergency service surveys",
                    "Reduction in fatalities or injuries": "((Previous fatalities/injuries - Current) / Previous) * 100"
                },
                "Strengthen community participation in safety programs": {
                    "Number of community road safety initiatives": "Total community safety initiatives",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participatory programs": "Average satisfaction score from participation surveys",
                    "Reduction in local accident hotspots": "((Previous hotspots - Current) / Previous) * 100"
                },
                "Monitor and report safety performance": {
                    "Number of safety performance reports published": "Total safety reports published",
                    "% of objectives achieved in road safety programs": "(Objectives achieved / Total objectives) * 100",
                    "Stakeholder satisfaction with reporting transparency": "Average satisfaction score from transparency surveys",
                    "Improvement in traffic safety indicators": "((Current indicators - Previous) / Previous) * 100"
                }
            },

            # Area 4: Public Transport Operations
            "Transport / Public Transport Operations": {
                "Increase reliability of public transport services": {
                    "% of services operating on schedule": "(On-time services / Total services) * 100",
                    "Average delay per route": "Total delay minutes / Number of routes",
                    "Passenger satisfaction with service reliability": "Average satisfaction score from reliability surveys",
                    "Reduction in service interruptions": "((Previous interruptions - Current) / Previous) * 100"
                },
                "Expand coverage of public transport network": {
                    "Number of new routes introduced": "Total new routes added",
                    "% of underserved areas covered": "(Covered underserved areas / Total underserved areas) * 100",
                    "Stakeholder satisfaction with accessibility improvements": "Average satisfaction score from accessibility surveys",
                    "Increase in ridership from newly served areas": "((Current ridership - Previous) / Previous) * 100"
                },
                "Enhance affordability for passengers": {
                    "% of trips within affordable pricing range": "(Affordable trips / Total trips) * 100",
                    "Number of subsidy programs implemented": "Total subsidy programs active",
                    "Passenger perception of value for money": "Average perception score from value surveys",
                    "Reduction in complaints regarding fare pricing": "((Previous pricing complaints - Current) / Previous) * 100"
                },
                "Promote safety in public transport": {
                    "Number of safety incidents reported": "Total safety incidents reported",
                    "% of incidents resolved within service standards": "(Incidents resolved within standards / Total incidents) * 100",
                    "Passenger perception of safety": "Average perception score from safety surveys",
                    "Number of safety awareness programs conducted": "Total safety awareness programs"
                },
                "Improve passenger experience and comfort": {
                    "Passenger satisfaction survey score": "Average satisfaction score from passenger surveys",
                    "Number of modernized vehicles or upgrades": "Total vehicles modernized or upgraded",
                    "Stakeholder perception of service quality": "Average perception score from quality surveys",
                    "Reduction in complaints regarding service comfort": "((Previous comfort complaints - Current) / Previous) * 100"
                },
                "Enhance accessibility for vulnerable groups": {
                    "% of transport vehicles accessible for persons with disabilities": "(Accessible vehicles / Total vehicles) * 100",
                    "Number of accessible facilities at stations": "Total accessible station facilities",
                    "Stakeholder satisfaction with inclusivity": "Average satisfaction score from inclusivity surveys",
                    "Increase in ridership among vulnerable groups": "((Current ridership - Previous) / Previous) * 100"
                },
                "Strengthen passenger engagement and feedback mechanisms": {
                    "Number of passenger feedback sessions conducted": "Total feedback sessions held",
                    "% of feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with responsiveness": "Average satisfaction score from responsiveness surveys",
                    "Number of suggestions leading to service improvement": "Total suggestions implemented"
                },
                "Foster trust and transparency": {
                    "Passenger trust index": "Composite trust score from passenger surveys",
                    "Number of public service performance reports": "Total performance reports published",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Number of recognitions for service excellence": "Total service excellence recognitions"
                }
            },

            # Area 5: Logistics & Freight Operations
            "Transport / Logistics & Freight Operations": {
                "Ensure timely delivery of goods": {
                    "% of shipments delivered on schedule": "(On-time shipments / Total shipments) * 100",
                    "Average delay per shipment": "Total delay time / Number of shipments",
                    "Stakeholder satisfaction with logistics reliability": "Average satisfaction score from logistics surveys",
                    "Reduction in late deliveries": "((Previous late deliveries - Current) / Previous) * 100"
                },
                "Enhance safety in freight operations": {
                    "Number of freight-related accidents reported": "Total freight accidents reported",
                    "% of incidents resolved within standards": "(Incidents resolved within standards / Total incidents) * 100",
                    "Stakeholder perception of freight safety": "Average perception score from freight safety surveys",
                    "Number of safety training programs for logistics staff": "Total safety training programs conducted"
                },
                "Improve efficiency of logistics operations": {
                    "Average turnaround time per shipment": "Total turnaround time / Number of shipments",
                    "% of shipments processed without errors": "(Error-free shipments / Total shipments) * 100",
                    "Stakeholder satisfaction with operational efficiency": "Average satisfaction score from efficiency surveys",
                    "Reduction in operational bottlenecks": "((Previous bottlenecks - Current) / Previous) * 100"
                },
                "Promote environmentally sustainable logistics": {
                    "% of fleet using low-emission or electric vehicles": "(Low-emission vehicles / Total fleet) * 100",
                    "Number of green logistics initiatives": "Total green initiatives implemented",
                    "Stakeholder perception of sustainability efforts": "Average perception score from sustainability surveys",
                    "Reduction in carbon emissions per shipment": "((Previous emissions - Current) / Previous) * 100"
                },
                "Increase transparency for customers and partners": {
                    "% of shipments tracked in real-time": "(Real-time tracked shipments / Total shipments) * 100",
                    "Number of logistics performance reports shared": "Total performance reports shared with stakeholders",
                    "Stakeholder satisfaction with information accuracy": "Average satisfaction score from information surveys",
                    "Reduction in customer complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Enhance collaboration with partners": {
                    "Number of joint logistics initiatives with stakeholders": "Total joint initiatives",
                    "% of feedback incorporated from partners": "(Partner feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with collaboration": "Average satisfaction score from collaboration surveys",
                    "Improvement in overall service performance": "((Current performance - Previous) / Previous) * 100"
                },
                "Improve infrastructure support for freight": {
                    "Number of warehouses, hubs, or depots upgraded": "Total facilities upgraded",
                    "% of freight facilities meeting operational standards": "(Facilities meeting standards / Total facilities) * 100",
                    "Stakeholder satisfaction with infrastructure support": "Average satisfaction score from infrastructure surveys",
                    "Reduction in congestion at freight hubs": "((Previous congestion - Current) / Previous) * 100"
                },
                "Strengthen monitoring and evaluation": {
                    "Number of logistics performance assessments conducted": "Total performance assessments",
                    "% of KPIs met per operational cycle": "(KPIs met / Total KPIs) * 100",
                    "Stakeholder satisfaction with monitoring": "Average satisfaction score from monitoring surveys",
                    "Improvement in delivery efficiency": "((Current efficiency - Previous) / Previous) * 100"
                }
            },

            # Area 6: Environmental Sustainability & Green Mobility
            "Transport / Environmental Sustainability & Green Mobility": {
                "Promote low-emission transport solutions": {
                    "% of vehicles using clean energy or fuel-efficient technology": "(Clean energy vehicles / Total vehicles) * 100",
                    "Number of green transport projects implemented": "Total green transport projects",
                    "Stakeholder perception of sustainability": "Average perception score from sustainability surveys",
                    "Reduction in emissions per km of transport": "((Previous emissions - Current) / Previous) * 100"
                },
                "Encourage public adoption of sustainable transport": {
                    "% of passengers using low-emission transport options": "(Passengers using green transport / Total passengers) * 100",
                    "Number of campaigns promoting sustainable mobility": "Total sustainability campaigns conducted",
                    "Stakeholder satisfaction with adoption initiatives": "Average satisfaction score from adoption surveys",
                    "Increase in ridership using green modes": "((Current ridership - Previous) / Previous) * 100"
                },
                "Reduce traffic congestion and pollution": {
                    "Average travel time in congested areas": "Total travel time in congestion / Number of areas",
                    "% reduction in traffic-related emissions": "((Previous emissions - Current) / Previous) * 100",
                    "Stakeholder perception of environmental impact": "Average perception score from environmental impact surveys",
                    "Number of traffic congestion mitigation projects": "Total congestion mitigation projects"
                },
                "Integrate environmental standards in infrastructure": {
                    "% of transport infrastructure meeting environmental standards": "(Infrastructure meeting standards / Total infrastructure) * 100",
                    "Number of eco-friendly projects implemented": "Total eco-friendly projects completed",
                    "Stakeholder satisfaction with sustainable design": "Average satisfaction score from design surveys",
                    "Reduction in environmental complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Promote community awareness and engagement": {
                    "Number of environmental workshops or events": "Total environmental events conducted",
                    "% of community participating in sustainable transport initiatives": "(Community participants / Total community) * 100",
                    "Stakeholder satisfaction with awareness programs": "Average satisfaction score from awareness surveys",
                    "Improvement in public knowledge of sustainable transport": "((Current knowledge - Previous) / Previous) * 100"
                },
                "Monitor and report environmental performance": {
                    "Number of environmental performance reports published": "Total environmental reports published",
                    "% of sustainability objectives achieved": "(Objectives achieved / Total objectives) * 100",
                    "Stakeholder satisfaction with reporting transparency": "Average satisfaction score from transparency surveys",
                    "Reduction in carbon footprint of transport operations": "((Previous footprint - Current) / Previous) * 100"
                },
                "Foster innovation in green transport solutions": {
                    "Number of innovative green transport solutions piloted": "Total green innovation pilots",
                    "% of successful pilot projects implemented": "(Successful pilots implemented / Total pilots) * 100",
                    "Stakeholder satisfaction with innovation programs": "Average satisfaction score from innovation surveys",
                    "Reduction in energy consumption per passenger/km": "((Previous consumption - Current) / Previous) * 100"
                },
                "Recognize and reward sustainability efforts": {
                    "Number of awards or recognitions for green initiatives": "Total sustainability awards received",
                    "% of projects or staff recognized for sustainability": "(Recognized entities / Total entities) * 100",
                    "Stakeholder perception of organizational commitment": "Average perception score from commitment surveys",
                    "Improvement in environmental performance indicators": "((Current indicators - Previous) / Previous) * 100"
                }
            },

            # Area 7: Traffic Management & Congestion Control
            "Transport / Traffic Management & Congestion Control": {
                "Improve traffic flow efficiency": {
                    "Average travel time on major routes": "Total travel time / Number of major routes",
                    "% reduction in congestion hotspots": "((Previous hotspots - Current) / Previous) * 100",
                    "Stakeholder satisfaction with traffic flow": "Average satisfaction score from traffic flow surveys",
                    "Number of congestion mitigation projects implemented": "Total congestion projects implemented"
                },
                "Reduce peak-hour delays": {
                    "% reduction in peak-hour travel time": "((Previous peak time - Current) / Previous) * 100",
                    "Average vehicle delay during peak hours": "Total delay minutes / Number of peak hours monitored",
                    "Stakeholder perception of improvement": "Average perception score from improvement surveys",
                    "Number of interventions implemented to manage peak-hour traffic": "Total peak-hour interventions"
                },
                "Enhance traffic monitoring and control systems": {
                    "Number of intelligent traffic systems installed": "Total intelligent systems installed",
                    "% of traffic incidents detected in real-time": "(Real-time detected incidents / Total incidents) * 100",
                    "Stakeholder satisfaction with monitoring systems": "Average satisfaction score from monitoring surveys",
                    "Reduction in response time for traffic incidents": "((Previous response time - Current) / Previous) * 100"
                },
                "Promote pedestrian and cyclist safety": {
                    "Number of pedestrian/cyclist pathways constructed": "Total new pathways constructed",
                    "% reduction in accidents involving non-motorized users": "((Previous accidents - Current) / Previous) * 100",
                    "Stakeholder satisfaction with safety measures": "Average satisfaction score from safety surveys",
                    "Increase in pedestrian/cyclist usage": "((Current usage - Previous) / Previous) * 100"
                },
                "Improve public awareness of traffic rules": {
                    "Number of traffic education campaigns conducted": "Total education campaigns",
                    "% of target population reached": "(Population reached / Target population) * 100",
                    "Stakeholder satisfaction with awareness programs": "Average satisfaction score from awareness surveys",
                    "Reduction in traffic violations": "((Previous violations - Current) / Previous) * 100"
                },
                "Strengthen enforcement of regulations": {
                    "% of traffic violations addressed": "(Violations addressed / Total violations) * 100",
                    "Number of traffic enforcement operations conducted": "Total enforcement operations",
                    "Stakeholder perception of regulatory effectiveness": "Average perception score from regulatory surveys",
                    "Reduction in repeat offenses": "((Previous repeat offenses - Current) / Previous) * 100"
                },
                "Engage communities in traffic solutions": {
                    "Number of public consultation sessions": "Total consultation sessions held",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participatory approach": "Average satisfaction score from participation surveys",
                    "Number of community-driven traffic improvement initiatives": "Total community-driven initiatives"
                },
                "Monitor and report performance": {
                    "Number of traffic performance reports published": "Total traffic reports published",
                    "% of traffic management KPIs achieved": "(KPIs achieved / Total KPIs) * 100",
                    "Stakeholder satisfaction with transparency": "Average satisfaction score from transparency surveys",
                    "Improvement in overall traffic efficiency": "((Current efficiency - Previous) / Previous) * 100"
                }
            },

            # Area 8: Accessibility & Inclusivity
            "Transport / Accessibility & Inclusivity": {
                "Increase access for persons with disabilities": {
                    "% of transport services fully accessible": "(Accessible services / Total services) * 100",
                    "Number of accessibility upgrades completed": "Total accessibility upgrades",
                    "Stakeholder satisfaction with inclusivity": "Average satisfaction score from inclusivity surveys",
                    "Increase in usage by disabled passengers": "((Current usage - Previous) / Previous) * 100"
                },
                "Enhance services for vulnerable populations": {
                    "Number of programs targeting elderly or low-income groups": "Total targeted programs",
                    "% of transport services serving underserved areas": "(Services in underserved areas / Total services) * 100",
                    "Stakeholder satisfaction with inclusivity programs": "Average satisfaction score from program surveys",
                    "Increase in ridership among vulnerable groups": "((Current ridership - Previous) / Previous) * 100"
                },
                "Promote gender-sensitive transport services": {
                    "% of transport routes and stations with safety features for women": "(Routes/stations with safety features / Total) * 100",
                    "Number of gender-inclusive initiatives implemented": "Total gender-inclusive initiatives",
                    "Stakeholder satisfaction with gender inclusivity": "Average satisfaction score from gender surveys",
                    "Reduction in complaints from female passengers": "((Previous complaints - Current) / Previous) * 100"
                },
                "Improve affordability for marginalized groups": {
                    "% of subsidized trips for low-income passengers": "(Subsidized trips / Total trips) * 100",
                    "Number of fare assistance programs implemented": "Total fare assistance programs",
                    "Stakeholder satisfaction with fare equity": "Average satisfaction score from equity surveys",
                    "Reduction in complaints regarding pricing": "((Previous pricing complaints - Current) / Previous) * 100"
                },
                "Foster community engagement in accessibility planning": {
                    "Number of public consultations conducted": "Total accessibility consultations",
                    "% of community feedback incorporated": "(Feedback incorporated / Total feedback) * 100",
                    "Stakeholder satisfaction with participatory planning": "Average satisfaction score from planning surveys",
                    "Number of accessibility improvements implemented": "Total accessibility improvements"
                },
                "Enhance information accessibility": {
                    "% of transport information available in multiple formats": "(Information in multiple formats / Total information) * 100",
                    "Number of accessibility-focused communication campaigns": "Total accessibility campaigns",
                    "Stakeholder satisfaction with information clarity": "Average satisfaction score from information surveys",
                    "Increase in awareness among vulnerable groups": "((Current awareness - Previous) / Previous) * 100"
                },
                "Monitor accessibility outcomes": {
                    "Number of accessibility audits conducted": "Total accessibility audits",
                    "% of objectives achieved in accessibility programs": "(Objectives achieved / Total objectives) * 100",
                    "Stakeholder satisfaction with reporting": "Average satisfaction score from reporting surveys",
                    "Improvement in accessibility indicators": "((Current indicators - Previous) / Previous) * 100"
                },
                "Recognize achievements in inclusivity": {
                    "Number of awards for accessibility or inclusivity": "Total inclusivity awards received",
                    "% of services recognized for inclusivity improvements": "(Services recognized / Total services) * 100",
                    "Stakeholder perception of commitment to inclusivity": "Average perception score from commitment surveys",
                    "Improvement in satisfaction levels of vulnerable groups": "((Current satisfaction - Previous) / Previous) * 100"
                }
            },

            # Area 9: Digital Services & Smart Mobility
            "Transport / Digital Services & Smart Mobility": {
                "Enhance digital ticketing and payment systems": {
                    "% of passengers using digital tickets": "(Digital ticket users / Total passengers) * 100",
                    "Average transaction time for digital payments": "Total transaction time / Number of digital transactions",
                    "Stakeholder satisfaction with digital services": "Average satisfaction score from digital service surveys",
                    "Reduction in ticketing-related complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Improve real-time passenger information": {
                    "% of passengers receiving real-time updates": "(Passengers receiving updates / Total passengers) * 100",
                    "Number of transport apps or digital platforms deployed": "Total digital platforms available",
                    "Stakeholder satisfaction with communication": "Average satisfaction score from communication surveys",
                    "Reduction in passenger complaints due to lack of information": "((Previous information complaints - Current) / Previous) * 100"
                },
                "Promote digital accessibility for all users": {
                    "% of digital services accessible to persons with disabilities": "(Accessible digital services / Total digital services) * 100",
                    "Number of inclusive design upgrades implemented": "Total inclusive design upgrades",
                    "Stakeholder satisfaction with digital accessibility": "Average satisfaction score from digital accessibility surveys",
                    "Increase in usage by diverse passenger groups": "((Current usage - Previous) / Previous) * 100"
                },
                "Integrate smart mobility solutions": {
                    "Number of smart traffic or vehicle management systems installed": "Total smart systems installed",
                    "% of operations managed via smart systems": "(Smart-managed operations / Total operations) * 100",
                    "Stakeholder satisfaction with technological innovation": "Average satisfaction score from innovation surveys",
                    "Reduction in operational inefficiencies": "((Previous inefficiencies - Current) / Previous) * 100"
                },
                "Foster passenger engagement through digital platforms": {
                    "Number of online feedback or consultation sessions": "Total digital engagement sessions",
                    "% of digital feedback incorporated into service improvements": "(Digital feedback implemented / Total digital feedback) * 100",
                    "Stakeholder satisfaction with responsiveness": "Average satisfaction score from responsiveness surveys",
                    "Increase in passenger engagement via apps or platforms": "((Current engagement - Previous) / Previous) * 100"
                },
                "Promote sustainability through smart mobility": {
                    "Number of eco-friendly mobility initiatives using digital solutions": "Total digital sustainability initiatives",
                    "% of smart transport projects achieving environmental targets": "(Projects meeting targets / Total projects) * 100",
                    "Stakeholder satisfaction with green mobility efforts": "Average satisfaction score from green mobility surveys",
                    "Reduction in emissions per passenger/km": "((Previous emissions - Current) / Previous) * 100"
                },
                "Monitor and evaluate digital service performance": {
                    "Number of performance reports generated": "Total digital performance reports",
                    "% of digital KPIs achieved": "(Digital KPIs achieved / Total digital KPIs) * 100",
                    "Stakeholder satisfaction with reporting transparency": "Average satisfaction score from transparency surveys",
                    "Improvement in user experience metrics": "((Current UX metrics - Previous) / Previous) * 100"
                },
                "Recognize innovation in digital transport": {
                    "Number of awards or recognitions for digital innovation": "Total digital innovation awards",
                    "% of projects or teams recognized": "(Recognized entities / Total entities) * 100",
                    "Stakeholder perception of technological leadership": "Average perception score from leadership surveys",
                    "Improvement in digital service adoption rates": "((Current adoption - Previous) / Previous) * 100"
                }
            },

            # Area 10: Freight & Logistics Efficiency
            "Transport / Freight & Logistics Efficiency": {
                "Optimize delivery times": {
                    "Average delivery time per shipment": "Total delivery time / Number of shipments",
                    "% of shipments delivered on schedule": "(On-time shipments / Total shipments) * 100",
                    "Stakeholder satisfaction with logistics speed": "Average satisfaction score from speed surveys",
                    "Reduction in delayed shipments": "((Previous delays - Current) / Previous) * 100"
                },
                "Reduce operational costs": {
                    "Cost per shipment or ton-km": "Total operational cost / Total shipments or ton-km",
                    "% reduction in fuel and maintenance costs": "((Previous costs - Current) / Previous) * 100",
                    "Stakeholder perception of efficiency": "Average perception score from efficiency surveys",
                    "Number of cost-saving initiatives implemented": "Total cost-saving initiatives"
                },
                "Enhance safety in freight operations": {
                    "Number of accidents/incidents reported": "Total freight accidents/incidents",
                    "% of incidents resolved within SLA": "(Incidents resolved within SLA / Total incidents) * 100",
                    "Stakeholder satisfaction with freight safety": "Average satisfaction score from freight safety surveys",
                    "Number of safety training programs for staff": "Total safety training programs"
                },
                "Improve reliability and predictability": {
                    "% of shipments delivered without deviation": "(Deviation-free shipments / Total shipments) * 100",
                    "Number of disruptions due to infrastructure or operational issues": "Total disruptions reported",
                    "Stakeholder satisfaction with reliability": "Average satisfaction score from reliability surveys",
                    "Reduction in repeated delays": "((Previous repeated delays - Current) / Previous) * 100"
                },
                "Promote environmentally sustainable logistics": {
                    "% of fleet using low-emission or electric vehicles": "(Low-emission vehicles / Total fleet) * 100",
                    "Number of green logistics initiatives": "Total green logistics initiatives",
                    "Stakeholder perception of environmental responsibility": "Average perception score from environmental surveys",
                    "Reduction in carbon footprint per shipment": "((Previous footprint - Current) / Previous) * 100"
                },
                "Enhance stakeholder collaboration": {
                    "Number of collaborative logistics projects with partners": "Total collaborative projects",
                    "% of partner feedback implemented": "(Partner feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with cooperation": "Average satisfaction score from cooperation surveys",
                    "Improvement in overall service delivery": "((Current service delivery - Previous) / Previous) * 100"
                },
                "Ensure infrastructure adequacy": {
                    "Number of freight hubs, warehouses, or depots upgraded": "Total facilities upgraded",
                    "% of facilities meeting operational standards": "(Facilities meeting standards / Total facilities) * 100",
                    "Stakeholder satisfaction with logistics infrastructure": "Average satisfaction score from infrastructure surveys",
                    "Reduction in congestion at hubs": "((Previous congestion - Current) / Previous) * 100"
                },
                "Monitor and report logistics performance": {
                    "Number of performance reports generated": "Total logistics performance reports",
                    "% of KPIs achieved per cycle": "(KPIs achieved / Total KPIs) * 100",
                    "Stakeholder satisfaction with transparency": "Average satisfaction score from transparency surveys",
                    "Improvement in delivery efficiency and reliability": "((Current efficiency - Previous) / Previous) * 100"
                }
            },

            # Area 11: Regulatory Compliance & Governance
            "Transport / Regulatory Compliance & Governance": {
                "Ensure compliance with transport regulations": {
                    "% of operations meeting local and national standards": "(Compliant operations / Total operations) * 100",
                    "Number of compliance audits conducted": "Total compliance audits",
                    "Stakeholder satisfaction with regulatory adherence": "Average satisfaction score from compliance surveys",
                    "Reduction in regulatory violations": "((Previous violations - Current) / Previous) * 100"
                },
                "Strengthen safety oversight": {
                    "Number of safety inspections completed": "Total safety inspections",
                    "% of non-compliance issues resolved": "(Non-compliance issues resolved / Total issues) * 100",
                    "Stakeholder perception of safety governance": "Average perception score from governance surveys",
                    "Reduction in repeat safety violations": "((Previous repeat violations - Current) / Previous) * 100"
                },
                "Promote transparency in operations": {
                    "Number of public reports shared": "Total public reports issued",
                    "% of stakeholder concerns addressed": "(Concerns addressed / Total concerns) * 100",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Increase in trust index": "((Current trust - Previous) / Previous) * 100"
                },
                "Foster ethical practices and integrity": {
                    "% of staff trained on ethics and compliance": "(Staff trained / Total staff) * 100",
                    "Number of ethical complaints received/resolved": "Total ethical complaints handled",
                    "Stakeholder trust index": "Composite trust score from stakeholder surveys",
                    "% of corrective actions implemented": "(Corrective actions implemented / Total required) * 100"
                },
                "Enhance community participation in governance": {
                    "Number of public consultations conducted": "Total governance consultations",
                    "% of community feedback incorporated": "(Feedback incorporated / Total feedback) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Number of co-created solutions implemented": "Total co-created governance solutions"
                },
                "Monitor environmental compliance": {
                    "% of operations adhering to environmental standards": "(Compliant operations / Total operations) * 100",
                    "Number of environmental violations addressed": "Total environmental violations resolved",
                    "Stakeholder satisfaction with sustainability governance": "Average satisfaction score from sustainability governance surveys",
                    "Reduction in environmental incidents": "((Previous incidents - Current) / Previous) * 100"
                },
                "Strengthen institutional capacity": {
                    "Number of staff trained in governance and compliance": "Total staff trained in governance",
                    "% of departments meeting operational standards": "(Departments meeting standards / Total departments) * 100",
                    "Stakeholder perception of organizational competence": "Average perception score from competence surveys",
                    "Improvement in audit performance": "((Current audit performance - Previous) / Previous) * 100"
                },
                "Recognize excellence in governance": {
                    "Number of awards or recognitions for compliance and ethics": "Total governance awards",
                    "% of projects or teams recognized": "(Recognized entities / Total entities) * 100",
                    "Stakeholder perception of organizational integrity": "Average perception score from integrity surveys",
                    "Improvement in governance indicators": "((Current indicators - Previous) / Previous) * 100"
                }
            },

            # Area 12: Innovation & Smart Mobility
            "Transport / Innovation & Smart Mobility": {
                "Implement smart traffic management systems": {
                    "Number of smart traffic systems deployed": "Total smart traffic systems",
                    "% of routes managed through smart systems": "(Smart-managed routes / Total routes) * 100",
                    "Stakeholder satisfaction with innovation": "Average satisfaction score from innovation surveys",
                    "Reduction in traffic congestion": "((Previous congestion - Current) / Previous) * 100"
                },
                "Promote mobility-as-a-service (MaaS)": {
                    "Number of integrated transport services offered": "Total MaaS services available",
                    "% of passengers using MaaS solutions": "(MaaS users / Total passengers) * 100",
                    "Stakeholder satisfaction with service integration": "Average satisfaction score from integration surveys",
                    "Increase in multimodal transport usage": "((Current multimodal usage - Previous) / Previous) * 100"
                },
                "Foster adoption of electric and low-emission vehicles": {
                    "% of fleet using electric or low-emission vehicles": "(Electric/low-emission vehicles / Total fleet) * 100",
                    "Number of pilot projects conducted": "Total electric vehicle pilot projects",
                    "Stakeholder perception of environmental responsibility": "Average perception score from environmental surveys",
                    "Reduction in emissions per passenger/km": "((Previous emissions - Current) / Previous) * 100"
                },
                "Enhance digital ticketing and mobile apps": {
                    "% of passengers using digital ticketing": "(Digital ticket users / Total passengers) * 100",
                    "Number of app downloads and active users": "Total app downloads and monthly active users",
                    "Stakeholder satisfaction with digital services": "Average satisfaction score from digital service surveys",
                    "Reduction in ticketing complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Encourage community engagement in innovation": {
                    "Number of participatory workshops on smart mobility": "Total innovation workshops",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Number of innovative solutions co-created": "Total co-created innovation solutions"
                },
                "Monitor innovation outcomes": {
                    "Number of performance reports on smart mobility projects": "Total innovation performance reports",
                    "% of innovation KPIs achieved": "(Innovation KPIs achieved / Total KPIs) * 100",
                    "Stakeholder satisfaction with results": "Average satisfaction score from results surveys",
                    "Improvement in operational efficiency": "((Current efficiency - Previous) / Previous) * 100"
                },
                "Promote safety through technology": {
                    "Number of technology-enabled safety interventions": "Total tech safety interventions",
                    "% reduction in incidents due to tech solutions": "((Previous incidents - Current) / Previous) * 100",
                    "Stakeholder perception of safety improvements": "Average perception score from safety surveys",
                    "Number of emergency response times improved": "Total response time improvements"
                },
                "Recognize achievements in innovation": {
                    "Number of awards or recognitions for innovation": "Total innovation awards",
                    "% of projects or teams recognized": "(Recognized entities / Total entities) * 100",
                    "Stakeholder perception of technological leadership": "Average perception score from leadership surveys",
                    "Improvement in service quality through innovation": "((Current quality - Previous) / Previous) * 100"
                }
            },

            # Area 13: Community Engagement & Stakeholder Participation
            "Transport / Community Engagement & Stakeholder Participation": {
                "Increase community involvement in transport planning": {
                    "Number of public consultations conducted": "Total planning consultations",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participatory planning": "Average satisfaction score from planning surveys",
                    "Number of co-created projects implemented": "Total co-created projects"
                },
                "Promote transparency with stakeholders": {
                    "Number of project updates shared publicly": "Total project updates shared",
                    "% of stakeholder queries addressed": "(Queries addressed / Total queries) * 100",
                    "Stakeholder perception of transparency": "Average perception score from transparency surveys",
                    "Increase in trust and confidence index": "((Current trust index - Previous) / Previous) * 100"
                },
                "Strengthen citizen awareness of transport projects": {
                    "Number of awareness campaigns conducted": "Total awareness campaigns",
                    "% of target population reached": "(Population reached / Target population) * 100",
                    "Stakeholder satisfaction with communication": "Average satisfaction score from communication surveys",
                    "Reduction in community complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Ensure equitable benefits to communities": {
                    "% of projects benefiting underserved populations": "(Projects benefiting underserved / Total projects) * 100",
                    "Number of local employment opportunities created": "Total local jobs created",
                    "Stakeholder perception of socio-economic impact": "Average perception score from impact surveys",
                    "Improvement in community access to transport": "((Current access - Previous) / Previous) * 100"
                },
                "Monitor and report engagement effectiveness": {
                    "Number of engagement reports published": "Total engagement reports",
                    "% of engagement objectives achieved": "(Objectives achieved / Total objectives) * 100",
                    "Stakeholder satisfaction with reporting": "Average satisfaction score from reporting surveys",
                    "Increase in participation rates": "((Current participation - Previous) / Previous) * 100"
                },
                "Promote social responsibility initiatives": {
                    "Number of community development programs supported": "Total community programs supported",
                    "% of projects contributing to local welfare": "(Projects contributing to welfare / Total projects) * 100",
                    "Stakeholder perception of social impact": "Average perception score from social impact surveys",
                    "Improvement in local quality-of-life indicators": "((Current QoL indicators - Previous) / Previous) * 100"
                },
                "Foster partnerships with local organizations": {
                    "Number of collaborative initiatives with NGOs, authorities, and community groups": "Total collaborative initiatives",
                    "% of partner feedback incorporated": "(Partner feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with collaboration": "Average satisfaction score from collaboration surveys",
                    "Increase in joint project outcomes": "((Current outcomes - Previous) / Previous) * 100"
                },
                "Recognize achievements in community engagement": {
                    "Number of awards or recognitions for social responsibility": "Total social responsibility awards",
                    "% of initiatives recognized": "(Initiatives recognized / Total initiatives) * 100",
                    "Stakeholder perception of commitment": "Average perception score from commitment surveys",
                    "Improvement in community satisfaction": "((Current satisfaction - Previous) / Previous) * 100"
                }
            },

            # Area 14: Environmental Sustainability & Green Mobility
            "Transport / Environmental Sustainability & Green Mobility": {
                "Reduce carbon emissions from transport operations": {
                    "% reduction in CO₂ emissions per km": "((Previous emissions - Current) / Previous) * 100",
                    "Number of low-emission vehicles deployed": "Total low-emission vehicles in operation",
                    "Stakeholder perception of environmental responsibility": "Average perception score from environmental surveys",
                    "Improvement in emission performance metrics": "((Current metrics - Previous) / Previous) * 100"
                },
                "Promote use of renewable energy in transport": {
                    "% of transport fleet using renewable energy sources": "(Renewable energy vehicles / Total fleet) * 100",
                    "Number of renewable energy initiatives implemented": "Total renewable energy initiatives",
                    "Stakeholder satisfaction with sustainability efforts": "Average satisfaction score from sustainability surveys",
                    "Reduction in fossil fuel consumption": "((Previous consumption - Current) / Previous) * 100"
                },
                "Increase adoption of eco-friendly transport solutions": {
                    "% of passengers using green transport options": "(Green transport users / Total passengers) * 100",
                    "Number of incentives for eco-friendly transport usage": "Total eco-friendly incentives",
                    "Stakeholder perception of environmental programs": "Average perception score from program surveys",
                    "Increase in ridership of sustainable modes": "((Current ridership - Previous) / Previous) * 100"
                },
                "Minimize environmental impact of infrastructure projects": {
                    "% of transport projects meeting environmental standards": "(Projects meeting standards / Total projects) * 100",
                    "Number of eco-friendly infrastructure projects completed": "Total eco-friendly projects",
                    "Stakeholder perception of sustainable design": "Average perception score from design surveys",
                    "Reduction in environmental complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Foster community awareness on sustainable transport": {
                    "Number of public awareness campaigns conducted": "Total sustainability awareness campaigns",
                    "% of community engaged in sustainability initiatives": "(Community engaged / Total community) * 100",
                    "Stakeholder satisfaction with awareness programs": "Average satisfaction score from awareness surveys",
                    "Improvement in public understanding of green mobility": "((Current understanding - Previous) / Previous) * 100"
                },
                "Monitor and report environmental performance": {
                    "Number of environmental performance reports generated": "Total environmental reports",
                    "% of sustainability KPIs achieved": "(Sustainability KPIs achieved / Total KPIs) * 100",
                    "Stakeholder satisfaction with transparency": "Average satisfaction score from transparency surveys",
                    "Improvement in environmental compliance indicators": "((Current indicators - Previous) / Previous) * 100"
                },
                "Encourage innovation in green transport": {
                    "Number of pilot projects for innovative green solutions": "Total green innovation pilots",
                    "% of successful projects implemented": "(Successful pilots implemented / Total pilots) * 100",
                    "Stakeholder perception of innovation": "Average perception score from innovation surveys",
                    "Reduction in energy consumption per passenger/km": "((Previous consumption - Current) / Previous) * 100"
                },
                "Recognize achievements in sustainability": {
                    "Number of awards or recognitions for environmental initiatives": "Total environmental awards",
                    "% of projects recognized for sustainability": "(Projects recognized / Total projects) * 100",
                    "Stakeholder perception of organizational commitment": "Average perception score from commitment surveys",
                    "Improvement in environmental performance indicators": "((Current indicators - Previous) / Previous) * 100"
                }
            },

            # Area 15: Accessibility & Inclusion
            "Transport / Accessibility & Inclusion": {
                "Enhance transport accessibility for persons with disabilities": {
                    "% of vehicles and stations accessible": "(Accessible vehicles/stations / Total) * 100",
                    "Number of accessibility upgrades completed": "Total accessibility upgrades",
                    "Stakeholder satisfaction with inclusivity measures": "Average satisfaction score from inclusivity surveys",
                    "Increase in usage by disabled passengers": "((Current usage - Previous) / Previous) * 100"
                },
                "Promote equitable access for vulnerable populations": {
                    "% of underserved areas served by transport": "(Served underserved areas / Total underserved) * 100",
                    "Number of programs targeting low-income and elderly passengers": "Total targeted programs",
                    "Stakeholder perception of accessibility": "Average perception score from accessibility surveys",
                    "Increase in ridership among vulnerable groups": "((Current ridership - Previous) / Previous) * 100"
                },
                "Ensure gender-sensitive transport services": {
                    "% of routes and stations with safety features for women": "(Routes/stations with safety features / Total) * 100",
                    "Number of initiatives promoting female safety and convenience": "Total gender-safety initiatives",
                    "Stakeholder satisfaction with gender inclusivity": "Average satisfaction score from gender surveys",
                    "Reduction in complaints from female passengers": "((Previous complaints - Current) / Previous) * 100"
                },
                "Foster community participation in accessibility planning": {
                    "Number of public consultations conducted": "Total accessibility consultations",
                    "% of community feedback implemented": "(Feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with participatory approach": "Average satisfaction score from participation surveys",
                    "Number of accessibility improvements co-created with communities": "Total co-created improvements"
                },
                "Improve affordability and fare equity": {
                    "% of trips within affordable pricing ranges": "(Affordable trips / Total trips) * 100",
                    "Number of subsidy programs implemented": "Total subsidy programs",
                    "Stakeholder perception of fare fairness": "Average perception score from fare surveys",
                    "Reduction in complaints regarding pricing": "((Previous pricing complaints - Current) / Previous) * 100"
                },
                "Strengthen monitoring of inclusion outcomes": {
                    "Number of accessibility audits conducted": "Total accessibility audits",
                    "% of KPIs met in inclusion programs": "(Inclusion KPIs met / Total KPIs) * 100",
                    "Stakeholder satisfaction with monitoring": "Average satisfaction score from monitoring surveys",
                    "Improvement in accessibility indicators": "((Current indicators - Previous) / Previous) * 100"
                },
                "Enhance information accessibility": {
                    "% of transport information available in multiple formats": "(Information in multiple formats / Total information) * 100",
                    "Number of awareness campaigns on accessible transport": "Total accessibility awareness campaigns",
                    "Stakeholder satisfaction with information clarity": "Average satisfaction score from information surveys",
                    "Increase in awareness and usage by vulnerable groups": "((Current awareness - Previous) / Previous) * 100"
                },
                "Recognize achievements in accessibility and inclusion": {
                    "Number of awards or recognitions for inclusivity": "Total inclusivity awards",
                    "% of services recognized for accessibility improvements": "(Services recognized / Total services) * 100",
                    "Stakeholder perception of commitment to inclusion": "Average perception score from commitment surveys",
                    "Improvement in satisfaction levels of vulnerable groups": "((Current satisfaction - Previous) / Previous) * 100"
                }
            },

            # Area 16: Digital & Smart Mobility Integration
            "Transport / Digital & Smart Mobility Integration": {
                "Implement real-time passenger information systems": {
                    "% of passengers receiving real-time updates": "(Passengers receiving updates / Total passengers) * 100",
                    "Number of transport apps or digital platforms deployed": "Total digital platforms available",
                    "Stakeholder satisfaction with communication": "Average satisfaction score from communication surveys",
                    "Reduction in complaints due to lack of information": "((Previous information complaints - Current) / Previous) * 100"
                },
                "Promote digital ticketing and payment solutions": {
                    "% of passengers using digital ticketing": "(Digital ticket users / Total passengers) * 100",
                    "Average transaction time per digital payment": "Total transaction time / Number of digital payments",
                    "Stakeholder satisfaction with digital services": "Average satisfaction score from digital service surveys",
                    "Reduction in ticketing-related complaints": "((Previous complaints - Current) / Previous) * 100"
                },
                "Foster adoption of Mobility-as-a-Service (MaaS)": {
                    "Number of integrated transport services offered": "Total MaaS services available",
                    "% of passengers using MaaS solutions": "(MaaS users / Total passengers) * 100",
                    "Stakeholder perception of service integration": "Average perception score from integration surveys",
                    "Increase in multimodal transport usage": "((Current multimodal usage - Previous) / Previous) * 100"
                },
                "Enhance safety through technology": {
                    "Number of technology-enabled safety interventions": "Total tech safety interventions",
                    "% reduction in incidents due to digital solutions": "((Previous incidents - Current) / Previous) * 100",
                    "Stakeholder perception of safety improvements": "Average perception score from safety surveys",
                    "Reduction in response time to emergencies": "((Previous response time - Current) / Previous) * 100"
                },
                "Promote sustainable transport through digital solutions": {
                    "Number of eco-friendly transport initiatives implemented digitally": "Total digital sustainability initiatives",
                    "% reduction in emissions per passenger/km": "((Previous emissions - Current) / Previous) * 100",
                    "Stakeholder perception of environmental responsibility": "Average perception score from environmental surveys",
                    "Increase in green transport adoption via apps": "((Current adoption - Previous) / Previous) * 100"
                },
                "Encourage community engagement via digital platforms": {
                    "Number of digital consultation sessions conducted": "Total digital consultations",
                    "% of feedback incorporated into service improvements": "(Digital feedback implemented / Total feedback) * 100",
                    "Stakeholder satisfaction with engagement": "Average satisfaction score from engagement surveys",
                    "Increase in public participation rates": "((Current participation - Previous) / Previous) * 100"
                },
                "Monitor and evaluate smart mobility performance": {
                    "Number of performance reports generated": "Total smart mobility reports",
                    "% of digital KPIs achieved": "(Digital KPIs achieved / Total KPIs) * 100",
                    "Stakeholder satisfaction with reporting transparency": "Average satisfaction score from transparency surveys",
                    "Improvement in operational efficiency": "((Current efficiency - Previous) / Previous) * 100"
                },
                "Recognize achievements in smart mobility": {
                    "Number of awards or recognitions for digital innovation": "Total digital innovation awards",
                    "% of projects or teams recognized": "(Recognized entities / Total entities) * 100",
                    "Stakeholder perception of technological leadership": "Average perception score from leadership surveys",
                    "Improvement in passenger experience through technology": "((Current experience - Previous) / Previous) * 100"
                }
            },

            #transport end

            #mining start
            # Area 1: Enhance Safety & Health of Workforce
            "Mining / Safety & Health of Workforce": {
                "Reduce Workplace Accidents": {
                    "Number of reported accidents per 1,000 workers": "(Total accidents / Total workers) * 1000",
                    "% reduction in accident rates year-over-year": "((Previous accident rate - Current rate) / Previous rate) * 100",
                    "% of safety drills conducted on schedule": "(Drills conducted on schedule / Total drills) * 100",
                    "Employee satisfaction with safety programs": "Average satisfaction score from safety program surveys"
                },
                "Improve Occupational Health Coverage": {
                    "% of workforce receiving regular health check-ups": "(Workers receiving check-ups / Total workers) * 100",
                    "Reduction in occupational illness rates": "((Previous illness rate - Current rate) / Previous rate) * 100",
                    "Average time to receive medical attention for workplace incidents": "Total response time / Number of incidents",
                    "Employee satisfaction with health services": "Average satisfaction score from health service surveys"
                },
                "Strengthen PPE & Safety Equipment Compliance": {
                    "% of employees using required PPE correctly": "(Workers using PPE correctly / Total workers) * 100",
                    "Number of safety inspections conducted": "Total safety inspections performed",
                    "% reduction in safety violations": "((Previous violations - Current violations) / Previous violations) * 100",
                    "Employee satisfaction with PPE availability": "Average satisfaction score from PPE availability surveys"
                },
                "Promote Safety Awareness & Training": {
                    "Number of safety training sessions conducted": "Total safety training sessions held",
                    "% of employees trained in safety procedures": "(Workers trained / Total workers) * 100",
                    "% of trained employees implementing safety practices": "(Workers implementing practices / Total trained) * 100",
                    "Satisfaction with training effectiveness": "Average satisfaction score from training effectiveness surveys"
                }
            },

            # Area 2: Improve Environmental Responsibility
            "Mining / Environmental Responsibility": {
                "Reduce Environmental Impact": {
                    "% reduction in emissions per ton of mineral produced": "((Previous emissions - Current emissions) / Previous emissions) * 100",
                    "% reduction in water usage per ton of mineral produced": "((Previous water usage - Current usage) / Previous usage) * 100",
                    "Compliance with environmental regulations": "(Compliant operations / Total operations) * 100",
                    "Stakeholder satisfaction with environmental performance": "Average satisfaction score from environmental performance surveys"
                },
                "Improve Waste Management Practices": {
                    "% of waste recycled or safely disposed": "(Waste properly managed / Total waste) * 100",
                    "% of waste incidents reported and resolved": "(Incidents resolved / Total incidents) * 100",
                    "Number of waste management audits conducted": "Total waste management audits performed",
                    "Satisfaction with waste handling practices": "Average satisfaction score from waste management surveys"
                },
                "Minimize Land Degradation & Rehabilitation": {
                    "Area of land rehabilitated annually": "Total hectares rehabilitated per year",
                    "% of mining sites following rehabilitation plans": "(Sites following plans / Total sites) * 100",
                    "Number of community complaints about land degradation": "Total community complaints received",
                    "Stakeholder satisfaction with land restoration": "Average satisfaction score from land restoration surveys"
                },
                "Promote Environmental Awareness & Training": {
                    "Number of employees trained on environmental policies": "Total workers trained on environmental policies",
                    "% of employees applying environmentally friendly practices": "(Workers applying practices / Total workers) * 100",
                    "Reduction in environmental incidents due to human error": "((Previous incidents - Current incidents) / Previous incidents) * 100",
                    "Satisfaction with environmental training": "Average satisfaction score from environmental training surveys"
                }
            },

            # Area 3: Increase Operational Efficiency for Customer Satisfaction
            "Mining / Operational Efficiency for Customer Satisfaction": {
                "Reduce Production Delays": {
                    "% of projects completed on schedule": "(Projects on schedule / Total projects) * 100",
                    "Average downtime per equipment": "Total downtime / Number of equipment units",
                    "% reduction in production bottlenecks": "((Previous bottlenecks - Current bottlenecks) / Previous bottlenecks) * 100",
                    "Customer satisfaction with delivery timelines": "Average satisfaction score from delivery timeline surveys"
                },
                "Improve Product Quality": {
                    "% of output meeting quality standards": "(Output meeting standards / Total output) * 100",
                    "Number of product quality audits passed": "Total quality audits passed",
                    "% of defective output reduced": "((Previous defects - Current defects) / Previous defects) * 100",
                    "Customer satisfaction with product quality": "Average satisfaction score from product quality surveys"
                },
                "Optimize Resource Utilization": {
                    "% increase in ore extraction efficiency": "((Current efficiency - Previous efficiency) / Previous efficiency) * 100",
                    "% reduction in energy consumption per ton of output": "((Previous consumption - Current consumption) / Previous consumption) * 100",
                    "% reduction in material wastage": "((Previous wastage - Current wastage) / Previous wastage) * 100",
                    "Customer satisfaction with resource sustainability": "Average satisfaction score from resource sustainability surveys"
                },
                "Enhance Maintenance & Equipment Reliability": {
                    "% of equipment operating at optimal performance": "(Equipment at optimal performance / Total equipment) * 100",
                    "Average time to repair critical equipment": "Total repair time / Number of critical equipment repairs",
                    "% reduction in unplanned downtime": "((Previous downtime - Current downtime) / Previous downtime) * 100",
                    "Customer satisfaction with service reliability": "Average satisfaction score from service reliability surveys"
                }
            },

            # Area 4: Strengthen Community Engagement & Development
            "Mining / Community Engagement & Development": {
                "Increase Community Participation": {
                    "% of local community members involved in mining projects": "(Community members involved / Total community) * 100",
                    "Number of community meetings held annually": "Total community meetings conducted",
                    "% of community suggestions implemented": "(Suggestions implemented / Total suggestions) * 100",
                    "Satisfaction of communities with engagement": "Average satisfaction score from community engagement surveys"
                },
                "Promote Local Employment": {
                    "% of workforce recruited locally": "(Local workers / Total workers) * 100",
                    "Number of jobs created annually": "Total new jobs created per year",
                    "% of local workforce retention": "(Local workers retained / Total local workers) * 100",
                    "Satisfaction with employment opportunities": "Average satisfaction score from employment opportunity surveys"
                },
                "Enhance Community Development Programs": {
                    "Number of development programs implemented": "Total development programs implemented",
                    "% of programs achieving target outcomes": "(Programs achieving outcomes / Total programs) * 100",
                    "% of community members benefiting from programs": "(Community members benefiting / Total community) * 100",
                    "Satisfaction with program impact": "Average satisfaction score from program impact surveys"
                },
                "Improve Communication & Transparency": {
                    "% of stakeholders receiving timely information": "(Stakeholders receiving info / Total stakeholders) * 100",
                    "Number of grievance mechanisms operational": "Total operational grievance mechanisms",
                    "% of grievances addressed promptly": "(Grievances addressed promptly / Total grievances) * 100",
                    "Stakeholder satisfaction with communication": "Average satisfaction score from communication surveys"
                }
            },

            # Area 5: Improve Regulatory Compliance & Reputation
            "Mining / Regulatory Compliance & Reputation": {
                "Ensure Legal & Regulatory Compliance": {
                    "% of inspections passed without violations": "(Inspections passed / Total inspections) * 100",
                    "Number of regulatory fines or penalties": "Total fines or penalties incurred",
                    "% of corrective actions implemented on time": "(Actions implemented on time / Total actions) * 100",
                    "Stakeholder satisfaction with compliance": "Average satisfaction score from compliance surveys"
                },
                "Maintain Mining Licenses & Certifications": {
                    "% of licenses renewed on schedule": "(Licenses renewed on time / Total licenses) * 100",
                    "Number of certifications maintained": "Total active certifications held",
                    "% of staff trained on regulatory requirements": "(Staff trained / Total staff) * 100",
                    "Satisfaction with regulatory adherence": "Average satisfaction score from regulatory adherence surveys"
                },
                "Promote Ethical Practices": {
                    "% of employees trained in ethical mining practices": "(Employees trained / Total employees) * 100",
                    "Number of ethical violations reported": "Total ethical violations reported",
                    "% of violations resolved effectively": "(Violations resolved / Total violations) * 100",
                    "Stakeholder perception of ethical behavior": "Average perception score from ethical behavior surveys"
                },
                "Enhance Corporate Reputation": {
                    "Corporate reputation index": "Composite score from reputation assessments",
                    "Number of positive media mentions per year": "Total positive media mentions",
                    "Stakeholder survey satisfaction score": "Average satisfaction score from stakeholder surveys",
                    "% improvement in trust ratings": "((Current trust rating - Previous rating) / Previous rating) * 100"
                }
            },

            # Area 6: Strengthen Supply Chain & Logistics
            "Mining / Supply Chain & Logistics": {
                "Improve On-Time Delivery to Customers": {
                    "% of orders delivered on schedule": "(Orders delivered on time / Total orders) * 100",
                    "Average delivery lead time": "Total delivery time / Number of deliveries",
                    "% of shipment delays resolved promptly": "(Delays resolved promptly / Total delays) * 100",
                    "Customer satisfaction with delivery timeliness": "Average satisfaction score from delivery timeliness surveys"
                },
                "Enhance Supply Chain Efficiency": {
                    "% of suppliers meeting delivery targets": "(Suppliers meeting targets / Total suppliers) * 100",
                    "% reduction in logistics costs": "((Previous costs - Current costs) / Previous costs) * 100",
                    "Number of supply chain disruptions per year": "Total supply chain disruptions",
                    "Customer satisfaction with supply consistency": "Average satisfaction score from supply consistency surveys"
                },
                "Improve Transportation & Handling of Minerals": {
                    "% of minerals transported without damage": "(Minerals undamaged / Total minerals transported) * 100",
                    "Number of transport incidents reported": "Total transport incidents reported",
                    "Average time from mine to customer": "Total transit time / Number of shipments",
                    "Customer satisfaction with transport quality": "Average satisfaction score from transport quality surveys"
                },
                "Increase Traceability & Transparency in Supply Chain": {
                    "% of minerals traceable from mine to customer": "(Traceable minerals / Total minerals) * 100",
                    "Number of supply chain audits conducted": "Total supply chain audits performed",
                    "% of traceability discrepancies resolved": "(Discrepancies resolved / Total discrepancies) * 100",
                    "Customer satisfaction with transparency": "Average satisfaction score from transparency surveys"
                }
            },

            # Area 7: Strengthen Workforce Development & Competency
            "Mining / Workforce Development & Competency": {
                "Increase Employee Training & Skills": {
                    "% of employees completing annual training programs": "(Employees completing training / Total employees) * 100",
                    "Average training hours per employee": "Total training hours / Number of employees",
                    "% of trained employees applying new skills": "(Employees applying skills / Total trained) * 100",
                    "Employee satisfaction with training programs": "Average satisfaction score from training program surveys"
                },
                "Improve Leadership & Management Capacity": {
                    "% of supervisors/managers trained in leadership": "(Leaders trained / Total leaders) * 100",
                    "Number of leadership development programs conducted": "Total leadership programs conducted",
                    "% of leadership roles successfully filled internally": "(Internal promotions / Total leadership roles) * 100",
                    "Satisfaction with management support": "Average satisfaction score from management support surveys"
                },
                "Enhance Employee Retention & Engagement": {
                    "Employee turnover rate": "(Employees leaving / Total employees) * 100",
                    "% of employees participating in engagement programs": "(Employees participating / Total employees) * 100",
                    "Employee satisfaction score": "Average score from employee satisfaction surveys",
                    "Reduction in absenteeism": "((Previous absenteeism - Current absenteeism) / Previous absenteeism) * 100"
                },
                "Promote Safety & Competency Culture": {
                    "% of employees adhering to safety protocols": "(Employees adhering to protocols / Total employees) * 100",
                    "Number of competency assessments conducted": "Total competency assessments performed",
                    "% of staff demonstrating improved safety skills": "(Staff showing improvement / Total staff) * 100",
                    "Satisfaction with competency and safety initiatives": "Average satisfaction score from competency initiative surveys"
                }
            },

            # Area 8: Improve Customer Service & Relations
            "Mining / Customer Service & Relations": {
                "Enhance Customer Communication": {
                    "% of customers receiving timely updates on deliveries": "(Customers receiving updates / Total customers) * 100",
                    "Number of communication channels actively used": "Total active communication channels",
                    "% of customer inquiries resolved within target time": "(Inquiries resolved on time / Total inquiries) * 100",
                    "Customer satisfaction with communication": "Average satisfaction score from communication surveys"
                },
                "Improve Responsiveness to Customer Needs": {
                    "Average response time to customer requests": "Total response time / Number of requests",
                    "% of customer requests resolved satisfactorily": "(Requests resolved satisfactorily / Total requests) * 100",
                    "% of repeat service requests": "(Repeat requests / Total requests) * 100",
                    "Customer satisfaction with responsiveness": "Average satisfaction score from responsiveness surveys"
                },
                "Increase Customer Feedback Utilization": {
                    "% of feedback collected from customers": "(Feedback collected / Target feedback) * 100",
                    "% of feedback actions implemented": "(Feedback actions implemented / Total feedback) * 100",
                    "Average resolution time for customer complaints": "Total resolution time / Number of complaints",
                    "Satisfaction with feedback handling": "Average satisfaction score from feedback handling surveys"
                },
                "Strengthen Long-Term Customer Relationships": {
                    "% of repeat customers": "(Repeat customers / Total customers) * 100",
                    "Customer retention rate": "(Customers retained / Total customers) * 100",
                    "Customer satisfaction survey score": "Average score from customer satisfaction surveys",
                    "Number of partnership agreements renewed": "Total partnership renewals"
                }
            },

            # Area 9: Enhance Technology & Innovation
            "Mining / Technology & Innovation": {
                "Adopt Advanced Mining Technology": {
                    "% of operations using modern mining technology": "(Operations using modern tech / Total operations) * 100",
                    "Number of technology upgrades implemented annually": "Total technology upgrades implemented",
                    "% increase in operational efficiency due to technology": "((Current efficiency - Previous efficiency) / Previous efficiency) * 100",
                    "Employee satisfaction with technology adoption": "Average satisfaction score from technology adoption surveys"
                },
                "Improve Data Management & Analytics": {
                    "% of operations using data analytics for decision-making": "(Operations using analytics / Total operations) * 100",
                    "Accuracy of production and operational reports": "(Accurate reports / Total reports) * 100",
                    "% reduction in errors due to better data management": "((Previous errors - Current errors) / Previous errors) * 100",
                    "Stakeholder satisfaction with reporting accuracy": "Average satisfaction score from reporting accuracy surveys"
                },
                "Promote Innovation in Mining Processes": {
                    "Number of process improvement initiatives implemented": "Total improvement initiatives implemented",
                    "% of innovation projects achieving targets": "(Projects achieving targets / Total projects) * 100",
                    "Reduction in operational costs due to innovations": "((Previous costs - Current costs) / Previous costs) * 100",
                    "Employee satisfaction with innovation programs": "Average satisfaction score from innovation program surveys"
                },
                "Strengthen Digital Communication & Reporting": {
                    "% of communications automated digitally": "(Digital communications / Total communications) * 100",
                    "Average time to generate operational reports": "Total report generation time / Number of reports",
                    "% of reports submitted on schedule": "(Reports submitted on time / Total reports) * 100",
                    "Stakeholder satisfaction with digital reporting": "Average satisfaction score from digital reporting surveys"
                }
            },

            # Area 10: Improve Environmental Monitoring & Compliance
            "Mining / Environmental Monitoring & Compliance": {
                "Enhance Air, Water & Soil Monitoring": {
                    "Number of environmental monitoring tests conducted": "Total environmental tests performed",
                    "% of parameters within compliance limits": "(Parameters within limits / Total parameters) * 100",
                    "Reduction in pollution incidents": "((Previous incidents - Current incidents) / Previous incidents) * 100",
                    "Stakeholder satisfaction with monitoring programs": "Average satisfaction score from monitoring program surveys"
                },
                "Strengthen Waste Management Practices": {
                    "% of waste properly treated or recycled": "(Waste properly managed / Total waste) * 100",
                    "Number of non-compliance incidents related to waste": "Total waste non-compliance incidents",
                    "% of corrective actions implemented on time": "(Actions implemented on time / Total actions) * 100",
                    "Stakeholder satisfaction with waste management": "Average satisfaction score from waste management surveys"
                },
                "Improve Biodiversity & Land Rehabilitation": {
                    "Area rehabilitated per year (hectares)": "Total hectares rehabilitated annually",
                    "Number of biodiversity conservation initiatives": "Total biodiversity initiatives implemented",
                    "% of mined land restored to sustainable use": "(Land restored / Total mined land) * 100",
                    "Stakeholder satisfaction with ecological restoration": "Average satisfaction score from ecological restoration surveys"
                },
                "Promote Environmental Reporting & Transparency": {
                    "% of environmental reports submitted on schedule": "(Reports submitted on time / Total reports) * 100",
                    "Accuracy of environmental impact reports": "(Accurate reports / Total reports) * 100",
                    "% of reports accessible to stakeholders": "(Accessible reports / Total reports) * 100",
                    "Stakeholder satisfaction with transparency": "Average satisfaction score from transparency surveys"
                }
            },

            # Area 11: Increase Stakeholder & Community Trust
            "Mining / Stakeholder & Community Trust": {
                "Strengthen Community Engagement Programs": {
                    "Number of community engagement events conducted": "Total community engagement events held",
                    "% of community members participating in programs": "(Community members participating / Total community) * 100",
                    "Satisfaction of community with engagement activities": "Average satisfaction score from engagement activity surveys",
                    "Number of stakeholder complaints addressed": "Total stakeholder complaints resolved"
                },
                "Enhance Social Responsibility Initiatives": {
                    "Number of CSR projects implemented": "Total CSR projects implemented",
                    "% of CSR projects achieving intended outcomes": "(Projects achieving outcomes / Total projects) * 100",
                    "Community satisfaction with CSR programs": "Average satisfaction score from CSR program surveys",
                    "Number of partnerships with local organizations": "Total local partnerships established"
                },
                "Improve Transparency & Reporting": {
                    "% of reports shared with stakeholders": "(Reports shared / Total reports) * 100",
                    "Timeliness of reporting to regulatory bodies": "(Reports submitted on time / Total reports) * 100",
                    "% of stakeholders satisfied with transparency": "(Satisfied stakeholders / Total stakeholders) * 100",
                    "Reduction in stakeholder disputes": "((Previous disputes - Current disputes) / Previous disputes) * 100"
                },
                "Promote Trust & Reputation": {
                    "Corporate reputation index": "Composite score from reputation assessments",
                    "% increase in positive stakeholder feedback": "((Current positive feedback - Previous) / Previous) * 100",
                    "Reduction in negative media coverage": "((Previous negative coverage - Current) / Previous) * 100",
                    "Stakeholder perception score": "Average perception score from stakeholder surveys"
                }
            },

            # Area 12: Strengthen Infrastructure & Operational Facilities
            "Mining / Infrastructure & Operational Facilities": {
                "Upgrade Mining Facilities": {
                    "% of facilities meeting operational standards": "(Facilities meeting standards / Total facilities) * 100",
                    "Number of facility upgrades completed per year": "Total facility upgrades completed",
                    "% reduction in equipment downtime": "((Previous downtime - Current downtime) / Previous downtime) * 100",
                    "Staff satisfaction with facility improvements": "Average satisfaction score from facility improvement surveys"
                },
                "Improve Transport & Logistics Infrastructure": {
                    "% of transport routes maintained and operational": "(Routes operational / Total routes) * 100",
                    "Reduction in transit delays": "((Previous delays - Current delays) / Previous delays) * 100",
                    "% of minerals delivered without damage": "(Minerals undamaged / Total minerals) * 100",
                    "Customer satisfaction with logistics": "Average satisfaction score from logistics surveys"
                },
                "Expand Storage & Processing Capacity": {
                    "% increase in storage capacity": "((Current capacity - Previous capacity) / Previous capacity) * 100",
                    "% of production processed on time": "(Production processed on time / Total production) * 100",
                    "% reduction in storage losses": "((Previous losses - Current losses) / Previous losses) * 100",
                    "Stakeholder satisfaction with storage efficiency": "Average satisfaction score from storage efficiency surveys"
                },
                "Enhance ICT & Communication Infrastructure": {
                    "% of operations using functional ICT systems": "(Operations with functional ICT / Total operations) * 100",
                    "Reduction in communication downtime": "((Previous downtime - Current downtime) / Previous downtime) * 100",
                    "Timeliness of operational reporting": "(Reports submitted on time / Total reports) * 100",
                    "Employee satisfaction with ICT infrastructure": "Average satisfaction score from ICT infrastructure surveys"
                }
            },

            # Area 13: Promote Operational Sustainability
            "Mining / Operational Sustainability": {
                "Reduce Energy Consumption": {
                    "% reduction in energy use per ton of output": "((Previous energy use - Current use) / Previous use) * 100",
                    "% of energy sourced from renewable sources": "(Renewable energy / Total energy) * 100",
                    "Reduction in carbon footprint per year": "((Previous footprint - Current footprint) / Previous footprint) * 100",
                    "Stakeholder satisfaction with energy efficiency": "Average satisfaction score from energy efficiency surveys"
                },
                "Minimize Water Usage & Waste": {
                    "% reduction in water consumption": "((Previous consumption - Current consumption) / Previous consumption) * 100",
                    "% of water recycled or reused": "(Water recycled / Total water used) * 100",
                    "% of mining sites meeting water compliance standards": "(Sites meeting standards / Total sites) * 100",
                    "Stakeholder satisfaction with water management": "Average satisfaction score from water management surveys"
                },
                "Optimize Raw Material Usage": {
                    "% increase in ore extraction efficiency": "((Current efficiency - Previous efficiency) / Previous efficiency) * 100",
                    "% reduction in material wastage": "((Previous wastage - Current wastage) / Previous wastage) * 100",
                    "% of material reuse implemented": "(Material reused / Total material) * 100",
                    "Stakeholder satisfaction with material sustainability": "Average satisfaction score from material sustainability surveys"
                },
                "Promote Sustainable Mining Practices": {
                    "Number of sustainable mining initiatives implemented": "Total sustainability initiatives implemented",
                    "% compliance with sustainability standards": "(Compliant operations / Total operations) * 100",
                    "% improvement in ESG performance ratings": "((Current rating - Previous rating) / Previous rating) * 100",
                    "Stakeholder satisfaction with sustainability practices": "Average satisfaction score from sustainability practice surveys"
                }
            },

            # Area 14: Improve Customer Satisfaction with Product Delivery
            "Mining / Customer Satisfaction with Product Delivery": {
                "Ensure Timely Delivery of Minerals": {
                    "% of deliveries made on schedule": "(Deliveries on time / Total deliveries) * 100",
                    "Average lead time per delivery": "Total lead time / Number of deliveries",
                    "% of delayed shipments resolved within target time": "(Delays resolved on time / Total delays) * 100",
                    "Customer satisfaction with delivery timeliness": "Average satisfaction score from delivery timeliness surveys"
                },
                "Increase Product Quality & Reliability": {
                    "% of minerals meeting quality specifications": "(Minerals meeting specs / Total minerals) * 100",
                    "Number of product quality audits conducted": "Total quality audits performed",
                    "% of defects or rejections reduced": "((Previous defects - Current defects) / Previous defects) * 100",
                    "Customer satisfaction with product reliability": "Average satisfaction score from product reliability surveys"
                },
                "Improve Packaging & Handling": {
                    "% of minerals transported without damage": "(Minerals undamaged / Total minerals) * 100",
                    "Number of packaging-related complaints": "Total packaging complaints received",
                    "% reduction in product loss during transport": "((Previous losses - Current losses) / Previous losses) * 100",
                    "Customer satisfaction with handling quality": "Average satisfaction score from handling quality surveys"
                },
                "Strengthen Customer Support & Service": {
                    "% of customer inquiries resolved promptly": "(Inquiries resolved promptly / Total inquiries) * 100",
                    "Average response time to service requests": "Total response time / Number of service requests",
                    "% of customers satisfied with support services": "(Satisfied customers / Total customers) * 100",
                    "% of repeat orders from satisfied customers": "(Repeat orders / Total orders) * 100"
                }
            },

            # Area 15: Enhance Risk Management & Crisis Response
            "Mining / Risk Management & Crisis Response": {
                "Improve Risk Identification & Assessment": {
                    "Number of operational risks identified annually": "Total operational risks identified",
                    "% of risks assessed and categorized": "(Risks assessed / Total risks) * 100",
                    "Reduction in unanticipated operational incidents": "((Previous incidents - Current incidents) / Previous incidents) * 100",
                    "Stakeholder satisfaction with risk management": "Average satisfaction score from risk management surveys"
                },
                "Strengthen Crisis Preparedness": {
                    "Number of emergency drills conducted": "Total emergency drills performed",
                    "Average response time during incidents": "Total response time / Number of incidents",
                    "% of crisis plans updated annually": "(Plans updated / Total plans) * 100",
                    "Employee satisfaction with preparedness programs": "Average satisfaction score from preparedness program surveys"
                },
                "Minimize Financial & Operational Losses": {
                    "% reduction in losses due to operational risks": "((Previous losses - Current losses) / Previous losses) * 100",
                    "% of insurance claims settled successfully": "(Claims settled / Total claims) * 100",
                    "Number of incidents with financial mitigation implemented": "Total incidents with mitigation",
                    "Stakeholder satisfaction with risk mitigation": "Average satisfaction score from risk mitigation surveys"
                },
                "Enhance Communication During Crises": {
                    "% of stakeholders receiving timely updates": "(Stakeholders receiving updates / Total stakeholders) * 100",
                    "Reduction in misinformation during crises": "((Previous misinformation - Current) / Previous) * 100",
                    "% of crisis communications documented and evaluated": "(Communications documented / Total communications) * 100",
                    "Stakeholder satisfaction with crisis management": "Average satisfaction score from crisis management surveys"
                }
            },

            # Area 16: Strengthen Corporate Governance & Ethical Practices
            "Mining / Corporate Governance & Ethical Practices": {
                "Promote Transparency & Accountability": {
                    "% of reports shared with board and stakeholders": "(Reports shared / Total reports) * 100",
                    "Number of governance audits conducted annually": "Total governance audits performed",
                    "% of compliance with corporate governance standards": "(Compliant standards / Total standards) * 100",
                    "Stakeholder satisfaction with transparency": "Average satisfaction score from transparency surveys"
                },
                "Strengthen Ethical Standards & Practices": {
                    "% of employees trained on ethics policies": "(Employees trained / Total employees) * 100",
                    "Number of ethical violations reported": "Total ethical violations reported",
                    "% of violations resolved effectively": "(Violations resolved / Total violations) * 100",
                    "Stakeholder perception of ethical behavior": "Average perception score from ethical behavior surveys"
                },
                "Enhance Decision-Making & Oversight": {
                    "% of strategic decisions reviewed by governance board": "(Decisions reviewed / Total decisions) * 100",
                    "Number of internal audits completed": "Total internal audits completed",
                    "% of corrective actions implemented on time": "(Actions implemented on time / Total actions) * 100",
                    "Stakeholder satisfaction with governance oversight": "Average satisfaction score from governance oversight surveys"
                },
                "Increase Stakeholder Confidence & Trust": {
                    "Corporate reputation index": "Composite score from reputation assessments",
                    "% of stakeholders expressing confidence in governance": "(Stakeholders confident / Total stakeholders) * 100",
                    "Number of positive external evaluations": "Total positive external evaluations received",
                    "Stakeholder satisfaction with corporate leadership": "Average satisfaction score from corporate leadership surveys"
                }
            },


            #mining end


            "Mining / NGO & Development Focus (Customer Perspective)": {
                "Enhance Local Community Resilience": {
                    "Income diversification for mining-affected communities": "(Households with multiple income sources / Total households) * 100",
                    "Community adaptive capacity score": "Composite score of adaptive capacity metrics",
                    "Food security index improvement": "((Current food security index - Previous) / Previous) * 100",
                    "Shock recovery time reduction": "((Previous recovery time - Current) / Previous) * 100"
                },
                "Promote Community-Led Development": {
                    "Community participation in decision-making": "(Active participants / Total community) * 100",
                    "Local resource mobilization effectiveness": "(Mobilized resources / Total potential) * 100",
                    "Community project sustainability": "(Self-sustaining projects / Total projects) * 100",
                    "Traditional knowledge integration rate": "(Projects using traditional knowledge / Total projects) * 100"
                },
                "Expand Livelihood Options": {
                    "Livelihood diversification index": "Average number of livelihood activities per household",
                    "Adoption of sustainable practices": "(Households practicing sustainability / Total households) * 100",
                    "Value addition initiatives": "(Households engaged in value addition / Total households) * 100",
                    "Eco-enterprise development": "Number of successful eco-enterprises established"
                },
                "Improve Gender Equality": {
                    "Women's access to mining-related resources": "(Women with equal resource access / Total women) * 100",
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


            "Mining / NGO & Development Focus": {
                "Enhance Local Community Resilience": {
                    "Income diversification for mining-affected communities": "(Households with multiple income sources / Total households) * 100",
                    "Community adaptive capacity score": "Composite score of adaptive capacity metrics",
                    "Food security index improvement": "((Current food security index - Previous) / Previous) * 100",
                    "Shock recovery time reduction": "((Previous recovery time - Current) / Previous) * 100"
                },
                "Promote Community-Led Development": {
                    "Community participation in decision-making": "(Active participants / Total community) * 100",
                    "Local resource mobilization effectiveness": "(Mobilized resources / Total potential) * 100",
                    "Community project sustainability": "(Self-sustaining projects / Total projects) * 100",
                    "Traditional knowledge integration rate": "(Projects using traditional knowledge / Total projects) * 100"
                },
                "Strengthen Local Organizations": {
                    "Organizational capacity of local groups": "Score based on governance and management assessment",
                    "Collective resource mobilization": "Total resources mobilized per group",
                    "Savings mobilization in community groups": "Total savings mobilized per member",
                    "Leadership development completion": "(Trained leaders / Total target leaders) * 100"
                },
                "Expand Livelihood Options": {
                    "Livelihood diversification index": "Average number of livelihood activities per household",
                    "Adoption of sustainable practices": "(Households practicing sustainability / Total households) * 100",
                    "Value addition initiatives": "(Households engaged in value addition / Total households) * 100",
                    "Eco-enterprise development": "Number of successful eco-enterprises established"
                },
                "Improve Gender Equality": {
                    "Women's access to mining-related resources": "(Women with equal resource access / Total women) * 100",
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

            "Mining / Government & Policy Focus": {
                "Strengthen Regulatory Frameworks": {
                    "Policy implementation rate": "(Implemented policies / Total policies) * 100",
                    "Stakeholder consultation effectiveness": "Score based on consultation quality",
                    "Environmental compliance rate": "(Compliant operations / Total operations) * 100",
                    "Mining license compliance": "(Compliant license holders / Total license holders) * 100"
                },
                "Enhance Safety & Environmental Standards": {
                    "Occupational safety incident reduction": "((Previous incidents - Current) / Previous) * 100",
                    "Mine rehabilitation compliance": "(Rehabilitated sites / Total mined sites) * 100",
                    "Water and air quality management": "Score based on monitoring compliance",
                    "Pollution incident reduction": "((Previous incidents - Current) / Previous) * 100"
                },
                "Invest in Rural & Mining Communities": {
                    "Infrastructure accessibility index": "Composite score of community infrastructure access",
                    "Community development investment efficiency": "Output per investment dollar",
                    "Local employment rate": "(Local employees / Total workforce) * 100",
                    "Community ownership participation": "(Community-owned initiatives / Total projects) * 100"
                },
                "Promote Research & Technology Development": {
                    "Research-to-practice translation": "(Applied research findings / Total findings) * 100",
                    "Mining innovation adoption": "(Innovations adopted / Total available innovations) * 100",
                    "Innovation commercialization rate": "(Commercialized research / Total research) * 100",
                    "R&D investment impact": "Economic return on R&D investment"
                },
                "Enhance Market Regulation & Resource Governance": {
                    "Resource management compliance": "(Compliant operations / Total operations) * 100",
                    "Market transparency index": "(Transparent markets / Total markets) * 100",
                    "Quality and safety standard compliance": "(Compliant products / Total products) * 100",
                    "Consumer and stakeholder protection effectiveness": "Score based on protection mechanisms"
                }
            },

            "Mining / Private Sector & Enterprise Focus": {
                "Develop Efficient Mining Value Chains": {
                    "Value chain integration rate": "(Integrated suppliers / Total suppliers) * 100",
                    "Supply chain reliability": "(On-time deliveries / Total deliveries) * 100",
                    "Mineral quality consistency achievement": "(Consistent quality batches / Total batches) * 100",
                    "Profitability from value-added products": "Profit margin from processed minerals"
                },
                "Enhance Market-Driven Production": {
                    "Market-responsive extraction planning": "(Area mined based on demand / Total area) * 100",
                    "Demand forecasting accuracy": "(Accurate forecasts / Total forecasts) * 100",
                    "Customer satisfaction index": "Composite score of customer satisfaction metrics",
                    "Brand equity growth": "((Current brand value - Previous) / Previous) * 100"
                },
                "Optimize Technology Solutions": {
                    "Mining tech adoption ROI": "Return on technology investments",
                    "Technology scalability achievement": "(Scalable technologies / Total technologies) * 100",
                    "Digital platform engagement": "(Active users / Total registered users) * 100",
                    "Innovation pipeline strength": "Number of viable innovations in pipeline"
                },
                "Strengthen Corporate Sustainability": {
                    "Sustainable sourcing percentage": "(Sustainably sourced minerals / Total minerals) * 100",
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

            "Mining / Multi-stakeholder Collaboration": {
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
                "Develop Mining Innovation Ecosystems": {
                    "Innovation ecosystem connectivity": "(Connected stakeholders / Total potential) * 100",
                    "Research commercialization rate": "(Commercialized research / Total research) * 100",
                    "Startup success rate": "(Successful startups / Total startups) * 100",
                    "Innovation funding accessibility": "(Accessible funding / Total needed funding) * 100"
                },
                "Strengthen Industry-Community Linkages": {
                    "Contracted community mining adoption": "(Communities in contracts / Total communities) * 100",
                    "Price premium achievement": "Average price premium over market rates",
                    "Quality standard compliance": "(Compliant suppliers / Total suppliers) * 100",
                    "Information sharing effectiveness": "(Shared information used / Total shared) * 100"
                },
                "Promote Knowledge Co-creation": {
                    "Joint research initiatives": "Number of collaborative research projects",
                    "Community-scientist interaction": "(Communities interacting with scientists / Total communities) * 100",
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

            "Mining / Digital & Technology Focus": {
                "Expand Digital Mining Platforms": {
                    "Platform adoption rate": "(Active users / Total target users) * 100",
                    "User retention rate": "(Retained users / Total users) * 100",
                    "Platform usability score": "User satisfaction with platform interface",
                    "Data-driven decision adoption": "(Decisions using platform data / Total decisions) * 100"
                },
                "Implement Precision Mining Technologies": {
                    "Precision extraction coverage": "(Area under precision extraction / Total area) * 100",
                    "Equipment monitoring coverage": "(Monitored equipment / Total critical equipment) * 100",
                    "Automation level achievement": "Score based on automation implementation",
                    "Resource use efficiency": "((Previous resource use - Current) / Previous) * 100"
                },
                "Develop Mining Data Ecosystems": {
                    "Data interoperability achievement": "(Interoperable systems / Total systems) * 100",
                    "Data quality assurance": "(Quality data sets / Total data sets) * 100",
                    "Real-time monitoring coverage": "(Monitored parameters / Total parameters) * 100",
                    "Predictive analytics accuracy": "(Accurate predictions / Total predictions) * 100"
                },
                "Enhance E-Mining Services": {
                    "Digital transaction volume": "Value of digital mining transactions",
                    "Mobile service penetration": "(Stakeholders using mobile services / Total stakeholders) * 100",
                    "Digital literacy improvement": "((Current literacy - Previous) / Previous) * 100",
                    "Service accessibility score": "Score based on access across demographics"
                },
                "Strengthen Cybersecurity in Mining": {
                    "Security incident reduction": "((Previous incidents - Current) / Previous) * 100",
                    "Data protection compliance": "(Compliant systems / Total systems) * 100",
                    "Privacy assurance effectiveness": "Score based on privacy protection",
                    "Cyber resilience capacity": "Capacity to withstand cyber threats"
                },
                "Promote IoT & Smart Mining": {
                    "IoT device adoption": "(Stakeholders using IoT devices / Total stakeholders) * 100",
                    "Sensor network coverage": "(Covered area / Total area) * 100",
                    "Remote monitoring effectiveness": "(Effective remote monitoring / Total monitoring) * 100",
                    "Automated system reliability": "(Reliable automated systems / Total systems) * 100"
                }
            },

            "Mining / Climate & Sustainability Focus": {
                "Promote Climate-Smart Mining": {
                    "Climate-smart practice adoption rate": "(Mines adopting CSA techniques / Total mines) * 100",
                    "Carbon sequestration achievement": "Tons of carbon reduced or offset",
                    "Water use efficiency improvement": "((Previous water use - Current) / Previous) * 100",
                    "Climate risk management effectiveness": "Score based on risk reduction"
                },
                "Enhance Biodiversity Conservation": {
                    "Biodiversity preservation initiatives": "Number of species or habitats protected",
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
                    "Environmental impact assessment completion": "(Assessed projects / Total projects) * 100",
                    "Sustainability reporting quality": "Score based on reporting standards"
                },
                "Develop Climate Resilience Strategies": {
                    "Adaptive capacity improvement": "((Current capacity - Previous) / Previous) * 100",
                    "Climate information utilization": "(Mines using climate info / Total mines) * 100",
                    "Resilient infrastructure development": "(Resilient infrastructure / Total infrastructure) * 100",
                    "Disaster risk financing coverage": "(Covered risks / Total risks) * 100"
                },
                "Promote Sustainable Intensification": {
                    "Productivity improvement": "((Current output - Previous output) / Previous output) * 100",
                    "Input use efficiency": "Output per unit of input",
                    "Land and site rehabilitation score": "Score based on land condition maintenance",
                    "Sustainable practice integration": "(Integrated practices / Total practices) * 100"
                }
            },

            "Mining / Social Inclusion & Equity": {
                "Enhance Youth Engagement": {
                    "Youth participation rate": "(Youth in mining / Total youth) * 100",
                    "Youth entrepreneurship development": "(Youth-led enterprises / Total youth enterprises) * 100",
                    "Digital skills acquisition": "(Youth with digital skills / Total youth) * 100",
                    "Career pathway accessibility": "(Accessible pathways / Total pathways) * 100"
                },
                "Strengthen Indigenous Knowledge Systems": {
                    "Traditional knowledge documentation": "(Documented knowledge / Total systems) * 100",
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
                    "Small-scale miner inclusion rate": "(Included small-scale miners / Total miners) * 100",
                    "Gender-sensitive value chain development": "(Gender-sensitive chains / Total chains) * 100",
                    "Pro-poor business model adoption": "(Adopted pro-poor models / Total models) * 100",
                    "Inclusive market access": "(Accessible markets / Total markets) * 100"
                },
                "Enhance Social Cohesion": {
                    "Community trust index": "Score based on trust levels",
                    "Conflict resolution effectiveness": "(Resolved conflicts / Total conflicts) * 100",
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

            "Mining / Mining Development": {
                "Improve operational productivity and safety": {
                    "Production efficiency improvement": "((Current output - Previous output) / Previous output) * 100",
                    "Occupational safety improvement": "((Previous incidents - Current) / Previous) * 100",
                    "Resource utilization efficiency": "Output per unit input",
                    "Equipment utilization rate": "(Operating equipment / Total equipment) * 100"
                },
                "Enhance access to inputs and services": {
                    "Input availability rate": "(Available inputs / Total required inputs) * 100",
                    "Equipment affordability index": "((Previous cost - Current) / Previous) * 100",
                    "Advisory & technical service access": "(Clients receiving support / Total clients) * 100",
                    "Mechanization adoption rate": "(Sites using mechanized tools / Total sites) * 100"
                },
                "Promote market access and value chain development": {
                    "Market participation rate": "(Supplied to formal markets / Total output) * 100",
                    "Value-added product share": "(Processed products / Total output) * 100",
                    "Loss reduction": "((Previous losses - Current) / Previous losses) * 100",
                    "Export growth rate": "((Current export value - Previous) / Previous) * 100"
                },
                "Strengthen workforce capability and empowerment": {
                    "Worker training participation": "(Trained workers / Total workforce) * 100",
                    "Adoption of improved techniques": "(Workers applying new knowledge / Total trained) * 100",
                    "Local employment rate": "(Local employees / Total workforce) * 100",
                    "Income growth": "((Current average income - Previous) / Previous) * 100"
                },
                "Promote climate-smart and resilient mining": {
                    "Climate-smart practice adoption": "(Mines adopting CSA techniques / Total mines) * 100",
                    "Drought/water management": "(Mines implementing water efficiency / Total mines) * 100",
                    "Insurance coverage": "(Insured operations / Total operations) * 100",
                    "Climate resilience index": "((Current resilience score - Previous) / Previous) * 100"
                },
                "Improve community livelihood and social impact": {
                    "Community food security index": "((Current score - Previous) / Previous) * 100",
                    "Poverty reduction among affected communities": "((Previous poverty rate - Current) / Previous) * 100",
                    "Access to nutritious food": "(Households consuming balanced diets / Total households) * 100",
                    "Livelihood diversification rate": "(Households with multiple income sources / Total households) * 100"
                },
                "Enhance digital and innovative solutions": {
                    "Use of digital platforms": "(Clients using platforms / Total clients) * 100",
                    "Access to real-time market & operational data": "(Clients accessing data / Total clients) * 100",
                    "Innovation adoption rate": "(New technologies adopted / Total introduced) * 100",
                    "Digital transaction volume": "Total transactions executed digitally"
                }
            },


            #mining end

            #manufacturing start
            "Manufacturing / Customer Perspective": {
                "Enhance Customer Satisfaction": {
                    "Customer satisfaction index": "Composite score from customer surveys",
                    "Customer complaint resolution rate": "(Resolved complaints / Total complaints) * 100",
                    "Net promoter score (NPS)": "(Promoters - Detractors) / Total respondents * 100",
                    "Repeat purchase rate": "(Customers making repeat purchases / Total customers) * 100"
                },
                "Improve Product Quality & Reliability": {
                    "Product defect rate": "(Defective products / Total products) * 100",
                    "On-time delivery rate": "(Orders delivered on time / Total orders) * 100",
                    "Warranty claim reduction": "((Previous claims - Current claims) / Previous claims) * 100",
                    "Customer return rate": "(Returned products / Total sold products) * 100"
                },
                "Expand Market Reach & Customer Acquisition": {
                    "New customer acquisition rate": "(New customers / Total target market) * 100",
                    "Market penetration index": "Percentage of target market reached",
                    "Lead-to-order conversion rate": "(Leads converted to orders / Total leads) * 100",
                    "Channel effectiveness score": "Composite score of sales channel performance"
                },
                "Strengthen Customer Engagement & Loyalty": {
                    "Customer retention rate": "(Retained customers / Total customers) * 100",
                    "Loyalty program participation": "(Participating customers / Total customers) * 100",
                    "Customer feedback implementation rate": "(Implemented suggestions / Total suggestions) * 100",
                    "Customer engagement index": "Score based on interactions and touchpoints"
                },
                "Deliver Innovative & Value-Added Solutions": {
                    "New product adoption rate": "(Customers adopting new products / Total target customers) * 100",
                    "Customization & personalization uptake": "(Customized orders / Total orders) * 100",
                    "Value-added service utilization": "(Customers using value-added services / Total customers) * 100",
                    "Innovation satisfaction score": "Customer rating of new solutions"
                },
                "Optimize Customer Support & Responsiveness": {
                    "Average response time": "Average time to respond to customer inquiries",
                    "First contact resolution rate": "(Issues resolved at first contact / Total inquiries) * 100",
                    "Support satisfaction index": "Customer feedback score on support",
                    "Self-service adoption rate": "(Customers using self-service tools / Total customers) * 100"
                }
            },


            #manufacturing end

            #health start
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
                },
                "Improve palliative and end-of-life care": {
                    "Pain control effectiveness": "(Patients with adequate pain control / Total patients) * 100",
                    "Family satisfaction rate": "(Satisfied families / Total families surveyed) * 100",
                    "Palliative care coverage": "(Patients receiving palliative support / Total eligible) * 100",
                    "Advance care plan documentation": "(Documented plans / Total patients) * 100"
                },
                "Enhance infection disease control": {
                    "Outbreak containment rate": "(Contained outbreaks / Total outbreaks) * 100",
                    "Infection surveillance completeness": "(Reported infections / Total detected) * 100",
                    "Public health response time": "Average hours from alert to intervention",
                    "Antimicrobial resistance monitoring": "(Monitored cases / Total infections) * 100"
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
                },
                "Promote healthy aging": {
                    "Routine screening uptake among elderly": "(Screened elderly / Total elderly) * 100",
                    "Elderly vaccination coverage": "(Vaccinated elderly / Total elderly) * 100",
                    "Falls prevention participation": "(Participants / Total elderly) * 100",
                    "Nutrition and mobility adherence": "(Adherent elderly / Total elderly) * 100"
                },
                "Advance adolescent health": {
                    "School health program coverage": "(Schools with programs / Total schools) * 100",
                    "Adolescent reproductive education": "(Educated adolescents / Total adolescents) * 100",
                    "Mental wellbeing participation": "(Participants / Total adolescents) * 100",
                    "Substance prevention awareness": "(Aware adolescents / Total adolescents) * 100"
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
                },
                "Improve transportation for healthcare access": {
                    "Medical transport availability": "(Available vehicles / Total required) * 100",
                    "Patient pickup timeliness": "(On-time pickups / Total pickups) * 100",
                    "Rural patient transport coverage": "(Covered rural patients / Total rural patients) * 100",
                    "Referral transfer success": "(Successful transfers / Total transfers) * 100"
                },
                "Strengthen community outreach services": {
                    "Mobile clinic coverage": "(Covered locations / Total target locations) * 100",
                    "Community visit frequency": "Average visits per community per year",
                    "Outreach service utilization": "(Utilized services / Total outreach capacity) * 100",
                    "Community satisfaction rate": "(Satisfied participants / Total surveyed) * 100"
                }
            },
            "Health / Health Development": {
                "Improve population health and wellness": {
                    "Population health index improvement": "((Current index - Previous index) / Previous index) * 100",
                    "Healthy lifestyle adoption rate": "(Population adopting healthy practices / Total population) * 100",
                    "Community wellness participation": "(Participants in wellness programs / Total target population) * 100",
                    "Health literacy improvement": "(Individuals with improved understanding / Total participants) * 100"
                },
                "Promote preventive health behaviors": {
                    "Vaccination coverage rate": "(Vaccinated individuals / Total eligible population) * 100",
                    "Health screening participation": "(Individuals screened / Total eligible population) * 100",
                    "Preventive behavior adherence": "(People maintaining preventive behaviors / Total targeted) * 100",
                    "Risk factor reduction rate": "((Previous risk prevalence - Current risk prevalence) / Previous risk prevalence) * 100"
                },
                "Enhance access to health services": {
                    "Primary healthcare access rate": "(Population with access / Total population) * 100",
                    "Health service utilization rate": "(Individuals using health services / Total population) * 100",
                    "Geographic equity in access": "(Equitably served regions / Total regions) * 100",
                    "Affordable care availability": "(Affordable services / Total health services) * 100"
                },
                "Strengthen community-based health development": {
                    "Community health outreach coverage": "(Communities reached / Total target communities) * 100",
                    "Local health initiative participation": "(Active participants / Total community population) * 100",
                    "Behavior change communication reach": "(Individuals reached / Total target audience) * 100",
                    "Community engagement satisfaction": "(Satisfied participants / Total respondents) * 100"
                },
                "Advance adolescent and youth health awareness": {
                    "Adolescent health education coverage": "(Adolescents educated / Total adolescent population) * 100",
                    "Youth wellness program participation": "(Participating youth / Total target youth) * 100",
                    "Risk behavior reduction among youth": "((Previous rate - Current rate) / Previous rate) * 100",
                    "Mental wellbeing awareness": "(Youth aware of mental health services / Total youth) * 100"
                },
                "Promote maternal and child health development": {
                    "Antenatal care coverage": "(Pregnant women with 4+ visits / Total pregnant women) * 100",
                    "Skilled birth attendance rate": "(Deliveries by skilled personnel / Total deliveries) * 100",
                    "Child growth monitoring participation": "(Children monitored / Total under-five children) * 100",
                    "Exclusive breastfeeding rate": "(Infants exclusively breastfed / Total infants) * 100"
                },
                "Enhance elderly health and wellbeing": {
                    "Routine check-up participation": "(Elderly with annual check-ups / Total elderly) * 100",
                    "Elderly physical activity rate": "(Active elderly / Total elderly) * 100",
                    "Chronic disease self-management": "(Elderly managing conditions / Total elderly with conditions) * 100",
                    "Elderly wellness satisfaction": "(Satisfied elderly / Total elderly surveyed) * 100"
                },
                "Empower customers through digital health": {
                    "Digital health app adoption": "(Users adopting health apps / Total population) * 100",
                    "Telehealth utilization": "(Individuals using telehealth / Total eligible population) * 100",
                    "Online health education access": "(Individuals accessing digital content / Total population) * 100",
                    "Customer satisfaction with e-health": "(Satisfied users / Total users) * 100"
                },
                "Improve patient and community satisfaction": {
                    "Customer satisfaction score": "(Satisfied patients / Total respondents) * 100",
                    "Trust in healthcare services": "(Respondents expressing trust / Total respondents) * 100",
                    "Feedback response rate": "(Feedback addressed / Total received) * 100",
                    "Customer recommendation index": "(Customers likely to recommend / Total customers) * 100"
                }
            },

            # health end
        }
