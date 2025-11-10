from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE
from management_project.services.strategy_hierarchy.customer_perspective import GENERIC_CUSTOMER_PERSPECTIVE

EDUCATION_PERSPECTIVE = {
    "Financial Perspective": {
        **GENERIC_FINANCE_PERSPECTIVE['Financial Perspective'],
        # ==================== 1. EDUCATION REVENUE GROWTH & DIVERSIFICATION ====================
        "Education Revenue Growth & Diversification": {
            "Increase Tuition and Fee Income": {
                "Tuition revenue growth (%)": "(Current tuition - Previous) / Previous * 100",
                "Student fee collection rate (%)": "(Fees collected / Fees billed) * 100",
                "Average revenue per student ($)": "Total tuition revenue / Total enrolled students",
                "New program enrollment revenue ($)": "Revenue from new degree or certificate programs"
            },
            "Diversify Funding Sources": {
                "Non-tuition revenue share (%)": "(Non-tuition income / Total revenue) * 100",
                "Grant funding ratio (%)": "(Grant revenue / Total revenue) * 100",
                "Industry partnership revenue ($)": "Revenue from corporate partnerships",
                "Philanthropic donations ($)": "Value of external contributions and endowments"
            },
            "Expand Research Funding": {
                "Research grants secured ($)": "Total research grant funding received",
                "Grant success rate (%)": "(Grants won / Grants applied) * 100",
                "External research funding growth (%)": "(Current - Previous) / Previous * 100",
                "Research income per faculty ($)": "Total research revenue / Total academic staff"
            },
            "Enhance International Student Revenue": {
                "International tuition share (%)": "(International student revenue / Total tuition) * 100",
                "International enrollment growth (%)": "(Current - Previous) / Previous * 100",
                "Revenue per international student ($)": "Total international revenue / Total international students",
                "Scholarship to revenue ratio (%)": "(Scholarship value / International tuition revenue) * 100"
            },
            "Increase Continuing Education Income": {
                "Short-course revenue growth (%)": "(Current - Previous) / Previous * 100",
                "Corporate training income ($)": "Revenue from professional/industry training programs",
                "Online learning revenue share (%)": "(Online program revenue / Total revenue) * 100",
                "Adult learner participation rate (%)": "(Adult learners / Total enrollment) * 100"
            },
            "Promote Innovation & Commercialization": {
                "Patents licensed (#)": "Number of university patents licensed to industry",
                "Commercialization revenue ($)": "Income from spin-offs and IP commercialization",
                "Innovation partnership income ($)": "Revenue from joint R&D and technology transfer",
                "Return on innovation investment (%)": "(Innovation income / Investment) * 100"
            },
            "Grow Alumni Contributions": {
                "Alumni donation growth (%)": "(Current donations - Previous) / Previous * 100",
                "Active alumni donors (%)": "(Donating alumni / Total alumni) * 100",
                "Endowment fund growth (%)": "(Current endowment - Previous) / Previous * 100",
                "Average gift size ($)": "Total donations / Number of donors"
            },
            "Enhance Revenue from Campus Assets": {
                "Facility rental income ($)": "Revenue from leasing or renting campus spaces",
                "Accommodation occupancy rate (%)": "(Occupied student beds / Total beds) * 100",
                "Cafeteria and bookstore profit margin (%)": "(Net profit / Revenue) * 100",
                "Event and conference revenue ($)": "Income from hosting external events"
            }
        },

        # ==================== 3. EDUCATION PROFITABILITY & RETURN ====================
        "Education Profitability & Return": {
            "Improve Overall Profit Margin": {
                "Net profit margin (%)": "(Net income / Total revenue) * 100",
                "Gross margin (%)": "(Revenue - Direct costs) / Revenue * 100",
                "EBITDA margin (%)": "(EBITDA / Revenue) * 100",
                "Operating profit growth (%)": "(Current - Previous) / Previous * 100"
            },
            "Enhance Program Profitability": {
                "Program ROI (%)": "(Program revenue - Cost) / Cost * 100",
                "Cost per enrolled student ($)": "Program cost / Students enrolled",
                "Program profit margin (%)": "(Net profit / Program revenue) * 100",
                "Break-even enrollment (#)": "Fixed costs / (Tuition - Variable cost per student)"
            },
            "Increase Research Profitability": {
                "Research project ROI (%)": "(Research income - Cost) / Cost * 100",
                "Overhead recovery rate (%)": "(Indirect cost recovered / Total research cost) * 100",
                "Research income growth (%)": "(Current - Previous) / Previous * 100",
                "Research cost efficiency (%)": "(Research output value / Research spending) * 100"
            },
            "Improve Auxiliary Services Profitability": {
                "Cafeteria profit margin (%)": "(Profit / Sales) * 100",
                "Accommodation profit per bed ($)": "Accommodation profit / Total beds",
                "Event service profit margin (%)": "(Profit / Revenue) * 100",
                "Bookstore ROI (%)": "(Bookstore income - Cost) / Cost * 100"
            },
            "Enhance Cost Recovery in Subsidized Programs": {
                "Subsidy recovery ratio (%)": "(Revenue / Total cost) * 100",
                "Scholarship efficiency index": "Proportion of funded students with completion success",
                "Fee waiver impact (%)": "(Waived revenue / Total tuition) * 100",
                "Funding leverage ratio": "(External funding / Institutional funding) * 100"
            },
            "Optimize Revenue-Cost Alignment": {
                "Revenue-cost ratio": "Total revenue / Total cost",
                "Operating leverage ratio": "(Revenue growth / Cost growth)",
                "Profit variance (%)": "(Budgeted profit - Actual) / Budgeted * 100",
                "Fixed cost absorption rate (%)": "(Revenue contribution / Fixed cost) * 100"
            },
            "Enhance Return on Institutional Assets": {
                "ROA (%)": "(Net income / Total assets) * 100",
                "Asset utilization ratio": "Revenue / Average assets",
                "Idle asset reduction (%)": "(Previous idle assets - Current) / Previous * 100",
                "Asset maintenance cost ratio (%)": "(Maintenance / Asset value) * 100"
            },
            "Increase Financial Sustainability": {
                "Operating surplus ratio (%)": "(Operating surplus / Operating revenue) * 100",
                "Liquidity ratio": "Current assets / Current liabilities",
                "Debt service coverage ratio": "Operating cash flow / Debt service",
                "Self-financing ratio (%)": "(Internal funds / Total funding) * 100"
            },

            # ==================== Education Infrastructure & Asset Finance ====================
            "Education Infrastructure & Asset Finance": {
                "Expand and Modernize Learning Facilities": {
                    "New classroom construction rate (%)": "(New classrooms / Total classrooms) * 100",
                    "New laboratory construction rate (%)": "(New labs / Total labs) * 100",
                    "Upgrade of faculty offices (%)": "(Offices meeting standards / Total offices) * 100",
                    "Capital investment per student ($)": "Total capital spent / Total students"
                },
                "Optimize Utilization of Educational Spaces": {
                    "Classroom occupancy rate (%)": "(Hours classrooms used / Total available hours) * 100",
                    "Lab usage efficiency (%)": "(Lab hours used / Total lab hours) * 100",
                    "Lecture hall utilization (%)": "(Scheduled lecture hours / Total available hours) * 100",
                    "Flexible space adaptation rate (%)": "(Multi-purpose rooms / Total rooms) * 100"
                },
                "Strengthen Digital Learning and ICT Infrastructure": {
                    "LMS adoption rate (%)": "(Students actively using LMS / Total students) * 100",
                    "Faculty ICT utilization (%)": "(Faculty using digital tools / Total faculty) * 100",
                    "Student-to-device ratio": "Total students / Available digital devices",
                    "Investment in digital teaching tools ($)": "Spending on e-learning platforms, software, and virtual labs"
                },
                "Enhance Preventive Maintenance and Lifecycle Management": {
                    "Preventive maintenance coverage (%)": "(Assets maintained preventively / Total assets) * 100",
                    "Average repair turnaround time (days)": "Average days to fix classrooms, labs, or offices",
                    "Classroom and lab functionality rate (%)": "(Functional classrooms/labs / Total) * 100",
                    "Maintenance backlog reduction (%)": "(Previous backlog - Current backlog) / Previous * 100"
                },
                "Improve Energy Efficiency in Academic Assets": {
                    "Energy cost per student ($)": "Total energy cost / Total students",
                    "Water cost per student ($)": "Total water cost / Total students",
                    "Green building adoption (%)": "(Energy-efficient classrooms / Total classrooms) * 100",
                    "Utility cost reduction (%)": "(Previous utility cost - Current) / Previous * 100"
                },
                "Leverage Public–Private Partnerships for Asset Development": {
                    "PPP-supported infrastructure ratio (%)": "(PPP-funded facilities / Total facilities) * 100",
                    "Private funding attracted for labs and classrooms ($)": "Funds contributed by private partners",
                    "Number of co-funded facility projects": "Projects jointly funded with private sector",
                    "Average project completion time (months)": "Average months to complete PPP projects"
                },
                "Maximize Return on Educational Assets": {
                    "Revenue per facility ($)": "Income from labs, classrooms, or event rentals",
                    "Asset contribution to student outcomes": "Score reflecting impact of facilities on learning",
                    "Reduction in idle facilities (%)": "(Previously unused facilities - Current) / Previous * 100",
                    "Facility productivity index": "Student contact hours per m² of academic space"
                },
                "Strengthen Asset Register and Compliance Monitoring": {
                    "Verified educational assets (%)": "(Verified classrooms, labs, and offices / Total assets) * 100",
                    "Accuracy of asset valuations (%)": "(Assets valued correctly / Total assets) * 100",
                    "Timeliness of asset reporting (%)": "(Reports submitted on time / Total reports) * 100",
                    "Compliance with asset management policies (%)": "(Assets managed per policy / Total assets) * 100"
                },
            },

            # ECONOMIC DEVELOPMENT & SOCIAL IMPACT
            # -------------------------------------------------------
            "Economic Development & Social Impact": {
                "Increase local economic contribution": {
                    "Local procurement ratio (%)": "(Local purchases / Total purchases) * 100",
                    "Jobs created through projects": "Number of local jobs supported",
                    "Income generated in communities (USD)": "Value of institutional spending locally",
                    "Multiplier effect ratio": "Indirect benefit / Direct expenditure",
                },
                "Promote graduate employability": {
                    "Graduate employment rate (%)": "(Employed graduates / Total graduates) * 100",
                    "Average time to employment (months)": "Average months post-graduation to job",
                    "Employer satisfaction index": "Survey rating from employers",
                    "Graduate self-employment rate (%)": "(Self-employed / Total employed) * 100",
                },
                "Support research for local innovation": {
                    "Research addressing local needs (%)": "(Local research / Total research) * 100",
                    "Number of community-based innovations": "Count of innovations applied locally",
                    "Partnerships with local enterprises": "Active collaborations with small businesses",
                    "Innovation adoption rate (%)": "(Implemented innovations / Proposed) * 100",
                },
                "Promote inclusive education access": {
                    "Scholarship beneficiaries (%)": "(Scholarship students / Total students) * 100",
                    "Students from low-income households (%)": "(Low-income students / Total) * 100",
                    "Dropout reduction rate (%)": "(Previous dropout - Current) / Previous * 100",
                    "Female enrollment ratio (%)": "(Female students / Total) * 100",
                },
                "Enhance contribution to national productivity": {
                    "Number of industry partnerships": "Active institutional collaborations with industries",
                    "Applied research projects (%)": "(Applied research / Total research) * 100",
                    "Economic return from education (%)": "(Graduate contribution / Public investment) * 100",
                    "Training programs delivered": "Count of workforce development programs",
                },
                "Support entrepreneurship and startups": {
                    "Student startups incubated": "Count of student-led enterprises supported",
                    "Incubator program success rate (%)": "(Sustainable startups / Total incubated) * 100",
                    "Startup funding attracted (USD)": "Total external funding raised by startups",
                    "Number of patents registered": "Patents filed or granted through incubator",
                },
                "Enhance social responsibility initiatives": {
                    "CSR budget allocation (%)": "(CSR budget / Total budget) * 100",
                    "Number of social outreach programs": "Community programs executed per year",
                    "Beneficiaries reached": "Individuals supported through CSR activities",
                    "Impact satisfaction score": "Survey-based social impact rating",
                },
                "Contribute to regional development goals": {
                    "Alignment with SDGs (%)": "(SDG-aligned projects / Total projects) * 100",
                    "Regional partnerships count": "Number of collaborations with local governments",
                    "Development fund leveraged (USD)": "Funds secured for regional projects",
                    "Infrastructure built in underserved areas": "Number of rural or low-income projects",
                },
            },
        },
    },
    "Customer Perspective": {

        **GENERIC_CUSTOMER_PERSPECTIVE['Customer Perspective'],

        "Access & Enrollment": {
            "Increase overall student enrollment": {
                "Enrollment growth rate (%)": "(Current enrolled - Previous enrolled) / Previous enrolled * 100",
                "Application-to-enrollment conversion (%)": "(Enrolled / Applications) * 100",
                "Enrollment from underserved communities (%)": "(Students from target areas / Total students) * 100",
                "Scholarship utilization rate (%)": "(Students receiving scholarships / Total eligible) * 100"
            },
            "Expand access to remote/distance learning": {
                "Distance learning enrollment (#)": "Number of students enrolled in remote programs",
                "Growth rate in distance enrollment (%)": "((Current - Previous) / Previous) * 100",
                "Digital platform adoption (%)": "(Students actively using platforms / Total students) * 100",
                "Course completion rate (%)": "(Completed / Enrolled) * 100"
            },
            "Promote inclusive education": {
                "Students with special needs supported (#)": "Count of students",
                "Accessibility facilities coverage (%)": "(Accessible facilities / Total facilities) * 100",
                "Faculty trained in inclusive practices (#)": "Number of faculty trained",
                "Satisfaction with inclusivity (%)": "Survey rating"
            },
            "Streamline admission process": {
                "Average application processing time (days)": "Mean processing days",
                "On-time admission completion (%)": "(Completed / Scheduled) * 100",
                "Admission errors (%)": "(Errors / Total processed) * 100",
                "Student satisfaction with admission process (%)": "Survey rating"
            },
            "Increase diversity of student body": {
                "Representation of underrepresented groups (%)": "(Number / Total students) * 100",
                "Retention of diverse students (%)": "(Continuing / Total diverse students) * 100",
                "Scholarship allocation to diverse groups (%)": "(Awarded / Total scholarships) * 100",
                "Engagement in diversity programs (%)": "(Participants / Eligible students) * 100"
            },
            "Strengthen international student enrollment": {
                "International student count (#)": "Number of enrolled international students",
                "Growth rate of international students (%)": "((Current - Previous) / Previous) * 100",
                "International student retention (%)": "(Continuing / Total enrolled) * 100",
                "Satisfaction of international students (%)": "Survey rating"
            },
            "Leverage partnerships with feeder schools": {
                "Feeder school partnerships (#)": "Total active partnerships",
                "Students recruited via partnerships (#)": "Count of students",
                "Retention of recruited students (%)": "(Continuing / Total recruited) * 100",
                "Engagement events with feeder schools (#)": "Count of workshops/events"
            },
            "Optimize digital recruitment campaigns": {
                "Conversion rate from digital channels (%)": "(Applications from digital / Total applications) * 100",
                "Cost per digital applicant ($)": "Total digital spend / Applicants",
                "Website engagement score": "Average user interaction metric",
                "Social media reach (#)": "Total reach via campaigns"
            }
        },
        "Student Satisfaction & Engagement": {
            "Enhance teaching quality": {
                "Course satisfaction (%)": "Survey rating",
                "Faculty evaluation score": "Average evaluation",
                "Course completion rate (%)": "(Completed / Registered) * 100",
                "Dropout rate reduction (%)": "((Previous - Current) / Previous) * 100"
            },
            "Improve academic support services": {
                "Tutoring utilization (%)": "(Students using tutoring / Total students) * 100",
                "Support satisfaction (%)": "Survey rating",
                "Support session attendance (#)": "Count of sessions",
                "Average student performance improvement (%)": "Average score improvement"
            },
            "Strengthen student engagement": {
                "Participation in clubs/activities (%)": "(Active / Total students) * 100",
                "Engagement survey score": "Survey rating",
                "Event attendance (#)": "Count of events attended",
                "Feedback implementation (%)": "(Implemented / Total feedback) * 100"
            },
            "Enhance campus facilities experience": {
                "Facilities satisfaction (%)": "Survey rating",
                "Facility usage rate (%)": "(Hours used / Available hours) * 100",
                "Maintenance completion rate (%)": "(Completed / Submitted) * 100",
                "Safety incident reduction (%)": "((Previous - Current) / Previous) * 100"
            },
            "Improve digital learning experience": {
                "E-learning course completion (%)": "(Completed / Enrolled) * 100",
                "Platform satisfaction (%)": "Survey rating",
                "Technical issue resolution (%)": "(Resolved / Reported) * 100",
                "Platform engagement score": "Metric of interactions per student"
            },
            "Enhance feedback & complaint resolution": {
                "Response time (days)": "Average days",
                "Resolution rate (%)": "(Resolved / Total complaints) * 100",
                "Student satisfaction with resolution (%)": "Survey rating",
                "Reduction in repeat complaints (%)": "((Previous - Current) / Previous) * 100"
            },
            "Promote student well-being": {
                "Counseling participation (%)": "(Participating / Total students) * 100",
                "Well-being satisfaction (%)": "Survey rating",
                "Stress incident reduction (%)": "((Previous - Current) / Previous) * 100",
                "Health program utilization (%)": "(Participants / Eligible students) * 100"
            },
            "Improve student communication": {
                "Query response rate (%)": "(Responded / Total queries) * 100",
                "Communication satisfaction (%)": "Survey rating",
                "Information dissemination effectiveness (%)": "Metric based on engagement",
                "Feedback loop closure (%)": "(Issues addressed / Total feedback) * 100"
            }
        },
        "Student Support & Wellbeing": {
            "Promote mental health programs": {
                "Participation in counseling (%)": "(Participating / Total students) * 100",
                "Student satisfaction with mental health support (%)": "Survey rating",
                "Reduction in stress incidents (%)": "((Previous - Current) / Previous) * 100",
                "Peer support program adoption (%)": "(Participants / Eligible students) * 100"
            },
            "Enhance health and safety services": {
                "Participation in health programs (%)": "(Participants / Eligible students) * 100",
                "Health satisfaction (%)": "Survey rating",
                "Safety incident reduction (%)": "((Previous - Current) / Previous) * 100",
                "Emergency response time (min)": "Average time to respond"
            },
            "Provide academic advising & mentorship": {
                "Advisor sessions attended (#)": "Count per student",
                "Satisfaction with advisors (%)": "Survey rating",
                "Advising session coverage (%)": "(Students with advisor / Total students) * 100",
                "Mentorship program adoption (%)": "(Students in mentorship / Eligible students) * 100"
            },
            "Enhance support for students with disabilities": {
                "Accessibility facility coverage (%)": "(Accessible / Total facilities) * 100",
                "Participation of students with disabilities (%)": "(Engaged / Total disabled students) * 100",
                "Satisfaction of disabled students (%)": "Survey rating",
                "Special support program adoption (%)": "(Participants / Eligible students) * 100"
            },
            "Promote inclusive support programs": {
                "Diversity program participation (%)": "(Participating / Total students) * 100",
                "Satisfaction with inclusivity support (%)": "Survey rating",
                "Program reach (%)": "(Engaged students / Total students) * 100",
                "Retention of participants (%)": "(Continuing / Total participants) * 100"
            },
            "Strengthen student counseling services": {
                "Counseling session completion (%)": "(Completed / Scheduled) * 100",
                "Student satisfaction (%)": "Survey rating",
                "Average session duration (min)": "Average minutes",
                "Follow-up adherence (%)": "(Followed-up / Total sessions) * 100"
            },
            "Promote extracurricular engagement": {
                "Participation in clubs (%)": "(Active / Total students) * 100",
                "Event satisfaction (%)": "Survey rating",
                "Hours spent in extracurricular activities (#)": "Total hours per student",
                "Peer engagement index": "Composite engagement measure"
            },
            "Provide financial support & scholarships": {
                "Scholarship coverage (%)": "(Recipients / Eligible students) * 100",
                "Satisfaction with financial support (%)": "Survey rating",
                "Timeliness of disbursement (%)": "(On-time / Total disbursement) * 100",
                "Impact on retention (%)": "((Retained - Not retained) / Total recipients) * 100"
            }
        },
        "Employability & Career Services": {
            "Increase internship placements": {
                "Placement rate (%)": "(Placed / Total students seeking internship) * 100",
                "Satisfaction with placements (%)": "Survey rating",
                "Employer feedback score": "Average employer rating",
                "Internship completion rate (%)": "(Completed / Assigned) * 100"
            },
            "Enhance career counseling": {
                "Career counseling utilization (%)": "(Students using service / Total students) * 100",
                "Satisfaction with counseling (%)": "Survey rating",
                "Sessions per student (#)": "Average number per student",
                "Follow-up action rate (%)": "(Implemented / Total recommended) * 100"
            },
            "Improve employability skills": {
                "Students completing skills programs (%)": "(Completed / Enrolled) * 100",
                "Satisfaction with skill programs (%)": "Survey rating",
                "Employer satisfaction (%)": "Employer survey rating",
                "Skill assessment improvement (%)": "Average improvement"
            },
            "Enhance job placement services": {
                "Job placement rate (%)": "(Placed / Graduates seeking jobs) * 100",
                "Time-to-placement (days)": "Average days to secure job",
                "Employer satisfaction (%)": "Survey rating",
                "Alumni referrals for placements (#)": "Count of referrals"
            },
            "Strengthen industry partnerships": {
                "Partnership agreements (#)": "Total active agreements",
                "Students benefiting from partnerships (#)": "Count",
                "Employer satisfaction with partnerships (%)": "Survey rating",
                "Internship/job conversion rate (%)": "(Students converted to jobs / Total students in program) * 100"
            },
            "Provide entrepreneurship support": {
                "Students engaged in entrepreneurship programs (#)": "Count",
                "Startup formation rate (%)": "(Startups formed / Participating students) * 100",
                "Revenue from student startups ($)": "Total revenue",
                "Satisfaction with entrepreneurship support (%)": "Survey rating"
            },
            "Offer career workshops & events": {
                "Participation rate (%)": "(Attending / Total students) * 100",
                "Satisfaction with workshops (%)": "Survey rating",
                "Employers attending events (#)": "Count",
                "Follow-up action rate (%)": "(Implemented / Total recommended) * 100"
            },
            "Improve alumni job network support": {
                "Alumni mentoring participation (%)": "(Engaged / Eligible alumni) * 100",
                "Student satisfaction with mentorship (%)": "Survey rating",
                "Job referrals via alumni (#)": "Count of referrals",
                "Employment outcome improvement (%)": "Average improvement"
            }
        },
        "Alumni Relations & Reputation": {
            "Increase alumni engagement": {
                "Alumni participation rate (%)": "(Active alumni / Total alumni) * 100",
                "Alumni event attendance (#)": "Count",
                "Alumni survey satisfaction (%)": "Survey rating",
                "Alumni program growth rate (%)": "((Current - Previous) / Previous) * 100"
            },
            "Strengthen alumni communications": {
                "Newsletter open rate (%)": "(Opened / Sent) * 100",
                "Social media engagement (#)": "Count",
                "Alumni feedback implementation (%)": "(Implemented / Total feedback) * 100",
                "Response time to alumni queries (days)": "Average"
            },
            "Promote alumni giving & donations": {
                "Donation participation (%)": "(Donating alumni / Total alumni) * 100",
                "Total donations ($)": "Amount",
                "Average donation per donor ($)": "Amount / Donors",
                "Repeat donation rate (%)": "(Repeat donors / Total donors) * 100"
            },
            "Showcase alumni achievements": {
                "Alumni achievements recorded (#)": "Count",
                "Media mentions (#)": "Count",
                "Alumni awards (#)": "Count",
                "Satisfaction with recognition (%)": "Survey rating"
            },
            "Enhance alumni mentoring & networking": {
                "Mentoring participation (#)": "Count",
                "Student satisfaction with mentorship (%)": "Survey rating",
                "Networking event attendance (#)": "Count",
                "Successful job placements (%)": "(Placed / Participating students) * 100"
            },
            "Build institutional reputation": {
                "Student satisfaction with reputation (%)": "Survey rating",
                "Positive media coverage (#)": "Count",
                "Employer satisfaction with graduates (%)": "Survey rating",
                "Peer institution ranking improvement (%)": "((Current - Previous) / Previous) * 100"
            },
            "Strengthen global alumni network": {
                "International alumni engagement (#)": "Count",
                "Global alumni event participation (#)": "Count",
                "Satisfaction with international network (%)": "Survey rating",
                "Alumni advocacy rate (%)": "(Actively promoting / Total alumni) * 100"
            },
            "Leverage alumni for institutional promotion": {
                "Alumni referrals (#)": "Count of students referred",
                "Participation in promotion campaigns (#)": "Count",
                "Impact on enrollment (%)": "((Increase due to alumni / Total new students) * 100)",
                "Satisfaction with alumni contribution (%)": "Survey rating"
            }
        },
        "Parent & Community Engagement": {
            "Increase parent involvement": {
                "Parent participation in school events (%)": "(Participating / Total invited) * 100",
                "Parent satisfaction with school communication (%)": "Survey rating",
                "Parent feedback implementation (%)": "(Implemented / Total feedback) * 100",
                "Parent-teacher meeting attendance (#)": "Count"
            },
            "Enhance community partnerships": {
                "Community partnership programs (#)": "Count",
                "Community engagement satisfaction (%)": "Survey rating",
                "Students benefiting from programs (#)": "Count",
                "Volunteer participation (#)": "Count"
            },
            "Improve school communication": {
                "Timely information dissemination (%)": "(On-time / Total updates) * 100",
                "Communication satisfaction (%)": "Survey rating",
                "Parent query response time (days)": "Average",
                "Feedback closure rate (%)": "(Closed / Total feedback) * 100"
            },
            "Promote collaborative decision-making": {
                "Parent representation in committees (#)": "Count",
                "Satisfaction with involvement (%)": "Survey rating",
                "Action taken based on parent input (#)": "Count",
                "Policy awareness (%)": "(Informed parents / Total parents) * 100"
            },
            "Strengthen social responsibility initiatives": {
                "Community program participation (#)": "Count",
                "Positive community feedback (%)": "Survey rating",
                "Students benefiting (#)": "Count",
                "Volunteer hours contributed (#)": "Total hours"
            },
            "Enhance partnerships with local organizations": {
                "Local organization partnerships (#)": "Count",
                "Student participation (%)": "(Participating / Total students) * 100",
                "Program satisfaction (%)": "Survey rating",
                "Sustainability of partnerships (%)": "(Ongoing / Total partnerships) * 100"
            },
            "Improve parent feedback systems": {
                "Feedback submission rate (%)": "(Submitted / Total invited) * 100",
                "Feedback response time (days)": "Average",
                "Parent satisfaction with feedback handling (%)": "Survey rating",
                "Repeat feedback resolution (%)": "(Resolved repeat issues / Total repeat feedback) * 100"
            },
            "Promote inclusive community engagement": {
                "Participation from diverse groups (%)": "(Participants / Total invited) * 100",
                "Satisfaction across community groups (%)": "Survey rating",
                "Engagement in programs (#)": "Count",
                "Retention of participants (%)": "(Continuing / Total participants) * 100"
            }
        },
        "Curriculum Relevance & Quality": {
            "Improve curriculum relevance": {
                "Employer satisfaction with graduates (%)": "Survey rating",
                "Curriculum alignment with industry standards (%)": "(Aligned courses / Total courses) * 100",
                "Student satisfaction with curriculum (%)": "Survey rating",
                "Graduate employability rate (%)": "(Employed / Total graduates) * 100"
            },
            "Enhance teaching quality": {
                "Faculty training completion (%)": "(Trained / Total faculty) * 100",
                "Student satisfaction with teaching (%)": "Survey rating",
                "Peer review score": "Average score",
                "Course evaluation improvement (%)": "((Current - Previous) / Previous) * 100"
            },
            "Promote experiential learning": {
                "Students in experiential programs (%)": "(Enrolled / Total students) * 100",
                "Satisfaction with experiential learning (%)": "Survey rating",
                "Skill improvement (%)": "Average improvement",
                "Completion rate of experiential activities (%)": "(Completed / Enrolled) * 100"
            },
            "Strengthen assessment methods": {
                "Assessment reliability score": "Metric score",
                "Student satisfaction with assessments (%)": "Survey rating",
                "Timeliness of feedback (%)": "(On-time / Total assessments) * 100",
                "Assessment coverage (%)": "(Assessed learning outcomes / Total outcomes) * 100"
            },
            "Integrate technology in curriculum": {
                "Courses using digital tools (%)": "(Courses using tech / Total courses) * 100",
                "Student satisfaction with tech use (%)": "Survey rating",
                "Digital learning adoption (%)": "(Students using tools / Total students) * 100",
                "Faculty satisfaction with tech integration (%)": "Survey rating"
            },
            "Promote continuous curriculum review": {
                "Curriculum review cycles completed (#)": "Count",
                "Updates implemented (%)": "(Updated / Total recommendations) * 100",
                "Stakeholder satisfaction with updates (%)": "Survey rating",
                "Impact on learning outcomes (%)": "Improvement in outcomes"
            },
            "Enhance interdisciplinary learning": {
                "Interdisciplinary courses offered (#)": "Count",
                "Student enrollment in interdisciplinary courses (#)": "Count",
                "Satisfaction with interdisciplinary learning (%)": "Survey rating",
                "Interdisciplinary project completion (%)": "(Completed / Assigned) * 100"
            },
            "Align curriculum with global standards": {
                "International accreditation (%)": "(Accredited programs / Total programs) * 100",
                "Benchmarking against global peers (#)": "Count",
                "Curriculum gap closure (%)": "(Closed gaps / Identified gaps) * 100",
                "Student satisfaction with global alignment (%)": "Survey rating"
            }
        },
        "Educational Infrastructure": {
            "Enhance campus facilities": {
                "Facility adequacy (%)": "(Facilities meeting standards / Total facilities) * 100",
                "Student satisfaction with facilities (%)": "Survey rating",
                "Maintenance completion rate (%)": "(Completed / Scheduled maintenance) * 100",
                "Facility utilization rate (%)": "(Used hours / Available hours) * 100"
            },
            "Improve digital & IT infrastructure": {
                "Internet coverage (%)": "(Areas covered / Total areas) * 100",
                "Digital resource availability (%)": "(Available resources / Required resources) * 100",
                "Student satisfaction with IT services (%)": "Survey rating",
                "Technical support resolution rate (%)": "(Resolved / Reported issues) * 100"
            },
            "Expand classroom & laboratory capacity": {
                "Classroom utilization (%)": "(Occupied / Total classrooms) * 100",
                "Lab equipment adequacy (%)": "(Functional / Total required) * 100",
                "Student satisfaction with labs (%)": "Survey rating",
                "Growth in capacity (%)": "((Current capacity - Previous) / Previous) * 100"
            },
            "Enhance accessibility and safety": {
                "Accessible facilities (%)": "(Accessible / Total facilities) * 100",
                "Safety compliance (%)": "(Facilities meeting safety standards / Total facilities) * 100",
                "Incident reduction rate (%)": "((Previous incidents - Current) / Previous) * 100",
                "Student satisfaction with safety (%)": "Survey rating"
            },
            "Improve housing and accommodation": {
                "Student housing occupancy (%)": "(Occupied / Total available) * 100",
                "Satisfaction with housing (%)": "Survey rating",
                "Maintenance response time (days)": "Average days to resolve",
                "Student retention due to housing (%)": "(Retained / Total students in housing) * 100"
            },
            "Optimize energy & utilities management": {
                "Energy efficiency improvement (%)": "((Previous - Current consumption)/Previous)*100",
                "Water supply adequacy (%)": "(Adequate supply / Total required) * 100",
                "Satisfaction with utilities (%)": "Survey rating",
                "Cost savings ($)": "Total utility savings"
            },
            "Strengthen transportation infrastructure": {
                "Student transport coverage (%)": "(Students served / Total students) * 100",
                "Satisfaction with transportation (%)": "Survey rating",
                "On-time transport service (%)": "(On-time trips / Total trips) * 100",
                "Incident reduction (%)": "((Previous incidents - Current) / Previous) * 100"
            },
            "Promote sustainable & green infrastructure": {
                "Green building compliance (%)": "(Compliant buildings / Total buildings) * 100",
                "Energy from renewable sources (%)": "(Renewable / Total energy) * 100",
                "Satisfaction with sustainable facilities (%)": "Survey rating",
                "Waste reduction (%)": "((Previous waste - Current)/Previous)*100"
            }
        },
        "Education Development": {
            "Improve curriculum innovation": {
                "New programs developed (#)": "Count of new courses or programs",
                "Student satisfaction with new programs (%)": "Survey rating",
                "Enrollment in innovative programs (#)": "Number of students enrolled",
                "Program completion rate (%)": "(Completed / Enrolled) * 100"
            },
            "Strengthen teacher development": {
                "Faculty training completion (%)": "(Trained / Total faculty) * 100",
                "Teaching effectiveness improvement (%)": "Average improvement",
                "Satisfaction with professional development (%)": "Survey rating",
                "Retention of trained faculty (%)": "(Retained / Trained faculty) * 100"
            },
            "Enhance research & knowledge creation": {
                "Research projects (#)": "Count",
                "Publications (#)": "Count",
                "Research citation impact": "Average citation per publication",
                "Student participation in research (%)": "(Engaged / Total students) * 100"
            },
            "Promote community & social impact": {
                "Community projects (#)": "Count of projects conducted",
                "Student participation (%)": "(Participants / Total students) * 100",
                "Positive community feedback (%)": "Survey rating",
                "Impact index": "Composite measure of outcomes"
            },
            "Increase international collaboration": {
                "Partnership agreements (#)": "Count of active agreements",
                "Student exchange participation (#)": "Number of students",
                "Joint programs developed (#)": "Count of programs",
                "Satisfaction with collaborations (%)": "Survey rating"
            },
            "Strengthen educational equity": {
                "Students from disadvantaged groups (%)": "(Enrolled / Total students) * 100",
                "Retention of disadvantaged students (%)": "(Retained / Enrolled) * 100",
                "Scholarships & support coverage (%)": "(Recipients / Eligible students) * 100",
                "Satisfaction with support programs (%)": "Survey rating"
            },
            "Enhance lifelong learning programs": {
                "Participants in lifelong learning (#)": "Count",
                "Completion rate (%)": "(Completed / Enrolled) * 100",
                "Satisfaction with learning programs (%)": "Survey rating",
                "Employment or skill application (%)": "(Applying skills / Total participants) * 100"
            },
            "Promote innovation & digital education": {
                "Digital courses offered (#)": "Count of courses",
                "Student enrollment in digital courses (#)": "Count",
                "Satisfaction with digital learning (%)": "Survey rating",
                "Learning outcome improvement (%)": "Average improvement"
            }
        },
    },
}
