#
# from management_project.models import Vision, OrganizationalProfile
#
#
# class VisionService:
#     # Nested mapping: sector -> classification -> list of vision statements
#     SECTOR_VISION_MAP = {
#         'education': {
#             'profitable': [
#                 "To create a world where every mind has access to learning",
#                 "To empower lifelong learners with innovative tools",
#                 "To foster curiosity, creativity, and critical thinking in all students",
#                 "To transform classrooms into hubs of innovation",
#                 "To inspire communities to value knowledge and growth",
#             ],
#             'non_profitable': [
#                 "To provide free access to quality education for all",
#                 "To support underserved communities with innovative learning",
#                 "To bridge educational inequality globally",
#                 "To nurture talent and lifelong skills in all learners",
#                 "To promote ethical and responsible citizenship through education",
#             ]
#         },
#
#         'healthcare': {
#             'profitable': [
#                 "To ensure health and well-being for every individual",
#                 "To leverage technology for better patient outcomes",
#                 "To expand access to premium healthcare services",
#                 "To optimize healthcare operations efficiently",
#                 "To innovate for sustainable healthcare solutions",
#             ],
#             'non_profitable': [
#                 "To provide healthcare access to underserved communities",
#                 "To reduce disparities in health globally",
#                 "To promote preventive care for vulnerable populations",
#                 "To support community-based health initiatives",
#                 "To foster collaboration among non-profit healthcare providers",
#             ]
#         },
#
#         'information_technology': {
#             'profitable': [
#                 "To empower businesses with digital transformation",
#                 "To provide secure and reliable IT solutions",
#                 "To innovate in cloud, AI, and automation services",
#                 "To accelerate growth with scalable IT solutions",
#                 "To lead the industry in technology solutions",
#             ],
#             'non_profitable': [
#                 "To provide open-source technology solutions for communities",
#                 "To support digital literacy programs globally",
#                 "To leverage IT for social impact projects",
#                 "To promote access to technology for underserved groups",
#                 "To foster innovation in educational technology",
#             ]
#         },
#
#         'finance_banking': {
#             'profitable': [
#                 "To innovate financial solutions for every client need",
#                 "To optimize banking operations through technology",
#                 "To provide secure, transparent financial services",
#                 "To expand wealth management and investment solutions",
#                 "To lead in global financial innovation",
#             ],
#             'non_profitable': [
#                 "To provide financial literacy and inclusion programs",
#                 "To support microfinance for underserved communities",
#                 "To enable access to basic banking services globally",
#                 "To foster responsible investment and social finance",
#                 "To empower non-profit organizations financially",
#             ]
#         },
#
#         'agriculture': {
#             'profitable': [
#                 "To maximize agricultural productivity sustainably",
#                 "To adopt modern farming and agritech solutions",
#                 "To optimize supply chains for high-value crops",
#                 "To innovate in agribusiness for competitive markets",
#                 "To expand global access to quality agricultural products",
#             ],
#             'non_profitable': [
#                 "To support smallholder farmers in developing regions",
#                 "To improve food security and nutrition globally",
#                 "To promote sustainable and environmentally friendly farming",
#                 "To provide training and tools for rural communities",
#                 "To reduce waste and maximize local food availability",
#             ]
#         },
#
#         'manufacturing': {
#             'profitable': [
#                 "To design and deliver quality products efficiently",
#                 "To adopt smart manufacturing and automation",
#                 "To enhance productivity through lean manufacturing",
#                 "To expand market reach with scalable production",
#                 "To lead in industrial innovation and sustainability",
#             ],
#             'non_profitable': [
#                 "To provide vocational training in manufacturing skills",
#                 "To support community-based production initiatives",
#                 "To implement sustainable and low-impact manufacturing",
#                 "To promote collaboration for socially responsible products",
#                 "To reduce waste and increase resource efficiency in local industries",
#             ]
#         },
#
#         'energy_utilities': {
#             'profitable': [
#                 "To provide reliable and sustainable energy solutions",
#                 "To optimize energy efficiency across operations",
#                 "To innovate in renewable and smart energy systems",
#                 "To expand energy access to high-value markets",
#                 "To lead in global energy innovation",
#             ],
#             'non_profitable': [
#                 "To provide clean energy access to underserved communities",
#                 "To reduce environmental impact of energy projects",
#                 "To support community-based energy solutions",
#                 "To promote renewable energy education",
#                 "To foster sustainable energy practices for social impact",
#             ]
#         },
#
#         'transport_logistics': {
#             'profitable': [
#                 "To optimize global logistics with cutting-edge solutions",
#                 "To deliver goods efficiently and reliably",
#                 "To innovate in supply chain and mobility services",
#                 "To expand transport solutions to premium clients",
#                 "To lead in transport innovation and infrastructure",
#             ],
#             'non_profitable': [
#                 "To provide safe and reliable transport for underserved areas",
#                 "To optimize public logistics and community mobility",
#                 "To foster sustainable and low-carbon transportation",
#                 "To support educational and health transport initiatives",
#                 "To enhance access to essential services via transport",
#             ]
#         },
#
#         'tourism_hospitality': {
#             'profitable': [
#                 "To provide exceptional travel experiences",
#                 "To expand luxury hospitality services globally",
#                 "To innovate in tourism offerings and experiences",
#                 "To optimize guest satisfaction and loyalty",
#                 "To lead in premium tourism and hotel services",
#             ],
#             'non_profitable': [
#                 "To promote sustainable and community-based tourism",
#                 "To increase access to travel experiences for all",
#                 "To foster cultural appreciation and local engagement",
#                 "To provide training and opportunities in hospitality",
#                 "To support eco-tourism and social impact travel",
#             ]
#         },
#     }


from management_project.models import Vision, OrganizationalProfile
from typing import List, Tuple, Optional
import random


