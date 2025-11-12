from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE
from management_project.services.strategy_hierarchy.internal_process_perspective import (
    GENERIC_INTERNAL_PROCESS_PERSPECTIVE,
)
from management_project.services.strategy_hierarchy.learning_and_growth_perspective import (
    GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE,
)

HEALTH_PERSPECTIVE = {
    "Financial Perspective": {
        # ==================== HEALTHCARE  ====================
        # ---------------- Core Generic Financial Objectives ----------------
        **GENERIC_FINANCE_PERSPECTIVE["Financial Perspective"],

        # ==================== 1. Healthcare Revenue Growth & Funding ====================
        "Healthcare Revenue Growth & Funding": {
            "Expand Healthcare Funding Sources": {
                "Government health funding ($)": "Funding from national/state health departments",
                "Insurance reimbursement revenue ($)": "Revenue from insurance claims and reimbursements",
                "Grant funding for health programs ($)": "Funding from health-focused grants and donors",
                "Private pay patient revenue ($)": "Revenue from self-paying patients"
            },
            "Increase Patient Service Revenue": {
                "Outpatient visit revenue growth (%)": "(Current - Previous) / Previous * 100",
                "Inpatient bed revenue ($)": "Revenue from hospitalized patients",
                "Surgical procedure revenue ($)": "Income from surgical operations and procedures",
                "Diagnostic service revenue ($)": "Revenue from lab tests, imaging, and diagnostics"
            },
            "Diversify Specialized Service Lines": {
                "Specialty clinic revenue ($)": "Income from specialized medical services",
                "Telehealth service revenue ($)": "Revenue from virtual consultations and remote care",
                "Chronic disease management revenue ($)": "Income from long-term condition management",
                "Preventive care program revenue ($)": "Revenue from wellness and prevention services"
            },
            "Optimize Payer Mix & Reimbursement": {
                "Medicare/Medicaid reimbursement rate (%)": "Collection rate from government payers",
                "Private insurance collection rate (%)": "Collection rate from private insurers",
                "Bad debt ratio (%)": "(Uncollectible revenue / Total revenue) * 100",
                "Average reimbursement per case ($)": "Total reimbursements / Number of cases"
            },
            "Leverage Public-Private Partnerships": {
                "PPP health project ratio (%)": "(PPP-funded health projects / Total projects) * 100",
                "Corporate wellness partnership revenue ($)": "Income from corporate health programs",
                "Pharmaceutical research funding ($)": "Funding from drug trials and research partnerships",
                "Medical equipment partnership value ($)": "Value of equipment partnerships and leases"
            },
            "Enhance Grant & Research Funding": {
                "Medical research grant success rate (%)": "(Grants awarded / Grants applied) * 100",
                "Clinical trial revenue ($)": "Income from pharmaceutical and device trials",
                "Research publication ROI": "Impact and value from research outputs",
                "Grant utilization efficiency (%)": "(Funds utilized / Funds awarded) * 100"
            }
        },

        # ==================== 2. Healthcare Infrastructure & Asset Finance ====================
        "Healthcare Infrastructure & Asset Finance": {
            "Modernize Medical Facilities": {
                "Hospital modernization investment ($)": "Capital spent on facility upgrades",
                "Medical equipment upgrade ratio (%)": "(Upgraded equipment / Total equipment) * 100",
                "Digital infrastructure investment ($)": "Spending on IT and digital systems",
                "Facility expansion capacity (%)": "(Added capacity / Current capacity) * 100"
            },
            "Optimize Medical Asset Utilization": {
                "Medical equipment utilization rate (%)": "(Hours used / Available hours) * 100",
                "Operating room utilization (%)": "(OR hours used / Total OR hours) * 100",
                "Bed occupancy rate (%)": "(Occupied beds / Available beds) * 100",
                "Imaging equipment throughput (patients/day)": "Patients served per equipment unit"
            },
            "Enhance Healthcare Technology": {
                "EMR/EHR system ROI (%)": "(Benefits - Cost) / Cost * 100",
                "Telemedicine platform investment ($)": "Spending on remote care technology",
                "Medical device technology index": "Score of technology advancement in medical devices",
                "Digital health adoption rate (%)": "(Digital services used / Total services) * 100"
            },
            "Preventive Maintenance & Equipment Lifecycle": {
                "Medical equipment uptime (%)": "(Available hours / Total hours) * 100",
                "Preventive maintenance compliance (%)": "(Equipment maintained / Total equipment) * 100",
                "Equipment replacement cycle (years)": "Average lifespan of medical equipment",
                "Maintenance cost per asset ($)": "Total maintenance spend / Number of assets"
            },
            "Improve Facility Efficiency": {
                "Energy cost per bed ($)": "Total energy cost / Number of beds",
                "Space utilization efficiency (%)": "(Utilized space / Total space) * 100",
                "Patient flow optimization score": "Efficiency of patient movement through facilities",
                "Infrastructure cost per patient ($)": "Facility costs / Number of patients served"
            }
        },

        # ==================== 3. Healthcare Profitability & Return ====================
        "Healthcare Profitability & Return": {
            "Improve Overall Healthcare Margins": {
                "Net patient service margin (%)": "(Net patient revenue - Patient costs) / Revenue * 100",
                "Operating margin (%)": "(Operating income / Total revenue) * 100",
                "EBITDA margin (%)": "EBITDA / Total revenue * 100",
                "Contribution margin per service line (%)": "(Revenue - Variable costs) / Revenue * 100"
            },
            "Enhance Clinical Service Profitability": {
                "Surgical procedure profitability (%)": "(Procedure revenue - Costs) / Revenue * 100",
                "Outpatient visit profit margin (%)": "(Visit revenue - Costs) / Revenue * 100",
                "Diagnostic service ROI (%)": "(Revenue - Equipment cost) / Equipment cost * 100",
                "Specialty clinic break-even time (months)": "Time for new clinics to become profitable"
            },
            "Optimize Resource Utilization": {
                "Cost per patient day ($)": "Total costs / Patient days",
                "Physician productivity (RVUs/provider)": "Relative Value Units per healthcare provider",
                "Staffing cost efficiency (%)": "(Actual staffing cost / Budgeted) * 100",
                "Supply cost per procedure ($)": "Medical supplies cost / Number of procedures"
            },
            "Maximize Payer Contract Performance": {
                "Contractual allowance rate (%)": "(Contractual adjustments / Gross revenue) * 100",
                "Denial rate (%)": "(Claims denied / Claims submitted) * 100",
                "Collection rate (%)": "(Amount collected / Amount billed) * 100",
                "Days in accounts receivable": "Average days to collect payments"
            },
            "Improve Ancillary Service Returns": {
                "Pharmacy profit margin (%)": "(Pharmacy revenue - Costs) / Revenue * 100",
                "Laboratory service ROI (%)": "(Lab revenue - Equipment cost) / Equipment cost * 100",
                "Radiology department margin (%)": "(Radiology revenue - Costs) / Revenue * 100",
                "Rehabilitation service profitability (%)": "(Therapy revenue - Costs) / Revenue * 100"
            }
        },

        # ==================== 4. Healthcare Financial Risk Management ====================
        "Healthcare Financial Risk Management": {
            "Manage Clinical & Malpractice Risk": {
                "Malpractice insurance cost ($)": "Total professional liability insurance costs",
                "Claims settlement ratio (%)": "(Settled claims / Total claims) * 100",
                "Risk management program effectiveness": "Score of risk mitigation program success",
                "Patient safety incident cost ($)": "Financial impact of safety events"
            },
            "Mitigate Regulatory Compliance Risk": {
                "HIPAA compliance audit score (%)": "Results of privacy and security audits",
                "Medicare compliance rate (%)": "(Compliant billing / Total billing) * 100",
                "Accreditation maintenance cost ($)": "Cost to maintain regulatory certifications",
                "Regulatory penalty avoidance ($)": "Estimated savings from compliance"
            },
            "Address Healthcare Market Risks": {
                "Market share volatility (%)": "Variation in patient volume and market position",
                "Payer mix stability index": "Consistency of insurance payer distribution",
                "Competitive pricing pressure index": "Impact of competitor pricing on margins",
                "Service demand forecasting accuracy (%)": "(Actual demand / Forecasted demand) * 100"
            },
            "Manage Operational & Continuity Risks": {
                "Business interruption insurance coverage (%)": "(Covered risks / Total risks) * 100",
                "Disaster recovery readiness score": "Preparedness for emergency scenarios",
                "Supply chain disruption cost ($)": "Financial impact of medical supply shortages",
                "Staffing shortage impact ($)": "Cost of temporary staff and overtime"
            }
        },

        # ==================== 5. Healthcare Cost Efficiency ====================
        "Healthcare Cost Efficiency": {
            "Optimize Clinical Operations Costs": {
                "Cost per case ($)": "Total treatment cost / Number of cases",
                "Medication cost per patient ($)": "Drug costs / Number of patients",
                "Laboratory test cost efficiency (%)": "(Standard cost / Actual cost) * 100",
                "Surgical supply utilization rate (%)": "(Supplies used / Supplies opened) * 100"
            },
            "Reduce Administrative Overhead": {
                "Administrative cost ratio (%)": "(Admin costs / Total revenue) * 100",
                "Billing and coding cost per claim ($)": "Revenue cycle costs / Number of claims",
                "IT support cost per user ($)": "IT costs / Number of system users",
                "Facility overhead per square foot ($)": "Overhead costs / Total facility space"
            },
            "Improve Staffing Efficiency": {
                "Nursing hours per patient day": "Direct care hours / Patient days",
                "Physician to support staff ratio": "Number of physicians / Support staff",
                "Overtime cost percentage (%)": "(Overtime costs / Total labor costs) * 100",
                "Employee turnover cost ($)": "Recruitment and training costs for replacements"
            },
            "Enhance Supply Chain Management": {
                "Medical supply cost savings ($)": "Savings from group purchasing and negotiations",
                "Inventory turnover ratio": "Cost of goods sold / Average inventory",
                "Pharmaceutical waste reduction (%)": "(Reduced waste / Previous waste) * 100",
                "Group purchasing organization savings ($)": "Savings from collective purchasing"
            }
        },

        # ==================== 6. Long-term Healthcare Sustainability & Investment ====================
        "Long-term Healthcare Sustainability & Investment": {
            "Develop Strategic Service Lines": {
                "Specialty service investment ROI (%)": "(Revenue - Investment) / Investment * 100",
                "New service line adoption rate (%)": "(Successful new services / Total launched) * 100",
                "Center of excellence development cost ($)": "Investment in specialized care centers",
                "Market leadership position index": "Competitive ranking in key service areas"
            },
            "Invest in Healthcare Innovation": {
                "Digital health technology ROI (%)": "(Efficiency gains - Cost) / Cost * 100",
                "Telemedicine adoption ROI (%)": "(Revenue - Implementation cost) / Cost * 100",
                "Clinical research investment ($)": "Funding for medical research and trials",
                "Medical technology upgrade cycle (years)": "Average equipment refresh rate"
            },
            "Ensure Financial Sustainability": {
                "Days cash on hand": "Cash reserves / Average daily expenses",
                "Debt service coverage ratio": "Operating income / Debt payments",
                "Capital expenditure ratio (%)": "(Capital spending / Depreciation) * 100",
                "Reserve fund growth (%)": "(Current reserves - Previous) / Previous * 100"
            },
            "Build Community Health Partnerships": {
                "Community health program investment ($)": "Funding for public health initiatives",
                "Partnership revenue growth (%)": "(Current - Previous) / Previous * 100",
                "Population health management ROI (%)": "(Health outcomes value / Program cost) * 100",
                "Preventive care program impact ($)": "Reduction in acute care costs from prevention"
            }
        },

        # ==================== 7. Healthcare Quality & Value-Based Finance ====================
        "Healthcare Quality & Value-Based Finance": {
            "Optimize Value-Based Care Performance": {
                "Value-based payment revenue ($)": "Income from outcomes-based contracts",
                "Quality incentive earnings ($)": "Bonuses from quality performance programs",
                "Readmission reduction savings ($)": "Savings from reduced hospital readmissions",
                "Patient outcome-based reimbursement (%)": "(Outcome-linked payments / Total revenue) * 100"
            },
            "Enhance Patient Experience Economics": {
                "Patient satisfaction revenue impact ($)": "Revenue linked to patient experience scores",
                "HCAHPS performance incentives ($)": "Earnings from patient survey performance",
                "Retention rate revenue value ($)": "Revenue from patient loyalty and retention",
                "Reputation-driven referral revenue ($)": "Income from word-of-mouth referrals"
            },
            "Improve Clinical Quality Finance": {
                "Infection prevention savings ($)": "Cost avoidance from reduced healthcare infections",
                "Medication error cost reduction ($)": "Savings from improved medication safety",
                "Clinical pathway efficiency gains ($)": "Savings from standardized care protocols",
                "Complication rate cost impact ($)": "Financial impact of reduced complications"
            }
        },

        # ==================== 8. Health Economic Development ====================
        "Health Economic Development": {
            "Strengthen Community Health Economics": {
                "Local healthcare employment growth (%)": "Increase in healthcare jobs in the community",
                "Community health expenditure ($)": "Total spending on public health programs",
                "Local health investment projects (#)": "Number of funded community health initiatives",
                "Healthcare SME support funding ($)": "Funding for small healthcare enterprises"
            },
            "Promote Workforce Development": {
                "Healthcare training program graduates (#)": "Number of trained professionals completing programs",
                "Staff retention rate (%)": "(Retained staff / Total staff) * 100",
                "Professional development investment ($)": "Spending on staff skills and training",
                "Healthcare workforce productivity index": "Performance and efficiency measure for staff"
            },
            "Enhance Public Health Infrastructure": {
                "New community clinics (#)": "Number of clinics opened in underserved areas",
                "Health facility coverage (%)": "(Population served / Total population) * 100",
                "Medical equipment provision ($)": "Funds spent on community medical equipment",
                "Digital health access index": "Measure of population access to digital health services"
            },
            "Drive Health System Investment": {
                "Public-private partnership projects (#)": "Number of PPP health initiatives",
                "Health innovation grants ($)": "Funding for local health innovation projects",
                "Preventive care outreach programs (#)": "Number of programs delivered",
                "Population health ROI (%)": "(Health outcomes improvement / Investment) * 100"
            }
        },
    },

    " Customer Perspective": {

        # ---------------- GENERIC CUSTOMER PERSPECTIVE ----------------
        **GENERIC_CUSTOMER_PERSPECTIVE["Customer Perspective"],
        # =========================================================
        # Access to Care
        # =========================================================
        "Access to Care": {
            "Reduce waiting time for appointments": {
                "Average patient wait time (minutes)": "Sum(wait time) / Total patients",
                "Same-day appointment rate (%)": "(Same-day appointments / Total appointments) * 100",
                "Telehealth utilization rate (%)": "(Telehealth visits / Total visits) * 100",
                "Missed appointment rate (%)": "(No-shows / Total scheduled) * 100",
            },
            "Expand care access to rural and remote populations": {
                "Mobile clinic visits per month": "Total outreach visits / Month",
                "Coverage of primary care per 10,000 population": "(Primary care centers / Population) * 10,000",
                "Population within 5 km of facility (%)": "(Nearby residents / Total population) * 100",
                "Community health worker density": "Health workers / 10,000 population",
            },
            "Improve appointment scheduling efficiency": {
                "Online booking utilization (%)": "(Online bookings / Total bookings) * 100",
                "Average appointment confirmation time (hours)": "Sum(time to confirm) / Total bookings",
                "Scheduling accuracy (%)": "(On-time appointments / Total scheduled) * 100",
                "Cancellation rate (%)": "(Cancelled appointments / Total appointments) * 100",
            },
            "Enhance affordability of care": {
                "Average out-of-pocket cost (USD)": "Sum(patient out-of-pocket) / Total patients",
                "Price transparency tool usage (%)": "(Users of estimator / Total patients) * 100",
                "Insurance coverage rate (%)": "(Insured patients / Total patients) * 100",
                "Financial assistance utilization (%)": "(Patients receiving support / Total patients) * 100",
            },
            "Increase service availability hours": {
                "Extended hour coverage (%)": "(Evening & weekend slots / Total slots) * 100",
                "Early morning appointment rate (%)": "(Morning slots used / Total appointments) * 100",
                "Patient satisfaction with hours (%)": "(Positive responses / Total respondents) * 100",
                "Clinic open days per month": "Number of operational days per month",
            },
            "Improve emergency care access": {
                "Emergency response time (minutes)": "Average time to arrival",
                "Ambulance availability rate (%)": "(Available ambulances / Total fleet) * 100",
                "Emergency triage compliance (%)": "(Triage completed within 5 min / Total ER patients) * 100",
                "Emergency satisfaction score (1–5)": "Average survey score",
            },
        },

        # =========================================================
        # Communication and Education
        # =========================================================
        "Communication and Education": {
            "Enhance patient understanding": {
                "Teach-back success rate (%)": "(Patients correctly recalling info / Total educated) * 100",
                "Education session attendance (%)": "(Attended / Total invited) * 100",
                "Average health literacy score": "Sum(scores) / Total assessed",
                "Post-session comprehension gain (%)": "((Post-test - Pre-test)/Pre-test)*100",
            },
            "Improve care communication clarity": {
                "Patient clarity satisfaction (%)": "(Satisfied responses / Total responses) * 100",
                "Interpreter utilization rate (%)": "(Interpretations provided / Total LEP patients) * 100",
                "Miscommunication incidents per 1000 visits": "(Reported incidents / Total visits) * 1000",
                "Provider communication training completion (%)": "(Trained providers / Total providers) * 100",
            },
            "Promote shared decision-making": {
                "SDM tool usage (%)": "(Patients using decision aids / Total patients) * 100",
                "Informed consent accuracy (%)": "(Valid consents / Total procedures) * 100",
                "Patient satisfaction with SDM (%)": "(Satisfied participants / Total) * 100",
                "Treatment plan adherence (%)": "(Patients following plan / Total patients) * 100",
            },
            "Increase preventive health education": {
                "Health campaign reach (%)": "(People reached / Target population) * 100",
                "Community event frequency": "Number of educational events per quarter",
                "Preventive material distribution rate (%)": "(Distributed / Planned) * 100",
                "Knowledge improvement (%)": "((Post-score - Pre-score)/Pre-score)*100",
            },
            "Leverage digital health education tools": {
                "App engagement rate (%)": "(Active users / Total registered) * 100",
                "E-learning completion rate (%)": "(Completions / Enrolled users) * 100",
                "Average session duration (min)": "Total minutes / Total sessions",
                "Digital literacy improvement (%)": "((Post-score - Pre-score)/Pre-score)*100",
            },
            "Enhance feedback and dialogue systems": {
                "Response rate to patient queries (%)": "(Queries responded / Total queries) * 100",
                "Average feedback resolution time (hours)": "Sum(time to resolve)/Total feedback",
                "Patient suggestion adoption rate (%)": "(Adopted suggestions / Total suggestions) * 100",
                "Communication channel satisfaction (%)": "(Positive feedback / Total responses) * 100",
            },
        },

        # =========================================================
        # Safety and Quality of Care
        # =========================================================
        "Safety and Quality of Care": {
            "Reduce hospital-acquired infections": {
                "HAI rate (%)": "(HAI cases / Total admissions) * 100",
                "Hand hygiene compliance (%)": "(Compliant observations / Total) * 100",
                "Sterilization compliance rate (%)": "(Compliant processes / Total) * 100",
                "Infection audit frequency": "Number of audits per quarter",
            },
            "Prevent medication errors": {
                "Medication error rate (%)": "(Errors / Total prescriptions) * 100",
                "Pharmacist review rate (%)": "(Reviewed orders / Total) * 100",
                "Electronic prescribing adoption (%)": "(e-Rx / Total prescriptions) * 100",
                "Adverse drug events per 1000 patients": "(ADEs / Total patients) * 1000",
            },
            "Enhance clinical guideline compliance": {
                "Guideline adherence rate (%)": "(Cases following guideline / Total cases) * 100",
                "Checklist utilization (%)": "(Checklists used / Required) * 100",
                "Audit success rate (%)": "(Passed audits / Total) * 100",
                "Protocol update frequency": "Number of updates per year",
            },
            "Reduce readmissions": {
                "30-day readmission rate (%)": "(Readmitted / Total discharged) * 100",
                "Post-discharge follow-up (%)": "(Follow-ups within 72h / Total discharges) * 100",
                "Average readmission cost (USD)": "Total readmission cost / Cases",
                "Preventable readmission rate (%)": "(Preventable cases / Total readmissions) * 100",
            },
            "Strengthen reporting culture": {
                "Incident reporting rate (%)": "(Reports / Total staff) * 100",
                "Non-punitive report ratio (%)": "(Anonymous reports / Total) * 100",
                "Time to closure (days)": "Average days to close incident",
                "Action plan implementation rate (%)": "(Implemented actions / Total reports) * 100",
            },
            "Improve safety training coverage": {
                "Safety training completion (%)": "(Trained staff / Total staff) * 100",
                "Simulation drills per quarter": "Number of safety drills conducted",
                "Post-training competency gain (%)": "((Post-score - Pre-score)/Pre-score)*100",
                "Safety culture score (1–5)": "Average staff survey rating",
            },
        },

        # =========================================================
        # Respect and Patient-Centeredness
        # =========================================================
        "Respect and Patient-Centeredness": {
            "Promote dignity and respect in care": {
                "Respectful care rating (%)": "(Positive survey responses / Total responses) * 100",
                "Patient complaint rate (%)": "(Complaints / Total patients) * 100",
                "Resolution satisfaction (%)": "(Satisfied complainants / Total) * 100",
                "Rounding compliance (%)": "(Completed rounds / Planned rounds) * 100",
            },
            "Strengthen inclusion and cultural sensitivity": {
                "Cultural competency training (%)": "(Trained staff / Total staff) * 100",
                "Language assistance usage (%)": "(Interpretations / LEP patients) * 100",
                "Patient diversity satisfaction (%)": "(Satisfied minorities / Total minorities) * 100",
                "Equity compliance index (%)": "(Policies audited as inclusive / Total) * 100",
            },
            "Encourage family participation in care": {
                "Family-inclusive rounds (%)": "(Rounds with family / Total rounds) * 100",
                "Shared care plan completion (%)": "(Family co-signed plans / Total plans) * 100",
                "Family satisfaction score (1–5)": "Average rating",
                "Complaint rate from families (%)": "(Family complaints / Total families) * 100",
            },
            "Improve comfort and pain management": {
                "Pain control success (%)": "(Patients reporting relief / Total) * 100",
                "Comfort satisfaction (%)": "(Satisfied with comfort / Total) * 100",
                "Average comfort score (1–5)": "Sum(scores)/Total responses",
                "Response time to call bell (minutes)": "Average response time",
            },
            "Integrate patient preferences into care": {
                "Preference documentation rate (%)": "(Documented preferences / Total patients) * 100",
                "Personalized plan compliance (%)": "(Plans implemented / Total plans) * 100",
                "Value-aligned care (%)": "(Patients satisfied with alignment / Total) * 100",
                "Decision review frequency": "Number of reviews per quarter",
            },
            "Enhance empathy and emotional support": {
                "Empathy rating (%)": "(Empathetic responses / Total feedback) * 100",
                "Emotional support requests met (%)": "(Requests fulfilled / Total requests) * 100",
                "Patient stress reduction score (1–5)": "Average rating",
                "Staff empathy training completion (%)": "(Trained / Total) * 100",
            },
        },

        # =========================================================
        # Care Environment and Experience
        # =========================================================
        "Care Environment and Experience": {
            "Enhance facility cleanliness and hygiene": {
                "Cleanliness audit compliance (%)": "(Compliant areas / Total audited) * 100",
                "Patient cleanliness satisfaction (%)": "(Satisfied patients / Total patients) * 100",
                "Infection control incident rate (%)": "(Incidents / Total patients) * 100",
                "Sanitation staff coverage (%)": "(Trained staff / Total sanitation staff) * 100",
            },
            "Improve wayfinding and navigation": {
                "Patient navigation satisfaction (%)": "(Positive responses / Total responses) * 100",
                "Signage clarity score (1–5)": "Average rating",
                "Time to reach destination (minutes)": "Average travel time",
                "Volunteer greeter utilization (%)": "(Greeters active / Planned shifts) * 100",
            },
            "Promote healing environment design": {
                "Natural light coverage (%)": "(Areas with daylight / Total areas) * 100",
                "Noise reduction compliance (%)": "(Compliant areas / Total areas) * 100",
                "Patient comfort score (1–5)": "Average rating",
                "Healing environment audit frequency": "Number of audits per year",
            },
            "Streamline patient flow": {
                "Average patient throughput (minutes)": "Total time / Total patients",
                "RTLS utilization rate (%)": "(Tracked patients / Total patients) * 100",
                "Waiting area congestion (%)": "(Overcapacity time / Total hours) * 100",
                "Process cycle time reduction (%)": "((Baseline - Current)/Baseline)*100",
            },
            "Simplify billing and financial experience": {
                "Billing error rate (%)": "(Errors / Total bills) * 100",
                "Average billing resolution time (days)": "Sum(days to resolve) / Total errors",
                "Patient billing satisfaction (%)": "(Satisfied patients / Total respondents) * 100",
                "Financial counselor utilization (%)": "(Counseling sessions / Total patients needing) * 100",
            },
            "Optimize safety and accessibility": {
                "Accessibility compliance (%)": "(Compliant areas / Total areas) * 100",
                "Patient fall rate (%)": "(Falls / Total patients) * 100",
                "Emergency exit accessibility (%)": "(Accessible exits / Total exits) * 100",
                "Safety audit frequency": "Number of audits per quarter",
            },
        },
        # =========================================================
        # Clinical Outcomes
        # =========================================================
        "Clinical Outcomes": {
            "Reduce mortality rates": {
                "Overall hospital mortality rate (%)": "(Deaths / Total admissions) * 100",
                "ICU mortality rate (%)": "(Deaths in ICU / Total ICU admissions) * 100",
                "Surgical mortality rate (%)": "(Deaths post-surgery / Total surgeries) * 100",
                "Condition-specific mortality (%)": "(Deaths / Total patients with condition) * 100",
            },
            "Reduce morbidity and complications": {
                "Hospital-acquired complication rate (%)": "(Complications / Total admissions) * 100",
                "Surgical complication rate (%)": "(Complications / Total surgeries) * 100",
                "Readmission due to complications (%)": "(Readmissions / Total discharges) * 100",
                "Adverse event rate (%)": "(Adverse events / Total patients) * 100",
            },
            "Improve treatment effectiveness": {
                "Treatment success rate (%)": "(Successful outcomes / Total treated) * 100",
                "Disease remission rate (%)": "(Remitted / Total patients) * 100",
                "Therapy adherence (%)": "(Adherent patients / Total patients) * 100",
                "Clinical target achievement (%)": "(Patients meeting clinical targets / Total patients) * 100",
            },
            "Enhance patient safety": {
                "Medication safety compliance (%)": "(Compliant prescriptions / Total prescriptions) * 100",
                "Procedure safety compliance (%)": "(Compliant procedures / Total procedures) * 100",
                "Fall prevention compliance (%)": "(Implemented measures / Total required) * 100",
                "Safety incident rate (%)": "(Incidents / Total patients) * 100",
            },
            "Optimize chronic disease control": {
                "HbA1c control rate (%)": "(Patients <7% / Total diabetic patients) * 100",
                "BP control rate (%)": "(Patients <140/90 / Total hypertensive patients) * 100",
                "Cholesterol target achievement (%)": "(Patients meeting LDL targets / Total patients) * 100",
                "Hospitalization reduction rate (%)": "(Reduced admissions / Baseline) * 100",
            },
            "Improve surgical outcomes": {
                "Surgical site infection rate (%)": "(SSIs / Total surgeries) * 100",
                "Post-op complication rate (%)": "(Complications / Total surgeries) * 100",
                "Average post-op recovery time (days)": "Sum(days) / Total surgeries",
                "Patient post-op satisfaction (%)": "(Satisfied / Total surveyed) * 100",
            },
        },

        # =========================================================
        # Health Outcomes
        # =========================================================
        "Health Outcomes": {
            "Reduce mortality rates": {
                "Overall mortality rate (%)": "(Deaths / Total patients) * 100",
                "Infant mortality rate (%)": "(Infant deaths / Total live births) * 100",
                "Maternal mortality rate (%)": "(Maternal deaths / Total live births) * 100",
                "Disease-specific mortality (%)": "(Deaths from disease / Total patients with disease) * 100",
            },
            "Reduce morbidity and complications": {
                "Hospital-acquired infection rate (%)": "(Infections / Total patients) * 100",
                "Surgical complication rate (%)": "(Complications / Total surgeries) * 100",
                "Chronic disease complication rate (%)": "(Patients with complications / Total patients) * 100",
                "Readmission due to complications (%)": "(Readmissions / Total discharged) * 100",
            },
            "Improve functional health outcomes": {
                "Functional independence score improvement": "Average post-pre score",
                "Mobility gain (%)": "((Post - Pre)/Pre) * 100",
                "Activities of daily living (ADL) improvement (%)": "((Post - Pre)/Pre) * 100",
                "Rehabilitation success rate (%)": "(Patients meeting rehab goals / Total rehab patients) * 100",
            },
            "Enhance chronic disease control": {
                "Diabetes control (%)": "(Patients with HbA1c <7% / Total diabetic patients) * 100",
                "Hypertension control (%)": "(Patients with BP <140/90 / Total hypertensive patients) * 100",
                "Cholesterol management (%)": "(Patients meeting LDL targets / Total patients) * 100",
                "Hospitalization reduction (%)": "(Reduced admissions / Baseline) * 100",
            },
            "Increase life expectancy": {
                "Average life expectancy (years)": "Calculated from population data",
                "Healthy life expectancy (years)": "Average years without disability",
                "Reduction in premature deaths (%)": "(Avoidable deaths / Baseline) * 100",
                "Population survival rate (%)": "(Survivors / Total population) * 100",
            },
            "Improve patient-reported outcomes": {
                "PROM improvement (%)": "(Improved / Total patients) * 100",
                "Quality of life improvement (%)": "(Post-pre improvement / Pre) * 100",
                "Symptom reduction (%)": "(Patients with reduced symptoms / Total patients) * 100",
                "Patient satisfaction with outcomes (%)": "(Satisfied / Total surveyed) * 100",
            },
        },

        # =========================================================
        # Patient Safety
        # =========================================================
        "Patient Safety": {
            "Reduce medication errors": {
                "Medication error rate (%)": "(Errors / Total prescriptions) * 100",
                "Adverse drug event rate (%)": "(Events / Total patients) * 100",
                "High-risk medication monitoring compliance (%)": "(Compliant cases / Total high-risk cases) * 100",
                "Medication reconciliation rate (%)": "(Patients reconciled / Total patients) * 100",
            },
            "Enhance procedural safety": {
                "Surgical checklist compliance (%)": "(Compliant surgeries / Total surgeries) * 100",
                "Procedure-related complication rate (%)": "(Complications / Total procedures) * 100",
                "Safety audit compliance (%)": "(Compliant areas / Total audits) * 100",
                "Time-out procedure compliance (%)": "(Performed / Total surgeries) * 100",
            },
            "Prevent hospital-acquired infections": {
                "Hand hygiene compliance (%)": "(Compliant actions / Total required) * 100",
                "CLABSI rate (%)": "(Central line infections / Total line days) * 1000",
                "CAUTI rate (%)": "(Catheter infections / Total catheter days) * 1000",
                "SSI rate (%)": "(Surgical site infections / Total surgeries) * 100",
            },
            "Reduce patient falls": {
                "Fall rate (%)": "(Falls / Total patient days) * 1000",
                "Fall injury rate (%)": "(Injurious falls / Total falls) * 100",
                "Fall risk assessment completion (%)": "(Assessed / Total patients) * 100",
                "Fall prevention intervention coverage (%)": "(Patients with interventions / Total at-risk patients) * 100",
            },
            "Improve safety culture": {
                "Safety event reporting rate (%)": "(Events reported / Total incidents) * 100",
                "Staff safety training completion (%)": "(Trained staff / Total staff) * 100",
                "Near-miss reporting rate (%)": "(Near-misses reported / Total near-misses) * 100",
                "Patient safety perception score (1–5)": "Average survey score",
            },
            "Enhance emergency preparedness": {
                "Emergency drill completion (%)": "(Drills conducted / Planned drills) * 100",
                "Disaster readiness compliance (%)": "(Compliant facilities / Total facilities) * 100",
                "Staff emergency training coverage (%)": "(Trained staff / Total staff) * 100",
                "Response time to emergencies (minutes)": "Average response time",
            },
        },

        # =========================================================
        # Digital Access to Care
        # =========================================================
        "Digital Access to Care": {
            "Increase telehealth adoption": {
                "Telehealth visit rate (%)": "(Telehealth visits / Total visits) * 100",
                "Patient telehealth satisfaction (%)": "(Satisfied / Total surveyed) * 100",
                "Provider telehealth utilization (%)": "(Providers using / Total providers) * 100",
                "Telehealth system uptime (%)": "(Available hours / Total hours) * 100",
            },
            "Improve patient portal engagement": {
                "Patient portal registration (%)": "(Registered / Total patients) * 100",
                "Portal activity rate (%)": "(Active users / Registered users) * 100",
                "Secure messaging response rate (%)": "(Responded messages / Total messages) * 100",
                "Lab/test result viewing rate (%)": "(Viewed / Total results) * 100",
            },
            "Support remote patient monitoring": {
                "RPM enrollment (%)": "(Enrolled / Eligible patients) * 100",
                "RPM data transmission rate (%)": "(Sent data / Expected data) * 100",
                "Early intervention triggered (%)": "(Triggered / Total patients monitored) * 100",
                "RPM patient adherence (%)": "(Adherent patients / Total patients) * 100",
            },
            "Enhance digital health literacy": {
                "Digital platform training participation (%)": "(Trained patients / Total patients) * 100",
                "Digital literacy improvement (%)": "((Post-test - Pre-test)/Pre-test) * 100",
                "Support request resolution time (hours)": "Average hours to resolve patient queries",
                "Patient confidence in digital tools (%)": "(Confident patients / Total patients) * 100",
            },
            "Strengthen system interoperability": {
                "EHR integration rate (%)": "(Integrated systems / Total systems) * 100",
                "Data exchange success rate (%)": "(Successful transfers / Total transfers) * 100",
                "Clinical decision support usage (%)": "(CDS alerts used / Total alerts) * 100",
                "Interoperability issue resolution time (hours)": "Average hours to resolve",
            },
            "Boost patient engagement through digital apps": {
                "App active usage rate (%)": "(Active users / Total registered) * 100",
                "Digital program adherence (%)": "(Patients following program / Total enrolled) * 100",
                "Patient feedback response rate (%)": "(Responded feedback / Total feedback) * 100",
                "Digital intervention outcome improvement (%)": "((Post - Pre)/Pre) * 100",
            },
        },

        # =========================================================
        # Preventive Health
        # =========================================================
        "Preventive Health": {
            "Increase vaccination coverage": {
                "Immunization rate (%)": "(Vaccinated / Target population) * 100",
                "Booster dose coverage (%)": "(Boosters / Eligible population) * 100",
                "Vaccine-preventable disease incidence (%)": "(Cases / Population) * 100",
                "Vaccination campaign reach (%)": "(Reached / Target population) * 100",
            },
            "Promote health screenings": {
                "Screening coverage (%)": "(Screened / Target population) * 100",
                "Early detection rate (%)": "(Detected early / Total cases) * 100",
                "Follow-up completion (%)": "(Completed follow-up / Total positive screenings) * 100",
                "Screening adherence (%)": "(Patients adhering to schedule / Total eligible) * 100",
            },
            "Encourage lifestyle interventions": {
                "Healthy diet adherence (%)": "(Compliant / Total participants) * 100",
                "Physical activity adherence (%)": "(Compliant / Total participants) * 100",
                "Smoking cessation success (%)": "(Quit / Total participants) * 100",
                "Weight management success (%)": "(Achieved target / Total participants) * 100",
            },
            "Improve maternal and child health": {
                "Antenatal care coverage (%)": "(Women receiving ANC / Total pregnant women) * 100",
                "Skilled birth attendance (%)": "(Deliveries attended / Total births) * 100",
                "Postnatal care coverage (%)": "(Women receiving PNC / Total delivered) * 100",
                "Child growth monitoring (%)": "(Monitored children / Total children) * 100",
            },
            "Strengthen disease prevention programs": {
                "TB treatment coverage (%)": "(Covered / Total patients) * 100",
                "HIV prevention program coverage (%)": "(Covered / Target population) * 100",
                "Malaria control program coverage (%)": "(Covered / Target population) * 100",
                "NCD prevention program coverage (%)": "(Covered / Target population) * 100",
            },
            "Enhance health education and promotion": {
                "Health education reach (%)": "(Population reached / Target population) * 100",
                "Behavior change adoption (%)": "(Adopted healthy behavior / Total targeted) * 100",
                "Community engagement score (1–5)": "Average rating",
                "Awareness campaign effectiveness (%)": "(Respondents aware / Total reached) * 100",
            },
        },
    },

    "Internal Process Perspective": {

        **GENERIC_INTERNAL_PROCESS_PERSPECTIVE["Internal Process Perspective"],

        # -------------------- 1. Clinical Services --------------------
        "Clinical Services": {
            "Manage patient admission": {
                "Reduce registration errors": "(Errors / Total registrations) * 100",
                "Improve registration speed": "Average registration time (min)",
                "Ensure documentation completeness": "(Complete / Total admissions) * 100",
                "Strengthen compliance to admission protocols": "(Compliant / Total admissions) * 100"
            },
            "Optimize outpatient management": {
                "Improve consultation efficiency": "Average consultation duration (min)",
                "Ensure adherence to treatment plans": "(Implemented / Planned treatments) * 100",
                "Strengthen follow-up process": "(Follow-ups executed / Planned) * 100",
                "Enhance workflow compliance": "(Compliant / Total workflows) * 100"
            },
            "Manage inpatient processes": {
                "Optimize bed utilization": "(Occupied beds / Total beds) * 100",
                "Reduce readmission rates": "(Readmissions / Total discharges) * 100",
                "Ensure care plan adherence": "(Completed / Planned care plans) * 100",
                "Improve length of stay efficiency": "Average length of stay (days)"
            },
            "Strengthen emergency care": {
                "Reduce triage response time": "Time from arrival to triage",
                "Ensure stabilization protocol adherence": "(Compliant / Critical cases) * 100",
                "Improve emergency intervention compliance": "(Compliant interventions / Total interventions) * 100",
                "Enhance critical incident response": "Average response time (min)"
            },
            "Manage surgical services": {
                "Improve operating room utilization": "(Hours used / Available hours) * 100",
                "Strengthen surgical checklist compliance": "(Completed / Total surgeries) * 100",
                "Ensure post-operative care adherence": "(Compliant / Total surgeries) * 100",
                "Optimize surgery scheduling": "(On-time surgeries / Total scheduled) * 100"
            },
            "Optimize nursing services": {
                "Strengthen care plan adherence": "(Implemented / Planned care plans) * 100",
                "Improve medication administration compliance": "(Correct doses / Total doses) * 100",
                "Enhance shift handover accuracy": "(Accurate handovers / Total handovers) * 100",
                "Ensure staff skill competency": "(Competent / Total staff) * 100"
            },
            "Manage specialized services": {
                "Ensure clinical guideline compliance": "(Compliant / Total cases) * 100",
                "Optimize referral management": "(Completed referrals / Planned referrals) * 100",
                "Enhance multidisciplinary coordination": "(Coordinated / Total complex cases) * 100",
                "Strengthen procedure execution": "(Compliant procedures / Total procedures) * 100"
            },
            "Manage maternal and child health": {
                "Improve antenatal protocol adherence": "(Completed / Planned) * 100",
                "Ensure safe delivery compliance": "(Compliant / Total deliveries) * 100",
                "Strengthen postnatal care processes": "(Completed / Planned) * 100",
                "Manage maternal and neonatal risks": "(Risks identified and managed / Total risks) * 100"
            },
            "Strengthen rehabilitation services": {
                "Improve treatment plan adherence": "(Completed sessions / Prescribed sessions) * 100",
                "Optimize therapy equipment use": "(Used / Available hours) * 100",
                "Enhance functional improvement measurement": "Patient functional improvement",
                "Ensure therapy schedule compliance": "(On-time sessions / Total planned) * 100"
            },
            "Manage chronic disease operations": {
                "Strengthen monitoring adherence": "(Compliant monitoring / Total patients) * 100",
                "Ensure medication review compliance": "(Completed reviews / Total patients) * 100",
                "Implement intervention plans": "(Implemented / Planned) * 100",
                "Improve clinical outcomes": "Composite clinical improvement score"
            },
            "Manage pain and palliative care": {
                "Improve pain assessment adherence": "(Completed assessments / Total patients) * 100",
                "Strengthen analgesic protocol compliance": "(Compliant dosing / Total doses) * 100",
                "Ensure symptom monitoring": "(Monitored / Total patients) * 100",
                "Optimize care coordination": "(Coordinated interventions / Planned interventions) * 100"
            },
            "Strengthen infection prevention": {
                "Improve hand hygiene compliance": "(Compliant actions / Total opportunities) * 100",
                "Ensure isolation protocol adherence": "(Compliant / Required cases) * 100",
                "Strengthen sterilization processes": "(Compliant / Required procedures) * 100",
                "Manage outbreak response": "(Responded / Detected events) * 100"
            },
            "Optimize discharge processes": {
                "Improve documentation completeness": "(Completed / Total discharges) * 100",
                "Strengthen follow-up process": "(Completed / Planned) * 100",
                "Implement readmission prevention measures": "(Implemented / Planned) * 100",
                "Enhance continuity of care": "(Coordinated cases / Total discharges) * 100"
            },
            "Manage clinical records": {
                "Ensure record completeness": "(Completed / Required) * 100",
                "Improve timeliness of documentation": "(On-time / Total records) * 100",
                "Strengthen data accuracy": "(Error-free / Total records) * 100",
                "Ensure audit compliance": "Internal audit evaluation"
            },
            "Strengthen patient safety": {
                "Manage adverse events": "(Reported / Expected) * 100",
                "Ensure safety protocol adherence": "(Compliant / Required cases) * 100",
                "Reduce medication errors": "(Errors prevented / Total doses) * 100",
                "Enhance staff safety training": "(Trained / Total staff) * 100"
            },
            "Enhance clinical audit": {
                "Complete audits on schedule": "(Completed / Planned audits) * 100",
                "Ensure guideline adherence": "(Compliant / Total cases) * 100",
                "Implement process improvements": "(Implemented / Planned) * 100",
                "Strengthen outcome improvement": "Measured improvement after interventions"
            },
            "Optimize resource utilization": {
                "Improve bed turnover efficiency": "Discharges / Average bed count",
                "Strengthen staff allocation": "(Worked hours / Scheduled hours) * 100",
                "Enhance equipment utilization": "(Used / Available hours) * 100",
                "Optimize consumable costs": "Actual cost / Standard cost per patient"
            },
            "Strengthen interdisciplinary coordination": {
                "Conduct multidisciplinary meetings": "(Held / Planned meetings) * 100",
                "Integrate care plans": "(Integrated / Total complex cases) * 100",
                "Follow-up on referrals": "(Completed / Total referrals) * 100",
                "Enhance clinical outcomes": "Composite score"
            }
        },

        # -------------------- 2. Diagnostic & Support Services --------------------
        "Diagnostic & Support Services": {
            "Manage laboratory operations": {
                "Improve test accuracy": "(Correct tests / Total tests) * 100",
                "Strengthen turnaround time": "Average hours from sample to result",
                "Ensure equipment calibration": "(Calibrated / Required) * 100",
                "Enhance process adherence": "(Compliant procedures / Total procedures) * 100"
            },
            "Optimize radiology services": {
                "Strengthen image quality": "(Compliant / Total images) * 100",
                "Improve report turnaround": "Average hours from scan to report",
                "Reduce repeat scans": "(Reduced repeats / Total scans) * 100",
                "Ensure workflow adherence": "(Compliant / Total workflows) * 100"
            },
            "Manage pharmacy operations": {
                "Strengthen dispensing accuracy": "(Correct doses / Total prescriptions) * 100",
                "Ensure inventory process compliance": "(Compliant / Total inventory actions) * 100",
                "Improve stock management": "(Managed / Total critical items) * 100",
                "Enhance medication review": "(Reviewed / Total patients) * 100"
            },
            "Manage blood bank": {
                "Ensure blood availability": "(Available / Required units) * 100",
                "Strengthen cross-match accuracy": "(Accurate / Total requests) * 100",
                "Improve transfusion protocol compliance": "(Compliant / Total transfusions) * 100",
                "Reduce emergency transfusion response time": "Average time in min"
            },
            "Strengthen infection prevention support": {
                "Enhance sterilization adherence": "(Compliant / Required procedures) * 100",
                "Improve hand hygiene compliance": "(Compliant actions / Total opportunities) * 100",
                "Ensure IPC protocol implementation": "(Implemented / Planned actions) * 100",
                "Strengthen outbreak response": "(Executed / Detected outbreaks) * 100"
            },
            "Optimize medical equipment management": {
                "Improve equipment uptime": "(Operational / Total hours) * 100",
                "Strengthen preventive maintenance": "(Completed / Planned) * 100",
                "Reduce breakdown incidents": "(Reduced incidents / Previous period) * 100",
                "Enhance utilization efficiency": "(Used / Available hours) * 100"
            },
            "Manage supply chain": {
                "Ensure inventory accuracy": "(Accurate / Total items) * 100",
                "Strengthen procurement compliance": "(On-time / Total procurements) * 100",
                "Optimize stock replenishment": "(Replenished / Required items) * 100",
                "Control cost variance": "(Actual - Budget) / Budget * 100"
            },
            "Enhance diagnostic reporting": {
                "Improve report accuracy": "(Error-free / Total reports) * 100",
                "Strengthen reporting timeliness": "(On-time / Total reports) * 100",
                "Ensure process compliance": "(Compliant / Total steps) * 100",
                "Optimize clinician access to data": "(Accessed / Required) * 100"
            },
            "Strengthen workflow standardization": {
                "Ensure SOP adherence": "(Compliant / Total steps) * 100",
                "Implement process optimization": "(Implemented / Planned) * 100",
                "Reduce errors": "(Reduced errors / Previous period) * 100",
                "Ensure audit compliance": "(Compliant / Total checks) * 100"
            },
            "Optimize test scheduling": {
                "Improve scheduling adherence": "(Scheduled / Planned) * 100",
                "Prioritize critical tests": "(Processed on time / High-priority) * 100",
                "Ensure sample handling compliance": "(Compliant / Total samples) * 100",
                "Strengthen turnaround efficiency": "Improvement % vs previous period"
            },
            "Manage clinical support coordination": {
                "Ensure request fulfillment": "(Completed / Total requests) * 100",
                "Strengthen response time": "Average hours",
                "Enhance process adherence": "(Compliant / Total processes) * 100",
                "Optimize workflow integration": "(Integrated / Total required processes) * 100"
            },
            "Strengthen quality assurance": {
                "Ensure internal QC compliance": "(Passed QC / Total tests) * 100",
                "Strengthen proficiency testing": "External lab rating",
                "Reduce error trends": "(Reduction / Previous period) * 100",
                "Implement corrective actions": "(Implemented / Required) * 100"
            },
            "Optimize laboratory throughput": {
                "Improve throughput rate": "(Processed / Capacity) * 100",
                "Enhance turnaround efficiency": "Improvement vs baseline",
                "Strengthen equipment utilization": "(Used / Available hours) * 100",
                "Balance staff workload": "(Balanced shifts / Total shifts) * 100"
            },
            "Enhance consumable management": {
                "Ensure reagent accuracy": "(Accurate / Total items) * 100",
                "Strengthen procurement compliance": "(Compliant / Total procurements) * 100",
                "Reduce expiry losses": "(Monitored / Total reagents) * 100",
                "Minimize waste": "(Reduced / Baseline period) * 100"
            },
            "Manage staff competency": {
                "Strengthen staff training": "(Trained / Total staff) * 100",
                "Enhance protocol knowledge": "(Compliant / Total steps) * 100",
                "Ensure continuing education participation": "(Participated / Required staff) * 100",
                "Optimize audit performance": "Internal audit compliance"
            },
            "Strengthen interdepartmental support": {
                "Ensure request completion": "(Completed / Total requests) * 100",
                "Optimize response time": "Average time",
                "Enhance communication compliance": "(Compliant / Total required communications) * 100",
                "Integrate processes": "Internal operational integration index"
            },
            "Implement corrective processes": {
                "Identify issues promptly": "(Identified / Expected issues) * 100",
                "Complete action plans": "(Completed / Planned) * 100",
                "Apply process improvements": "(Implemented / Planned improvements) * 100",
                "Verify follow-up": "(Verified / Total actions) * 100"
            },
            "Optimize resource allocation": {
                "Ensure staff allocation": "(Allocated / Required staff) * 100",
                "Enhance equipment utilization": "(Optimized / Available) * 100",
                "Improve consumable efficiency": "(Used efficiently / Total used) * 100",
                "Reduce process cycle time": "(Reduced vs baseline) * 100"
            }
        },

        # -------------------- 3. Public Health Services --------------------
        "Public Health Services": {
            "Manage disease surveillance": {
                "Strengthen case detection": "(Detected cases / Expected cases) * 100",
                "Improve data reporting": "(Reported / Total cases) * 100",
                "Optimize data analysis": "(Completed analyses / Total datasets) * 100",
                "Ensure timely alert dissemination": "(Alerts sent / Planned alerts) * 100"
            },
            "Strengthen epidemiological investigations": {
                "Ensure protocol adherence": "(Compliant / Total investigations) * 100",
                "Improve outbreak response time": "Average hours to respond",
                "Manage data quality": "(Accurate / Total entries) * 100",
                "Enhance field coordination": "(Coordinated / Total investigations) * 100"
            },
            "Manage immunization programs": {
                "Ensure vaccine stock management": "(Available / Required doses) * 100",
                "Strengthen cold chain processes": "(Compliant / Total units) * 100",
                "Optimize vaccination scheduling": "(On-time / Planned sessions) * 100",
                "Enhance data recording accuracy": "(Accurate / Total records) * 100"
            },
            "Strengthen preventive health programs": {
                "Implement health promotion activities": "(Implemented / Planned) * 100",
                "Manage risk factor monitoring": "(Monitored / Planned) * 100",
                "Enhance intervention adherence": "(Implemented / Planned) * 100",
                "Optimize program reporting": "(Completed / Planned reports) * 100"
            },
            "Manage environmental health operations": {
                "Ensure inspection compliance": "(Compliant / Planned inspections) * 100",
                "Strengthen hazard mitigation": "(Mitigated / Identified hazards) * 100",
                "Manage waste regulation adherence": "(Compliant / Required actions) * 100",
                "Optimize follow-up inspections": "(Completed / Planned follow-ups) * 100"
            },
            "Strengthen occupational health management": {
                "Ensure workplace hazard assessments": "(Assessed / Required) * 100",
                "Manage risk controls": "(Implemented / Required) * 100",
                "Enhance staff safety adherence": "(Compliant / Total staff) * 100",
                "Optimize incident response": "(Responded / Total incidents) * 100"
            },
            "Manage nutrition and food safety": {
                "Strengthen inspection compliance": "(Compliant / Planned inspections) * 100",
                "Ensure food quality testing": "(Tested / Required samples) * 100",
                "Optimize reporting processes": "(Completed / Planned reports) * 100",
                "Enhance corrective action implementation": "(Implemented / Required actions) * 100"
            },
            "Strengthen disaster and emergency preparedness": {
                "Manage emergency plans": "(Developed / Required plans) * 100",
                "Conduct drills": "(Completed / Planned drills) * 100",
                "Ensure equipment readiness": "(Ready / Required equipment) * 100",
                "Optimize staff readiness": "(Trained / Required staff) * 100"
            },
            "Manage vector control programs": {
                "Ensure intervention adherence": "(Implemented / Planned interventions) * 100",
                "Strengthen data collection": "(Collected / Planned datasets) * 100",
                "Optimize resource deployment": "(Allocated / Planned resources) * 100",
                "Enhance response coordination": "(Coordinated / Required responses) * 100"
            },
            "Manage health risk assessments": {
                "Conduct routine assessments": "(Completed / Planned) * 100",
                "Ensure mitigation plan execution": "(Implemented / Planned actions) * 100",
                "Optimize reporting accuracy": "(Accurate / Total reports) * 100",
                "Strengthen stakeholder communication": "(Communicated / Required stakeholders) * 100"
            },
            "Strengthen occupational health surveillance": {
                "Manage hazard reporting": "(Reported / Total expected) * 100",
                "Ensure protocol compliance": "(Compliant / Required cases) * 100",
                "Optimize intervention execution": "(Implemented / Planned interventions) * 100",
                "Enhance follow-up adherence": "(Followed-up / Required cases) * 100"
            },
            "Manage community health interventions": {
                "Strengthen program implementation": "(Implemented / Planned programs) * 100",
                "Ensure process compliance": "(Compliant / Total steps) * 100",
                "Optimize coordination": "(Coordinated / Required teams) * 100",
                "Enhance monitoring": "(Monitored / Planned activities) * 100"
            },
            "Strengthen disease prevention campaigns": {
                "Manage campaign planning": "(Completed / Planned campaigns) * 100",
                "Ensure execution adherence": "(Implemented / Planned actions) * 100",
                "Optimize outcome measurement": "(Measured / Planned metrics) * 100",
                "Enhance reporting efficiency": "(Reported / Planned) * 100"
            },
            "Manage health education programs": {
                "Strengthen material development": "(Developed / Planned materials) * 100",
                "Ensure delivery compliance": "(Delivered / Planned sessions) * 100",
                "Optimize participant engagement": "(Engaged / Expected participants) * 100",
                "Enhance feedback incorporation": "(Incorporated / Total feedback) * 100"
            },
            "Strengthen surveillance data management": {
                "Ensure timely data entry": "(Entered / Expected datasets) * 100",
                "Improve data validation": "(Validated / Total datasets) * 100",
                "Enhance reporting timeliness": "(Reported / Required) * 100",
                "Optimize analysis utilization": "(Used / Required reports) * 100"
            },
            "Manage vaccination cold chain": {
                "Ensure temperature monitoring": "(Monitored / Total units) * 100",
                "Strengthen protocol compliance": "(Compliant / Total checks) * 100",
                "Optimize maintenance schedules": "(Maintained / Planned units) * 100",
                "Enhance corrective action execution": "(Implemented / Planned) * 100"
            },
            "Strengthen outbreak investigation processes": {
                "Manage investigation initiation": "(Initiated / Required) * 100",
                "Ensure procedure adherence": "(Compliant / Total cases) * 100",
                "Optimize resource allocation": "(Allocated / Planned) * 100",
                "Enhance reporting accuracy": "(Accurate / Total reports) * 100"
            },
            "Manage preventive intervention monitoring": {
                "Strengthen implementation tracking": "(Tracked / Planned interventions) * 100",
                "Ensure compliance with SOPs": "(Compliant / Total steps) * 100",
                "Optimize performance measurement": "(Measured / Planned) * 100",
                "Enhance corrective actions": "(Implemented / Required) * 100"
            }
        },

        # -------------------- 4. Infrastructure & Facility Management --------------------
        "Infrastructure & Facility Management": {
            "Manage facility maintenance": {
                "Strengthen preventive maintenance": "(Completed / Planned tasks) * 100",
                "Ensure equipment operational readiness": "(Operational / Total equipment) * 100",
                "Optimize maintenance scheduling": "(On-time / Planned) * 100",
                "Reduce breakdown incidents": "(Reduced / Previous period) * 100"
            },
            "Ensure biomedical equipment functionality": {
                "Optimize utilization": "(Used / Available hours) * 100",
                "Strengthen calibration compliance": "(Calibrated / Required) * 100",
                "Manage equipment repairs": "(Completed / Reported) * 100",
                "Enhance monitoring adherence": "(Monitored / Required) * 100"
            },
            "Manage medical waste processes": {
                "Strengthen segregation adherence": "(Compliant / Total waste streams) * 100",
                "Ensure safe disposal": "(Disposed / Required) * 100",
                "Optimize handling procedures": "(Compliant / Planned steps) * 100",
                "Enhance regulatory compliance": "(Compliant / Required audits) * 100"
            },
            "Optimize utility systems": {
                "Strengthen monitoring": "(Monitored / Required systems) * 100",
                "Ensure uninterrupted supply": "(Operational hours / Total hours) * 100",
                "Manage emergency response": "(Responded / Planned incidents) * 100",
                "Enhance efficiency": "Energy efficiency index"
            },
            "Manage transport services": {
                "Strengthen ambulance readiness": "(Ready / Total ambulances) * 100",
                "Ensure route adherence": "(Compliant / Planned trips) * 100",
                "Optimize dispatch efficiency": "(Dispatched / Requested trips) * 100",
                "Enhance vehicle maintenance": "(Maintained / Planned vehicles) * 100"
            },
            "Ensure safety and security": {
                "Strengthen access control": "(Compliant / Required points) * 100",
                "Manage incident response": "(Responded / Total incidents) * 100",
                "Enhance staff training": "(Trained / Required staff) * 100",
                "Optimize risk mitigation": "(Mitigated / Identified risks) * 100"
            },
            "Optimize facility planning": {
                "Manage space allocation": "(Allocated / Planned areas) * 100",
                "Strengthen utilization": "(Used / Available) * 100",
                "Ensure workflow efficiency": "(Efficient / Total areas) * 100",
                "Enhance infrastructure upgrades": "(Upgraded / Planned projects) * 100"
            },
            "Strengthen preventive safety processes": {
                "Ensure fire safety compliance": "(Compliant / Required areas) * 100",
                "Manage emergency drills": "(Conducted / Planned) * 100",
                "Optimize hazard mitigation": "(Mitigated / Identified hazards) * 100",
                "Enhance safety inspections": "(Inspected / Planned areas) * 100"
            },
            "Enhance energy & utilities management": {
                "Monitor energy usage": "kWh per month",
                "Optimize water consumption": "Liters per patient/day",
                "Strengthen utility fault response": "(Responded / Detected faults) * 100",
                "Ensure sustainable operations": "(Implemented / Planned sustainability actions) * 100"
            },
            "Manage facility audit processes": {
                "Strengthen audit compliance": "(Compliant / Planned audits) * 100",
                "Ensure corrective action implementation": "(Implemented / Planned) * 100",
                "Optimize reporting": "(Completed / Planned reports) * 100",
                "Enhance risk identification": "(Identified / Expected risks) * 100"
            },
            "Optimize construction & renovation management": {
                "Ensure project completion": "(Completed / Planned projects) * 100",
                "Strengthen contractor compliance": "(Compliant / Total contractors) * 100",
                "Manage timeline adherence": "(On-time / Total projects) * 100",
                "Enhance budget control": "(Actual / Planned budget) * 100"
            },
            "Strengthen facility lifecycle management": {
                "Manage asset inventory": "(Recorded / Total assets) * 100",
                "Ensure maintenance scheduling": "(Completed / Planned) * 100",
                "Optimize asset replacement": "(Replaced / Planned) * 100",
                "Enhance lifecycle tracking": "(Tracked / Total assets) * 100"
            }
        },

        # -------------------- 5. Health Information & Digital Systems --------------------
        "Health Information & Digital Systems": {
            "Manage EMR/EHR processes": {
                "Strengthen documentation completeness": "(Complete / Total records) * 100",
                "Ensure timeliness of entries": "(On-time / Total records) * 100",
                "Enhance data accuracy": "(Error-free / Total records) * 100",
                "Optimize user compliance": "(Compliant / Total users) * 100"
            },
            "Optimize telehealth services": {
                "Manage consultation workflow": "(Completed / Scheduled) * 100",
                "Strengthen data entry adherence": "(Compliant / Total sessions) * 100",
                "Enhance scheduling efficiency": "(On-time / Total appointments) * 100",
                "Ensure reporting accuracy": "(Accurate / Total reports) * 100"
            },
            "Manage data analytics processes": {
                "Strengthen data extraction": "(Extracted / Planned datasets) * 100",
                "Ensure data cleaning adherence": "(Compliant / Total datasets) * 100",
                "Optimize report generation": "(Completed / Planned reports) * 100",
                "Enhance decision support": "(Used / Required reports) * 100"
            },
            "Ensure HIS system change management": {
                "Manage update requests": "(Processed / Total requests) * 100",
                "Strengthen testing compliance": "(Tested / Planned updates) * 100",
                "Optimize deployment efficiency": "(Deployed / Planned updates) * 100",
                "Enhance user training": "(Trained / Required users) * 100"
            },
            "Manage cybersecurity processes": {
                "Strengthen access control": "(Compliant / Required points) * 100",
                "Monitor system threats": "(Detected / Expected threats) * 100",
                "Ensure incident response": "(Responded / Total incidents) * 100",
                "Optimize security compliance": "(Compliant / Total audits) * 100"
            },
            "Optimize interoperability": {
                "Ensure system integration": "(Integrated / Planned systems) * 100",
                "Strengthen data exchange compliance": "(Compliant / Total transactions) * 100",
                "Manage interface errors": "(Resolved / Total errors) * 100",
                "Enhance operational efficiency": "(Improvement / Baseline)"
            },
            "Manage digital training & support": {
                "Strengthen staff training": "(Trained / Total staff) * 100",
                "Ensure helpdesk response": "(Resolved / Total tickets) * 100",
                "Optimize knowledgebase usage": "(Accessed / Total staff) * 100",
                "Enhance system adoption": "(Adopted / Total users) * 100"
            },
            "Enhance data quality management": {
                "Manage data validation": "(Validated / Total datasets) * 100",
                "Strengthen correction processes": "(Corrected / Detected errors) * 100",
                "Ensure audit compliance": "(Compliant / Total checks) * 100",
                "Optimize reporting accuracy": "(Accurate / Total reports) * 100"
            },
            "Optimize health IT infrastructure": {
                "Ensure uptime": "(Operational hours / Total hours) * 100",
                "Strengthen maintenance processes": "(Completed / Planned maintenance) * 100",
                "Manage resource allocation": "(Allocated / Planned) * 100",
                "Enhance scalability": "(Implemented / Planned upgrades) * 100"
            },
            "Strengthen decision support systems": {
                "Optimize dashboard updates": "(Updated / Planned) * 100",
                "Ensure data accuracy": "(Accurate / Total reports) * 100",
                "Manage alerts and notifications": "(Resolved / Total alerts) * 100",
                "Enhance analytical outputs": "(Used / Total outputs) * 100"
            },
            "Manage digital compliance": {
                "Ensure policy adherence": "(Compliant / Total checks) * 100",
                "Strengthen audit processes": "(Completed / Planned audits) * 100",
                "Optimize documentation": "(Accurate / Total records) * 100",
                "Enhance corrective actions": "(Implemented / Required) * 100"
            },
            "Optimize digital workflow": {
                "Strengthen process standardization": "(Compliant / Total workflows) * 100",
                "Ensure system efficiency": "(Efficient / Total steps) * 100",
                "Manage bottleneck resolution": "(Resolved / Total detected) * 100",
                "Enhance workflow compliance": "(Compliant / Total steps) * 100"
            }
        },
    },

    "Learning & Growth Perspective": {
        **GENERIC_LEARNING_AND_GROWTH_PERSPECTIVE["Learning & Growth Perspective"],
    },

}
