from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE
from management_project.services.strategy_hierarchy.internal_process_perspective import \
    GENERIC_INTERNAL_PROCESS_PERSPECTIVE
from management_project.services.strategy_hierarchy.learning_and_growth_perspective import \
    GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE

INSURANCE_PERSPECTIVE = {
    "Financial Perspective": {

        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],

        "Insurance Revenue Growth & Diversification": {
            "Increase premium income from life insurance": {
                "Life insurance premium growth (%)": "(Current life premiums - Previous) / Previous * 100",
                "Average life premium per policy ($)": "Total life premiums / Number of life policies",
                "New life policy contribution (%)": "Revenue from new policies / Total life premiums * 100",
                "Number of life policies issued": "Total life policies issued in period"
            },
            "Increase premium income from health insurance": {
                "Health insurance premium growth (%)": "(Current health premiums - Previous) / Previous * 100",
                "Average health premium per policy ($)": "Total health premiums / Number of health policies",
                "New health policy contribution (%)": "Revenue from new policies / Total health premiums * 100",
                "Number of health policies issued": "Total health policies issued"
            },
            "Increase premium income from property and casualty insurance": {
                "Property & casualty premium growth (%)": "(Current P&C premiums - Previous) / Previous * 100",
                "Average P&C premium per policy ($)": "Total P&C premiums / Number of P&C policies",
                "New P&C policy contribution (%)": "Revenue from new policies / Total P&C premiums * 100",
                "Number of P&C policies issued": "Total P&C policies issued"
            },
            "Grow fee income from bancassurance channels": {
                "Bancassurance revenue ($)": "Revenue from bank-distributed policies",
                "Bancassurance revenue growth (%)": "(Current - Previous) / Previous * 100",
                "Number of bancassurance policies sold": "Total policies via bancassurance",
                "Fee income as % of total revenue": "Bancassurance fees / Total revenue * 100"
            },
            "Expand corporate insurance revenue": {
                "Corporate premium revenue ($)": "Total premiums from corporate policies",
                "Corporate premium growth (%)": "(Current - Previous) / Previous * 100",
                "Average premium per corporate policy ($)": "Corporate premiums / Number of corporate policies",
                "Corporate revenue share (%)": "Corporate premiums / Total premiums * 100"
            },
            "Increase digital sales revenue": {
                "Digital revenue share (%)": "Revenue from digital channels / Total revenue * 100",
                "Digital policies sold (#)": "Number of policies sold via digital channels",
                "Digital customer adoption (%)": "(Active digital users / Total customers) * 100",
                "Revenue per digital customer ($)": "Revenue from digital channels / Digital customers"
            },
            "Develop niche insurance products (e.g., microinsurance)": {
                "Niche product revenue ($)": "Revenue from niche products",
                "Number of niche policies sold (#)": "Total niche policies sold",
                "Niche product growth (%)": "(Current - Previous) / Previous * 100",
                "Niche revenue share (%)": "Revenue from niche products / Total revenue * 100"
            },
            "Capture new customer segments (youth, SMEs, rural)": {
                "Revenue from new segments ($)": "Revenue from targeted segments",
                "Customer acquisition rate (%)": "(New segment customers / Total segment population) * 100",
                "Segment policy count (#)": "Number of policies in target segments",
                "Revenue growth from segments (%)": "(Current - Previous) / Previous * 100"
            }
        },

        "Insurance Cost Efficiency & Operational Optimization": {
            "Reduce claims processing costs": {
                "Claims processing cost per policy ($)": "Total claims cost / Number of claims",
                "Average claims processing time (days)": "Total processing days / Number of claims",
                "Automation ratio (%)": "(Automated claims / Total claims) * 100",
                "Claims error rate (%)": "(Errors / Total claims) * 100"
            },
            "Reduce administrative expenses": {
                "Administrative expense ratio (%)": "Admin expenses / Total revenue * 100",
                "Admin expense growth (%)": "(Current - Previous) / Previous * 100",
                "Cost per policy issued ($)": "Admin expenses / Total policies",
                "Overhead cost ratio (%)": "Admin expenses / Operating expenses * 100"
            },
            "Optimize underwriting efficiency": {
                "Underwriting cost per policy ($)": "Total underwriting expenses / Policies underwritten",
                "Average underwriting time (hours)": "Total underwriting hours / Number of policies",
                "Underwriting accuracy (%)": "(Correctly assessed policies / Total policies) * 100",
                "Policies processed per underwriter": "Total policies / Number of underwriters"
            },
            "Streamline policy issuance processes": {
                "Average policy issuance time (hours)": "Total issuance time / Policies issued",
                "Issuance cost per policy ($)": "Total issuance expenses / Policies issued",
                "Policies issued per staff": "Total policies / Number of staff",
                "Automated issuance ratio (%)": "(Automated issuances / Total policies) * 100"
            },
            "Automate customer service workflows": {
                "Customer service automation (%)": "(Automated workflows / Total workflows) * 100",
                "Average response time (hours)": "Total response time / Number of requests",
                "Customer satisfaction (%)": "Satisfied customers / Total surveyed * 100",
                "Cost savings from automation ($)": "Previous cost - Current cost after automation"
            },
            "Automate policy management processes": {
                "Policy management automation (%)": "(Automated processes / Total processes) * 100",
                "Cost savings per policy ($)": "Savings from automation / Number of policies",
                "Error reduction rate (%)": "(Previous errors - Current errors) / Previous * 100",
                "Average processing time per policy (hours)": "Total processing time / Number of policies"
            },
            "Automate claims management processes": {
                "Claims management automation (%)": "(Automated claims / Total claims) * 100",
                "Claims processing cost savings ($)": "Previous cost - Current cost after automation",
                "Average claims resolution time (days)": "Total resolution time / Number of claims",
                "Claims error reduction (%)": "(Previous errors - Current errors) / Previous * 100"
            },
            "Improve staff productivity per policy issued": {
                "Policies issued per employee": "Total policies / Total employees",
                "Revenue per employee ($)": "Total revenue / Total employees",
                "Profit per employee ($)": "Net profit / Total employees",
                "Staff cost per policy ($)": "Total staff cost / Total policies"
            }
        },

        "Insurance Profitability & Return Optimization": {
            "Improve underwriting profitability for all product lines": {
                "Underwriting profit ($)": "Premiums - Claims - Underwriting expenses",
                "Underwriting margin (%)": "Underwriting profit / Premiums * 100",
                "Profit per product line ($)": "Profit by line of business",
                "Combined ratio (%)": "(Claims + Expenses) / Premiums * 100"
            },
            "Optimize investment income from collected premiums": {
                "Investment yield (%)": "Investment income / Average invested premiums * 100",
                "Investment income growth (%)": "(Current - Previous) / Previous * 100",
                "Net investment return ($)": "Investment income - Investment expenses",
                "Return per premium dollar ($)": "Net investment return / Total premiums collected"
            },
            "Improve combined ratio": {
                "Combined ratio (%)": "(Claims + Expenses) / Premiums * 100",
                "Loss ratio (%)": "Claims / Premiums * 100",
                "Expense ratio (%)": "Expenses / Premiums * 100",
                "Combined ratio improvement (%)": "(Previous - Current) / Previous * 100"
            },
            "Improve loss ratio": {
                "Loss ratio (%)": "Claims / Premiums * 100",
                "Loss ratio improvement (%)": "(Previous - Current) / Previous * 100",
                "Average claim per policy ($)": "Total claims / Number of policies",
                "High-loss policy count (#)": "Policies with above-average claims"
            },
            "Increase net profit margin": {
                "Net profit margin (%)": "Net income / Total revenue * 100",
                "Profit growth (%)": "(Current - Previous) / Previous * 100",
                "Profit per policy ($)": "Net profit / Total policies",
                "ROE (%)": "Net income / Shareholders equity * 100"
            },
            "Reduce operational cost-to-income ratio": {
                "Cost-to-income ratio (%)": "Operating expenses / Operating income * 100",
                "Operational cost reduction (%)": "(Previous expenses - Current) / Previous * 100",
                "Expense per policy ($)": "Operating expenses / Total policies",
                "Overhead cost ratio (%)": "Admin expenses / Total operating expenses * 100"
            },
            "Maximize return on equity (ROE)": {
                "ROE (%)": "Net income / Shareholders equity * 100",
                "Profit after tax ($)": "Net income after tax",
                "Shareholder value added (%)": "(Net profit - Cost of equity) / Shareholders' equity * 100",
                "ROE growth (%)": "(Current - Previous) / Previous * 100"
            },
            "Maximize return on assets (ROA)": {
                "ROA (%)": "Net income / Total assets * 100",
                "Income-to-assets ratio (%)": "Operating income / Total assets * 100",
                "Asset turnover ratio": "Revenue / Total assets",
                "Net profit to assets (%)": "Net profit / Total assets * 100"
            }
        },

        "Investment & Portfolio Management": {
            "Optimize overall investment portfolio yield": {
                "Portfolio yield (%)": "Investment income / Total investments * 100",
                "Investment income growth (%)": "(Current - Previous) / Previous * 100",
                "Return per investment dollar ($)": "Net investment return / Total investments",
                "Portfolio diversification index": "Weighted score of investment across asset classes"
            },
            "Diversify investments across bonds and fixed income": {
                "Bond allocation (%)": "Total bonds / Total investment portfolio * 100",
                "Fixed income yield (%)": "Interest from bonds & fixed income / Total investment * 100",
                "Portfolio risk-adjusted return (%)": "Return / Volatility measure",
                "Bond portfolio growth (%)": "(Current - Previous) / Previous * 100"
            },
            "Diversify investments across equities": {
                "Equity allocation (%)": "Total equities / Total investment portfolio * 100",
                "Equity portfolio return (%)": "Equity gains / Total equities * 100",
                "Equity risk-adjusted return (%)": "Equity return / Equity volatility * 100",
                "Equity portfolio growth (%)": "(Current - Previous) / Previous * 100"
            },
            "Diversify alternative investments (real estate, private equity)": {
                "Alternative investment allocation (%)": "Total alternative investments / Total portfolio * 100",
                "Alternative investment yield (%)": "Income from alternatives / Total alternatives * 100",
                "Portfolio risk-adjusted return (%)": "Return / Volatility measure",
                "Growth in alternative assets (%)": "(Current - Previous) / Previous * 100"
            },
            "Strengthen liquidity management": {
                "Liquid assets to total assets (%)": "Liquid assets / Total assets * 100",
                "Cash conversion from premiums (%)": "Cash collected / Premiums billed * 100",
                "Liquidity buffer coverage (%)": "Available liquid assets / Required liquidity * 100",
                "Short-term investment ratio (%)": "Short-term investments / Total investments * 100"
            },
            "Improve asset-liability matching (ALM)": {
                "ALM gap (days)": "Weighted average asset maturity - liability maturity",
                "Repricing gap (%)": "Rate-sensitive assets - Rate-sensitive liabilities / Total assets * 100",
                "Maturity mismatch ratio (%)": "Assets maturing within 1 year / Liabilities due within 1 year * 100",
                "ALM compliance rate (%)": "ALM strategy adherence / Total requirements * 100"
            },
            "Minimize investment losses using risk-adjusted strategies": {
                "Risk-adjusted return (%)": "Portfolio return / Portfolio risk",
                "Value at Risk (VaR $)": "Maximum expected loss over period at confidence level",
                "Investment loss ratio (%)": "Losses / Total investments * 100",
                "Portfolio loss events (#)": "Number of negative investment events"
            },
            "Increase ESG-compliant investment share": {
                "ESG investment ratio (%)": "ESG-compliant assets / Total portfolio * 100",
                "Green bonds purchased ($)": "Total green bonds bought",
                "Sustainable yield (%)": "Return from ESG assets / ESG assets * 100",
                "ESG compliance score": "Internal ESG compliance rating index"
            }
        },

        "Insurance Risk Management & Solvency": {
            "Maintain regulatory solvency ratio": {
                "Solvency ratio (%)": "Available capital / Required capital * 100",
                "Regulatory compliance rate (%)": "Compliant measures / Total requirements * 100",
                "Solvency trend (%)": "(Current - Previous) / Previous * 100",
                "Capital adequacy coverage (%)": "Available capital / Minimum regulatory capital * 100"
            },
            "Maintain capital adequacy ratio (CAR)": {
                "CAR (%)": "Total capital / Risk-weighted assets * 100",
                "Tier 1 capital ratio (%)": "Tier 1 capital / Risk-weighted assets * 100",
                "Tier 2 capital ratio (%)": "Tier 2 capital / Risk-weighted assets * 100",
                "CAR buffer above minimum (%)": "(CAR - Minimum requirement) / Minimum requirement * 100"
            },
            "Accurately manage claims reserves": {
                "Claims reserve adequacy (%)": "Reserves / Expected claims * 100",
                "Reserve growth rate (%)": "(Current - Previous) / Previous * 100",
                "Reserve error rate (%)": "(Under/over reserved policies / Total policies) * 100",
                "Claims reserve utilization (%)": "Claims paid / Claims reserves * 100"
            },
            "Accurately manage policy provisioning": {
                "Policy provisioning ratio (%)": "Provisioned amount / Required provision * 100",
                "Provision adequacy (%)": "Provisioned policies / Total policies needing provision * 100",
                "Provision error rate (%)": "(Incorrectly provisioned policies / Total policies) * 100",
                "Provision growth rate (%)": "(Current - Previous) / Previous * 100"
            },
            "Reduce exposure to high-risk policies": {
                "High-risk policy ratio (%)": "High-risk policies / Total policies * 100",
                "Premium concentration ratio (%)": "Top 10 policies / Total premiums * 100",
                "Risk-adjusted revenue ($)": "Revenue weighted by policy risk",
                "Policy default probability (%)": "Expected default policies / Total policies * 100"
            },
            "Strengthen reinsurance coverage": {
                "Reinsurance coverage ratio (%)": "Reinsured policies / Total policies * 100",
                "Claims ceded to reinsurer ($)": "Claims paid via reinsurance",
                "Reinsurance cost ratio (%)": "Reinsurance premiums / Total premiums * 100",
                "Reinsurance risk transfer (%)": "Claims exposure transferred / Total claims exposure * 100"
            },
            "Implement predictive models for claim spikes": {
                "Predictive model accuracy (%)": "(Correctly predicted claims / Total predictions) * 100",
                "Claims spike detection rate (%)": "(Detected spikes / Total spikes) * 100",
                "Response time to spikes (hours)": "Average time to mitigate spike",
                "False positive rate (%)": "(False alerts / Total alerts) * 100"
            },
            "Reduce portfolio concentration risk": {
                "Portfolio concentration ratio (%)": "(Top 10 policies / Total policies) * 100",
                "Sectoral exposure ratio (%)": "Exposure to single sector / Total portfolio * 100",
                "Geographical concentration (%)": "Revenue from top region / Total revenue * 100",
                "Diversification index": "Weighted diversification score across policies"
            }
        },

        "Insurance Liquidity & Cash Flow Management": {
            "Maintain liquidity for timely claim settlements": {
                "Liquidity coverage ratio (LCR %)": "Liquid assets / Net cash outflows over 30 days * 100",
                "Cash available for claims ($)": "Total liquid cash for immediate claims",
                "Claims settlement timeliness (%)": "Claims paid on-time / Total claims * 100",
                "Liquidity gap (%)": "(Cash available - Required cash) / Required cash * 100"
            },
            "Improve premium collection efficiency": {
                "Collection ratio (%)": "Premiums collected / Premiums due * 100",
                "Average collection time (days)": "Total days to collect / Number of policies",
                "Past due premium ratio (%)": "Past due premiums / Total premiums * 100",
                "Collection growth rate (%)": "(Current - Previous) / Previous * 100"
            },
            "Forecast cash flow for operational needs": {
                "Cash flow forecast accuracy (%)": "(Actual cash - Forecast) / Forecast * 100",
                "Operating cash balance ($)": "Cash available for operations",
                "Cash flow variance ($)": "Actual cash inflows - Forecasted inflows",
                "Forecast coverage ratio (%)": "Forecasted cash / Total operating requirements * 100"
            },
            "Balance short-term and long-term liabilities": {
                "Short-term liability coverage (%)": "Current assets / Short-term liabilities * 100",
                "Long-term debt ratio (%)": "Long-term debt / Total assets * 100",
                "Debt-to-equity ratio": "Total liabilities / Equity",
                "Liability maturity matching (%)": "Aligned assets to liabilities / Total liabilities * 100"
            },
            "Maintain contingency funds for unexpected claims": {
                "Contingency fund ratio (%)": "Contingency fund / Total expected claims * 100",
                "Contingency fund growth (%)": "(Current - Previous) / Previous * 100",
                "Contingency fund utilization (%)": "Used funds / Total contingency * 100",
                "Contingency coverage ratio (%)": "Available contingency / Required contingency * 100"
            },
            "Reduce idle cash and excess reserves": {
                "Idle cash ratio (%)": "Idle cash / Total cash * 100",
                "Excess reserve ratio (%)": "Excess reserves / Required reserves * 100",
                "Cash optimization ($)": "Amount released from idle/excess cash",
                "Reserve utilization efficiency (%)": "Reserves used / Total reserves * 100"
            },
            "Improve cash conversion from premiums": {
                "Cash conversion cycle (days)": "Days from premium billed to cash received",
                "Cash conversion efficiency (%)": "Actual cash collected / Potential cash * 100",
                "Average receivable days": "Total days of accounts receivable / Number of policies",
                "Premium-to-cash ratio (%)": "Cash received / Premiums billed * 100"
            },
            "Strengthen regulatory liquidity buffers": {
                "Regulatory liquidity ratio (%)": "Required buffer / Total liquid assets * 100",
                "Buffer compliance rate (%)": "Compliant periods / Total periods * 100",
                "Liquidity buffer growth (%)": "(Current - Previous) / Previous * 100",
                "Buffer adequacy (%)": "Available buffer / Required buffer * 100"
            }
        },

        "Insurance Resource Utilization": {

            "Enhance Staff Productivity": {
                "Policies issued per employee (#)": "Total policies issued / Total staff",
                "Revenue per employee ($)": "Total insurance revenue / Total staff",
                "Claims processed per employee (#)": "Total claims handled / Total staff",
                "Customer service efficiency (%)": "(Policies or claims processed without escalation / Total processed) * 100"
            },

            "Optimize Branch & Agent Network": {
                "Revenue per branch/agency ($)": "Total revenue / Number of branches or agencies",
                "Profit per branch/agency ($)": "Net profit / Number of branches or agencies",
                "Policies sold per branch/agency (#)": "Total policies sold / Number of branches or agencies",
                "Customer per branch/agency (#)": "Active customers / Number of branches or agencies"
            },

            "Improve Claims & Policy Management Efficiency": {
                "Average claims processing time (days)": "Total processing days / Number of claims",
                "Average policy issuance time (days)": "Total time for policy issuance / Number of policies",
                "Claims error rate (%)": "(Incorrectly processed claims / Total claims) * 100",
                "Policy amendment error rate (%)": "(Errors in policy updates / Total policy updates) * 100"
            },

            "Enhance Digital Channel Efficiency": {
                "Digital policy sales ratio (%)": "(Digital policies / Total policies) * 100",
                "Online claims submission ratio (%)": "(Claims submitted online / Total claims) * 100",
                "Cost per digital transaction ($)": "Digital channel operating cost / Number of digital transactions",
                "Mobile & online adoption rate (%)": "(Active digital users / Total customers) * 100"
            },

            "Optimize IT & Technology Resources": {
                "IT cost per transaction ($)": "Total IT operating cost / Total transactions or policies",
                "System uptime (%)": "(System availability time / Total scheduled time) * 100",
                "Automation ratio (%)": "(Automated transactions / Total transactions) * 100",
                "Tech ROI (%)": "(Revenue or savings from IT initiatives / IT investment) * 100"
            },

            "Optimize Physical & Facility Resources": {
                "Energy cost per branch/agency ($)": "Total energy expense / Number of branches or agencies",
                "Facility utilization rate (%)": "(Used branch/office space / Total available space) * 100",
                "Paper usage per policy (#)": "Total paper used / Number of policies processed",
                "Maintenance cost per branch/agency ($)": "Facility maintenance expense / Number of branches or agencies"
            },

            "Improve Capital & Fund Utilization": {
                "Return on Assets (ROA %)": "(Net income / Total assets) * 100",
                "Return on Equity (ROE %)": "(Net income / Shareholders' equity) * 100",
                "Liquidity coverage ratio (LCR %)": "(High-quality liquid assets / Net cash outflows over 30 days) * 100",
                "Fund deployment efficiency (%)": "(Funds invested or deployed / Total available funds) * 100"
            }
        },
    },

    "Customer Perspective": {

        **GENERIC_CUSTOMER_PERSPECTIVE["Customer Perspective"],

        # ---------------- Policyholder Acquisition & Market Reach ----------------
        "Policyholder Acquisition & Market Reach": {
            "Target underserved populations": {
                "Insurance penetration in underserved areas (%)": "Number of insured individuals in underserved areas / Total population in those areas * 100",
                "New policyholders from underserved regions (#)": "Number of new policies sold in underserved regions",
                "Premium revenue from new segments ($)": "Total premiums collected from newly targeted segments",
                "Awareness of insurance products (%)": "Population aware of insurance offerings / Total target population * 100"
            },
            "Increase qualified lead generation": {
                "Number of qualified leads per month": "Count of leads meeting qualification criteria per month",
                "Lead generation cost per channel": "Total marketing spend per channel / Number of leads generated per channel",
                "Lead-to-policy conversion rate (%)": "(Leads converted to policyholders / Total leads) * 100",
                "Marketing qualified lead volume growth (%)": "((Current MQL volume - Previous MQL volume) / Previous MQL volume) * 100"
            },
            "Expand digital acquisition channels": {
                "Online policy purchase rate (%)": "Number of policies purchased online / Total policies sold * 100",
                "Digital marketing ROI (%)": "((Revenue from digital campaigns - Campaign cost) / Campaign cost) * 100",
                "Website conversion rate (%)": "(Policies purchased online / Total website visitors) * 100",
                "Click-through rate improvement (%)": "((Current CTR - Previous CTR) / Previous CTR) * 100"
            }
        },

        # ---------------- Policyholder Satisfaction & Experience ----------------
        "Policyholder Satisfaction & Experience": {
            "Enhance claims handling": {
                "Average claims processing time (days)": "Average days from claim submission to settlement",
                "Claims resolution rate (%)": "Claims settled successfully / Total claims * 100",
                "Customer satisfaction with claims (%)": "Surveyed satisfaction among policyholders who filed claims",
                "Complaint escalation reduction (%)": "((Previous escalations - Current escalations) / Previous escalations) * 100"
            },
            "Improve digital insurance services": {
                "Mobile app adoption rate (%)": "Users actively using the insurance mobile app / Total policyholders * 100",
                "Digital claims submission success (%)": "Successful online claims / Total digital claims submitted * 100",
                "Self-service adoption rate (%)": "Number of policyholders using self-service channels / Total policyholders * 100",
                "Digital experience satisfaction (%)": "Surveyed satisfaction with digital platforms"
            },
            "Streamline policy onboarding": {
                "Onboarding completion rate (%)": "New policyholders completing onboarding / Total new policyholders * 100",
                "Time to first coverage (days)": "Average time from purchase to policy activation",
                "New policyholder satisfaction score (%)": "Surveyed satisfaction of newly onboarded customers",
                "Onboarding cost per policyholder ($)": "Total onboarding cost / Number of onboarded policyholders"
            },
            "Enhance customer communication": {
                "Communication open rate (%)": "(Emails/messages opened / Total sent) * 100",
                "Response rate to inquiries (%)": "(Responses delivered / Total inquiries) * 100",
                "Customer engagement score": "Composite score based on interactions with policyholders",
                "Timeliness of communication (%)": "Queries responded within target time / Total queries * 100"
            }
        },

        # ---------------- Policyholder Loyalty & Retention ----------------
        "Policyholder Loyalty & Retention": {
            "Reduce policy lapse/churn": {
                "Policy lapse rate (%)": "Lapsed policies / Total active policies * 100",
                "Renewal rate (%)": "Renewed policies / Policies due for renewal * 100",
                "Retention by product type (%)": "Retained policyholders per product / Total policyholders per product * 100",
                "Customer lifetime value (CLV) growth ($)": "Current CLV - Previous CLV"
            },
            "Enhance loyalty programs": {
                "Reward program participation (%)": "Enrolled policyholders / Total eligible policyholders * 100",
                "Referral rate (%)": "New policies via referrals / Total policies * 100",
                "Retention uplift from loyalty program (%)": "((Retention of participants - Retention of non-participants) / Retention of non-participants) * 100",
                "Cross-product adoption (%)": "Policyholders holding multiple insurance products / Total policyholders * 100"
            },
            "Strengthen engagement & communication": {
                "Active policyholder engagement rate (%)": "Engaged policyholders / Total policyholders * 100",
                "Personalized communication adoption (%)": "Policyholders receiving personalized offers / Total policyholders * 100",
                "Interaction frequency increase (%)": "((Current interactions - Previous interactions) / Previous interactions) * 100",
                "Customer satisfaction with engagement (%)": "Surveyed satisfaction with engagement efforts"
            }
        },

        # ---------------- Policyholder Value & Relationship Management ----------------
        "Policyholder Value & Relationship Management": {
            "Increase cross-selling / up-selling": {
                "Uptake rate of complementary products (%)": "New products purchased by existing policyholders / Total eligible policyholders * 100",
                "Revenue per policyholder ($)": "Total revenue from policyholder / Total policyholders",
                "Account penetration depth (# of products per customer)": "Average number of products held per policyholder",
                "Upsell conversion rate (%)": "(Successful upsell conversions / Eligible policyholders) * 100"
            },
            "Strengthen broker/agent relationships": {
                "Broker satisfaction score (%)": "Surveyed satisfaction of brokers/agents",
                "Number of active brokers (#)": "Total brokers actively selling policies",
                "Premium contribution per broker ($)": "Total premiums sold per broker",
                "Retention of distribution partners (%)": "(Partners retained / Total partners) * 100"
            },
            "Develop policyholder success programs": {
                "Program completion rate (%)": "Completed initiatives / Total programs initiated * 100",
                "Adoption rate of recommended actions (%)": "Policyholders applying program recommendations / Total participants * 100",
                "Policyholder satisfaction with programs (%)": "Surveyed satisfaction of participants",
                "Business outcomes achieved (%)": "Defined KPIs or outcomes met / Total outcomes planned * 100"
            }
        },

        # ---------------- Policyholder Insights & Analytics ----------------
        "Policyholder Insights & Analytics": {
            "Enhance data collection for underwriting": {
                "Complete policyholder profiles (%)": "Profiles with all required data fields / Total profiles * 100",
                "Risk profiling accuracy (%)": "(Correct risk predictions / Total assessments) * 100",
                "Real-time claims insights availability (%)": "Insights available in real-time / Total required insights * 100",
                "Customer feedback utilization rate (%)": "Implemented suggestions / Total suggestions collected * 100"
            },
            "Leverage behavioral analytics": {
                "Predictive claim risk accuracy (%)": "(Correct predictions / Total predictions) * 100",
                "Personalized policy offer acceptance (%)": "Accepted personalized offers / Total offers * 100",
                "Engagement via personalized communication (%)": "Policyholders responding to personalized outreach / Total contacted * 100",
                "Analytics-driven policy adjustments (%)": "Policies updated based on analytics recommendations / Total applicable policies * 100"
            },
            "Enhance journey analytics": {
                "Journey mapping completeness (%)": "Mapped policyholder journey stages / Total stages * 100",
                "Drop-off point identification (%)": "Identified drop-offs / Total possible drop-offs * 100",
                "Improvement in experience metrics (%)": "Change in key journey KPIs after optimization",
                "Cross-channel visibility (%)": "Interactions visible across channels / Total interactions * 100"
            }
        },

        # ---------------- Community & Social Impact ----------------
        "Community & Social Impact": {
            "Promote financial literacy & inclusion": {
                "Participants in literacy programs (#)": "Number of participants in insurance or financial literacy programs",
                "Awareness of insurance products (%)": "Population aware of insurance offerings",
                "Policy adoption from literacy programs (%)": "New policies purchased by participants / Total participants * 100",
                "Community satisfaction with initiatives (%)": "Survey-based satisfaction with literacy efforts"
            },
            "CSR & disaster mitigation": {
                "Community projects supported (#)": "Number of CSR initiatives conducted",
                "Relief provided during disasters ($)": "Financial or in-kind support delivered",
                "Beneficiaries of CSR programs (#)": "Number of community members benefiting",
                "Community trust index (%)": "Survey-based trust in organization/community support"
            }
        },

        # ---------------- Regulatory & Stakeholder Engagement ----------------
        "Regulatory & Stakeholder Engagement": {
            "Ensure compliance & transparency": {
                "Regulatory reporting accuracy (%)": "Correctly submitted reports / Total required reports * 100",
                "Compliance audit pass rate (%)": "Successful audits / Total audits conducted * 100",
                "Policyholder grievance resolution (%)": "Resolved grievances / Total received * 100",
                "Stakeholder satisfaction with compliance (%)": "Survey-based satisfaction score"
            },
            "Strengthen stakeholder relationships": {
                "Number of active stakeholders (#)": "Stakeholders engaged in insurance initiatives",
                "Stakeholder engagement rate (%)": "Engaged stakeholders / Total stakeholders * 100",
                "Satisfaction with engagement (%)": "Survey-based satisfaction of stakeholders",
                "Net Promoter Score (NPS) for stakeholders": "Likelihood of stakeholders to recommend the organization"
            }
        }
    },

    "Internal_Process_Perspective": {

        **GENERIC_INTERNAL_PROCESS_PERSPECTIVE["Internal Process Perspective"],

        # -------------------- Actuarial (Pricing & Risk Analysis) --------------------

        "Pricing Accuracy & Risk Modeling": {
            "Ensure premium adequacy": {
                "Premium adequacy (%)": "(Calculated premium / Required premium) * 100",
                "Rate review frequency (times/year)": "Number of reviews conducted",
                "Deviation from target (%)": "(Target - Actual) / Target * 100",
                "Pricing exception rate (%)": "(Exceptions / Total cases) * 100"
            },
            "Improve predictive model accuracy": {
                "Model prediction accuracy (%)": "(Correct predictions / Total cases) * 100",
                "Back-testing coverage (%)": "(Tested / Total models) * 100",
                "Model error rate (%)": "(Errors / Total predictions) * 100",
                "Scenario testing completion (%)": "(Completed / Planned scenarios) * 100"
            },
            "Enhance portfolio risk diversification": {
                "Diversified risk ratio (%)": "(Diversified risks / Total portfolio) * 100",
                "Sector exposure compliance (%)": "(Compliant exposures / Total sectors) * 100",
                "Concentration risk index": "Weighted exposure across sectors",
                "Risk-adjusted exposure ratio (%)": "(Adjusted / Total portfolio) * 100"
            },
            "Strengthen reserve adequacy": {
                "Reserve coverage (%)": "(Adequate reserves / Required reserves) * 100",
                "Reserve review cycle (days)": "Average days to review reserves",
                "Reserve estimation error (%)": "(Estimated - Actual) / Actual * 100",
                "Compliance with regulatory reserve standards (%)": "(Compliant / Total reserves) * 100"
            },
            "Improve data quality & completeness": {
                "Data completeness (%)": "(Complete datasets / Total datasets) * 100",
                "Data validation error rate (%)": "(Invalid records / Total records) * 100",
                "Data timeliness (%)": "(Updated on time / Total datasets) * 100",
                "Data processing turnaround (days)": "Average processing time"
            },
            "Enhance risk monitoring & reporting": {
                "Risk report coverage (%)": "(Reports generated / Total required) * 100",
                "Report accuracy (%)": "(Accurate reports / Total reports) * 100",
                "Timeliness of reporting (%)": "(Reports on time / Total reports) * 100",
                "Stakeholder feedback score": "Survey rating"
            }
        },

        # --------------------Underwriting (Risk Selection & Approval) --------------------
        "Underwriting (Risk Selection & Approval)": {
            "Standardize risk assessment process": {
                "Assessment process adherence (%)": "(Compliant assessments / Total) * 100",
                "Average assessment time (days)": "Average days per assessment",
                "Assessment error rate (%)": "(Errors / Total assessments) * 100",
                "Review completion rate (%)": "(Completed reviews / Total reviews) * 100"
            },
            "Enhance policy approval accuracy": {
                "Approval accuracy (%)": "(Correct approvals / Total approvals) * 100",
                "Rework rate (%)": "(Re-assessments / Total policies) * 100",
                "Compliance with underwriting guidelines (%)": "(Compliant / Total approvals) * 100",
                "Underwriting exception rate (%)": "(Exceptions / Total policies) * 100"
            },
            "Reduce underwriting cycle time": {
                "Average approval turnaround (days)": "Average days from submission to approval",
                "Policy backlog reduction (%)": "(Previous backlog - Current) / Previous * 100",
                "Time-to-first-decision (days)": "Average days to initial decision",
                "Process bottleneck incidents (#)": "Number of bottlenecks identified"
            },
            "Strengthen risk classification & scoring": {
                "Risk classification accuracy (%)": "(Correct classifications / Total policies) * 100",
                "Scoring model compliance (%)": "(Compliant / Total models) * 100",
                "High-risk detection rate (%)": "(High-risk identified / Total high-risk cases) * 100",
                "Risk reassessment frequency (times/year)": "Number of reassessments"
            },
            "Improve document & data management": {
                "Document completeness (%)": "(Complete files / Total files) * 100",
                "Data entry accuracy (%)": "(Accurate entries / Total entries) * 100",
                "Document retrieval time (minutes)": "Average minutes to retrieve",
                "Digital records adoption (%)": "(Digital records / Total policies) * 100"
            },
            "Monitor underwriting compliance & audit": {
                "Internal audit coverage (%)": "(Audited policies / Total policies) * 100",
                "Audit finding closure rate (%)": "(Closed findings / Total findings) * 100",
                "Regulatory compliance (%)": "(Compliant policies / Total policies) * 100",
                "Exception reporting timeliness (%)": "(Reported on time / Total exceptions) * 100"
            },
        },

        # -------------------- Sales & Distribution (Selling Policies) --------------------
        "Sales & Distribution (Selling Policies)": {
            "Streamline policy issuance process": {
                "Policy issuance time (days)": "Average days from application to issuance",
                "Process compliance (%)": "(Compliant processes / Total sales) * 100",
                "Error rate (%)": "(Incorrect issuances / Total policies) * 100",
                "Digital sales adoption (%)": "(Digital channels used / Total sales) * 100"
            },
            "Enhance agent performance management": {
                "Agent compliance rate (%)": "(Compliant agents / Total agents) * 100",
                "Training completion (%)": "(Trained / Total agents) * 100",
                "Sales process adherence (%)": "(Adhered / Total sales) * 100",
                "Client feedback score": "Survey rating"
            },
            "Improve customer onboarding experience": {
                "Onboarding completion time (days)": "Average days per new client",
                "Customer satisfaction score": "Survey rating",
                "Documentation error rate (%)": "(Errors / Total new policies) * 100",
                "Digital onboarding adoption (%)": "(Digital onboarding / Total new policies) * 100"
            },
            "Monitor sales compliance & ethics": {
                "Regulatory compliance (%)": "(Compliant sales / Total sales) * 100",
                "Sales audit coverage (%)": "(Audited / Total sales) * 100",
                "Ethical violation incidents (#)": "Number of violations",
                "Remediation closure rate (%)": "(Closed / Total violations) * 100"
            },
            "Enhance channel management & coverage": {
                "Channel utilization (%)": "(Active channels / Total channels) * 100",
                "Policy distribution coverage (%)": "(Covered regions / Total regions) * 100",
                "Channel performance index": "Weighted performance score",
                "Inactive channel reduction (%)": "(Previous - Current) / Previous * 100"
            },
            "Improve lead management & conversion": {
                "Lead response time (hours)": "Average hours to respond",
                "Lead conversion rate (%)": "(Converted / Total leads) * 100",
                "Lead qualification accuracy (%)": "(Correctly qualified / Total leads) * 100",
                "Follow-up completion rate (%)": "(Completed follow-ups / Total leads) * 100"
            },
        },

        # -------------------- Policyholder Services (Customer Service & Policy Management) --------------------
        "Policyholder Services": {
            "Ensure timely policy updates": {
                "Update cycle time (days)": "Average days to update policies",
                "Process compliance (%)": "(Compliant updates / Total updates) * 100",
                "Error rate (%)": "(Incorrect updates / Total updates) * 100",
                "Customer satisfaction score": "Survey rating"
            },
            "Improve policyholder data management": {
                "Data accuracy (%)": "(Accurate records / Total records) * 100",
                "Data completeness (%)": "(Complete records / Total records) * 100",
                "Data timeliness (%)": "(Updated on time / Total records) * 100",
                "Data access speed (seconds)": "Average retrieval time"
            },
            "Enhance customer inquiry handling": {
                "Inquiry response time (hours)": "Average time to respond",
                "Inquiry resolution rate (%)": "(Resolved / Total inquiries) * 100",
                "Escalation rate (%)": "(Escalated / Total inquiries) * 100",
                "Customer satisfaction score": "Survey rating"
            },
            "Streamline policy renewal process": {
                "Renewal processing time (days)": "Average days",
                "Renewal completion rate (%)": "(Completed / Total due) * 100",
                "Policy lapse rate (%)": "(Lapsed / Total policies) * 100",
                "Process compliance (%)": "(Compliant renewals / Total renewals) * 100"
            },
            "Monitor service compliance & quality": {
                "Regulatory compliance (%)": "(Compliant processes / Total processes) * 100",
                "Internal audit coverage (%)": "(Audited / Total processes) * 100",
                "Customer complaints rate (%)": "(Complaints / Total clients) * 100",
                "Complaint resolution timeliness (%)": "(Resolved on time / Total complaints) * 100"
            },
            "Enhance self-service & digital adoption": {
                "Digital platform usage (%)": "(Active users / Total clients) * 100",
                "Self-service completion rate (%)": "(Completed / Total attempts) * 100",
                "Customer satisfaction score": "Survey rating",
                "Error rate (%)": "(Errors / Total digital interactions) * 100"
            },
        },

        # -------------------- Claims (Handling and Paying Claims) --------------------

        "Claims Processing Efficiency": {
            "Reduce claim processing time": {
                "Average claim processing time (days)": "Average days per claim",
                "Process compliance (%)": "(Compliant claims / Total claims) * 100",
                "Error rate (%)": "(Incorrect claims / Total claims) * 100",
                "Claims backlog reduction (%)": "(Previous - Current) / Previous * 100"
            },
            "Improve claim assessment accuracy": {
                "Assessment accuracy (%)": "(Correct assessments / Total claims) * 100",
                "Reassessment rate (%)": "(Reassessed / Total claims) * 100",
                "Fraud detection rate (%)": "(Detected fraud / Total claims) * 100",
                "High-risk claim identification (%)": "(High-risk identified / Total claims) * 100"
            },
            "Enhance customer communication & transparency": {
                "Customer satisfaction score": "Survey rating",
                "Inquiry response time (hours)": "Average time",
                "Claim status update frequency (#)": "Number of updates per claim",
                "Escalation handling time (days)": "Average days to resolve escalations"
            },
            "Monitor compliance & audit in claims": {
                "Regulatory compliance (%)": "(Compliant claims / Total claims) * 100",
                "Audit coverage (%)": "(Audited claims / Total claims) * 100",
                "Internal policy adherence (%)": "(Compliant / Total claims) * 100",
                "Exception reporting timeliness (%)": "(Reported on time / Total exceptions) * 100"
            },
            "Optimize resource allocation in claims": {
                "Staff productivity": "Claims processed per staff",
                "Resource utilization (%)": "(Used resources / Total allocated) * 100",
                "Process automation adoption (%)": "(Automated processes / Total processes) * 100",
                "Cost-efficiency index": "Internal measure of operational efficiency"
            },
            "Strengthen fraud prevention & detection": {
                "Fraud detection effectiveness (%)": "(Detected / Total attempts) * 100",
                "Suspicious claim reporting timeliness (%)": "(Reported on time / Total detected)",
                "Investigations closed (%)": "(Closed / Total investigations) * 100",
                "Claims rework due to fraud (%)": "(Reworked / Total claims) * 100"
            }
        },

        # -------------------- Finance & Investments (Managing Money & Investments) --------------------

        "Investment & Fund Management": {
            "Ensure regulatory compliance in investments": {
                "Compliance coverage (%)": "(Compliant portfolios / Total portfolios) * 100",
                "Audit coverage (%)": "(Audited / Total portfolios) * 100",
                "Reporting timeliness (%)": "(Submitted on time / Total reports) * 100",
                "Exception resolution rate (%)": "(Resolved / Total exceptions) * 100"
            },
            "Monitor portfolio risk & diversification": {
                "Portfolio diversification index": "Weighted diversification score",
                "Risk-adjusted exposure (%)": "(Adjusted exposure / Total portfolio) * 100",
                "High-risk exposure identification (%)": "(Identified / Total exposures) * 100",
                "Rebalancing cycle compliance (%)": "(On time / Planned rebalances) * 100"
            },
            "Enhance fund performance monitoring": {
                "Target benchmark adherence (%)": "(Achieved / Planned) * 100",
                "Performance review frequency (times/year)": "Number of reviews",
                "Variance from target (%)": "(Target - Actual) / Target * 100",
                "Exception handling timeliness (%)": "(Resolved / Total exceptions) * 100"
            },
            "Optimize cash & liquidity management": {
                "Liquidity coverage ratio (%)": "High-quality liquid assets / Net outflows * 100",
                "Cash position accuracy (%)": "(Accurate / Total days) * 100",
                "Cash forecast timeliness (%)": "(Submitted on time / Total forecasts) * 100",
                "Compliance with cash policy (%)": "(Compliant / Total periods) * 100"
            },
            "Improve process efficiency in finance operations": {
                "Cycle time reduction (%)": "(Previous - Current) / Previous * 100",
                "Process automation adoption (%)": "(Automated / Total processes) * 100",
                "Error reduction rate (%)": "(Previous errors - Current) / Previous * 100",
                "Staff productivity index": "Internal measure"
            },
            "Strengthen financial risk management": {
                "Risk assessment coverage (%)": "(Covered / Total portfolios) * 100",
                "Stress test compliance (%)": "(Compliant / Total tests) * 100",
                "Emerging risk monitoring (%)": "(Monitored / Total identified) * 100",
                "Mitigation plan implementation (%)": "(Implemented / Total planned) * 100"
            },
        },

        # -------------------- Fraud Prevention & Investigation --------------------

        "Fraud Detection & Risk Mitigation": {
            "Enhance fraud detection capabilities": {
                "Fraud cases detected (%)": "(Detected / Total claims) * 100",
                "False positive rate (%)": "(Incorrectly flagged / Total flagged) * 100",
                "Detection time (days)": "Average days from fraud occurrence to detection",
                "High-risk case coverage (%)": "(High-risk cases analyzed / Total high-risk cases) * 100"
            },
            "Strengthen internal investigation processes": {
                "Investigation completion rate (%)": "(Completed / Initiated) * 100",
                "Average investigation time (days)": "Average days to complete",
                "Investigation accuracy (%)": "(Accurate conclusions / Total investigations) * 100",
                "Case backlog reduction (%)": "(Previous - Current) / Previous * 100"
            },
            "Monitor fraud prevention compliance": {
                "Policy adherence (%)": "(Compliant / Total policies) * 100",
                "Audit coverage (%)": "(Audited / Total units) * 100",
                "Regulatory reporting timeliness (%)": "(Reported on time / Total reports) * 100",
                "Exception handling rate (%)": "(Resolved / Total exceptions) * 100"
            },
            "Enhance analytics & early warning systems": {
                "Predictive model accuracy (%)": "(Correct predictions / Total cases) * 100",
                "Model coverage (%)": "(Covered policies / Total policies) * 100",
                "Suspicious activity alerts (#)": "Number of alerts generated",
                "Follow-up completion rate (%)": "(Completed / Total alerts) * 100"
            },
            "Train & empower staff in fraud awareness": {
                "Training completion (%)": "(Completed / Total staff) * 100",
                "Staff detection rate (%)": "(Fraud cases identified by staff / Total cases) * 100",
                "Knowledge retention score": "Test scores post-training",
                "Incident reporting compliance (%)": "(Reported / Total incidents) * 100"
            },
            "Strengthen collaboration with external partners": {
                "Information sharing rate (%)": "(Shared / Required) * 100",
                "Joint investigation coverage (%)": "(Covered / Planned cases) * 100",
                "External audit compliance (%)": "(Compliant / Total audits) * 100",
                "Resolution of cross-partner cases (%)": "(Resolved / Total cross-partner cases) * 100"
            }
        },
        # -------------------- Reinsurance / Partner Management --------------------

        "Reinsurance Strategy & Optimization": {
            "Optimize reinsurance coverage": {
                "Coverage adequacy (%)": "(Reinsured / Total exposure) * 100",
                "Retention ratio (%)": "(Retained risk / Total risk) * 100",
                "Reinsurance cost efficiency (%)": "(Budgeted cost / Actual cost) * 100",
                "Reinsurance compliance (%)": "(Compliant contracts / Total contracts) * 100"
            },
            "Strengthen partner relationships": {
                "Partner satisfaction score": "Survey rating",
                "Contract renewal rate (%)": "(Renewed / Total contracts) * 100",
                "Partner performance index": "Weighted score across KPIs",
                "Timely communication rate (%)": "(Communicated on time / Total interactions) * 100"
            },
            "Monitor counterparty risk": {
                "Counterparty risk coverage (%)": "(Monitored / Total counterparties) * 100",
                "Default risk incidents (#)": "Number of defaults detected",
                "Risk mitigation action rate (%)": "(Actions taken / Total identified risks) * 100",
                "Exposure compliance (%)": "(Compliant / Total exposures) * 100"
            },
            "Enhance reinsurance contract management": {
                "Contract review timeliness (%)": "(Reviewed on time / Total contracts) * 100",
                "Contract accuracy (%)": "(Accurate / Total contracts) * 100",
                "Dispute resolution rate (%)": "(Resolved / Total disputes) * 100",
                "Documentation completeness (%)": "(Complete / Total contracts) * 100"
            },
            "Improve process efficiency in partner management": {
                "Process automation adoption (%)": "(Automated / Total processes) * 100",
                "Partner onboarding time (days)": "Average time",
                "Process error rate (%)": "(Errors / Total processes) * 100",
                "Staff productivity index": "Internal rating"
            },
            "Strengthen reporting & analytics for partners": {
                "Report accuracy (%)": "(Accurate / Total reports) * 100",
                "Report timeliness (%)": "(On time / Total reports) * 100",
                "Analytics coverage (%)": "(Partners analyzed / Total partners) * 100",
                "Actionable insight rate (%)": "(Insights applied / Total insights) * 100"
            },
        },
    },

    "Learning & Growth Perspective": {

        **GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE["Learning & Growth Perspective"],

    },
}