class VisionService:
    """
    A comprehensive vision statement service providing tailored visions
    based on sector and organization classification (profitable/non-profitable).
    """

    SECTOR_VISION_MAP = {
        'agriculture': {
            'profitable': [
                "To become the leading agribusiness enterprise through innovation and sustainable practices",
                "To maximize shareholder value through efficient farming operations and market expansion",
                "To dominate agricultural markets with premium quality products and strong brand recognition",
                "To achieve consistent growth through technological innovation in precision agriculture",
                "To revolutionize farming practices through data-driven decision making and automation",
                "To build a diversified agricultural portfolio spanning multiple product lines and regions",
                "To create the world's most efficient farm-to-consumer supply chain system",
                "To lead the industry in sustainable practices that optimize environmental resources",
                "To optimize crop yields and quality through advanced genetics and cultivation techniques",
                "To establish new standards for organic and specialty crop production worldwide",
                "To deliver superior returns to investors through disciplined capital management",
                "To develop innovative agricultural products meeting evolving consumer preferences",
                "To build lasting partnerships with retailers, distributors, and food processors",
                "To achieve cost leadership through scale economies and process optimization",
                "To create proprietary technologies providing sustainable competitive advantages",
                "To develop high-value products commanding premium prices in global markets",
                "To expand into emerging markets with significant growth potential",
                "To build resilient operations withstanding climate and market volatility",
                "To pioneer digital agriculture solutions transforming farm management",
                "To create enduring value for shareholders, customers, and partners"
            ],
            'non_profitable': [
                "To eliminate hunger and malnutrition through sustainable community-based food systems",
                "To promote agricultural practices preserving biodiversity and ecosystem health",
                "To empower small-scale farmers with knowledge, resources, and market access",
                "To advocate for fair trade policies ensuring equitable returns for producers",
                "To preserve traditional farming knowledge and protect indigenous crop varieties",
                "To combat food insecurity through locally adapted and culturally appropriate solutions",
                "To promote climate-resilient agriculture withstanding environmental challenges",
                "To secure land rights and resource access for marginalized farming communities",
                "To build local food economies supporting rural development and food sovereignty",
                "To influence policies prioritizing family farms and sustainable agriculture",
                "To advance agroecological practices working in harmony with natural systems",
                "To ensure communities maintain control over their food systems and resources",
                "To protect agricultural biodiversity as the foundation of food security",
                "To strengthen farmer cooperatives enhancing collective bargaining power",
                "To promote gender equality and women's leadership in agriculture",
                "To ensure sustainable water management practices in agricultural communities",
                "To combat soil degradation and promote land restoration initiatives",
                "To advocate for responsible agricultural investments benefiting communities",
                "To engage youth in agriculture as a viable and rewarding career path",
                "To build community resilience through diversified farming systems"
            ]
        },

        'mining': {
            'profitable': [
                "To become the industry's safest and most efficient mining company globally",
                "To maximize shareholder returns through disciplined resource development",
                "To dominate mineral markets with superior extraction and processing technologies",
                "To achieve operational excellence across all mining operations worldwide",
                "To revolutionize mining through automation, digitalization, and innovation",
                "To build a diversified mineral portfolio across multiple commodities",
                "To establish new benchmarks for environmental stewardship in mining",
                "To lead the industry in community engagement and social responsibility",
                "To optimize resource recovery through advanced mineral processing",
                "To set new standards for safety performance and workplace culture",
                "To deliver consistent returns through strategic capital allocation",
                "To develop innovative solutions for complex mining challenges",
                "To build strong, mutually beneficial relationships with host communities",
                "To achieve cost leadership through operational efficiency and innovation",
                "To create proprietary technologies transforming mining practices",
                "To generate value through strategic partnerships and joint ventures",
                "To expand into new mineral resources and geographic markets",
                "To build resilient operations adapting to changing market conditions",
                "To lead in responsible tailings management and mine closure practices",
                "To create sustainable long-term value for all stakeholders"
            ],
            'non_profitable': [
                "To protect communities and ecosystems from adverse mining impacts",
                "To advocate for transparent and accountable mining operations worldwide",
                "To ensure mining revenues benefit local communities fairly and equitably",
                "To promote environmental justice in mining-affected regions",
                "To preserve cultural heritage sites and indigenous territories from mining",
                "To combat illegal mining and its destructive environmental consequences",
                "To ensure proper mine closure and comprehensive site rehabilitation",
                "To advocate for stronger mining regulations and effective enforcement",
                "To promote meaningful community participation in mining decisions",
                "To protect water resources from mining contamination and overuse",
                "To secure indigenous rights in mining development and operations",
                "To promote sustainable alternative livelihoods in mining regions",
                "To advocate for fair revenue sharing from mineral resource extraction",
                "To combat corruption in mining licensing and revenue management",
                "To promote formalization and support for artisanal mining communities",
                "To ensure gender equality and women's rights in mining areas",
                "To advocate for climate-responsible mining practices and emissions reduction",
                "To promote circular economy principles in mineral use and recycling",
                "To ensure human rights protection throughout mining operations",
                "To build community resilience and capacity in mining-affected regions"
            ]
        },

        'manufacturing': {
            'profitable': [
                "To become the manufacturing partner of choice for global industry leaders",
                "To maximize profitability through operational excellence and efficiency",
                "To dominate product categories with superior quality and innovation",
                "To achieve world-class manufacturing standards across all facilities",
                "To revolutionize production through Industry 4.0 digital technologies",
                "To build a diversified manufacturing portfolio across multiple sectors",
                "To establish new benchmarks for sustainable manufacturing practices",
                "To lead in product design, development, and engineering excellence",
                "To optimize supply chain management and inventory control systems",
                "To establish a global manufacturing footprint with local presence",
                "To deliver superior returns to shareholders through strategic growth",
                "To create innovative products that anticipate and meet market needs",
                "To build strong, lasting customer relationships and brand loyalty",
                "To achieve cost leadership through continuous improvement",
                "To develop proprietary manufacturing technologies and processes",
                "To create value through strategic acquisitions and partnerships",
                "To expand into high-growth market segments and geographic regions",
                "To build resilient manufacturing operations with business continuity",
                "To lead in quality management systems and industry certifications",
                "To create sustainable value for customers, employees, and communities"
            ],
            'non_profitable': [
                "To promote ethical manufacturing practices across global supply chains",
                "To advocate for workers' rights, fair wages, and decent working conditions",
                "To ensure safe and healthy working environments in manufacturing facilities",
                "To promote environmental sustainability in manufacturing operations",
                "To combat forced labor, child labor, and modern slavery in manufacturing",
                "To ensure responsible and transparent supply chain management",
                "To promote circular economy principles in production and consumption",
                "To advocate for green manufacturing practices and clean production",
                "To ensure local communities benefit from manufacturing operations",
                "To promote gender equality and women's empowerment in manufacturing",
                "To combat industrial pollution and environmental degradation",
                "To ensure product safety, quality, and responsible consumption",
                "To promote local manufacturing creating quality employment",
                "To advocate for sustainable resource use and waste reduction",
                "To ensure transparency and accountability in manufacturing operations",
                "To promote innovation in sustainable product design and manufacturing",
                "To ensure fair trade practices in manufactured goods markets",
                "To promote waste reduction, recycling, and material efficiency",
                "To ensure energy efficiency and renewable energy adoption",
                "To build sustainable manufacturing communities and local economies"
            ]
        },

        'construction': {
            'profitable': [
                "To become the most trusted and reliable construction company in the industry",
                "To maximize returns through exceptional project execution and management",
                "To dominate construction markets with unparalleled quality and reliability",
                "To achieve superior project delivery consistently on time and within budget",
                "To revolutionize construction through cutting-edge technology and innovation",
                "To build a diverse portfolio of landmark construction projects and services",
                "To establish new industry standards for sustainable construction practices",
                "To lead in construction innovation and advanced building technologies",
                "To optimize project management processes and operational systems",
                "To establish a strong national construction presence and stellar reputation",
                "To maximize shareholder value through strategic growth and expansion",
                "To create innovative construction solutions and groundbreaking methodologies",
                "To build strong, collaborative, and lasting client relationships",
                "To achieve cost efficiency and value engineering excellence",
                "To develop proprietary construction methods and advanced techniques",
                "To create exceptional value through strategic projects and partnerships",
                "To expand into new construction segments and specialized services",
                "To build resilient construction operations and robust capabilities",
                "To lead in safety performance and quality assurance standards",
                "To create lasting value for clients, communities, and all stakeholders"
            ],
            'non_profitable': [
                "To ensure adequate, safe, and affordable housing for all people",
                "To advocate for construction workers' rights and fair treatment",
                "To promote sustainable and environmentally friendly building practices",
                "To ensure safe and healthy working conditions on construction sites",
                "To combat substandard construction and prevent building failures",
                "To ensure meaningful community participation in construction planning",
                "To promote green building standards and energy efficiency measures",
                "To advocate for affordable housing and innovative shelter solutions",
                "To ensure disaster-resilient construction and enhanced building safety",
                "To promote local construction materials and traditional techniques",
                "To ensure universal accessibility and inclusive design in buildings",
                "To promote energy-efficient and climate-responsive construction methods",
                "To ensure fair wages and comprehensive benefits for construction workers",
                "To promote community-led construction and self-build programs",
                "To ensure environmental protection and conservation during construction",
                "To promote traditional building skills and preserve craftsmanship",
                "To ensure transparent and ethical construction practices industry-wide",
                "To promote waste reduction and recycling initiatives in construction",
                "To ensure quality construction standards and regulatory compliance",
                "To build sustainable, inclusive, and resilient communities worldwide"
            ]
        },

        'energy': {
            'profitable': [
                "To become the leading provider of reliable and sustainable energy solutions",
                "To maximize energy production efficiency and distribution optimization",
                "To dominate energy markets with competitive pricing and superior service",
                "To achieve operational excellence across all energy generation facilities",
                "To revolutionize energy production through technological innovation",
                "To build a diversified energy portfolio across multiple renewable sources",
                "To establish new industry standards for sustainable energy development",
                "To lead in energy innovation and cutting-edge technology development",
                "To optimize energy distribution systems and smart grid management",
                "To establish comprehensive energy infrastructure networks",
                "To maximize shareholder returns through strategic growth initiatives",
                "To create innovative energy efficiency solutions and services",
                "To build strong customer relationships and ensure high satisfaction",
                "To achieve cost leadership in energy production and distribution",
                "To develop proprietary energy technologies and advanced solutions",
                "To create exceptional value through strategic partnerships",
                "To expand energy services and broaden geographic coverage",
                "To build resilient energy operations and robust systems",
                "To lead in safety standards and environmental performance metrics",
                "To create sustainable energy value for all stakeholders"
            ],
            'non_profitable': [
                "To promote rapid and equitable transition to renewable energy sources",
                "To advocate for universal access to affordable clean energy worldwide",
                "To ensure just transition from fossil fuels to sustainable energy systems",
                "To combat energy poverty and ensure basic energy access for all",
                "To ensure local communities benefit fairly from energy projects",
                "To promote comprehensive energy conservation and efficiency measures",
                "To advocate for decisive climate action and emissions reduction",
                "To ensure fair and transparent energy pricing structures",
                "To promote community-owned and locally managed energy solutions",
                "To ensure environmental protection in all energy development projects",
                "To promote energy democracy and enhanced community control",
                "To advocate for progressive energy policies and effective regulations",
                "To ensure sustainable and responsible energy development practices",
                "To promote energy education and widespread public awareness",
                "To ensure rapid renewable energy adoption and seamless integration",
                "To promote community energy ownership and equitable benefits",
                "To ensure energy justice and equitable access for all populations",
                "To promote green energy technologies and sustainable innovation",
                "To ensure transparent energy operations and impact assessment",
                "To build community energy resilience and long-term security"
            ]
        },

        'transport': {
            'profitable': [
                "To become the world's most efficient transport and logistics provider",
                "To maximize profitability through optimized operations and premium services",
                "To dominate transport markets with superior reliability and service quality",
                "To achieve operational excellence across all transport operations globally",
                "To revolutionize transport through advanced technology and innovation",
                "To build a diversified transport portfolio across all modes and regions",
                "To establish new industry standards for sustainable transport practices",
                "To lead in transport innovation and service development excellence",
                "To optimize route planning and sophisticated fleet management systems",
                "To establish comprehensive transport networks and infrastructure",
                "To maximize shareholder returns through strategic expansion",
                "To create innovative transport solutions and enhanced services",
                "To build strong customer relationships and ensure lasting loyalty",
                "To achieve cost leadership in transport operations and management",
                "To develop proprietary transport technologies and advanced systems",
                "To create exceptional value through strategic partnerships",
                "To expand transport services and extend geographic coverage",
                "To build resilient transport operations and robust networks",
                "To lead in safety standards and operational performance metrics",
                "To create sustainable transport value for all stakeholders"
            ],
            'non_profitable': [
                "To promote accessible and affordable transport for all people",
                "To advocate for sustainable and environmentally friendly transport systems",
                "To ensure transport systems effectively serve community needs",
                "To combat transport-related pollution and environmental damage",
                "To ensure transport benefits local communities and economies",
                "To promote public transport and shared mobility solutions",
                "To advocate for transport safety and comprehensive user protection",
                "To ensure fair and equitable transport access for all",
                "To promote non-motorized and active transport options",
                "To ensure environmental protection in transport development",
                "To promote transport justice and equitable access systems",
                "To advocate for progressive transport policies and planning",
                "To ensure sustainable transport system development worldwide",
                "To promote transport education and enhanced user awareness",
                "To ensure accessible transport for vulnerable population groups",
                "To promote community participation in transport planning",
                "To ensure transparent transport operations and fair pricing",
                "To promote green transport technologies and clean fuels",
                "To ensure transport worker rights and fair treatment",
                "To build community transport resilience and connectivity"
            ]
        },

        'trade': {
            'profitable': [
                "To become the leading global trade and commerce enterprise",
                "To maximize profitability through efficient trade operations",
                "To dominate trade markets with superior service and reliability",
                "To achieve operational excellence in all trade activities",
                "To revolutionize trade through digital platforms and innovation",
                "To build a diversified trade portfolio across products and regions",
                "To establish new standards for ethical and sustainable trade",
                "To lead in trade innovation and market development",
                "To optimize supply chain and logistics management",
                "To establish comprehensive global trade networks",
                "To maximize shareholder returns through strategic growth",
                "To create innovative trade solutions and services",
                "To build strong partner relationships and networks",
                "To achieve cost leadership in trade operations",
                "To develop proprietary trade technologies and platforms",
                "To create value through strategic alliances and partnerships",
                "To expand trade services and market coverage",
                "To build resilient trade operations and supply chains",
                "To lead in trade compliance and risk management",
                "To create sustainable trade value for all stakeholders"
            ],
            'non_profitable': [
                "To promote fair and equitable trade practices globally",
                "To advocate for trade justice and producer rights protection",
                "To ensure trade benefits marginalized communities fairly",
                "To combat exploitative trade practices and relationships",
                "To ensure transparent and accountable trade systems",
                "To promote local and regional trade development",
                "To advocate for sustainable and ethical trade standards",
                "To ensure community participation in trade decisions",
                "To promote traditional products and artisan trades",
                "To ensure environmental sustainability in trade",
                "To promote trade education and capacity building",
                "To advocate for progressive trade policies and agreements",
                "To ensure sustainable trade system development",
                "To promote fair trade certification and standards",
                "To ensure gender equality in trade opportunities",
                "To promote community-based trade initiatives",
                "To ensure transparent trade operations and impacts",
                "To promote green trade practices and products",
                "To ensure trade worker rights and fair treatment",
                "To build community trade resilience and capacity"
            ]
        },

        'finance': {
            'profitable': [
                "To become the most trusted and innovative financial institution",
                "To maximize profitability through diversified financial services",
                "To dominate financial markets with superior products and service",
                "To achieve operational excellence across all financial operations",
                "To revolutionize finance through technology and digital innovation",
                "To build a diversified financial portfolio and service offering",
                "To establish new standards for ethical and transparent finance",
                "To lead in financial innovation and product development",
                "To optimize risk management and compliance systems",
                "To establish comprehensive financial networks and partnerships",
                "To maximize shareholder returns through strategic growth",
                "To create innovative financial solutions and services",
                "To build strong client relationships and trust",
                "To achieve cost leadership in financial operations",
                "To develop proprietary financial technologies and platforms",
                "To create value through strategic acquisitions and partnerships",
                "To expand financial services and market presence",
                "To build resilient financial operations and systems",
                "To lead in compliance standards and regulatory excellence",
                "To create sustainable financial value for all stakeholders"
            ],
            'non_profitable': [
                "To promote financial inclusion and access for all people",
                "To advocate for transparent and ethical financial systems",
                "To ensure financial services benefit marginalized communities",
                "To combat predatory lending and financial exploitation",
                "To ensure fair and equitable financial access worldwide",
                "To promote community banking and microfinance initiatives",
                "To advocate for financial literacy and comprehensive education",
                "To ensure responsible and sustainable financial practices",
                "To promote local financial institutions and cooperatives",
                "To ensure environmental consideration in financial decisions",
                "To promote financial justice and consumer protection",
                "To advocate for progressive financial policies and regulations",
                "To ensure sustainable financial system development",
                "To promote financial education and capability building",
                "To ensure accessible financial services for vulnerable groups",
                "To promote community-based financial initiatives",
                "To ensure transparent financial operations and reporting",
                "To promote green finance and sustainable investment",
                "To ensure financial worker rights and fair treatment",
                "To build community financial resilience and security"
            ]
        },

        'tourism': {
            'profitable': [
                "To become the leading provider of exceptional tourism experiences",
                "To maximize profitability through quality services and operations",
                "To dominate tourism markets with unique offerings and service",
                "To achieve operational excellence across all tourism operations",
                "To revolutionize tourism through innovation and technology",
                "To build a diversified tourism portfolio and destination network",
                "To establish new standards for sustainable tourism practices",
                "To lead in tourism innovation and experience development",
                "To optimize tourism operations and customer service",
                "To establish comprehensive tourism networks and partnerships",
                "To maximize shareholder returns through strategic growth",
                "To create innovative tourism products and experiences",
                "To build strong customer relationships and loyalty",
                "To achieve cost leadership in tourism operations",
                "To develop proprietary tourism technologies and platforms",
                "To create value through strategic partnerships and ventures",
                "To expand tourism services and destination coverage",
                "To build resilient tourism operations and businesses",
                "To lead in service quality and customer satisfaction",
                "To create sustainable tourism value for all stakeholders"
            ],
            'non_profitable': [
                "To promote responsible and sustainable tourism practices",
                "To advocate for tourism that benefits local communities",
                "To ensure tourism preserves cultural heritage and traditions",
                "To combat exploitative and damaging tourism practices",
                "To ensure fair and equitable tourism benefits distribution",
                "To promote community-based and eco-tourism initiatives",
                "To advocate for tourist rights and responsible travel",
                "To ensure sustainable tourism development and management",
                "To promote local tourism enterprises and employment",
                "To ensure environmental protection in tourism development",
                "To promote tourism education and awareness",
                "To advocate for progressive tourism policies and planning",
                "To ensure sustainable tourism system development",
                "To promote cultural exchange and understanding through tourism",
                "To ensure accessible tourism for all people",
                "To promote community participation in tourism planning",
                "To ensure transparent tourism operations and impacts",
                "To promote green tourism practices and standards",
                "To ensure tourism worker rights and fair treatment",
                "To build community tourism resilience and benefits"
            ]
        },

        'hotels': {
            'profitable': [
                "To become the most preferred hotel brand globally",
                "To maximize profitability through exceptional guest experiences",
                "To dominate hotel markets with superior service and amenities",
                "To achieve operational excellence across all hotel properties",
                "To revolutionize hospitality through innovation and technology",
                "To build a diversified hotel portfolio across categories and regions",
                "To establish new standards for sustainable hotel operations",
                "To lead in hospitality innovation and service excellence",
                "To optimize hotel operations and guest satisfaction",
                "To establish comprehensive hotel networks and systems",
                "To maximize shareholder returns through strategic expansion",
                "To create innovative hotel concepts and experiences",
                "To build strong guest relationships and loyalty",
                "To achieve cost leadership in hotel operations",
                "To develop proprietary hotel technologies and systems",
                "To create value through strategic partnerships and management",
                "To expand hotel services and property portfolio",
                "To build resilient hotel operations and businesses",
                "To lead in service quality and brand reputation",
                "To create sustainable hotel value for all stakeholders"
            ],
            'non_profitable': [
                "To promote ethical and fair hotel employment practices",
                "To advocate for hotels that benefit local communities",
                "To ensure hotels respect cultural and environmental values",
                "To combat exploitative labor practices in hotels",
                "To ensure fair distribution of hotel tourism benefits",
                "To promote community-involved hotel initiatives",
                "To advocate for guest rights and responsible hospitality",
                "To ensure sustainable hotel development and operations",
                "To promote local employment and enterprise in hotels",
                "To ensure environmental protection in hotel operations",
                "To promote hospitality education and training",
                "To advocate for progressive hotel policies and standards",
                "To ensure sustainable hotel industry development",
                "To promote cultural sensitivity in hotel services",
                "To ensure accessible hotel facilities for all guests",
                "To promote community participation in hotel planning",
                "To ensure transparent hotel operations and impacts",
                "To promote green hotel practices and certification",
                "To ensure hotel worker rights and fair treatment",
                "To build community benefits from hotel development"
            ]
        },

        'food': {
            'profitable': [
                "To become the leading provider of quality food products",
                "To maximize profitability through efficient food operations",
                "To dominate food markets with superior products and brands",
                "To achieve operational excellence across food value chain",
                "To revolutionize food production through innovation and technology",
                "To build a diversified food portfolio across categories and regions",
                "To establish new standards for food safety and quality",
                "To lead in food innovation and product development",
                "To optimize food supply chain and distribution",
                "To establish comprehensive food networks and partnerships",
                "To maximize shareholder returns through strategic growth",
                "To create innovative food products and solutions",
                "To build strong customer relationships and trust",
                "To achieve cost leadership in food operations",
                "To develop proprietary food technologies and processes",
                "To create value through strategic acquisitions and partnerships",
                "To expand food services and market presence",
                "To build resilient food operations and supply chains",
                "To lead in food safety and quality standards",
                "To create sustainable food value for all stakeholders"
            ],
            'non_profitable': [
                "To promote food as a basic human right for all",
                "To advocate for sustainable and equitable food systems",
                "To ensure food production benefits local communities",
                "To combat food waste and promote efficient distribution",
                "To ensure safe, nutritious, and adequate food access",
                "To promote local and traditional food systems",
                "To advocate for food sovereignty and security",
                "To ensure sustainable food production practices",
                "To promote small-scale food producers and processors",
                "To ensure environmental protection in food systems",
                "To promote food education and nutrition awareness",
                "To advocate for progressive food policies and regulations",
                "To ensure sustainable food system development",
                "To promote food diversity and cultural heritage",
                "To ensure accessible food for vulnerable populations",
                "To promote community-based food initiatives",
                "To ensure transparent food operations and labeling",
                "To promote organic and sustainable food practices",
                "To ensure food worker rights and fair treatment",
                "To build community food resilience and security"
            ]
        },

        'professional_services': {
            'profitable': [
                "To become the most trusted professional services firm",
                "To maximize profitability through exceptional client service",
                "To dominate professional markets with expertise and quality",
                "To achieve operational excellence across all service lines",
                "To revolutionize professional services through innovation",
                "To build a diversified professional services portfolio",
                "To establish new standards for ethical professional practice",
                "To lead in professional innovation and service development",
                "To optimize service delivery and client management",
                "To establish comprehensive professional networks and partnerships",
                "To maximize shareholder returns through strategic growth",
                "To create innovative professional solutions and services",
                "To build strong client relationships and trust",
                "To achieve cost leadership in service delivery",
                "To develop proprietary methodologies and technologies",
                "To create value through strategic partnerships and alliances",
                "To expand professional services and expertise areas",
                "To build resilient professional operations and capabilities",
                "To lead in professional standards and quality assurance",
                "To create sustainable professional value for all stakeholders"
            ],
            'non_profitable': [
                "To promote access to professional services for all communities",
                "To advocate for ethical and responsible professional practice",
                "To ensure professional services benefit marginalized groups",
                "To combat exploitation and unprofessional practices",
                "To ensure fair and equitable access to professional expertise",
                "To promote pro bono and community service initiatives",
                "To advocate for professional standards and accountability",
                "To ensure sustainable professional practice development",
                "To promote local professional capacity and development",
                "To ensure social responsibility in professional services",
                "To promote professional education and development",
                "To advocate for progressive professional regulations",
                "To ensure sustainable professional sector development",
                "To promote diversity in professional representation",
                "To ensure accessible professional services for all",
                "To promote community-based professional initiatives",
                "To ensure transparent professional operations and conduct",
                "To promote green professional practices and advice",
                "To ensure professional worker rights and fair treatment",
                "To build community professional capacity and access"
            ]
        },

        'ict': {
            'profitable': [
                "To become the leading ICT solutions provider globally",
                "To maximize profitability through innovative technology services",
                "To dominate ICT markets with cutting-edge solutions and support",
                "To achieve operational excellence across all ICT operations",
                "To revolutionize business through digital transformation services",
                "To build a diversified ICT portfolio and service offering",
                "To establish new standards for secure and reliable ICT services",
                "To lead in ICT innovation and technology development",
                "To optimize ICT infrastructure and service delivery",
                "To establish comprehensive ICT networks and partnerships",
                "To maximize shareholder returns through strategic growth",
                "To create innovative ICT solutions and digital services",
                "To build strong client relationships and trust",
                "To achieve cost leadership in ICT operations",
                "To develop proprietary ICT technologies and platforms",
                "To create value through strategic acquisitions and partnerships",
                "To expand ICT services and market presence",
                "To build resilient ICT operations and systems",
                "To lead in cybersecurity and data protection standards",
                "To create sustainable ICT value for all stakeholders"
            ],
            'non_profitable': [
                "To promote digital inclusion and technology access for all",
                "To advocate for open and accessible technology solutions",
                "To ensure ICT benefits underserved and marginalized communities",
                "To combat digital divide and technology inequality",
                "To ensure fair and equitable access to digital resources",
                "To promote digital literacy and skills development",
                "To advocate for digital rights and privacy protection",
                "To ensure sustainable and responsible technology use",
                "To promote local ICT capacity and development",
                "To ensure environmental consideration in technology",
                "To promote digital justice and equitable access",
                "To advocate for progressive technology policies",
                "To ensure sustainable ICT system development",
                "To promote technology education and awareness",
                "To ensure accessible technology for vulnerable groups",
                "To promote community-based technology initiatives",
                "To ensure transparent technology operations",
                "To promote green computing and sustainable ICT",
                "To ensure technology worker rights and fair treatment",
                "To build community digital resilience and capacity"
            ]
        },

        'telecommunications': {
            'profitable': [
                "To become the leading telecommunications provider worldwide",
                "To maximize profitability through efficient network operations",
                "To dominate telecom markets with superior connectivity and service",
                "To achieve operational excellence across all telecom operations",
                "To revolutionize telecommunications through technological innovation",
                "To build a diversified telecom portfolio and service offering",
                "To establish new standards for network reliability and performance",
                "To lead in telecom innovation and service development",
                "To optimize network infrastructure and service delivery",
                "To establish comprehensive telecom networks and coverage",
                "To maximize shareholder returns through strategic growth",
                "To create innovative telecom solutions and services",
                "To build strong customer relationships and loyalty",
                "To achieve cost leadership in telecom operations",
                "To develop proprietary telecom technologies and systems",
                "To create value through strategic partnerships and alliances",
                "To expand telecom services and geographic coverage",
                "To build resilient telecom operations and networks",
                "To lead in network security and quality standards",
                "To create sustainable telecom value for all stakeholders"
            ],
            'non_profitable': [
                "To promote universal telecommunications access for all",
                "To advocate for affordable and reliable communication services",
                "To ensure telecom benefits underserved and remote communities",
                "To combat communication inequality and digital exclusion",
                "To ensure fair and equitable access to communication",
                "To promote community telecommunications initiatives",
                "To advocate for communication rights and access",
                "To ensure sustainable telecom development and operations",
                "To promote local telecom capacity and infrastructure",
                "To ensure environmental protection in telecom operations",
                "To promote communication education and digital literacy",
                "To advocate for progressive telecom policies and regulations",
                "To ensure sustainable telecom system development",
                "To promote affordable communication for all",
                "To ensure accessible telecom for vulnerable populations",
                "To promote community-based telecom initiatives",
                "To ensure transparent telecom operations and pricing",
                "To promote green telecom practices and efficiency",
                "To ensure telecom worker rights and fair treatment",
                "To build community communication resilience and access"
            ]
        },

        'research': {
            'profitable': [
                "To become the leading research and development organization",
                "To maximize profitability through innovative research solutions",
                "To dominate research markets with breakthrough discoveries",
                "To achieve operational excellence across all research operations",
                "To revolutionize industries through cutting-edge research",
                "To build a diversified research portfolio and capabilities",
                "To establish new standards for research quality and impact",
                "To lead in research innovation and methodology development",
                "To optimize research processes and knowledge management",
                "To establish comprehensive research networks and collaborations",
                "To maximize shareholder returns through strategic research",
                "To create innovative research solutions and applications",
                "To build strong research partnerships and collaborations",
                "To achieve cost leadership in research operations",
                "To develop proprietary research methodologies and technologies",
                "To create value through strategic research partnerships",
                "To expand research services and expertise areas",
                "To build resilient research operations and capabilities",
                "To lead in research ethics and quality standards",
                "To create sustainable research value for all stakeholders"
            ],
            'non_profitable': [
                "To promote open science and knowledge sharing globally",
                "To advocate for research that addresses global challenges",
                "To ensure research benefits communities and society",
                "To combat research inequality and knowledge gaps",
                "To ensure fair and equitable access to research",
                "To promote community-based and participatory research",
                "To advocate for research ethics and integrity",
                "To ensure sustainable and responsible research practices",
                "To promote local research capacity and development",
                "To ensure environmental consideration in research",
                "To promote research education and public understanding",
                "To advocate for progressive research policies and funding",
                "To ensure sustainable research system development",
                "To promote research diversity and inclusion",
                "To ensure accessible research for all communities",
                "To promote citizen science and public engagement",
                "To ensure transparent research operations and findings",
                "To promote green research practices and sustainability",
                "To ensure research worker rights and fair treatment",
                "To build community research capacity and engagement"
            ]
        },

        'education': {
            'profitable': [
                "To become the leading provider of quality education services",
                "To maximize profitability through excellent educational programs",
                "To dominate education markets with superior learning outcomes",
                "To achieve operational excellence across all educational operations",
                "To revolutionize education through innovative teaching methods",
                "To build a diversified education portfolio and programs",
                "To establish new standards for educational quality and impact",
                "To lead in educational innovation and curriculum development",
                "To optimize educational processes and student services",
                "To establish comprehensive education networks and partnerships",
                "To maximize shareholder returns through strategic growth",
                "To create innovative educational solutions and programs",
                "To build strong student and parent relationships",
                "To achieve cost leadership in educational operations",
                "To develop proprietary educational methodologies and technologies",
                "To create value through strategic educational partnerships",
                "To expand educational services and program offerings",
                "To build resilient educational operations and institutions",
                "To lead in educational quality and accreditation standards",
                "To create sustainable educational value for all stakeholders"
            ],
            'non_profitable': [
                "To promote education as a fundamental human right for all",
                "To advocate for quality and accessible education worldwide",
                "To ensure education benefits marginalized and underserved communities",
                "To combat educational inequality and access barriers",
                "To ensure fair and equitable access to quality education",
                "To promote community-based and alternative education",
                "To advocate for inclusive and equitable education systems",
                "To ensure sustainable and responsible educational practices",
                "To promote local educational capacity and development",
                "To ensure environmental education and sustainability",
                "To promote lifelong learning and skills development",
                "To advocate for progressive education policies and funding",
                "To ensure sustainable education system development",
                "To promote education for sustainable development",
                "To ensure accessible education for vulnerable populations",
                "To promote community participation in education",
                "To ensure transparent educational operations and outcomes",
                "To promote green schools and sustainable campuses",
                "To ensure education worker rights and fair treatment",
                "To build community educational capacity and access"
            ]
        },

        'health': {
            'profitable': [
                "To become the leading provider of comprehensive healthcare services",
                "To maximize profitability through efficient healthcare operations",
                "To dominate healthcare markets with superior medical outcomes",
                "To achieve operational excellence across all healthcare facilities",
                "To revolutionize healthcare through medical innovation and technology",
                "To build a diversified healthcare portfolio and services",
                "To establish new standards for healthcare quality and safety",
                "To lead in healthcare innovation and treatment development",
                "To optimize healthcare processes and patient services",
                "To establish comprehensive healthcare networks and partnerships",
                "To maximize shareholder returns through strategic growth",
                "To create innovative healthcare solutions and treatments",
                "To build strong patient relationships and trust",
                "To achieve cost leadership in healthcare operations",
                "To develop proprietary medical technologies and treatments",
                "To create value through strategic healthcare partnerships",
                "To expand healthcare services and facility coverage",
                "To build resilient healthcare operations and systems",
                "To lead in medical quality and safety standards",
                "To create sustainable healthcare value for all stakeholders"
            ],
            'non_profitable': [
                "To promote health as a fundamental human right for all",
                "To advocate for universal access to quality healthcare",
                "To ensure healthcare benefits marginalized and vulnerable communities",
                "To combat health inequality and access barriers",
                "To ensure fair and equitable access to healthcare services",
                "To promote community-based and primary healthcare",
                "To advocate for comprehensive public health systems",
                "To ensure sustainable and responsible healthcare practices",
                "To promote local healthcare capacity and development",
                "To ensure environmental health and protection",
                "To promote health education and prevention programs",
                "To advocate for progressive health policies and funding",
                "To ensure sustainable healthcare system development",
                "To promote mental health and wellness services",
                "To ensure accessible healthcare for vulnerable populations",
                "To promote community participation in health planning",
                "To ensure transparent healthcare operations and outcomes",
                "To promote green healthcare practices and sustainability",
                "To ensure healthcare worker rights and fair treatment",
                "To build community health resilience and capacity"
            ]
        },

        'creative': {
            'profitable': [
                "To become the leading creative services and content provider",
                "To maximize profitability through innovative creative solutions",
                "To dominate creative markets with exceptional artistic quality",
                "To achieve operational excellence across all creative operations",
                "To revolutionize creative industries through innovation",
                "To build a diversified creative portfolio and services",
                "To establish new standards for creative excellence and impact",
                "To lead in creative innovation and artistic development",
                "To optimize creative processes and project management",
                "To establish comprehensive creative networks and partnerships",
                "To maximize shareholder returns through strategic growth",
                "To create innovative creative solutions and content",
                "To build strong client relationships and collaborations",
                "To achieve cost leadership in creative operations",
                "To develop proprietary creative technologies and methods",
                "To create value through strategic creative partnerships",
                "To expand creative services and artistic offerings",
                "To build resilient creative operations and studios",
                "To lead in creative quality and industry standards",
                "To create sustainable creative value for all stakeholders"
            ],
            'non_profitable': [
                "To promote creative expression as essential for human development",
                "To advocate for arts and culture access for all communities",
                "To ensure creative industries benefit local communities",
                "To combat creative inequality and access barriers",
                "To ensure fair and equitable access to creative opportunities",
                "To promote community-based and traditional arts",
                "To advocate for cultural preservation and diversity",
                "To ensure sustainable and responsible creative practices",
                "To promote local creative capacity and development",
                "To ensure environmental consideration in creative work",
                "To promote arts education and creative development",
                "To advocate for progressive cultural policies and funding",
                "To ensure sustainable creative sector development",
                "To promote cultural diversity and inclusion",
                "To ensure accessible creative opportunities for all",
                "To promote community participation in cultural life",
                "To ensure transparent creative operations and funding",
                "To promote green creative practices and sustainability",
                "To ensure creative worker rights and fair treatment",
                "To build community creative capacity and expression"
            ]
        },

        'environment': {
            'profitable': [
                "To become the leading environmental solutions provider",
                "To maximize profitability through sustainable environmental services",
                "To dominate environmental markets with innovative solutions",
                "To achieve operational excellence across environmental operations",
                "To revolutionize environmental protection through technology",
                "To build a diversified environmental portfolio and services",
                "To establish new standards for environmental performance",
                "To lead in environmental innovation and solution development",
                "To optimize environmental processes and service delivery",
                "To establish comprehensive environmental networks and partnerships",
                "To maximize shareholder returns through strategic growth",
                "To create innovative environmental solutions and services",
                "To build strong client relationships and environmental impact",
                "To achieve cost leadership in environmental operations",
                "To develop proprietary environmental technologies and methods",
                "To create value through strategic environmental partnerships",
                "To expand environmental services and solution offerings",
                "To build resilient environmental operations and capabilities",
                "To lead in environmental quality and sustainability standards",
                "To create sustainable environmental value for all stakeholders"
            ],
            'non_profitable': [
                "To promote environmental protection as essential for all life",
                "To advocate for sustainable development and conservation",
                "To ensure environmental actions benefit communities and ecosystems",
                "To combat environmental degradation and climate change",
                "To ensure fair and equitable environmental protection",
                "To promote community-based environmental initiatives",
                "To advocate for strong environmental policies and regulations",
                "To ensure sustainable and responsible environmental practices",
                "To promote local environmental capacity and stewardship",
                "To ensure comprehensive ecosystem protection and restoration",
                "To promote environmental education and awareness",
                "To advocate for progressive environmental policies and action",
                "To ensure sustainable environmental system development",
                "To promote biodiversity conservation and protection",
                "To ensure accessible environmental benefits for all",
                "To promote community participation in environmental protection",
                "To ensure transparent environmental operations and impacts",
                "To promote green technologies and sustainable practices",
                "To ensure environmental worker rights and fair treatment",
                "To build community environmental resilience and sustainability"
            ]
        }
    }
    def __init__(self, org_obj: OrganizationalProfile):
        self.org = org_obj
        if org_obj:
            self.sector_name = org_obj.sector_name
            self.classification = org_obj.organization_classification
        else:
            self.sector_name = None
            self.classification = None

    def get_choices(self):
        """Return list of tuples for form select based on sector + classification."""
        if not self.sector_name or not self.classification:
            return []

        visions_by_sector = self.SECTOR_VISION_MAP.get(self.sector_name, {})
        visions = visions_by_sector.get(self.classification, [])
        return [(v, v) for v in visions]

    def validate_choice(self, vision_statement):
        if not self.sector_name or not self.classification:
            raise ValueError("Organization sector or classification not set.")

        visions_by_sector = self.SECTOR_VISION_MAP.get(self.sector_name, {})
        valid_visions = visions_by_sector.get(self.classification, [])
        if vision_statement not in valid_visions:
            raise ValueError(
                f"Invalid vision '{vision_statement}' for sector '{self.sector_name}' and classification '{self.classification}'.")

    def create_vision(self, vision_statement):
        self.validate_choice(vision_statement)
        return Vision.objects.create(organization_name=self.org, vision_statement=vision_statement)



