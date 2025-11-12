
from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE
from management_project.services.strategy_hierarchy.internal_process_perspective import (
    GENERIC_INTERNAL_PROCESS_PERSPECTIVE,
)
from management_project.services.strategy_hierarchy.learning_and_growth_perspective import (
    GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE,
)

BANKING_PERSPECTIVE = {
    "Financial Perspective": {

        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],

        "Banking Revenue Growth & Diversification": {
            "Increase net interest income through loan portfolio expansion": {
                "Loan portfolio growth rate (%)": "(Current loan portfolio - Previous loan portfolio) / Previous loan portfolio * 100",
                "Net interest income growth (%)": "(Current NII - Previous NII) / Previous NII * 100",
                "Interest spread (%)": "Average lending rate - Average deposit rate",
                "Average yield on loans (%)": "Total interest income from loans / Total loans * 100"
            },
            "Grow fee-based income from trade finance": {
                "Trade finance income growth (%)": "(Current trade finance income - Previous) / Previous * 100",
                "Number of trade transactions": "Total trade finance transactions in period",
                "Fee income as % of total revenue": "Trade finance fee income / Total revenue * 100",
                "Average fee per transaction": "Trade finance fee income / Number of transactions"
            },
            "Grow remittance service income": {
                "Remittance volume (USD)": "Total remittance volume processed",
                "Remittance income growth (%)": "(Current remittance income - Previous) / Previous * 100",
                "Number of active remittance customers": "Customers using remittance services at period end",
                "Average remittance fee (%)": "Total fees from remittance / Remittance volume * 100"
            },
            "Diversify income across retail, corporate, and SME segments": {
                "Revenue share by segment (%)": "Revenue per segment / Total revenue * 100",
                "Growth rate per segment (%)": "(Current revenue per segment - Previous) / Previous * 100",
                "Number of SME and retail clients": "Active clients in SME + retail segments",
                "Revenue concentration ratio (%)": "Revenue from top 10 clients / Total revenue * 100"
            },
            "Increase contribution from digital banking channels": {
                "Digital revenue share (%)": "Revenue from digital channels / Total revenue * 100",
                "Digital transaction volume": "Number of transactions via digital channels",
                "Digital customer base growth (%)": "(Current digital customers - Previous) / Previous * 100",
                "Average revenue per digital customer": "Revenue from digital channels / Number of digital customers"
            },
            "Enhance cross-selling of deposit, credit, and insurance products": {
                "Cross-sell ratio (%)": "Customers with multiple products / Total customers * 100",
                "Average products per customer": "Total products sold / Total customers",
                "Cross-sell revenue contribution (%)": "Revenue from cross-sell / Total revenue * 100",
                "Customer conversion rate (%)": "Number of cross-sell conversions / Customers contacted * 100"
            },
            "Expand card business revenue": {
                "Card transaction volume": "Total card transactions in period",
                "Card fee income (%)": "Fee income from cards / Total revenue * 100",
                "Number of active cards": "Active credit/debit/prepaid cards",
                "Card portfolio growth rate (%)": "(Current card portfolio - Previous) / Previous * 100"
            },
            "Strengthen foreign exchange and treasury income": {
                "FX income growth (%)": "(Current FX income - Previous) / Previous * 100",
                "Treasury income contribution (%)": "Treasury revenue / Total revenue * 100",
                "FX transaction volume": "Total FX transactions processed",
                "Trading gain/loss ratio (%)": "Trading gains / Trading losses * 100"
            },
            "Capture new market segments": {
                "New market customer acquisition (%)": "(New customers in segment / Total segment customers) * 100",
                "Rural/youth/women account share (%)": "Accounts in target segment / Total accounts * 100",
                "Market penetration ratio (%)": "Number of target segment customers / Total potential customers * 100",
                "Segment revenue growth (%)": "(Current revenue from segment - Previous) / Previous * 100"
            },
            "Increase commission income from partnerships and fintech services": {
                "Commission income from partners (%)": "Commission revenue / Total revenue * 100",
                "Number of fintech partnerships": "Active fintech partners in period",
                "Revenue share from fintech (%)": "Revenue from fintech partnerships / Total revenue * 100",
                "Partner retention rate (%)": "(Partners retained / Total partners) * 100"
            },
            "Core & Retail Banking Revenue": {
                "Average balance per account ($)": "Total deposits / Number of accounts",
                "Deposit growth rate (%)": "(Current deposits - Previous deposits) / Previous deposits * 100",
                "Loan revenue per product ($)": "Total loan revenue / Number of loan products",
                "Revenue per transaction ($)": "Total transaction revenue / Number of transactions"
            },

            "Commercial & Corporate Banking Revenue": {
                "Commercial loan revenue ($)": "Total revenue from business loans",
                "Cash management revenue ($)": "Fees from treasury and cash management services",
                "Overdraft revenue ($)": "Revenue from business overdraft facilities",
                "M&A advisory revenue ($)": "Fees from mergers and acquisitions advisory"
            },
            "Investment & Capital Markets Revenue": {
                "Revenue per deal ($)": "Total revenue from IB deals / Number of deals",
                "Underwriting revenue ($)": "Fees from debt/equity underwriting",
                "Trading P&L ($)": "Net profit/loss from proprietary trading",
                "Structured products revenue ($)": "Revenue from customized financial products"
            },
            "Private Banking & Wealth Management": {
                "Revenue per private client ($)": "Total private banking revenue / Number of private clients",
                "Alternative investments revenue ($)": "Revenue from alternative investments",
                "Assets under management growth ($)": "Period-over-period AUM growth"
            },
        },

        "Banking Cost Management": {
            "Reduce cost-to-income ratio": {
                "Cost-to-income ratio (%)": "Operating expenses / Operating income * 100",
                "Operating expense growth (%)": "(Current expenses - Previous) / Previous * 100",
                "Expense per transaction ($)": "Operating expenses / Total transactions",
                "Overhead cost ratio (%)": "Administrative expenses / Total operating expenses * 100"
            },
            "Optimize branch network cost": {
                "Cost per branch ($)": "Operating cost per branch",
                "Branch energy cost ($)": "Energy expense per branch",
                "Branch maintenance cost ($)": "Maintenance expense per branch",
                "Branch IT cost ($)": "IT expense per branch"
            },
            "Reduce personnel costs": {
                "Salary & benefits ratio (%)": "Total staff cost / Operating expenses * 100",
                "Revenue per employee ($)": "Total revenue / Number of employees",
                "Profit per employee ($)": "Net profit / Number of employees",
                "Staff cost per transaction ($)": "Total staff cost / Total transactions"
            },
            "Optimize IT and technology costs": {
                "IT cost ratio (%)": "IT operating cost / Operating expenses * 100",
                "Cloud adoption savings ($)": "Cost reduction from cloud migration",
                "Automation cost savings ($)": "Reduction in manual processing costs",
                "System maintenance cost ($)": "Annual maintenance expense for IT systems"
            },
            "Digitize processes to reduce cost": {
                "Digitization coverage (%)": "(Digitized processes / Total processes) * 100",
                "Cost reduction per automated process ($)": "Savings from automation / Automated processes",
                "Manual process reduction (%)": "(Previous manual processes - Current) / Previous * 100",
                "Process efficiency cost index": "Cost per transaction before vs after automation"
            },
            "Optimize procurement and vendor spending": {
                "Procurement cost savings ($)": "Previous cost - Current cost",
                "Vendor consolidation savings ($)": "Savings from reducing number of vendors",
                "Cost per procurement transaction ($)": "Procurement expenses / Total procurement transactions",
                "Supplier performance cost efficiency": "Weighted supplier cost vs quality index"
            },
            "Reduce energy and facilities costs": {
                "Energy cost per branch ($)": "Total energy expense / Number of branches",
                "Facility maintenance cost ($)": "Maintenance expense per branch",
                "Paper and consumables cost ($)": "Cost of office supplies per transaction",
                "Space utilization efficiency (%)": "(Used branch space / Total branch space) * 100"
            },
            "Minimize compliance and reporting costs": {
                "Cost per compliance process ($)": "Compliance-related expenses / Number of processes",
                "Audit cost per branch ($)": "Audit expense / Number of branches",
                "Regulatory reporting cost ($)": "Total reporting cost per period",
                "Automation savings in compliance ($)": "Reduction in compliance cost through automation"
            },
            "Reduce digital transaction costs": {
                "Cost per digital transaction ($)": "Digital channel operating cost / Digital transactions",
                "IT cost ratio for digital channels (%)": "IT expenses for digital / Digital revenue * 100",
                "Digital channel overhead ($)": "Support cost per digital channel",
                "Digital adoption cost savings ($)": "Savings from migrating transactions online"
            },
        },

        "Banking Asset Quality & Credit Risk Management": {
            "Reduce non-performing loans (NPL)": {
                "NPL ratio (%)": "Non-performing loans / Total loans * 100",
                "Loan recovery rate (%)": "Recovered loans / Total defaulted loans * 100",
                "Write-off ratio (%)": "Loans written off / Total loans * 100",
                "Credit loss provision (%)": "Loan loss provisions / Total loans * 100"
            },
            "Improve credit appraisal systems": {
                "Credit scoring accuracy (%)": "(Correctly scored loans / Total scored loans) * 100",
                "Average approval time (hours)": "Sum of approval times / Number of applications",
                "Rejection rate (%)": "Rejected applications / Total applications * 100",
                "Loan default probability (%)": "Expected defaults / Total loans * 100"
            },
            "Enhance post-disbursement monitoring": {
                "Post-disbursement audit coverage (%)": "(Loans audited / Total loans) * 100",
                "Recovery follow-up success rate (%)": "(Successful recoveries / Total recoveries attempted) * 100",
                "Loan monitoring frequency": "Average number of monitoring activities per loan",
                "Customer delinquency alerts count": "Number of alerts triggered for overdue accounts"
            },
            "Diversify credit portfolio": {
                "Portfolio concentration ratio (%)": "(Top 10 loans / Total loans) * 100",
                "Industry exposure index": "Exposure to single industry / Total loan portfolio * 100",
                "Sectoral loan share (%)": "Loans per sector / Total loans * 100",
                "Credit diversification score": "Weighted diversification index across sectors"
            },
            "Develop early warning delinquency models": {
                "Early warning model accuracy (%)": "(Correctly predicted delinquencies / Total predictions) * 100",
                "Detected risky accounts (%)": "(Accounts flagged / Total accounts) * 100",
                "Response time to alerts (hours)": "Average hours to action flagged accounts",
                "Model false positive rate (%)": "(False alerts / Total alerts) * 100"
            }
        },

        "Banking Liquidity & Capital Management": {
            "Maintain optimal liquidity coverage ratio": {
                "Liquidity Coverage Ratio (LCR %)": "(High-quality liquid assets / Net cash outflows over 30 days) * 100",
                "Net Stable Funding Ratio (NSFR %)": "(Available stable funding / Required stable funding) * 100",
                "Liquid assets to total assets (%)": "(Liquid assets / Total assets) * 100",
                "Daily liquidity gap variance (%)": "(Daily gap deviation / Total assets) * 100"
            },
            "Ensure adequate capital adequacy ratio": {
                "Capital Adequacy Ratio (CAR %)": "(Regulatory capital / Risk-weighted assets) * 100",
                "Tier 1 capital ratio (%)": "(Tier 1 capital / Risk-weighted assets) * 100",
                "Risk-weighted assets (%)": "(Risk-weighted assets / Total assets) * 100",
                "Capital buffer above regulatory minimum (%)": "(Capital - Required minimum) / Required minimum * 100"
            },
            "Strengthen deposit mobilization": {
                "Total deposits growth rate (%)": "(Current deposits - Previous deposits) / Previous * 100",
                "New deposit accounts opened": "Count of new deposit accounts",
                "Retail deposits share (%)": "(Retail deposits / Total deposits) * 100",
                "Deposit retention ratio (%)": "(Deposits retained / Deposits maturing) * 100"
            },
            "Increase low-cost deposits (CASA)": {
                "CASA ratio (%)": "(Current + Savings accounts / Total deposits) * 100",
                "Average cost of deposits (%)": "(Interest expense on deposits / Total deposits) * 100",
                "Savings account growth (%)": "(Current savings accounts - Previous) / Previous * 100",
                "Current account growth (%)": "(Current current accounts - Previous) / Previous * 100"
            }
        },

        "Banking Profitability & Financial Sustainability": {
            "Increase return on equity": {
                "ROE (%)": "(Net income / Shareholders' equity) * 100",
                "Profit after tax (USD)": "Net income after tax",
                "Shareholder value added (%)": "(Net profit - Cost of equity) / Shareholders' equity * 100",
                "Net profit growth rate (%)": "(Current net profit - Previous) / Previous * 100"
            },
            "Improve return on assets": {
                "ROA (%)": "(Net income / Total assets) * 100",
                "Income to assets ratio (%)": "(Operating income / Total assets) * 100",
                "Net profit to assets (%)": "(Net profit / Total assets) * 100",
                "Asset turnover ratio": "Revenue / Total assets"
            },
            "Enhance profitability of high-value customers": {
                "Profit per high-value customer": "Revenue from top clients / Number of top clients",
                "High-value retention rate (%)": "(High-value clients retained / Total high-value clients) * 100",
                "Cross-sell ratio (%)": "(High-value clients with multiple products / Total high-value clients) * 100",
                "Revenue from top 10% customers (%)": "(Revenue from top 10% clients / Total revenue) * 100"
            },
            "Improve pricing models": {
                "Average lending rate (%)": "(Total interest income / Total loans) * 100",
                "Average deposit rate (%)": "(Total interest paid / Total deposits) * 100",
                "Net interest margin (%)": "Net interest income / Average earning assets * 100",
                "Interest spread (%)": "Average lending rate - Average deposit rate"
            },
            "Lending & Deposit Products": {
                "Net interest margin by product (%)": "(Interest income - Interest expense) / Earning assets * 100",
                "Loan product contribution margin (%)": "(Loan revenue - Direct costs) / Loan revenue * 100",
                "Credit card profitability index": "Revenue per card / Cost to service per card"
            },
            "Fee-Based Services": {
                "Advisory service margin (%)": "(Advisory fees - Service delivery cost) / Advisory fees * 100",
                "Transaction service profitability ($)": "Net revenue per transaction type",
                "Cash management service ROI (%)": "Revenue from cash management / Platform investment"
            },
            "Investment & Trading Products": {
                "Wealth management fee efficiency": "Revenue from AUM / Cost to manage AUM",
                "Trading desk profitability ($)": "P&L per trading desk / Capital allocated",
                "Structured product margin (%)": "(Product revenue - Hedging costs) / Product revenue * 100"
            },

            "Banking Profitability & Financial Sustainability": {
                "Overall bank ROE (%)": "Net income / Total equity",
                "Total bank revenue growth (%)": "(Current total revenue - Previous) / Previous * 100",
                "Revenue diversification index": "1 - (Largest business line revenue / Total revenue)",
                "Cost-to-income ratio (%)": "Total operating expenses / Total operating income"
            },

            "Retail Banking Profitability": {
                "Retail net interest margin (%)": "Retail NII / Retail earning assets",
                "Retail revenue per product ($)": "Total retail revenue / Number of retail products",
                "Retail cost-to-income ratio (%)": "Retail expenses / Retail revenue",
                "Credit card profitability index": "Card revenue / Card servicing cost"
            },

            "Corporate Banking Profitability": {
                "Corporate loan yield (%)": "Corporate interest income / Corporate loans",
                "Cash management service margin (%)": "(Cash management fees - Direct costs) / Fees",
                "Corporate banking ROA (%)": "Corporate net income / Corporate assets"
            },

            "Investment Banking Profitability": {
                "Revenue per deal ($)": "Total IB revenue / Number of deals",
                "Underwriting margin (%)": "(Underwriting fees - Syndication costs) / Fees",
                "Trading desk P&L ($)": "Net profit per trading desk"
            },
        },

        "Banking Treasury & Investment Portfolio Management": {
            "Optimize investment portfolio yield": {
                "Average investment yield (%)": "(Investment income / Total investments) * 100",
                "Investment income share (%)": "(Investment income / Total revenue) * 100",
                "Duration-adjusted return (%)": "(Return adjusted for portfolio duration / Total investments) * 100",
                "Portfolio turnover ratio": "Total investment bought/sold / Average portfolio value"
            },
            "Strengthen asset-liability maturity matching": {
                "Weighted maturity gap (days)": "Sum of (Asset maturity - Liability maturity) * Weight",
                "Short-term assets to liabilities (%)": "(Short-term assets / Short-term liabilities) * 100",
                "Repricing gap (%)": "(Rate-sensitive assets - Rate-sensitive liabilities) / Total assets * 100",
                "Liquidity mismatch ratio (%)": "(Liquidity gap / Total assets) * 100"
            },
            "Diversify treasury income sources": {
                "FX income share (%)": "(FX income / Total treasury income) * 100",
                "Derivatives income growth (%)": "(Current derivatives income - Previous) / Previous * 100",
                "Repo volume (USD)": "Total repurchase agreements volume",
                "Bond trading profit margin (%)": "(Profit from bond trading / Bond trading revenue) * 100"
            },
            "Increase ESG-compliant investments": {
                "% of portfolio in ESG assets": "(ESG assets / Total portfolio) * 100",
                "Green bonds purchased": "Total value of green bonds purchased",
                "Sustainable yield (%)": "(Income from ESG assets / ESG assets) * 100",
                "ESG compliance score": "Internal ESG compliance rating index"
            },
            "Treasury Revenue Generation": {
                "Treasury revenue ($)": "Net interest + Trading income from treasury",
                "Liquidity portfolio yield (%)": "Income from liquid assets / Average liquid assets * 100",
                "Funds transfer pricing contribution ($)": "Net contribution from internal funds pricing"
            },
            "Capital Allocation Efficiency": {
                "Return on risk-weighted assets (%)": "Net income / Risk-weighted assets * 100",
                "Business line capital efficiency ($)": "Revenue per unit of allocated capital",
                "Economic value added (EVA) ($)": "Net operating profit after tax - (Capital * Cost of capital)"
            },
            "Balance Sheet Optimization": {
                "Net interest margin (%)": "(Interest income - Interest expense) / Earning assets * 100",
                "Cost of funds optimization (%)": "Average interest rate paid on deposits and borrowings",
                "Asset-liability management gap ($)": "Interest rate sensitivity of net interest income"
            }
        },

        "Banking Resource Utilization": {
            "Enhance Staff Productivity": {
                "Revenue per employee ($)": "Total bank revenue / Total number of employees",
                "Profit per employee ($)": "Net profit / Total number of employees",
                "Transactions per employee (#)": "Total customer transactions / Total number of employees",
                "Customer service efficiency (%)": "(Transactions handled without escalation / Total transactions) * 100"
            },
            "Optimize Branch & ATM Network": {
                "Revenue per branch ($)": "Total revenue / Number of branches",
                "Profit per branch ($)": "Net profit / Number of branches",
                "Customer per branch (#)": "Total active customers / Number of branches",
                "ATM utilization rate (%)": "(Transactions through ATM / Total ATM capacity) * 100"
            },
            "Improve Deposit & Loan Utilization": {
                "Loan-to-deposit ratio (%)": "(Total loans / Total deposits) * 100",
                "Yield on loan portfolio (%)": "(Interest income from loans / Total loans) * 100",
                "Deposit cost ratio (%)": "(Interest paid on deposits / Total deposits) * 100",
                "Funds deployment efficiency (%)": "(Loans + Investments) / Total funds available * 100"
            },
            "Enhance Digital Channel Efficiency": {
                "Digital transaction share (%)": "(Digital channel transactions / Total transactions) * 100",
                "Digital revenue contribution (%)": "(Revenue from digital channels / Total revenue) * 100",
                "Cost per digital transaction ($)": "Digital channel operating cost / Digital transactions",
                "Mobile banking adoption rate (%)": "(Active mobile users / Total customers) * 100"
            },
            "Optimize IT & Technology Resources": {
                "IT cost per transaction ($)": "Total IT operating cost / Total transactions",
                "System uptime (%)": "(System availability time / Total scheduled time) * 100",
                "Automation ratio (%)": "(Automated transactions / Total transactions) * 100",
                "Tech ROI (%)": "(Revenue or savings from IT initiatives / IT investment) * 100"
            },
            "Improve Capital & Liquidity Utilization": {
                "Return on Assets (ROA %)": "(Net income / Total assets) * 100",
                "Return on Equity (ROE %)": "(Net income / Shareholders' equity) * 100",
                "Liquidity coverage ratio (LCR %)": "(High-quality liquid assets / Net cash outflows over 30 days) * 100",
                "Capital utilization ratio (%)": "(Total assets / Total regulatory capital) * 100"
            },
            "Optimize Energy & Physical Resource Use": {
                "Energy cost per branch ($)": "Total energy expense / Number of branches",
                "Branch operational efficiency (%)": "(Revenue per branch / Operating cost per branch) * 100",
                "Paper usage per transaction (#)": "Total paper used / Total transactions",
                "Facility utilization rate (%)": "(Used branch capacity / Total branch capacity) * 100"
            }
        },
    },

    "Customer Perspective": {

        **GENERIC_CUSTOMER_PERSPECTIVE["Customer Perspective"],
    },

    "Internal_Process_Perspective": {

        **GENERIC_INTERNAL_PROCESS_PERSPECTIVE["Internal Process Perspective"],

        # -------------------- 1. Core Banking Functions --------------------
        "Core Banking Functions": {
            "Optimize Deposit Management": {
                "Deposit accuracy rate (%)": "(Accurate deposit entries / Total deposits) * 100",
                "New accounts processed (#)": "Number of new accounts opened",
                "Deposit retention process compliance (%)": "(Compliant retention / Total deposits) * 100",
                "Average processing time per account (days)": "Average time to open or maintain accounts"
            },
            "Enhance Loan Management": {
                "Loan application processing time (days)": "Average time to process loan applications",
                "Loan documentation completeness (%)": "(Complete docs / Total loans) * 100",
                "Loan approval accuracy (%)": "(Correct approvals / Total approvals) * 100",
                "Loan review compliance (%)": "(Compliant reviews / Total reviews) * 100"
            },
            "Improve Payments & Settlements": {
                "Transaction success rate (%)": "(Successful / Total) * 100",
                "Average settlement time (minutes)": "Time to settle transactions",
                "Payment exception rate (%)": "(Exceptions / Total transactions) * 100",
                "Process standard adherence (%)": "(Transactions following standard / Total) * 100"
            },
            "Optimize Account Management": {
                "Account error rate (%)": "(Errors / Total accounts) * 100",
                "Average account lifecycle time (days)": "Time from opening to closure",
                "Process compliance score": "Survey/assessment of process adherence",
                "Account activity ratio (%)": "(Active accounts / Total accounts) * 100"
            },
            "Enhance Core Banking IT Systems": {
                "System uptime (%)": "Operational hours / Total hours * 100",
                "Transaction processing speed": "Average time per transaction",
                "System incident rate (#)": "Number of system failures",
                "IT support resolution time (hours)": "Average resolution time"
            },
            "Improve Compliance in Core Operations": {
                "Regulatory compliance (%)": "Compliant operations / Total operations * 100",
                "Audit finding reduction (%)": "(Baseline findings - Current findings) / Baseline findings * 100",
                "Fraud detection effectiveness (%)": "(Detected fraud / Total fraud incidents) * 100",
                "Customer grievance resolution (%)": "(Resolved / Total complaints) * 100"
            }
        },

        # -------------------- 2. Retail Banking --------------------
        "Retail Banking": {
            "Optimize Personal Loan Operations": {
                "Loan processing accuracy (%)": "(Correctly processed loans / Total loans) * 100",
                "Approval turnaround time (days)": "Average days to approve",
                "Documentation completeness (%)": "(Complete docs / Total loans) * 100",
                "Compliance with lending policies (%)": "(Compliant loans / Total loans) * 100"
            },
            "Optimize Savings & Deposit Operations": {
                "New account processing time (days)": "Average time to open accounts",
                "Deposit management accuracy (%)": "(Correct entries / Total deposits) * 100",
                "Deposit retention compliance (%)": "(Compliant retention / Total deposits) * 100",
                "Customer process satisfaction": "Survey rating"
            },
            "Enhance Mortgage Processing": {
                "Mortgage application processing time (days)": "Average days to process",
                "Documentation completeness (%)": "(Complete docs / Total mortgages) * 100",
                "Approval accuracy (%)": "(Correct approvals / Total approvals) * 100",
                "Process compliance (%)": "(Compliant processes / Total processes) * 100"
            },
            "Streamline Investment Product Processes": {
                "Product adoption compliance (%)": "(Products processed as per standards / Total products) * 100",
                "Process error rate (%)": "(Errors / Total products) * 100",
                "Customer process satisfaction": "Survey rating",
                "Product renewal process efficiency (%)": "(Renewed on time / Total products) * 100"
            },
            "Enhance Customer Experience Processes": {
                "Branch service compliance (%)": "(Compliant service processes / Total services) * 100",
                "Digital adoption process efficiency (%)": "(Completed digital processes / Total digital requests) * 100",
                "Call center resolution time (minutes)": "Average time per call",
                "Complaint resolution rate (%)": "(Resolved / Total complaints) * 100"
            }
        },

        # -------------------- 3. Business / Commercial Banking --------------------
        "Business / Commercial Banking": {
            "SME Loan Operations": {
                "Loan processing time (days)": "Average days to process",
                "Documentation completeness (%)": "(Complete docs / Total loans) * 100",
                "Approval accuracy (%)": "(Correct approvals / Total approvals) * 100",
                "Policy compliance (%)": "(Compliant loans / Total loans) * 100"
            },
            "Business Account & Cash Management Processes": {
                "New business account processing time (days)": "Average time",
                "Cash management process adoption (%)": "(Businesses following processes / Total clients) * 100",
                "Process error rate (%)": "(Errors / Total processes) * 100",
                "Customer process satisfaction": "Survey rating"
            },
            "Trade Finance Processes": {
                "Application processing time (days)": "Average time",
                "Documentation compliance (%)": "(Complete docs / Total applications) * 100",
                "Process error rate (%)": "(Errors / Total transactions) * 100",
                "Compliance adherence (%)": "(Compliant processes / Total processes) * 100"
            },
            "Business Credit Operations": {
                "Overdraft approval accuracy (%)": "(Correct approvals / Total approvals) * 100",
                "Process turnaround time (days)": "Average days to complete",
                "Default monitoring compliance (%)": "(Monitored / Total overdrafts) * 100",
                "Customer process satisfaction": "Survey rating"
            },
            "Risk Management Processes": {
                "Credit assessment accuracy (%)": "(Correct assessments / Total assessments) * 100",
                "Fraud detection (%)": "(Detected / Total fraud attempts) * 100",
                "Compliance rate (%)": "(Compliant operations / Total operations) * 100",
                "Portfolio process performance index": "Weighted performance of operational processes"
            },
            "Operational Efficiency Processes": {
                "Process cost per transaction ($)": "Total process cost / Total transactions",
                "Staff productivity": "Transactions handled per staff",
                "Turnaround time reduction (%)": "(Previous - Current) / Previous * 100",
                "Automation adoption (%)": "(Automated processes / Total processes) * 100"
            }
        },

        # -------------------- 4. Corporate Banking --------------------
        "Corporate Banking": {
            "Corporate Lending Processes": {
                "Loan processing accuracy (%)": "(Correct approvals / Total approvals) * 100",
                "Documentation completeness (%)": "(Complete docs / Total loans) * 100",
                "Application turnaround time (days)": "Average days per application",
                "Syndication process success (%)": "(Compliant syndications / Total syndications) * 100"
            },
            "Treasury & Cash Management Processes": {
                "Process adoption rate (%)": "(Clients following processes / Total clients) * 100",
                "Process error rate (%)": "(Errors / Total processes) * 100",
                "Liquidity management compliance (%)": "(Compliant processes / Total) * 100",
                "Transaction accuracy rate (%)": "(Correct transactions / Total transactions) * 100"
            },
            "Advisory & Deal Processes": {
                "Documentation completeness (%)": "(Complete docs / Total advisory cases) * 100",
                "Compliance with advisory standards (%)": "(Compliant cases / Total cases) * 100",
                "Process turnaround time (days)": "Average days per advisory",
                "Client satisfaction with process": "Survey rating"
            },
            "Risk Assessment Processes": {
                "Default monitoring compliance (%)": "(Monitored / Total loans) * 100",
                "Fraud detection effectiveness (%)": "(Detected fraud / Total incidents) * 100",
                "Process compliance rate (%)": "(Compliant operations / Total operations) * 100",
                "Portfolio operational performance": "Weighted performance of processes"
            },
            "Operational Efficiency": {
                "Process time per transaction (days)": "Average time",
                "Error rate (%)": "(Errors / Total transactions) * 100",
                "Staff productivity": "Transactions handled per staff",
                "Automation adoption (%)": "(Automated processes / Total processes) * 100"
            }
        },

        # -------------------- 5. Investment Banking --------------------
        "Investment Banking": {
            "Capital Markets Operations": {
                "Deal processing accuracy (%)": "(Correctly processed deals / Total deals) * 100",
                "Process adherence (%)": "(Deals processed per standards / Total deals) * 100",
                "Average deal processing time (days)": "Average days per deal",
                "Compliance adherence (%)": "(Compliant deals / Total deals) * 100"
            },
            "Mergers & Acquisitions Processes": {
                "Documentation completeness (%)": "(Complete docs / Total deals) * 100",
                "Process turnaround time (days)": "Average time per mandate",
                "Client process satisfaction": "Survey rating",
                "Compliance adherence (%)": "(Compliant / Total deals) * 100"
            },
            "Underwriting Operations": {
                "Underwriting accuracy (%)": "(Correct underwriting / Total underwriting) * 100",
                "Process error rate (%)": "(Errors / Total underwriting) * 100",
                "Turnaround time (days)": "Average days per underwriting",
                "Compliance adherence (%)": "(Compliant / Total underwriting) * 100"
            },
            "Structured Products & Proprietary Trading": {
                "Process adoption rate (%)": "(Processes followed / Total trades) * 100",
                "Error rate (%)": "(Errors / Total trades) * 100",
                "Client process satisfaction": "Survey rating",
                "Risk management compliance (%)": "(Compliant trades / Total trades) * 100"
            },
            "Deal Origination Processes": {
                "New mandate processing time (days)": "Average days",
                "Process compliance (%)": "(Compliant / Total mandates) * 100",
                "Client process satisfaction": "Survey rating",
                "Workflow adherence (%)": "(Steps followed / Total steps) * 100"
            },
            "Risk & Compliance in Investment Banking": {
                "Compliance incident rate (#)": "Reported / Total operations",
                "Regulatory adherence (%)": "Compliant operations / Total operations * 100",
                "Audit finding reduction (%)": "(Previous - Current) / Previous * 100",
                "Fraud detection effectiveness (%)": "(Detected fraud / Total fraud incidents) * 100"
            }
        },

        # -------------------- 6. Private Banking / Wealth Management --------------------
        "Private Banking / Wealth Management": {
            "Wealth Planning Processes": {
                "Plans implemented on time (%)": "(Implemented / Total plans) * 100",
                "Plan documentation completeness (%)": "(Complete docs / Total plans) * 100",
                "Client process satisfaction": "Survey rating",
                "Plan review compliance (%)": "(Reviewed / Total plans) * 100"
            },
            "Investment Advisory & Portfolio Management": {
                "Portfolio review compliance (%)": "(Reviewed portfolios / Total portfolios) * 100",
                "Process error rate (%)": "(Errors / Total advisory activities) * 100",
                "Turnaround time per advisory (days)": "Average time",
                "Client process satisfaction": "Survey rating"
            },
            "Estate & Tax Planning": {
                "Documentation completeness (%)": "(Complete docs / Total plans) * 100",
                "Process adherence (%)": "(Compliant / Total plans) * 100",
                "Review turnaround time (days)": "Average days",
                "Client process satisfaction": "Survey rating"
            },
            "Alternative Investments & Family Office Services": {
                "Process compliance (%)": "(Compliant / Total services) * 100",
                "Error rate (%)": "(Errors / Total services) * 100",
                "Review turnaround time (days)": "Average days",
                "Client satisfaction with process": "Survey rating"
            },
            "Client Acquisition Processes": {
                "New client onboarding time (days)": "Average time",
                "Process adherence (%)": "(Compliant / Total onboarding) * 100",
                "Client satisfaction with process": "Survey rating",
                "Referral process compliance (%)": "(Compliant referrals / Total referrals) * 100"
            },
            "Compliance & Risk Management Processes": {
                "Regulatory compliance (%)": "(Compliant operations / Total operations) * 100",
                "AML/KYC process coverage (%)": "(Verified clients / Total clients) * 100",
                "Audit finding reduction (%)": "(Previous - Current) / Previous * 100",
                "Fraud detection effectiveness (%)": "(Detected / Total fraud incidents) * 100"
            }
        },

        # -------------------- 7. Transaction Banking --------------------
        "Transaction Banking": {
            "Payment & Collection Services": {
                "Transaction success rate (%)": "(Successful / Total) * 100",
                "Average processing time (hours)": "Average hours per transaction",
                "Process error rate (%)": "(Failed / Total transactions) * 100",
                "Client process satisfaction": "Survey rating"
            },
            "Trade Finance Processes": {
                "Application processing time (days)": "Average time",
                "Documentation completeness (%)": "(Complete docs / Total applications) * 100",
                "Error rate (%)": "(Errors / Total transactions) * 100",
                "Compliance adherence (%)": "(Compliant / Total transactions) * 100"
            },
            "Cash Management & Liquidity Processes": {
                "Process adoption rate (%)": "(Clients following processes / Total clients) * 100",
                "Process error rate (%)": "(Errors / Total operations) * 100",
                "Liquidity process compliance (%)": "(Compliant / Total transactions) * 100",
                "Client satisfaction with process": "Survey rating"
            },
            "Foreign Exchange & Hedging Processes": {
                "Process adherence (%)": "(Compliant FX processes / Total transactions) * 100",
                "Error rate (%)": "(Errors / Total FX transactions) * 100",
                "Client process satisfaction": "Survey rating",
                "Compliance adherence (%)": "(Compliant / Total transactions) * 100"
            },
            "Supply Chain Finance Processes": {
                "Process turnaround time (days)": "Average time",
                "Process compliance (%)": "(Compliant / Total financing) * 100",
                "Default monitoring compliance (%)": "(Monitored / Total financed) * 100",
                "Error rate (%)": "(Errors / Total transactions) * 100"
            },
            "Operational Efficiency": {
                "Process error rate (%)": "(Errors / Total transactions) * 100",
                "Automation adoption (%)": "(Automated / Total processes) * 100",
                "Staff productivity": "Transactions handled per staff",
                "Process turnaround time reduction (%)": "(Previous - Current) / Previous * 100"
            }
        },

        # -------------------- 8. Risk & Compliance --------------------
        "Risk & Compliance": {
            "Credit Risk Management": {
                "Non-performing loan monitoring (%)": "(NPLs monitored / Total NPLs) * 100",
                "Loan review compliance (%)": "(Compliant reviews / Total loans) * 100",
                "Portfolio risk diversification index": "Diversification of risk across sectors",
                "Approval cycle time (days)": "Average days to approve"
            },
            "Market Risk Management": {
                "Risk exposure monitoring coverage (%)": "(Monitored positions / Total positions) * 100",
                "Market loss incidents (#)": "Number exceeding internal limits",
                "Stress test compliance (%)": "(Compliant / Total stress tests) * 100",
                "Mitigation plan implementation (%)": "(Implemented / Total planned) * 100"
            },
            "Operational Risk Management": {
                "Operational loss events (#)": "Number of process failures",
                "Process failure rate (%)": "(Failed processes / Total processes) * 100",
                "Risk control assessment coverage (%)": "(Reviewed / Total processes) * 100",
                "Incident resolution time (days)": "Average days to resolve"
            },
            "Compliance & Regulatory Affairs": {
                "Regulatory compliance (%)": "(Compliant operations / Total operations) * 100",
                "Audit findings (#)": "Number of audit findings",
                "Reporting accuracy (%)": "(Accurate / Total reports) * 100",
                "Timely submissions (%)": "(Submitted on time / Total required) * 100"
            },
            "Internal Audit": {
                "Audit coverage (%)": "(Audited units / Total units) * 100",
                "Findings closure rate (%)": "(Closed / Total findings) * 100",
                "Recommendations implemented (%)": "(Implemented / Total recommendations) * 100",
                "Audit cycle time (days)": "Average days per audit"
            },
            "Fraud & Financial Crime Prevention": {
                "Process compliance coverage (%)": "(Verified processes / Total processes) * 100",
                "Fraud detection effectiveness (%)": "(Detected / Total incidents) * 100",
                "Suspicious transaction reporting timeliness (%)": "(On-time reports / Total reports) * 100",
                "Number of incidents (#)": "Total reported incidents"
            }
        },

        # -------------------- 9. Operations & Technology --------------------
        "Operations & Technology": {
            "IT & Digital Platforms": {
                "System uptime (%)": "(Operational hours / Total hours) * 100",
                "Digital process adoption (%)": "(Completed digital processes / Total) * 100",
                "Incident response time (hours)": "Average time to resolve",
                "IT project delivery on-time (%)": "(On-time / Total projects) * 100"
            },
            "Cybersecurity & Threat Management": {
                "Security incidents (#)": "Number of reported incidents",
                "Mean time to detect/respond (hours)": "Average response time",
                "Compliance coverage (%)": "(Compliant systems / Total systems) * 100",
                "Phishing test pass rate (%)": "(Users passed / Total users) * 100"
            },
            "Payment Processing Systems": {
                "Transaction success rate (%)": "(Successful / Total) * 100",
                "Average processing time (seconds)": "Average time per transaction",
                "Process error rate (%)": "(Failed / Total transactions) * 100",
                "Process compliance (%)": "(Compliant transactions / Total) * 100"
            },
            "Loan Operations & Processing": {
                "Processing time (days)": "Average time per loan",
                "Approval accuracy (%)": "(Correct approvals / Total approvals) * 100",
                "Documentation completeness (%)": "(Complete / Total loans) * 100",
                "Customer satisfaction with process": "Survey rating"
            },
            "Branch Operations": {
                "Transaction efficiency (%)": "(Completed / Total requests) * 100",
                "Customer wait time (minutes)": "Average wait",
                "Staff productivity": "Transactions handled per staff",
                "Process compliance (%)": "(Compliant / Total transactions) * 100"
            },
            "Operational Cost Management": {
                "Cost per transaction ($)": "Total operational cost / Total transactions",
                "Process standardization (%)": "(Standardized processes / Total processes) * 100",
                "Automation adoption (%)": "(Automated processes / Total processes) * 100",
                "Efficiency gain (%)": "(Previous cost - Current cost) / Previous cost * 100"
            }
        },

        # -------------------- 10. Service Excellence & Customer Support --------------------
        "Service Excellence & Customer Support": {
            "Call Center Operations": {
                "First-call resolution (%)": "(Resolved first call / Total calls) * 100",
                "Average handling time (minutes)": "Average call duration",
                "Call abandonment rate (%)": "(Abandoned / Total calls) * 100",
                "Customer satisfaction score": "Survey rating"
            },
            "Branch Service Excellence": {
                "Process compliance (%)": "(Compliant / Total branch operations) * 100",
                "Transaction error rate (%)": "(Errors / Total transactions) * 100",
                "Average service time (minutes)": "Average minutes per customer",
                "Customer satisfaction score": "Survey rating"
            },
            "Digital Support & Chatbots": {
                "Resolution rate (%)": "(Resolved / Total digital requests) * 100",
                "Average response time (minutes)": "Average minutes to respond",
                "Process compliance (%)": "(Compliant processes / Total requests) * 100",
                "Customer satisfaction score": "Survey rating"
            },
            "Complaint Management": {
                "Average resolution time (days)": "Average days to resolve",
                "Resolution compliance (%)": "(Compliant resolution / Total complaints) * 100",
                "Repeat complaint rate (%)": "(Repeat complaints / Total complaints) * 100",
                "Customer satisfaction with complaint process": "Survey rating"
            }
        },

        # -------------------- 11. Innovation & Continuous Improvement --------------------
        "Innovation & Continuous Improvement": {
            "Process Reengineering": {
                "Processes redesigned (#)": "Number of redesigned processes",
                "Efficiency gain (%)": "(Previous cost/time - Current) / Previous * 100",
                "Error rate reduction (%)": "(Previous errors - Current errors) / Previous * 100",
                "Compliance adherence (%)": "(Compliant redesigned processes / Total redesigned) * 100"
            },
            "Automation & Robotics": {
                "Automated processes (#)": "Number of automated processes",
                "Error reduction (%)": "(Previous errors - Current errors) / Previous * 100",
                "Processing time reduction (%)": "(Previous time - Current time) / Previous * 100",
                "Operational cost reduction (%)": "(Previous cost - Current cost) / Previous * 100"
            },
            "Digital Transformation": {
                "Digital adoption rate (%)": "(Digital processes used / Total processes) * 100",
                "Customer digital satisfaction": "Survey rating",
                "Process efficiency improvement (%)": "(Previous time - Current time) / Previous * 100",
                "Innovation implementation rate (%)": "(Implemented innovations / Total planned) * 100"
            },
            "Knowledge Management & Training": {
                "Staff trained (#)": "Number of staff trained",
                "Process adherence improvement (%)": "(Post-training compliance - Pre-training compliance) / Pre * 100",
                "Training coverage (%)": "(Trained staff / Total staff) * 100",
                "Knowledge reuse rate (%)": "(Reused knowledge assets / Total assets) * 100"
            },
            "Continuous Improvement Initiatives": {
                "Improvement projects (#)": "Number of improvement initiatives",
                "Project success rate (%)": "(Successful projects / Total projects) * 100",
                "Efficiency gain (%)": "(Previous cost/time - Current) / Previous * 100",
                "Stakeholder satisfaction (%)": "Survey rating"
            }
        }
    },

    "Learning & Growth Perspective": {

        **GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE["Learning & Growth Perspective"],

    },
}
