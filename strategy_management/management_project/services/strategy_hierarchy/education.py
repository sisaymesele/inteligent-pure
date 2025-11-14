
from management_project.services.strategy_hierarchy.default import DEFAULT_PERSPECTIVE


EDUCATION_PERSPECTIVE = {
    "Financial Perspective": {
        **DEFAULT_PERSPECTIVE["Financial Perspective"],
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

        **DEFAULT_PERSPECTIVE["Customer Perspective"],

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

    "Internal Process Perspective": {

        **DEFAULT_PERSPECTIVE["Internal Process Perspective"],

        # -------------------- Curriculum Development & Design --------------------
        "Curriculum Development & Design": {
            "Ensure curriculum relevance": {
                "Curriculum alignment with national standards (%)": "(Aligned courses / Total courses) * 100",
                "Stakeholder satisfaction (%)": "(Satisfied / Total surveyed) * 100",
                "Periodic curriculum review (times/year)": "Number of reviews conducted",
                "Emerging trends integration (%)": "(Integrated trends / Total courses) * 100"
            },
            "Innovate course content": {
                "New course development (%)": "(New courses / Total courses) * 100",
                "Interdisciplinary course adoption (%)": "(Adopted / Total courses) * 100",
                "Student feedback incorporation (%)": "(Feedback applied / Total feedback) * 100",
                "Content update cycle (days)": "Average days per update"
            },
            "Ensure accreditation readiness": {
                "Accreditation compliance (%)": "(Compliant programs / Total programs) * 100",
                "Documentation completeness (%)": "(Complete docs / Total docs) * 100",
                "Audit pass rate (%)": "(Passed / Total audits) * 100",
                "Accreditation cycle adherence (%)": "(On-time / Planned cycles) * 100"
            },
            "Enhance program learning outcomes": {
                "Program outcome achievement (%)": "(Achieved / Target) * 100",
                "Graduate competency index": "Weighted index",
                "Course learning outcome alignment (%)": "(Aligned / Total courses) * 100",
                "Periodic outcome assessment (times/year)": "Number of assessments"
            },
            "Strengthen faculty input in curriculum": {
                "Faculty participation rate (%)": "(Participating / Total faculty) * 100",
                "Faculty satisfaction (%)": "(Satisfied / Total faculty) * 100",
                "Curriculum proposal adoption (%)": "(Adopted / Proposed) * 100",
                "Faculty feedback cycle adherence (%)": "(On-time / Planned feedback cycles) * 100"
            },
            "Integrate technology in curriculum": {
                "Digital content utilization (%)": "(Used / Total courses) * 100",
                "E-learning module adoption (%)": "(Adopted / Total modules) * 100",
                "Faculty tech training completion (%)": "(Completed / Total faculty) * 100",
                "Student tech engagement index": "Weighted engagement measure"
            },
            "Promote interdisciplinary learning": {
                "Interdisciplinary programs (%)": "(Programs / Total programs) * 100",
                "Student enrollment in interdisciplinary courses (%)": "(Enrolled / Eligible) * 100",
                "Faculty collaboration rate (%)": "(Collaborative projects / Total projects) * 100",
                "Outcome assessment effectiveness (%)": "(Achieved / Target) * 100"
            },
            "Continuous curriculum improvement": {
                "Feedback implementation rate (%)": "(Implemented / Total feedback) * 100",
                "Curriculum review frequency (times/year)": "Number of reviews conducted",
                "Course update effectiveness (%)": "(Improved / Total courses) * 100",
                "Stakeholder satisfaction (%)": "(Satisfied / Total surveyed) * 100"
            }
        },

        # -------------------- Instructional & Teaching Effectiveness --------------------
        "Instructional & Teaching Effectiveness": {
            "Enhance teaching quality": {
                "Class observation score": "Average observation rating",
                "Student feedback score": "Survey rating",
                "Teaching plan adherence (%)": "(Adhered / Total sessions) * 100",
                "Faculty development participation (%)": "(Participated / Total faculty) * 100"
            },
            "Promote active learning": {
                "Active learning session adoption (%)": "(Adopted / Total sessions) * 100",
                "Student engagement score": "Weighted score",
                "Interactive material utilization (%)": "(Used / Total materials) * 100",
                "Learning outcome improvement (%)": "(Post - Pre assessment) / Pre * 100"
            },
            "Improve assessment methods": {
                "Diverse assessment adoption (%)": "(Adopted / Total courses) * 100",
                "Assessment reliability (%)": "(Reliable / Total assessments) * 100",
                "Formative assessment coverage (%)": "(Covered / Total courses) * 100",
                "Feedback timeliness (days)": "Average days to provide feedback"
            },
            "Faculty performance development": {
                "Faculty training completion (%)": "(Completed / Total faculty) * 100",
                "Mentorship program participation (%)": "(Participated / Total faculty) * 100",
                "Performance improvement (%)": "(Post - Pre performance) / Pre * 100",
                "Peer review score": "Average rating"
            },
            "Support innovative pedagogy": {
                "Project-based learning adoption (%)": "(Adopted / Total courses) * 100",
                "Flipped classroom adoption (%)": "(Adopted / Total courses) * 100",
                "Faculty innovation score": "Survey/assessment rating",
                "Student outcome improvement (%)": "(Post - Pre assessment) / Pre * 100"
            },
            "Ensure teaching compliance & standards": {
                "Compliance with academic policies (%)": "(Compliant / Total sessions) * 100",
                "Audit coverage (%)": "(Audited / Total faculty) * 100",
                "Lesson plan accuracy (%)": "(Correct / Total plans) * 100",
                "Ethics & integrity incidents (#)": "Number of incidents"
            },
            "Enhance teaching technology use": {
                "LMS adoption (%)": "(Courses using LMS / Total courses) * 100",
                "Faculty digital competency (%)": "(Competent / Total faculty) * 100",
                "Digital content usage (%)": "(Used / Total courses) * 100",
                "Online class effectiveness score": "Weighted student survey"
            },
            "Improve student feedback loop": {
                "Feedback collection rate (%)": "(Collected / Total classes) * 100",
                "Feedback response rate (%)": "(Responded / Total feedback) * 100",
                "Action implementation rate (%)": "(Implemented / Total feedback) * 100",
                "Student satisfaction score": "Survey rating"
            }
        },

        # -------------------- Student Support & Engagement --------------------
        "Student Support & Engagement": {
            "Enhance academic advising": {
                "Advisor-to-student ratio": "Average number of students per advisor",
                "Advising session completion (%)": "(Completed / Scheduled) * 100",
                "Student satisfaction score": "Survey rating",
                "Follow-up adherence (%)": "(Followed-up / Total sessions) * 100"
            },
            "Improve counseling services": {
                "Counseling session completion (%)": "(Completed / Scheduled) * 100",
                "Student mental health score": "Survey/assessment rating",
                "Response time to requests (hours)": "Average hours",
                "Service utilization rate (%)": "(Used / Total eligible) * 100"
            },
            "Enhance extracurricular engagement": {
                "Program participation rate (%)": "(Participated / Total students) * 100",
                "Event attendance rate (%)": "(Attended / Total events) * 100",
                "Student satisfaction score": "Survey rating",
                "Activity diversity index": "Weighted diversity score"
            },
            "Promote student retention": {
                "Retention rate (%)": "(Retained / Total enrolled) * 100",
                "Dropout rate (%)": "(Dropped / Total enrolled) * 100",
                "At-risk student identification (%)": "(Identified / Total students) * 100",
                "Intervention effectiveness (%)": "(Improved / Total interventions) * 100"
            },
            "Support student career readiness": {
                "Internship placement rate (%)": "(Placed / Eligible students) * 100",
                "Career counseling completion (%)": "(Completed / Total students) * 100",
                "Employer satisfaction score": "Survey rating",
                "Job placement rate (%)": "(Placed / Graduates) * 100"
            },
            "Monitor student satisfaction": {
                "Survey completion rate (%)": "(Completed / Total students) * 100",
                "Overall satisfaction score": "Survey rating",
                "Complaint resolution rate (%)": "(Resolved / Total complaints) * 100",
                "Response time to complaints (days)": "Average days"
            },
            "Enhance student feedback integration": {
                "Feedback collection coverage (%)": "(Collected / Total programs) * 100",
                "Actionable feedback implementation (%)": "(Implemented / Total feedback) * 100",
                "Communication effectiveness score": "Survey rating",
                "Follow-up timeliness (days)": "Average days"
            },
            "Promote inclusive education": {
                "Participation of students with special needs (%)": "(Enrolled / Eligible) * 100",
                "Accessibility compliance (%)": "(Compliant facilities / Total) * 100",
                "Diversity & inclusion training (%)": "(Trained / Total staff) * 100",
                "Student satisfaction with inclusivity": "Survey rating"
            }
        },

        # -------------------- Academic Research & Innovation --------------------
        "Academic Research & Innovation": {
            "Increase research output": {
                "Research publication count (#)": "Number of peer-reviewed papers per year",
                "Research productivity per faculty": "Publications / Faculty",
                "Citation index": "Average citations per publication",
                "External collaboration ratio (%)": "(Collaborative / Total research) * 100"
            },
            "Enhance research funding & grants": {
                "Grant success rate (%)": "(Approved / Applied) * 100",
                "Total research funding ($)": "Sum of approved grants",
                "Funding diversification index": "Weighted diversity of funding sources",
                "Proposal submission timeliness (%)": "(On time / Total proposals) * 100"
            },
            "Strengthen interdisciplinary research": {
                "Interdisciplinary projects (%)": "(Cross-department projects / Total projects) * 100",
                "Joint publication ratio (%)": "(Joint papers / Total papers) * 100",
                "Inter-faculty collaboration score": "Survey or index rating",
                "Project success rate (%)": "(Completed / Total projects) * 100"
            },
            "Promote innovation & patents": {
                "Patent applications (#)": "Number filed annually",
                "Patents granted (%)": "(Granted / Filed) * 100",
                "Commercialized research (%)": "(Commercialized / Total research) * 100",
                "Innovation recognition awards (#)": "Number received per year"
            },
            "Improve research infrastructure": {
                "Lab utilization rate (%)": "(Used time / Available time) * 100",
                "Equipment uptime (%)": "(Operational hours / Total hours) * 100",
                "Facility compliance rate (%)": "(Compliant / Total labs) * 100",
                "Research space adequacy (%)": "(Available / Required) * 100"
            },
            "Enhance postgraduate research support": {
                "Graduate research completion rate (%)": "(Completed / Total enrolled) * 100",
                "Average completion time (months)": "Mean duration per thesis",
                "Supervision quality score": "Survey rating",
                "Postgraduate satisfaction (%)": "(Satisfied / Total surveyed) * 100"
            },
            "Encourage publication ethics & integrity": {
                "Research misconduct cases (#)": "Detected per year",
                "Ethics training completion (%)": "(Completed / Total researchers) * 100",
                "Plagiarism-free submission rate (%)": "(Compliant / Total submissions) * 100",
                "Ethical review compliance (%)": "(Reviewed / Total proposals) * 100"
            },
            "Foster community-based research": {
                "Community project count (#)": "Projects involving local communities",
                "Societal impact index": "Weighted impact score",
                "Stakeholder engagement rate (%)": "(Engaged / Total stakeholders) * 100",
                "Research visibility index": "Public outreach score"
            }
        },

        # -------------------- Faculty Development & Performance --------------------
        "Faculty Development & Performance": {
            "Enhance faculty competency": {
                "Training participation rate (%)": "(Participated / Total faculty) * 100",
                "Certification completion rate (%)": "(Certified / Total trained) * 100",
                "Faculty competency index": "Weighted rating",
                "Post-training performance improvement (%)": "(Post - Pre) / Pre * 100"
            },
            "Promote academic qualification advancement": {
                "Faculty pursuing higher studies (%)": "(Enrolled / Total faculty) * 100",
                "Doctorate completion rate (%)": "(Completed / Total enrolled) * 100",
                "Promotion eligibility rate (%)": "(Eligible / Total faculty) * 100",
                "Funding support utilization (%)": "(Utilized / Total available) * 100"
            },
            "Strengthen teaching evaluation system": {
                "Evaluation coverage (%)": "(Evaluated / Total faculty) * 100",
                "Feedback incorporation rate (%)": "(Implemented / Total feedback) * 100",
                "Performance improvement (%)": "(Post - Pre evaluation) / Pre * 100",
                "Evaluation timeliness (%)": "(On-time / Total evaluations) * 100"
            },
            "Encourage faculty research engagement": {
                "Research participation rate (%)": "(Participated / Total faculty) * 100",
                "Publications per faculty": "Total publications / Faculty count",
                "Grant applications submitted (#)": "Number submitted annually",
                "Cross-disciplinary participation (%)": "(Collaborative / Total research) * 100"
            },
            "Recognize & reward faculty excellence": {
                "Awards received (#)": "Number per year",
                "Performance bonus distribution rate (%)": "(Received / Eligible) * 100",
                "Faculty satisfaction score": "Survey rating",
                "Recognition event participation (%)": "(Participated / Total faculty) * 100"
            },
            "Improve faculty workload balance": {
                "Average teaching load (hours/week)": "Mean hours",
                "Workload variance (%)": "(Max - Min) / Mean * 100",
                "Research time allocation (%)": "(Research hours / Total hours) * 100",
                "Burnout rate (%)": "(Reported / Total faculty) * 100"
            },
            "Enhance mentorship & peer support": {
                "Mentorship pairings (#)": "Number of active mentorships",
                "Peer observation sessions (#)": "Sessions per semester",
                "Feedback utilization rate (%)": "(Implemented / Total feedback) * 100",
                "Mentee satisfaction score": "Survey rating"
            },
            "Promote faculty digital skills": {
                "Digital competency completion (%)": "(Completed / Total faculty) * 100",
                "Online teaching readiness index": "Self-assessed readiness score",
                "LMS utilization rate (%)": "(Used / Total courses) * 100",
                "Digital content creation rate (%)": "(Created / Total faculty) * 100"
            }
        },

        # -------------------- Academic Administration & Governance --------------------
        "Academic Administration & Governance": {
            "Strengthen institutional governance": {
                "Policy compliance rate (%)": "(Compliant / Total policies) * 100",
                "Board meeting timeliness (%)": "(On-time / Total meetings) * 100",
                "Strategic plan implementation rate (%)": "(Implemented / Total planned) * 100",
                "Audit finding closure rate (%)": "(Closed / Total findings) * 100"
            },
            "Improve decision-making transparency": {
                "Public disclosure compliance (%)": "(Disclosed / Required) * 100",
                "Meeting documentation completeness (%)": "(Complete / Total) * 100",
                "Stakeholder participation rate (%)": "(Involved / Total stakeholders) * 100",
                "Transparency rating": "External audit score"
            },
            "Enhance academic record management": {
                "Record accuracy (%)": "(Accurate / Total records) * 100",
                "Digitization coverage (%)": "(Digitized / Total records) * 100",
                "Data retrieval time (minutes)": "Average minutes per record",
                "Data loss incidents (#)": "Reported per year"
            },
            "Ensure policy compliance": {
                "Policy adherence (%)": "(Compliant / Total processes) * 100",
                "Non-compliance incidents (#)": "Reported per quarter",
                "Policy update frequency (times/year)": "Number of updates",
                "Regulatory audit success rate (%)": "(Passed / Total audits) * 100"
            },
            "Promote participatory governance": {
                "Committee participation rate (%)": "(Active members / Total) * 100",
                "Student representation (%)": "(Student seats filled / Total available) * 100",
                "Feedback implementation (%)": "(Implemented / Total feedback) * 100",
                "Meeting attendance rate (%)": "(Attended / Scheduled) * 100"
            },
            "Streamline administrative efficiency": {
                "Process cycle time (days)": "Average days per process",
                "Automation adoption (%)": "(Automated / Total processes) * 100",
                "Error rate (%)": "(Errors / Total processes) * 100",
                "Staff productivity index": "Internal measure"
            },
            "Enhance internal communication": {
                "Message delivery timeliness (%)": "(On-time / Total messages) * 100",
                "Communication satisfaction (%)": "(Satisfied / Total surveyed) * 100",
                "Information accuracy (%)": "(Accurate / Total communications) * 100",
                "Response rate (%)": "(Responded / Total messages) * 100"
            },
            "Monitor governance performance": {
                "Governance KPI achievement (%)": "(Achieved / Planned) * 100",
                "Audit compliance (%)": "(Compliant / Total audits) * 100",
                "Stakeholder trust index": "Survey score",
                "Board review frequency (times/year)": "Total board meetings"
            }
        },
        # ================================================
        # ================================================
        "Library & Learning Resources": {
            "Enhance accessibility of learning materials": {
                "Library access rate (%)": "(Active users / Total students) * 100",
                "Online resource access frequency (#)": "Average logins per user per month",
                "Resource borrowing turnaround (days)": "Average days between borrow and return",
                "Collection utilization rate (%)": "(Borrowed items / Total collection) * 100",
            },
            "Improve digital library systems": {
                "System uptime (%)": "(Operational time / Total time) * 100",
                "Digital access success rate (%)": "(Successful logins / Total logins) * 100",
                "Content upload timeliness (%)": "(Uploaded on schedule / Total uploads) * 100",
                "Metadata accuracy (%)": "(Correct entries / Total entries) * 100",
            },
            "Expand and update learning collections": {
                "New acquisitions growth (%)": "(Current - Previous) / Previous * 100",
                "Outdated material replacement (%)": "(Replaced / Total outdated) * 100",
                "Open access content (%)": "(Free-access materials / Total resources) * 100",
                "Curriculum alignment rate (%)": "(Aligned materials / Total resources) * 100",
            },
            "Improve user support & reference services": {
                "User satisfaction score": "Survey-based rating",
                "Inquiry response time (hours)": "Average response time",
                "Resolved user issues (%)": "(Resolved / Total queries) * 100",
                "Training participation (%)": "(Attendees / Total invited) * 100",
            },
            "Increase library learning integration": {
                "Course-linked resource usage (%)": "(Course-related resources used / Total) * 100",
                "Faculty collaboration rate (%)": "(Collaborative faculty / Total faculty) * 100",
                "Library orientation coverage (%)": "(Trained students / Total students) * 100",
                "Learning session satisfaction score": "Post-session survey rating",
            },
            "Enhance research support services": {
                "Citation support requests handled (#)": "Number processed",
                "Plagiarism check coverage (%)": "(Checked papers / Total papers) * 100",
                "Research database usage (%)": "(Active users / Eligible researchers) * 100",
                "Data repository upload compliance (%)": "(Uploaded / Total required) * 100",
            },
            "Optimize resource allocation": {
                "Resource utilization efficiency (%)": "(Used / Available) * 100",
                "Space occupancy rate (%)": "(Used spaces / Total spaces) * 100",
                "Budget variance (%)": "(Actual - Planned) / Planned * 100",
                "Maintenance compliance (%)": "(Completed / Scheduled) * 100",
            },
            "Strengthen library performance monitoring": {
                "Library KPI review frequency (#)": "Reviews per year",
                "Service audit compliance (%)": "(Audited services / Total services) * 100",
                "Feedback response rate (%)": "(Responded / Total feedback) * 100",
                "Performance improvement plan completion (%)": "(Completed / Planned) * 100",
            },
        },

        # ================================================
        "Online Program Management": {
            "Ensure online course quality": {
                "Course review compliance (%)": "(Reviewed / Total courses) * 100",
                "Student satisfaction (%)": "(Positive feedback / Total feedback) * 100",
                "Course error rate (%)": "(Errors / Total modules) * 100",
                "Accreditation alignment (%)": "(Compliant courses / Total courses) * 100",
            },
            "Improve digital platform stability": {
                "System uptime (%)": "(Operational time / Total time) * 100",
                "Average downtime (hours)": "Total downtime / Incidents",
                "Incident resolution rate (%)": "(Resolved / Total incidents) * 100",
                "Platform response time (seconds)": "Average page load time",
            },
            "Enhance online learning engagement": {
                "Active participation rate (%)": "(Active learners / Total enrolled) * 100",
                "Assignment submission rate (%)": "(Submitted / Assigned) * 100",
                "Forum participation index": "(Posts + replies) / Total students",
                "Video engagement time (minutes)": "Average viewing time per learner",
            },
            "Strengthen instructor readiness for e-learning": {
                "Training completion (%)": "(Trained instructors / Total) * 100",
                "Course design competency score": "Rubric-based rating",
                "Instructor satisfaction (%)": "(Satisfied / Total instructors) * 100",
                "Tech-support usage rate (%)": "(Requests / Total instructors) * 100",
            },
            "Expand online program reach": {
                "Enrollment growth (%)": "(Current - Previous) / Previous * 100",
                "International enrollment share (%)": "(Foreign / Total students) * 100",
                "Partnership-based program count (#)": "Number of collaborations",
                "New market penetration (%)": "(New region students / Total new regions) * 100",
            },
            "Ensure academic integrity online": {
                "Plagiarism detection rate (%)": "(Detected / Total submissions) * 100",
                "Identity verification compliance (%)": "(Verified / Total participants) * 100",
                "Exam proctoring coverage (%)": "(Proctored exams / Total exams) * 100",
                "Integrity violation incidents (#)": "Recorded cases",
            },
            "Improve online student support services": {
                "Average response time (hours)": "Time to resolve tickets",
                "Resolution satisfaction (%)": "(Satisfied / Total responses) * 100",
                "Online advising session completion (%)": "(Completed / Scheduled) * 100",
                "Chatbot accuracy (%)": "(Correct responses / Total queries) * 100",
            },
            "Monitor online program performance": {
                "Program completion rate (%)": "(Graduated / Enrolled) * 100",
                "Dropout rate (%)": "(Dropped / Enrolled) * 100",
                "Learner outcome achievement (%)": "(Achieved / Targeted outcomes) * 100",
                "KPI review frequency (#)": "Reviews per year",
            },
        },
        # -------------------- Technology & E-Learning Infrastructure --------------------
        "Technology & E-Learning Infrastructure": {
            "Enhance ICT infrastructure reliability": {
                "System uptime (%)": "(Operational hours / Total hours) * 100",
                "Incident response time (minutes)": "Average resolution time",
                "Network coverage rate (%)": "(Covered areas / Total) * 100",
                "Infrastructure satisfaction score": "Survey rating"
            },
            "Promote e-learning adoption": {
                "Online course adoption (%)": "(Online / Total courses) * 100",
                "LMS usage rate (%)": "(Users active / Total users) * 100",
                "Digital material access (%)": "(Accessed / Available) * 100",
                "Student satisfaction with e-learning": "Survey rating"
            },
            "Ensure cybersecurity & data privacy": {
                "Cybersecurity incident rate (#)": "Detected per quarter",
                "Data breach prevention rate (%)": "(Prevented / Attempted) * 100",
                "Policy compliance (%)": "(Compliant / Total systems) * 100",
                "Staff cybersecurity training completion (%)": "(Completed / Total staff) * 100"
            },
            "Optimize IT service delivery": {
                "IT ticket resolution time (hours)": "Average time to resolve",
                "User satisfaction rate (%)": "(Satisfied / Total users) * 100",
                "Service availability (%)": "(Available / Total planned time) * 100",
                "Process automation ratio (%)": "(Automated / Total processes) * 100"
            },
            "Enhance digital learning resources": {
                "E-resource usage (%)": "(Accessed / Available) * 100",
                "Digital content growth rate (%)": "(Current - Previous) / Previous * 100",
                "Content accuracy rate (%)": "(Accurate / Total materials) * 100",
                "Student feedback score": "Average rating"
            },
            "Promote innovation in teaching technology": {
                "Smart classroom adoption (%)": "(Installed / Total rooms) * 100",
                "AR/VR course integration (%)": "(Integrated / Total courses) * 100",
                "Faculty training completion (%)": "(Completed / Total faculty) * 100",
                "Technology satisfaction index": "Survey score"
            },
            "Improve digital literacy": {
                "Student digital competency (%)": "(Competent / Total students) * 100",
                "Faculty digital competency (%)": "(Competent / Total faculty) * 100",
                "ICT workshop participation (%)": "(Attended / Total invited) * 100",
                "Skill improvement index": "Pre vs Post test"
            },
            "Ensure system integration & interoperability": {
                "Integrated systems (%)": "(Integrated / Total systems) * 100",
                "Data sync success rate (%)": "(Successful / Total syncs) * 100",
                "API uptime (%)": "(Operational hours / Total hours) * 100",
                "Error resolution rate (%)": "(Resolved / Total errors) * 100"
            }
        },

        # -------------------- Quality Assurance & Accreditation --------------------
        "Quality Assurance & Accreditation": {
            "Strengthen quality assurance systems": {
                "Internal audit completion rate (%)": "(Completed / Planned) * 100",
                "Corrective action implementation (%)": "(Implemented / Recommended) * 100",
                "Quality audit score": "Average internal audit rating",
                "Audit non-compliance rate (%)": "(Findings / Total audits) * 100"
            },
            "Ensure continuous quality improvement": {
                "Process improvement initiatives (#)": "Number initiated per year",
                "Improvement success rate (%)": "(Implemented / Total initiatives) * 100",
                "Stakeholder satisfaction improvement (%)": "(Current - Previous) / Previous * 100",
                "Quality review frequency (#)": "Number per semester"
            },
            "Achieve accreditation compliance": {
                "Accreditation coverage (%)": "(Accredited / Total programs) * 100",
                "Accreditation renewal timeliness (%)": "(On-time / Total) * 100",
                "Compliance audit success rate (%)": "(Passed / Total audits) * 100",
                "Documentation completeness (%)": "(Complete / Required documents) * 100"
            },
            "Standardize academic processes": {
                "Process documentation rate (%)": "(Documented / Total processes) * 100",
                "Process deviation rate (%)": "(Deviations / Total executions) * 100",
                "Policy adherence rate (%)": "(Compliant / Total policies) * 100",
                "Process improvement cycle time (days)": "Average completion time"
            },
            "Enhance program review mechanisms": {
                "Program review completion rate (%)": "(Reviewed / Planned) * 100",
                "Program improvement implementation (%)": "(Implemented / Recommended) * 100",
                "Curriculum revision timeliness (%)": "(On-time / Total revisions) * 100",
                "Stakeholder feedback incorporation (%)": "(Incorporated / Total feedback) * 100"
            },
            "Promote evidence-based decision-making": {
                "Data-driven decisions (%)": "(Based on data / Total decisions) * 100",
                "KPI monitoring compliance (%)": "(Tracked / Planned KPIs) * 100",
                "Performance dashboard update frequency (#)": "Updates per quarter",
                "Decision accuracy index": "Post-evaluation rating"
            },
            "Improve benchmarking practices": {
                "Benchmark coverage (%)": "(Benchmarked areas / Total areas) * 100",
                "Gap reduction rate (%)": "(Previous gap - Current gap) / Previous gap * 100",
                "External comparison success index": "Relative performance rating",
                "Peer institution collaboration rate (%)": "(Collaborations / Total benchmarks) * 100"
            },
            "Cultivate a culture of quality": {
                "Quality awareness training (%)": "(Trained / Total staff) * 100",
                "Quality participation rate (%)": "(Participants / Total employees) * 100",
                "Quality improvement suggestions (#)": "Ideas submitted per year",
                "Quality satisfaction index": "Survey rating"
            }
        },

        # -------------------- Campus Operations & Safety --------------------
        "Campus Operations & Safety": {
            "Ensure campus safety": {
                "Safety incident rate (#)": "Incidents per 1,000 people",
                "Emergency response time (minutes)": "Average time to respond",
                "Safety inspection compliance (%)": "(Compliant / Total inspections) * 100",
                "Safety awareness training completion (%)": "(Completed / Total staff & students) * 100"
            },
            "Enhance facility management": {
                "Facility maintenance timeliness (%)": "(On-time / Total requests) * 100",
                "Facility utilization rate (%)": "(Used / Available) * 100",
                "Repair backlog reduction (%)": "(Previous backlog - Current) / Previous * 100",
                "Infrastructure satisfaction index": "Survey rating"
            },
            "Promote environmental sustainability": {
                "Energy consumption reduction (%)": "(Previous - Current) / Previous * 100",
                "Water usage efficiency (%)": "Output / Water used",
                "Waste recycling rate (%)": "(Recycled / Total waste) * 100",
                "Green certification compliance (%)": "(Compliant / Required) * 100"
            },
            "Improve transportation & mobility": {
                "Transport punctuality rate (%)": "(On-time / Total trips) * 100",
                "Vehicle utilization rate (%)": "(Used / Total vehicles) * 100",
                "Fuel efficiency (km/l)": "Average efficiency of campus vehicles",
                "Transport satisfaction index": "Survey rating"
            },
            "Optimize energy management": {
                "Energy efficiency index": "Output per kWh",
                "Renewable energy usage (%)": "(Renewable / Total energy) * 100",
                "Power outage frequency (#)": "Per month",
                "Energy cost savings (%)": "(Previous - Current) / Previous * 100"
            },
            "Strengthen health & safety standards": {
                "Health compliance audit score": "Inspection score",
                "Medical incident response time (minutes)": "Average response time",
                "Emergency preparedness (%)": "(Prepared / Total departments) * 100",
                "First-aid coverage (%)": "(Stations / Total buildings) * 100"
            },
            "Improve facility accessibility": {
                "Accessibility compliance (%)": "(Compliant facilities / Total) * 100",
                "Assistive technology coverage (%)": "(Available / Required) * 100",
                "Accessible route coverage (%)": "(Accessible / Total routes) * 100",
                "Accessibility satisfaction index": "Survey rating"
            },
            "Maintain campus aesthetics": {
                "Landscape maintenance completion rate (%)": "(Completed / Planned) * 100",
                "Cleanliness satisfaction index": "Survey score",
                "Waste collection timeliness (%)": "(On-time / Total collections) * 100",
                "Facility condition index": "Average inspection rating"
            }
        },
    },

    "Learning & Growth Perspective": {
        **DEFAULT_PERSPECTIVE["Learning & Growth Perspective"],
    },
}
