
from management_project.services.strategy_hierarchy.finance_perspective import GENERIC_FINANCE_PERSPECTIVE_DATA



EDUCATION_SECTOR = {
    "Financial Perspective": {
        **GENERIC_FINANCE_PERSPECTIVE_DATA['Financial Perspective'],

        # =============
# ==================== PROFITABILITY ====================
        "Profitability": {
            "Maximize Net Educational Income": {
                "Net operating margin (%)": "(Net operating income / Total revenue) * 100",
                "Profit growth rate (%)": "(Current surplus - Previous) / Previous * 100",
                "Return per student ($/student)": "Net income / Total enrolled students",
                "Educational quality investment ratio": "(Instruction spending / Total spending) * 100"
            },
            "Enhance Program Gross Margins": {
                "Program gross margin (%)": "(Program revenue - Direct program costs) / Program revenue * 100",
                "Program-specific margin improvement (%)": "Margin increase in underperforming programs",
                "Direct instructional cost efficiency (%)": "Reduction in faculty, classroom, materials costs per student",
                "Pricing strategy effectiveness": "Impact of tuition adjustments on enrollment and revenue"
            },
            "Improve Institutional Operating Efficiency": {
                "Administrative cost ratio (%)": "(Administrative costs / Total expenses) * 100",
                "Student-to-administrator ratio": "Total students / Total administrative staff",
                "Facilities utilization efficiency": "Classroom/space usage hours / Available hours",
                "Break-even enrollment optimization": "Minimum enrollment needed to cover fixed costs"
            },
            "Optimize Educational Contribution Margins": {
                "Average contribution margin per program (%)": "(Program revenue - Variable costs) / Program revenue * 100",
                "Departmental profitability index": "Financial contribution by academic departments",
                "Program mix optimization (%)": "Weighted margin across program portfolio",
                "Variable cost control efficiency (%)": "Reduction in direct instructional costs"
            }
        },

        # ==================== REVENUE GROWTH ====================
        "Revenue Growth": {
            "Enhance Student Enrollment Revenue": {
                "Total tuition revenue growth (%)": "(Current tuition revenue - Previous) / Previous * 100",
                "Revenue per student ($/student)": "Total tuition revenue / Total enrolled students",
                "Student retention rate revenue impact": "Revenue from retained students vs. lost students",
                "Program capacity utilization rate (%)": "(Actual enrollment / Maximum capacity) * 100"
            },
            "Strengthen Market Position & Program Appeal": {
                "Market share in key programs (%)": "(Our enrollment / Total regional enrollment in program) * 100",
                "Revenue from high-demand programs ($)": "Income from STEM, healthcare, business programs",
                "Geographic expansion revenue ($)": "Revenue from online, satellite campuses, international students",
                "Admission yield rate (%)": "(Students enrolling / Students accepted) * 100"
            },
            "Accelerate New Program Revenue": {
                "Revenue from new academic programs (%)": "(Revenue from new programs / Total revenue) * 100",
                "Time-to-break-even for new programs (months)": "Months for program revenue to cover development costs",
                "R&D ROI on curriculum development (%)": "(Revenue from new curricula / Development investment) * 100",
                "Employer partnership program revenue": "Revenue from corporate training and custom programs"
            },
            "Diversify Educational Revenue Streams": {
                "Revenue diversity index": "1 - (Tuition revenue / Total revenue)",
                "Revenue from continuing education ($)": "Income from professional development, certificates",
                "Revenue from executive education ($)": "Income from non-degree executive programs",
                "Summer/winter session revenue growth (%)": "(Off-term revenue - Previous) / Previous * 100"
            }
        },

        # ==================== COST MANAGEMENT ====================
        "Cost Management": {
            "Administrative Cost Optimization": {
                "Administrative cost ratio (%)": "(Admin costs / Total expenses) * 100",
                "Staff cost per student ($)": "Total staff cost / Total students",
                "Overhead reduction (%)": "(Previous overhead - Current) / Previous * 100",
                "Procurement efficiency": "Cost savings through optimized purchasing"
            },
            "Instructional Cost Efficiency": {
                "Instruction cost per student ($)": "Instruction spending / Total students",
                "Faculty workload utilization (%)": "(Courses taught / Max course capacity) * 100",
                "Resource cost savings ($)": "Savings from shared resources",
                "Cost variance per program (%)": "(Planned - Actual) / Planned * 100"
            },
            "Operational Expense Control": {
                "Facilities cost per student ($)": "Facilities cost / Total students",
                "Energy cost reduction (%)": "(Previous energy - Current) / Previous * 100",
                "Maintenance cost efficiency": "Maintenance cost per square foot",
                "Administrative process cost reduction (%)": "Improvement in processing cost efficiency"
            },
            "Optimize Auxiliary Services Costs": {
                "Auxiliary service cost ratio (%)": "(Direct service costs / Auxiliary revenue) * 100",
                "Labor cost per service unit ($)": "Labor costs / Service units delivered",
                "Material cost efficiency": "Reduction in materials cost per service",
                "Service cost variance reduction (%)": "Planned vs Actual cost savings"
            }
        },

        # ==================== RESOURCE UTILIZATION ====================
        "Resource Utilization": {
            "Optimize Facility Utilization": {
                "Classroom utilization rate (%)": "(Actual classroom hours used / Available hours) * 100",
                "Space efficiency index": "Educational output per square foot",
                "Multiple scheduling efficiency": "Different programs using same facilities",
                "Energy cost reduction per student (%)": "(Previous energy cost - Current) / Previous * 100"
            },
            "Improve Instructional Productivity": {
                "Revenue per faculty member": "Total educational revenue / Number of faculty",
                "Student-to-faculty ratio": "Total students / Total instructional faculty",
                "Course completion rate (%)": "(Courses completed / Courses started) * 100",
                "Online program efficiency ratio": "Cost per online student vs. traditional student"
            },
            "Enhance Technology Efficiency": {
                "Technology cost per student": "Total technology costs / Total students",
                "Digital resource utilization rate": "(Active digital resource users / Total users) * 100",
                "IT support efficiency": "Support tickets resolved per IT staff member",
                "Learning management system ROI": "Educational benefits / Technology investment"
            },
            "Optimize Auxiliary Resource Utilization": {
                "Service utilization rate (%)": "(Actual service usage / Service capacity) * 100",
                "Facility operating efficiency": "Energy, maintenance costs per square foot",
                "Break-even service volume optimization": "Minimum usage needed to cover fixed costs",
                "Variable cost control efficiency (%)": "Reduction in direct service delivery costs"
            }
        },

        # ==================== ECONOMIC DEVELOPMENT & GDP CONTRIBUTION ====================
        "Economic Development": {
            "Increase Graduate Earnings Premium": {
                "Graduate median income ($)": "Median graduate income",
                "Premium over non-graduates (%)": "(Graduate - Non-graduate) / Non-graduate * 100",
                "Graduate employment rate (%)": "(Employed graduates / Total graduates) * 100",
                "Career progression acceleration (yrs)": "Time to mid-level positions"
            },
            "Promote Regional Economic Contribution": {
                "Education sector GDP share (%)": "(Value of education services / Regional GDP) * 100",
                "Jobs created (#)": "Direct + indirect employment",
                "Industry partnerships (#)": "Number of active collaborations",
                "Regional innovation impact (#)": "Patents/startups linked to institution"
            },
            "Increase Research Commercialization": {
                "Revenue from patents/licensing ($)": "Income from IP",
                "Startups created (#)": "Number of spin-offs",
                "Industry collaboration revenue ($)": "Revenue from partnerships",
                "Research impact index (%)": "Weighted impact on economy"
            },
            "Promote Lifelong Learning Economic Value": {
                "Adult learner employment rate (%)": "(Employed / Total adult learners) * 100",
                "Revenue per adult learner ($)": "Revenue / Adult learners",
                "Credential impact index": "Job improvements per credential",
                "Return on learning investment (%)": "(Benefits / Cost) * 100"
            },
            "Enhance Global Education Contribution": {
                "International student revenue ($)": "Revenue from foreign students",
                "Cross-border program enrollment (#)": "Students enrolled in international programs",
                "Global ranking improvement (#)": "Ranking change over previous year",
                "International partnership revenue ($)": "Revenue from collaborations"
            },
            "Increase Education's GDP Contribution": {
                "Education GDP contribution (%)": "(Value of education sector output / Total GDP) * 100",
                "Education value-added per student ($)": "GDP contribution / Total students",
                "Growth in education GDP contribution (%)": "(Current - Previous) / Previous * 100",
                "Sectoral impact multiplier": "Indirect economic impact of education spending"
            },
            "Enhance Employment Impact of Education": {
                "Total education employment (#)": "Number of people employed in education sector",
                "Jobs created per $1M revenue": "Employment impact per revenue unit",
                "Faculty/staff retention rate (%)": "(Retained / Total) * 100",
                "Skill gap reduction index": "Improvement in workforce readiness"
            },
            "Increase Knowledge & Innovation Contribution": {
                "Patents & IP generated (#)": "Number of patents or licenses filed",
                "Startups created (#)": "New companies launched from research",
                "R&D output per faculty (#)": "Research outputs per faculty member",
                "Innovation index (%)": "Weighted measure of tech transfer and commercialization"
            },
            "Promote Social & Community Impact": {
                "Community education outreach (#)": "Programs delivered to local community",
                "Volunteer student/staff hours (#)": "Total volunteer hours",
                "Economic uplift in local region ($)": "Income generated via local engagement",
                "Community engagement ROI (%)": "(Benefits / Cost of programs) * 100"
            },
            "Enhance Sustainable Economic Impact": {
                "Green campus investment ROI (%)": "Benefits of sustainable infrastructure / Cost",
                "Reduction in carbon footprint (%)": "(Previous emissions - Current) / Previous * 100",
                "Energy efficiency savings ($)": "Savings from efficiency programs",
                "Long-term financial sustainability index": "Endowment & reserve adequacy for 5-10 years"
            }
        },
    },

    "Student & Stakeholder Perspective": {
        "Student Success & Learning Outcomes": {
            "Improve Student Academic Achievement": {
                "Course completion rate": "(Completed courses / Attempted courses) * 100",
                "GPA improvement rate": "((Current average GPA - Previous) / Previous) * 100",
                "Learning outcome achievement": "(Achieved outcomes / Total outcomes) * 100",
                "Academic proficiency growth": "((Current proficiency - Previous) / Previous) * 100"
            },
            "Enhance Student Retention and Persistence": {
                "First-year retention rate": "(Returning students / Total first-year students) * 100",
                "Persistence to graduation rate": "(Persisting students / Cohort students) * 100",
                "Stop-out reduction rate": "((Previous stop-outs - Current stop-outs) / Previous) * 100",
                "Academic progress rate": "(Making progress students / Total students) * 100"
            },
            "Increase Graduation and Completion Rates": {
                "Graduation rate improvement": "((Current rate - Previous rate) / Previous) * 100",
                "Time-to-degree reduction": "((Previous time - Current time) / Previous) * 100",
                "Program completion rate": "(Completed programs / Started programs) * 100",
                "Degree attainment growth": "((Current attainment - Previous) / Previous) * 100"
            },
            "Strengthen Student Learning Engagement": {
                "Active learning participation": "(Participating students / Total students) * 100",
                "Classroom engagement score": "Average classroom engagement assessment",
                "Learning technology utilization": "(Utilizing technology / Available technology) * 100",
                "Collaborative learning effectiveness": "(Effective collaboration / Total collaboration) * 100"
            },
            "Improve Critical Thinking and Problem-Solving Skills": {
                "Critical thinking assessment improvement": "((Current scores - Previous scores) / Previous) * 100",
                "Problem-solving competency growth": "((Current competency - Previous) / Previous) * 100",
                "Analytical skills development": "(Developed skills / Required skills) * 100",
                "Real-world application success": "(Successful applications / Total applications) * 100"
            },
            "Enhance Digital Literacy and Technology Skills": {
                "Digital literacy assessment improvement": "((Current literacy - Previous literacy) / Previous) * 100",
                "Technology skill development": "(Developed skills / Required skills) * 100",
                "Digital tool proficiency": "(Proficient students / Total students) * 100",
                "Online learning readiness": "(Ready students / Total students) * 100"
            },
            "Strengthen Career Readiness and Employability": {
                "Career readiness assessment": "(Ready students / Total students) * 100",
                "Employability skill development": "(Developed skills / Required skills) * 100",
                "Internship and co-op participation": "(Participating students / Eligible students) * 100",
                "Job placement rate improvement": "((Current placement - Previous placement) / Previous) * 100"
            },
            "Improve Graduate Outcomes and Success": {
                "Graduate employment rate": "(Employed graduates / Total graduates) * 100",
                "Further education rate": "(Continuing education / Total graduates) * 100",
                "Graduate satisfaction with education": "Average graduate satisfaction score",
                "Long-term career success": "(Successful careers / Total graduates) * 100"
            }
        },

        "Student Experience & Satisfaction": {
            "Elevate Overall Student Satisfaction": {
                "Student satisfaction score": "Average satisfaction survey results",
                "Net Promoter Score (NPS)": "Promoters % - Detractors %",
                "Satisfaction trend improvement": "((Current satisfaction - Previous) / Previous) * 100",
                "Experience consistency score": "(Consistent experiences / Total experiences) * 100"
            },
            "Enhance Teaching Quality and Effectiveness": {
                "Teaching evaluation scores": "Average teaching assessment scores",
                "Student-faculty interaction quality": "Average interaction quality score",
                "Instructional method effectiveness": "(Effective methods / Total methods) * 100",
                "Faculty accessibility and support": "Average accessibility satisfaction"
            },
            "Improve Campus Life and Student Engagement": {
                "Campus activity participation": "(Participating students / Total students) * 100",
                "Student organization involvement": "(Involved students / Total students) * 100",
                "Campus community satisfaction": "Average community satisfaction score",
                "Student leadership development": "(Developed leaders / Total students) * 100"
            },
            "Strengthen Student Support Services": {
                "Support service utilization": "(Utilized services / Available services) * 100",
                "Service satisfaction scores": "Average support service satisfaction",
                "Support access improvement": "((Current access - Previous access) / Previous) * 100",
                "Early intervention effectiveness": "(Effective interventions / Total interventions) * 100"
            },
            "Optimize Learning Environment Quality": {
                "Classroom facility satisfaction": "Average facility satisfaction score",
                "Learning technology reliability": "(Reliable technology / Total technology) * 100",
                "Study space adequacy": "(Adequate spaces / Total spaces) * 100",
                "Environmental comfort improvement": "((Current comfort - Previous comfort) / Previous) * 100"
            },
            "Enhance Diversity, Equity and Inclusion Experience": {
                "Inclusion perception score": "Average inclusion assessment",
                "Diverse student satisfaction": "Average satisfaction among diverse populations",
                "Equity in student experience": "(Equitable experiences / Total experiences) * 100",
                "Cultural competence development": "(Developed competence / Total students) * 100"
            },
            "Improve Health and Wellness Support": {
                "Wellness service utilization": "(Utilized services / Available services) * 100",
                "Mental health support effectiveness": "(Effective support / Total support) * 100",
                "Student wellness improvement": "((Current wellness - Previous wellness) / Previous) * 100",
                "Health education participation": "(Participating students / Total students) * 100"
            },
            "Strengthen Career Development Services": {
                "Career service utilization": "(Utilized services / Available services) * 100",
                "Career counseling satisfaction": "Average counseling satisfaction score",
                "Internship placement success": "(Successful placements / Total placements) * 100",
                "Alumni network engagement": "(Engaged alumni / Total alumni) * 100"
            }
        },

        "Access & Equity": {
            "Expand Educational Access and Opportunity": {
                "Underrepresented student enrollment": "(Underrepresented students / Total students) * 100",
                "First-generation student access": "(First-generation students / Total students) * 100",
                "Geographic diversity improvement": "((Current diversity - Previous diversity) / Previous) * 100",
                "Access program effectiveness": "(Effective programs / Total programs) * 100"
            },
            "Enhance Financial Aid and Affordability": {
                "Financial aid distribution equity": "(Equitable distribution / Total distribution) * 100",
                "Student debt reduction": "((Previous debt - Current debt) / Previous) * 100",
                "Scholarship availability growth": "((Current scholarships - Previous) / Previous) * 100",
                "Affordability satisfaction": "Average affordability satisfaction score"
            },
            "Improve Digital Access and Inclusion": {
                "Digital access equity": "(Equitable access / Total access) * 100",
                "Technology resource availability": "(Available resources / Required resources) * 100",
                "Digital literacy support effectiveness": "(Effective support / Total support) * 100",
                "Online learning accessibility": "(Accessible online courses / Total courses) * 100"
            },
            "Strengthen Support for Diverse Learning Needs": {
                "Learning accommodation effectiveness": "(Effective accommodations / Total accommodations) * 100",
                "Specialized support service utilization": "(Utilized services / Available services) * 100",
                "Inclusive teaching practices": "(Inclusive practices / Total practices) * 100",
                "Diverse learning style accommodation": "(Accommodated styles / Total styles) * 100"
            },
            "Enhance Transfer and Articulation Pathways": {
                "Transfer student success rate": "(Successful transfers / Total transfers) * 100",
                "Articulation agreement effectiveness": "(Effective agreements / Total agreements) * 100",
                "Credit transfer efficiency": "(Efficient transfers / Total transfers) * 100",
                "Pathway program completion": "(Completed pathways / Total pathways) * 100"
            },
            "Improve Adult and Continuing Education Access": {
                "Adult learner enrollment growth": "((Current adult learners - Previous) / Previous) * 100",
                "Flexible program availability": "(Available flexible programs / Total programs) * 100",
                "Workforce development participation": "(Participating workers / Eligible workers) * 100",
                "Lifelong learning access": "(Accessible programs / Total programs) * 100"
            },
            "Strengthen International Student Support": {
                "International student satisfaction": "Average international student satisfaction",
                "Cross-cultural support effectiveness": "(Effective support / Total support) * 100",
                "Global learning opportunities": "(Available opportunities / Required opportunities) * 100",
                "International student retention": "(Retained international students / Total international) * 100"
            },
            "Enhance Community Education Access": {
                "Community program participation": "(Participating community members / Target population) * 100",
                "Outreach program effectiveness": "(Effective outreach / Total outreach) * 100",
                "Community partnership access points": "(Access points / Required points) * 100",
                "Lifelong learning community engagement": "(Engaged community / Total community) * 100"
            }
        },

        "Stakeholder Engagement & Partnerships": {
            "Strengthen Parent and Family Engagement": {
                "Parent satisfaction score": "Average parent satisfaction assessment",
                "Family engagement participation": "(Engaged families / Total families) * 100",
                "Communication effectiveness with families": "(Effective communications / Total communications) * 100",
                "Family support program utilization": "(Utilized programs / Available programs) * 100"
            },
            "Enhance Employer and Industry Partnerships": {
                "Industry partnership satisfaction": "Average partnership satisfaction score",
                "Work-based learning opportunities": "(Available opportunities / Required opportunities) * 100",
                "Employer feedback integration": "(Integrated feedback / Total feedback) * 100",
                "Industry advisory board effectiveness": "(Effective boards / Total boards) * 100"
            },
            "Improve Community Relations and Impact": {
                "Community satisfaction with institution": "Average community satisfaction score",
                "Community service participation": "(Participating students / Total students) * 100",
                "Local economic impact": "Economic contribution / Total operations * 100",
                "Community program collaboration": "(Collaborative programs / Total programs) * 100"
            },
            "Strengthen K-12 Educational Partnerships": {
                "Partnership program effectiveness": "(Effective programs / Total programs) * 100",
                "College readiness collaboration": "(Collaborative readiness / Total readiness) * 100",
                "Dual enrollment participation": "(Participating students / Eligible students) * 100",
                "Educational pathway alignment": "(Aligned pathways / Total pathways) * 100"
            },
            "Enhance Government and Policy Relations": {
                "Policy advocacy effectiveness": "(Effective advocacy / Total advocacy) * 100",
                "Regulatory compliance rate": "(Compliant operations / Total operations) * 100",
                "Government relationship satisfaction": "Average relationship satisfaction",
                "Public policy influence": "(Influenced policies / Total policy engagements) * 100"
            },
            "Improve Alumni Engagement and Support": {
                "Alumni engagement rate": "(Engaged alumni / Total alumni) * 100",
                "Alumni satisfaction score": "Average alumni satisfaction assessment",
                "Alumni giving participation": "(Donating alumni / Total alumni) * 100",
                "Alumni network effectiveness": "(Effective network / Total network) * 100"
            },
            "Strengthen Research and Academic Partnerships": {
                "Collaborative research success": "(Successful collaborations / Total collaborations) * 100",
                "Joint publication rate": "(Joint publications / Total publications) * 100",
                "Academic partnership satisfaction": "Average partnership satisfaction",
                "Knowledge exchange effectiveness": "(Effective exchanges / Total exchanges) * 100"
            },
            "Enhance International Educational Partnerships": {
                "Global partnership satisfaction": "Average international partnership satisfaction",
                "Study abroad participation": "(Participating students / Eligible students) * 100",
                "International research collaboration": "(Collaborative research / Total research) * 100",
                "Cross-cultural program effectiveness": "(Effective programs / Total programs) * 100"
            }
        }
    },

    "Internal Process Perspective": {
        "Academic Excellence & Curriculum Development": {
            "Enhance Curriculum Quality and Relevance": {
                "Curriculum review completion rate": "(Reviewed programs / Total programs) * 100",
                "Industry relevance assessment": "(Relevant curricula / Total curricula) * 100",
                "Learning outcome alignment": "(Aligned outcomes / Total outcomes) * 100",
                "Curriculum innovation rate": "(Innovative elements / Total curriculum) * 100"
            },
            "Improve Teaching Methodologies and Pedagogy": {
                "Evidence-based teaching adoption": "(Adopted methods / Available methods) * 100",
                "Faculty development participation": "(Participating faculty / Total faculty) * 100",
                "Teaching innovation implementation": "(Implemented innovations / Total innovations) * 100",
                "Student-centered approach adoption": "(Adopted approaches / Total approaches) * 100"
            },
            "Strengthen Academic Program Assessment": {
                "Program assessment completion": "(Assessed programs / Total programs) * 100",
                "Assessment data utilization": "(Utilized data / Collected data) * 100",
                "Continuous improvement implementation": "(Implemented improvements / Total improvements) * 100",
                "Accreditation standard compliance": "(Compliant standards / Total standards) * 100"
            },
            "Optimize Course Scheduling and Delivery": {
                "Course availability rate": "(Available courses / Required courses) * 100",
                "Schedule efficiency improvement": "((Current efficiency - Previous efficiency) / Previous) * 100",
                "Classroom utilization optimization": "(Optimized utilization / Total utilization) * 100",
                "Student schedule satisfaction": "Average schedule satisfaction score"
            },
            "Enhance Interdisciplinary Program Development": {
                "Interdisciplinary course offerings": "(Interdisciplinary courses / Total courses) * 100",
                "Cross-departmental collaboration": "(Collaborative programs / Total programs) * 100",
                "Integrated learning opportunities": "(Available opportunities / Required opportunities) * 100",
                "Interdisciplinary research participation": "(Participating faculty / Total faculty) * 100"
            },
            "Improve Online and Hybrid Course Quality": {
                "Online course quality standards": "(Meeting standards courses / Total online courses) * 100",
                "Hybrid learning effectiveness": "(Effective hybrid courses / Total hybrid courses) * 100",
                "Digital content quality": "(Quality content / Total content) * 100",
                "Online student engagement": "(Engaged online students / Total online students) * 100"
            },
            "Strengthen Undergraduate Research Opportunities": {
                "Research participation rate": "(Participating undergraduates / Total undergraduates) * 100",
                "Mentored research opportunities": "(Available opportunities / Required opportunities) * 100",
                "Research presentation rate": "(Presenting students / Research students) * 100",
                "Undergraduate publication rate": "(Publishing students / Research students) * 100"
            },
            "Enhance Capstone and Experiential Learning": {
                "Experiential learning participation": "(Participating students / Eligible students) * 100",
                "Capstone project completion": "(Completed projects / Total projects) * 100",
                "Real-world application success": "(Successful applications / Total applications) * 100",
                "Industry project collaboration": "(Collaborative projects / Total projects) * 100"
            }
        },

        "Faculty & Staff Excellence": {
            "Improve Faculty Recruitment and Retention": {
                "Faculty retention rate": "(Retained faculty / Total faculty) * 100",
                "Time-to-fill faculty positions": "Average days to fill faculty positions",
                "Faculty diversity improvement": "((Current diversity - Previous diversity) / Previous) * 100",
                "Candidate quality index": "Composite score of faculty candidate quality"
            },
            "Enhance Faculty Development and Support": {
                "Professional development participation": "(Participating faculty / Total faculty) * 100",
                "Mentoring program effectiveness": "(Effective mentoring / Total mentoring) * 100",
                "Research support satisfaction": "Average research support satisfaction",
                "Teaching resource availability": "(Available resources / Required resources) * 100"
            },
            "Strengthen Faculty Research and Scholarship": {
                "Research productivity growth": "((Current productivity - Previous productivity) / Previous) * 100",
                "Grant funding success rate": "(Awarded grants / Submitted grants) * 100",
                "Publication impact factor": "Average citation impact per publication",
                "Interdisciplinary research collaboration": "(Collaborative research / Total research) * 100"
            },
            "Optimize Faculty Workload and Balance": {
                "Workload equity assessment": "(Equitable workloads / Total workloads) * 100",
                "Work-life balance satisfaction": "Average work-life balance satisfaction",
                "Faculty burnout reduction": "((Previous burnout - Current burnout) / Previous) * 100",
                "Productivity optimization": "(Optimized productivity / Total productivity) * 100"
            },
            "Improve Staff Professional Development": {
                "Staff training completion rate": "(Completed training / Required training) * 100",
                "Career advancement opportunities": "(Available opportunities / Required opportunities) * 100",
                "Skill development effectiveness": "(Effective development / Total development) * 100",
                "Cross-training participation": "(Cross-trained staff / Total staff) * 100"
            },
            "Enhance Staff Performance and Engagement": {
                "Staff performance evaluation completion": "(Completed evaluations / Total staff) * 100",
                "Staff engagement score": "Average staff engagement assessment",
                "Performance improvement rate": "((Current performance - Previous performance) / Previous) * 100",
                "Recognition program effectiveness": "(Effective recognition / Total recognition) * 100"
            },
            "Strengthen Administrative Efficiency": {
                "Process standardization rate": "(Standardized processes / Total processes) * 100",
                "Administrative response time": "Average time for administrative responses",
                "Cross-departmental coordination": "(Coordinated activities / Total activities) * 100",
                "Administrative technology utilization": "(Utilized technology / Available technology) * 100"
            },
            "Improve HR Services and Support": {
                "HR service satisfaction": "Average HR service satisfaction score",
                "Benefits utilization rate": "(Utilized benefits / Available benefits) * 100",
                "Recruitment process efficiency": "(Efficient recruitment / Total recruitment) * 100",
                "Employee relations effectiveness": "(Effective relations / Total relations) * 100"
            }
        },

        "Educational Technology & Infrastructure": {
            "Enhance Learning Management System Effectiveness": {
                "LMS utilization rate": "(Active users / Total users) * 100",
                "System reliability score": "(Reliable operation time / Total time) * 100",
                "Feature adoption rate": "(Adopted features / Available features) * 100",
                "User satisfaction with LMS": "Average LMS satisfaction score"
            },
            "Improve Classroom Technology Integration": {
                "Technology-enhanced classroom rate": "(Enhanced classrooms / Total classrooms) * 100",
                "Classroom technology reliability": "(Reliable technology / Total technology) * 100",
                "Faculty technology proficiency": "(Proficient faculty / Total faculty) * 100",
                "Student technology satisfaction": "Average technology satisfaction score"
            },
            "Strengthen Digital Learning Resources": {
                "Digital resource availability": "(Available resources / Required resources) * 100",
                "Resource utilization rate": "(Utilized resources / Available resources) * 100",
                "Open educational resource adoption": "(Adopted OER / Total resources) * 100",
                "Digital content quality assessment": "(Quality content / Total content) * 100"
            },
            "Optimize IT Infrastructure and Support": {
                "Network reliability improvement": "((Current reliability - Previous reliability) / Previous) * 100",
                "Help desk response time": "Average time to help desk response",
                "System uptime percentage": "(Uptime / Total operational time) * 100",
                "IT service satisfaction": "Average IT service satisfaction score"
            },
            "Enhance Data Analytics for Student Success": {
                "Predictive analytics accuracy": "(Accurate predictions / Total predictions) * 100",
                "Early alert system effectiveness": "(Effective alerts / Total alerts) * 100",
                "Data-driven intervention rate": "(Data-informed interventions / Total interventions) * 100",
                "Analytics platform utilization": "(Utilized platform / Available platform) * 100"
            },
            "Improve Cybersecurity and Data Protection": {
                "Security incident reduction": "((Previous incidents - Current incidents) / Previous) * 100",
                "Security training completion": "(Trained users / Total users) * 100",
                "Data protection compliance": "(Compliant data / Total data) * 100",
                "Security audit success rate": "(Successful audits / Total audits) * 100"
            },
            "Strengthen Educational Software Integration": {
                "Software integration success rate": "(Successful integrations / Total integrations) * 100",
                "Application interoperability": "(Interoperable applications / Total applications) * 100",
                "User proficiency with software": "(Proficient users / Total users) * 100",
                "Software ROI achievement": "(Achieved ROI / Target ROI) * 100"
            },
            "Enhance Mobile and Remote Access": {
                "Mobile app adoption rate": "(Active app users / Total users) * 100",
                "Remote access reliability": "(Reliable access / Total access attempts) * 100",
                "Mobile feature utilization": "(Utilized features / Available features) * 100",
                "User satisfaction with mobile access": "Average mobile access satisfaction"
            }
        },

        "Operational Excellence & Administration": {
            "Improve Enrollment Management Processes": {
                "Application processing time": "Average days to process applications",
                "Enrollment yield rate improvement": "((Current yield - Previous yield) / Previous) * 100",
                "Admissions communication effectiveness": "(Effective communications / Total communications) * 100",
                "Enrollment forecasting accuracy": "(1 - |Actual enrollment - Forecasted| / Actual) * 100"
            },
            "Enhance Student Information System Management": {
                "Data accuracy rate": "(Accurate records / Total records) * 100",
                "System integration effectiveness": "(Effective integrations / Total integrations) * 100",
                "User proficiency with SIS": "(Proficient users / Total users) * 100",
                "Reporting efficiency improvement": "((Current efficiency - Previous efficiency) / Previous) * 100"
            },
            "Optimize Financial Aid Administration": {
                "Financial aid processing time": "Average days to process aid applications",
                "Award accuracy rate": "(Accurate awards / Total awards) * 100",
                "Compliance with aid regulations": "(Compliant processes / Total processes) * 100",
                "Student satisfaction with aid services": "Average aid service satisfaction"
            },
            "Strengthen Registrar Operations": {
                "Course registration efficiency": "(Efficient registrations / Total registrations) * 100",
                "Transcript processing time": "Average days to process transcript requests",
                "Degree audit accuracy": "(Accurate audits / Total audits) * 100",
                "Registration system reliability": "(Reliable system / Total operation time) * 100"
            },
            "Improve Facilities Management": {
                "Maintenance request completion": "(Completed requests / Total requests) * 100",
                "Facility condition improvement": "((Current condition - Previous condition) / Previous) * 100",
                "Energy efficiency improvement": "((Current efficiency - Previous efficiency) / Previous) * 100",
                "Space utilization optimization": "(Optimized space / Total space) * 100"
            },
            "Enhance Campus Safety and Security": {
                "Safety incident reduction": "((Previous incidents - Current incidents) / Previous) * 100",
                "Emergency response time": "Average time to emergency response",
                "Security system reliability": "(Reliable systems / Total systems) * 100",
                "Campus safety satisfaction": "Average safety satisfaction score"
            },
            "Optimize Procurement and Supply Chain": {
                "Procurement cycle time reduction": "((Previous cycle time - Current cycle time) / Previous) * 100",
                "Vendor performance improvement": "((Current performance - Previous performance) / Previous) * 100",
                "Cost savings achievement": "(Actual savings / Target savings) * 100",
                "Sustainable procurement rate": "(Sustainable purchases / Total purchases) * 100"
            },
            "Improve Event and Conference Management": {
                "Event planning efficiency": "(Efficient planning / Total planning) * 100",
                "Participant satisfaction score": "Average event satisfaction score",
                "Facility utilization for events": "(Utilized facilities / Available facilities) * 100",
                "Revenue generation from events": "Event revenue / Total event costs * 100"
            }
        }
    },

    "Learning & Growth Perspective": {
        "Organizational Learning & Development": {
            "Enhance Institutional Research and Assessment": {
                "Research project completion rate": "(Completed projects / Total projects) * 100",
                "Data-driven decision rate": "(Data-informed decisions / Total decisions) * 100",
                "Assessment methodology improvement": "((Current methodology - Previous) / Previous) * 100",
                "Research impact on policy": "(Influenced policies / Total research) * 100"
            },
            "Improve Knowledge Management Systems": {
                "Knowledge sharing participation": "(Participating staff / Total staff) * 100",
                "Best practice adoption rate": "(Adopted practices / Available practices) * 100",
                "Document management efficiency": "(Efficient management / Total documents) * 100",
                "Knowledge retention effectiveness": "(Retained knowledge / Total knowledge) * 100"
            },
            "Strengthen Continuous Improvement Culture": {
                "Improvement initiative participation": "(Participating employees / Total employees) * 100",
                "Process improvement success rate": "(Successful improvements / Total improvements) * 100",
                "Innovation suggestion rate": "(Submitted suggestions / Total employees) * 100",
                "Quality improvement measurement": "(Measured improvements / Total improvements) * 100"
            },
            "Enhance Leadership Development Programs": {
                "Leadership training completion": "(Completed training / Required training) * 100",
                "Leadership competency improvement": "((Current competency - Previous competency) / Previous) * 100",
                "Succession plan readiness": "(Ready successors / Key positions) * 100",
                "Leadership program satisfaction": "Average leadership program satisfaction"
            },
            "Improve Change Management Capability": {
                "Change initiative success rate": "(Successful initiatives / Total initiatives) * 100",
                "Employee change readiness": "Average change readiness assessment",
                "Change adoption rate improvement": "((Current adoption - Previous adoption) / Previous) * 100",
                "Change resistance reduction": "((Previous resistance - Current resistance) / Previous) * 100"
            },
            "Strengthen Strategic Planning Processes": {
                "Strategic goal achievement": "(Achieved goals / Total goals) * 100",
                "Planning process satisfaction": "Average planning process satisfaction",
                "Stakeholder input integration": "(Integrated input / Total planning) * 100",
                "Strategic alignment score": "Composite score of organizational alignment"
            },
            "Enhance Performance Management Systems": {
                "Performance review completion": "(Completed reviews / Total employees) * 100",
                "Goal achievement rate": "(Achieved goals / Total goals) * 100",
                "Feedback quality improvement": "((Current quality - Previous quality) / Previous) * 100",
                "Development plan implementation": "(Implemented plans / Total plans) * 100"
            },
            "Improve Organizational Agility and Resilience": {
                "Agility index score": "Composite score of organizational agility",
                "Response time to challenges": "Average time to respond to challenges",
                "Adaptive capacity improvement": "((Current capacity - Previous capacity) / Previous) * 100",
                "Crisis management effectiveness": "(Effective management / Total crises) * 100"
            }
        },

        "Innovation & Educational Research": {
            "Enhance Educational Innovation Programs": {
                "Innovation project initiation": "(Initiated projects / Proposed projects) * 100",
                "Educational technology adoption rate": "(Adopted technologies / Available technologies) * 100",
                "Pedagogical innovation implementation": "(Implemented innovations / Total innovations) * 100",
                "Innovation impact measurement": "(Measured impact / Total innovations) * 100"
            },
            "Improve Research and Development Infrastructure": {
                "R&D facility utilization": "(Utilized facilities / Available facilities) * 100",
                "Research equipment availability": "(Available equipment / Required equipment) * 100",
                "Collaborative research space effectiveness": "(Effective spaces / Total spaces) * 100",
                "Research support service satisfaction": "Average research support satisfaction"
            },
            "Strengthen Intellectual Property Management": {
                "IP disclosure rate": "(Disclosed inventions / Total inventions) * 100",
                "Patent application success": "(Successful applications / Total applications) * 100",
                "Technology transfer effectiveness": "(Effective transfers / Total transfers) * 100",
                "Commercialization revenue growth": "((Current revenue - Previous revenue) / Previous) * 100"
            },
            "Optimize Innovation Ecosystem Development": {
                "Industry partnership innovation": "(Innovative partnerships / Total partnerships) * 100",
                "Startup incubation success": "(Successful incubations / Total incubations) * 100",
                "Innovation network expansion": "((Current network - Previous network) / Previous) * 100",
                "Cross-sector collaboration rate": "(Collaborative projects / Total projects) * 100"
            },
            "Enhance Educational Research Quality": {
                "Research publication rate": "(Published research / Completed research) * 100",
                "Citation impact improvement": "((Current impact - Previous impact) / Previous) * 100",
                "Peer review success rate": "(Successful reviews / Total submissions) * 100",
                "Research methodology innovation": "(Innovative methods / Total methods) * 100"
            },
            "Improve Grant Writing and Management": {
                "Grant writing training effectiveness": "(Effective training / Total training) * 100",
                "Grant management compliance": "(Compliant management / Total grants) * 100",
                "Multi-investigator grant success": "(Successful team grants / Total team grants) * 100",
                "Grant outcome achievement": "(Achieved outcomes / Funded outcomes) * 100"
            },
            "Strengthen Research Ethics and Compliance": {
                "IRB approval efficiency": "(Efficient approvals / Total approvals) * 100",
                "Research ethics training completion": "(Completed training / Required training) * 100",
                "Compliance audit success rate": "(Successful audits / Total audits) * 100",
                "Research integrity assessment": "(Integrity maintained / Total research) * 100"
            },
            "Enhance Knowledge Translation and Dissemination": {
                "Research dissemination effectiveness": "(Effective dissemination / Total research) * 100",
                "Public engagement in research": "(Engaged public / Target public) * 100",
                "Policy impact from research": "(Influenced policies / Total research) * 100",
                "Community research partnership satisfaction": "Average partnership satisfaction"
            }
        },

        "Technology & Digital Transformation": {
            "Improve Digital Literacy Development": {
                "Digital skills assessment improvement": "((Current skills - Previous skills) / Previous) * 100",
                "Technology training participation": "(Participating community / Total community) * 100",
                "Digital tool proficiency growth": "((Current proficiency - Previous proficiency) / Previous) * 100",
                "Technology confidence improvement": "((Current confidence - Previous confidence) / Previous) * 100"
            },
            "Enhance Educational Technology Integration": {
                "Technology integration success rate": "(Successful integrations / Total integrations) * 100",
                "EdTech ROI achievement": "(Achieved ROI / Target ROI) * 100",
                "User adoption rate improvement": "((Current adoption - Previous adoption) / Previous) * 100",
                "Technology-enhanced learning effectiveness": "(Effective enhancement / Total enhancement) * 100"
            },
            "Strengthen Data Analytics Capability": {
                "Analytics platform utilization": "(Utilized platform / Available platform) * 100",
                "Predictive modeling accuracy": "(Accurate predictions / Total predictions) * 100",
                "Data-driven intervention effectiveness": "(Effective interventions / Total interventions) * 100",
                "Analytics skill development": "(Developed skills / Required skills) * 100"
            },
            "Optimize Cloud Infrastructure and Services": {
                "Cloud service reliability": "(Reliable services / Total services) * 100",
                "Cloud cost optimization": "((Previous costs - Current costs) / Previous) * 100",
                "Cloud security compliance": "(Compliant security / Total security) * 100",
                "User satisfaction with cloud services": "Average cloud service satisfaction"
            },
            "Enhance Cybersecurity Awareness and Training": {
                "Security awareness training completion": "(Completed training / Required training) * 100",
                "Phishing test success rate": "(Successful tests / Total tests) * 100",
                "Security incident response time": "Average time to security incident response",
                "Data protection compliance rate": "(Compliant data / Total data) * 100"
            },
            "Improve IT Governance and Strategy": {
                "IT governance effectiveness": "(Effective governance / Total governance) * 100",
                "Technology strategy alignment": "(Aligned strategy / Total strategy) * 100",
                "IT project success rate": "(Successful projects / Total projects) * 100",
                "Technology investment optimization": "(Optimized investments / Total investments) * 100"
            },
            "Strengthen Digital Accessibility and Inclusion": {
                "Digital accessibility compliance": "(Compliant digital assets / Total digital assets) * 100",
                "Assistive technology availability": "(Available technology / Required technology) * 100",
                "Universal design implementation": "(Implemented design / Total design) * 100",
                "Accessibility training completion": "(Completed training / Required training) * 100"
            },
            "Enhance Emerging Technology Adoption": {
                "Emerging technology evaluation rate": "(Evaluated technologies / Available technologies) * 100",
                "AI and machine learning implementation": "(Implemented AI/ML / Available AI/ML) * 100",
                "Technology pilot success rate": "(Successful pilots / Total pilots) * 100",
                "Future-ready technology infrastructure": "(Ready infrastructure / Total infrastructure) * 100"
            }
        },

        "Strategic Partnerships & Community Engagement": {
            "Enhance Industry-Academia Collaboration": {
                "Industry partnership satisfaction": "Average partnership satisfaction score",
                "Work-integrated learning opportunities": "(Available opportunities / Required opportunities) * 100",
                "Joint research project success": "(Successful projects / Total projects) * 100",
                "Industry feedback integration": "(Integrated feedback / Total feedback) * 100"
            },
            "Improve Community Outreach and Service": {
                "Community service participation": "(Participating members / Total members) * 100",
                "Outreach program effectiveness": "(Effective programs / Total programs) * 100",
                "Community need assessment completion": "(Completed assessments / Required assessments) * 100",
                "Local impact measurement": "(Measured impact / Total impact) * 100"
            },
            "Strengthen Global Educational Partnerships": {
                "International partnership satisfaction": "Average international partnership satisfaction",
                "Global learning opportunity creation": "(Created opportunities / Required opportunities) * 100",
                "Cross-cultural program effectiveness": "(Effective programs / Total programs) * 100",
                "International student exchange success": "(Successful exchanges / Total exchanges) * 100"
            },
            "Optimize Alumni Relations and Engagement": {
                "Alumni network growth": "((Current network - Previous network) / Previous) * 100",
                "Alumni event participation": "(Participating alumni / Total alumni) * 100",
                "Alumni mentorship program effectiveness": "(Effective mentorship / Total mentorship) * 100",
                "Alumni career support satisfaction": "Average career support satisfaction"
            },
            "Enhance Government and Policy Engagement": {
                "Policy advocacy effectiveness": "(Effective advocacy / Total advocacy) * 100",
                "Government relationship satisfaction": "Average relationship satisfaction",
                "Regulatory compliance improvement": "((Current compliance - Previous compliance) / Previous) * 100",
                "Public policy contribution": "(Contributed policies / Total policy engagements) * 100"
            },
            "Improve Educational Consortium Participation": {
                "Consortium collaboration effectiveness": "(Effective collaboration / Total collaboration) * 100",
                "Shared resource utilization": "(Utilized resources / Available resources) * 100",
                "Joint program success rate": "(Successful programs / Total programs) * 100",
                "Consortium value contribution": "(Contributed value / Total value) * 100"
            },
            "Strengthen K-12 and Higher Education Alignment": {
                "Educational pathway effectiveness": "(Effective pathways / Total pathways) * 100",
                "College readiness program success": "(Successful programs / Total programs) * 100",
                "Teacher professional development collaboration": "(Collaborative development / Total development) * 100",
                "Dual credit program quality": "(Quality programs / Total programs) * 100"
            },
            "Enhance Research and Innovation Networks": {
                "Research network participation": "(Participating researchers / Total researchers) * 100",
                "Collaborative publication rate": "(Collaborative publications / Total publications) * 100",
                "Knowledge sharing effectiveness": "(Effective sharing / Total sharing) * 100",
                "Network impact measurement": "(Measured impact / Total network) * 100"
            }
        }
    }
}
