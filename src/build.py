#!/usr/bin/env python3
"""Bell Enviro static site generator. Run: python3 build.py  -> writes ./out/"""
import os, json, shutil, html
from datetime import date

OUT = "out"
BASE = "https://bellenviro.au"
PHONE = "0424 577 159"; PHONE_INTL = "+61424577159"; EMAIL = "chris@bellenviro.au"
TODAY = date.today().isoformat()

# ---------------------------------------------------------------- site data
SERVICES = [
 dict(slug="contaminated-land-assessment", nav="Contaminated Land",
  title="Contaminated Land Assessment Darwin NT | PSI & DSI",
  h1="Contaminated land assessment — PSI and DSI",
  desc="NEPM-aligned preliminary and detailed site investigations (PSI/DSI) in Darwin, Palmerston and across the NT. Fixed-price, principal-delivered reports accepted by NT EPA and auditors.",
  intro="Preliminary and detailed site investigations for land transactions, development approvals, fuel storage decommissioning and civil works. Delivered in line with the National Environment Protection (Assessment of Site Contamination) Measure 1999 (ASC NEPM) and NT EPA guidance, with NATA-accredited laboratory analysis.",
  bullets=["Preliminary Site Investigation (PSI): site history, desktop review, walkover and conceptual site model",
           "Detailed Site Investigation (DSI): soil, groundwater and vapour sampling design and execution",
           "Waste classification and off-site disposal documentation (VENM/ENM and contaminated fill)",
           "Underground and above-ground fuel storage decommissioning and validation",
           "Acid sulfate soil assessment and management plans",
           "Site validation and clearance reporting for auditors and regulators"],
  who="Developers and land purchasers doing due diligence, civil head contractors encountering unexpected fill or odours mid-project, Defence and aviation precinct works, and interstate consultancies needing Darwin-based field capacity.",
  pricing="PSIs are fixed price. DSIs are fixed price for design, fieldwork and reporting with laboratory analysis at cost.",
  faqs=[("Do I need a PSI or a DSI?","A PSI is the first step: it establishes whether contamination is plausible from the site's history and a walkover. If the PSI identifies potential contamination, a DSI collects samples to confirm and delineate it. Most land transactions and development applications start with a PSI."),
        ("Will the NT EPA accept the report?","Reports are prepared to the ASC NEPM and NT EPA contaminated land guidelines, which is the standard NT regulators and contaminated land auditors assess against."),
        ("How long does a PSI take in Darwin?","Typically two to three weeks from engagement, depending on title search and records turnaround. DSIs depend on laboratory turnaround, usually five to ten business days after sampling.")]),
 dict(slug="pfas-investigation", nav="PFAS",
  title="PFAS Investigation & Management Darwin NT",
  h1="PFAS investigation and management",
  desc="PFAS soil, groundwater and surface water investigations in Darwin and the NT, delivered to the PFAS National Environmental Management Plan. Sampling, waste classification and management plans for civil works.",
  intro="Per- and polyfluoroalkyl substances (PFAS) are a live issue around Darwin's airport, Defence and firefighting training precincts and legacy industrial land. Bell Enviro designs and runs PFAS investigations to the PFAS National Environmental Management Plan (NEMP), with contamination-free sampling protocols and NATA-accredited analysis.",
  bullets=["PFAS screening within PSI/DSI programs",
           "Soil, groundwater, surface water and sediment sampling to NEMP protocols",
           "PFAS waste classification and disposal pathway advice for excavated material",
           "PFAS management plans for civil works in affected precincts",
           "Dewatering and stockpile management advice where PFAS-impacted water or soil is encountered"],
  who="Civil contractors working in or near Darwin International Airport, RAAF Base Darwin, East Arm and other PFAS-affected precincts; developers acquiring legacy industrial land; project managers needing a disposal pathway for excavated material.",
  pricing="Fixed price for investigation design, fieldwork and reporting; laboratory analysis at cost.",
  faqs=[("Where is PFAS a concern in the Darwin region?","PFAS investigation areas around Darwin include the airport and RAAF Base precincts and surrounding suburbs, plus other sites where firefighting foam was historically used. Any excavation in these areas may need PFAS screening before material leaves site."),
        ("Can PFAS-impacted soil be reused on site?","Often yes, under a management plan consistent with the PFAS NEMP. Off-site disposal requires classification and an approved receiving facility, which is limited in the NT, so on-site reuse is usually the practical option."),
        ("What sampling precautions are needed?","PFAS is present in many everyday materials, so sampling uses PFAS-free equipment, clothing and containers and strict decontamination. Bell Enviro's field protocols follow NEMP guidance.")]),
 dict(slug="construction-environmental-management-plan", nav="CEMPs & ESCPs",
  title="CEMP & Erosion and Sediment Control Plans NT | Contract-Ready",
  h1="Construction Environmental Management Plans (CEMPs) and ESCPs",
  desc="Contract-ready CEMPs, erosion and sediment control plans, weed hygiene and dust/noise plans for NT Government, Defence and council civil works. Fixed price, fast turnaround, Darwin-based.",
  intro="A CEMP is usually a condition of contract on NT Government, Defence, council and private civil works. Bell Enviro writes CEMPs that superintendents approve first time, because they are built from the actual contract conditions, site constraints and the contractor's real methodology, not a generic template.",
  bullets=["Construction Environmental Management Plans to NTG, Defence and council specifications",
           "Erosion and Sediment Control Plans (ESCPs) for the Top End Wet season",
           "Weed hygiene and management plans, weed hygiene declarations and vehicle wash-down procedures",
           "Dust, noise, vibration and water quality management plans",
           "Incident and non-conformance procedures that contractors will actually use",
           "CEMP implementation support: inductions, inspections and monitoring programs"],
  who="Civil head contractors and subcontractors tendering for or delivering roads, water and sewer, subdivisions, airfield, Defence estate and remote community works across the NT.",
  pricing="Fixed price per plan, scoped to the contract requirements. Implementation support at day rates or under a retainer.",
  faqs=[("Do I need a CEMP for NT Government civil works?","Most NT Government, Defence and council construction contracts require a CEMP before site establishment, and many require it to be approved by the superintendent. Check the contract's environmental clauses; Bell Enviro can review them with you."),
        ("How quickly can you turn a CEMP around?","A standard civil works CEMP is typically delivered within five to ten business days of receiving the contract documents and methodology. Urgent turnaround is available."),
        ("Can you also implement the CEMP on site?","Yes. Bell Enviro provides environmental inspections, monitoring, incident support and close-out reporting for live civil works, either per visit or under a retainer.")]),
 dict(slug="environmental-auditing-compliance", nav="Auditing & Compliance",
  title="Environmental Compliance Audits & Inspections Darwin NT",
  h1="Environmental auditing, inspections and compliance",
  desc="ISO 19011-based environmental audits, site compliance inspections, monitoring programs and incident reporting systems for civil works in Darwin and across the NT.",
  intro="Independent environmental audits and compliance inspections that give head contractors, principals and financiers evidence that conditions are being met. Audits follow ISO 19011 principles, and findings are written as actionable items with owners and dates, not pages of generic observations.",
  bullets=["Environmental compliance audits against approvals, licences, CEMPs and contract conditions",
           "Scheduled site environmental inspections for live civil works",
           "Monitoring programs: water quality, dust, noise, stockpiles and sediment controls",
           "Incident reporting and non-conformance systems contractors can run themselves",
           "Retrospective compliance reviews where records have gaps",
           "Close-out and completion reporting for project handover"],
  who="Head contractors needing an independent check before a principal's audit, principals and project managers wanting assurance on contractor performance, and operators holding NT EPA environment protection licences or approvals.",
  pricing="Fixed price per audit or inspection program, or day rate.",
  faqs=[("What does an environmental audit involve?","A document review of your approvals and plans, a site inspection, interviews with site staff, and a report of conformances, non-conformances and opportunities for improvement, each with a recommended action."),
        ("How often should civil sites be inspected?","Weekly inspections are typical during earthworks and the Wet season, extending to fortnightly or monthly once the site is stabilised. Many contracts specify a frequency."),
        ("Can you fix a project's compliance records retrospectively?","Bell Enviro can reconstruct monitoring, inspection and incident records from available evidence, identify gaps honestly, and set up a system so the gaps do not recur.")]),
 dict(slug="environmental-approvals", nav="Approvals",
  title="Environmental Approvals & Statutory Compliance NT",
  h1="Environmental approvals and statutory compliance",
  desc="NT EPA referrals, environment protection licences, land clearing and water approvals, and statutory environmental compliance advice for projects in Darwin, the Top End and the NT.",
  intro="Navigating the NT Environment Protection Act 2019, the Water Act, Planning Act, Weeds Management Act and Commonwealth EPBC Act takes someone who has dealt with the regulators before. Bell Enviro scopes which approvals a project actually needs, prepares the applications and supporting assessments, and manages the conversation with the agency.",
  bullets=["Approvals pathway scoping: which Acts, which agency, how long",
           "NT EPA referrals and environmental impact assessment support",
           "Environment protection licences and approvals for extractives, waste and industrial activities",
           "Land clearing, water extraction and waste discharge licence applications",
           "Development application environmental reports and conditions compliance",
           "EPBC Act self-assessment and referral support"],
  who="Developers, quarry and extractive operators, civil contractors with self-performed approvals obligations, and interstate proponents unfamiliar with NT processes.",
  pricing="Fixed price for pathway scoping and standard applications; scoped per project for assessments.",
  faqs=[("Does my project need NT EPA referral?","Referral is required where a project has the potential to have a significant impact on the environment. Many civil projects do not, but extractives, large clearing and works in sensitive areas may. A short scoping review answers this early."),
        ("How long do NT environmental approvals take?","Simple licences and permits can take weeks; EPA assessments take many months. Starting the scoping early is the single biggest time saver."),
        ("Can you deal with the agency on my behalf?","Yes. Bell Enviro routinely liaises with NT EPA, DEPWS, Development Consent Authority and AAPA on behalf of clients.")]),
 dict(slug="environmental-department-as-a-service", nav="Retainer",
  title="Environmental Department as a Service | Retainer for NT Civil Contractors",
  h1="Your environmental department, as a service",
  desc="A monthly retainer giving NT civil contractors standing environmental advice, document review, incident support and priority delivery of CEMPs, audits and investigations, without hiring an environmental officer.",
  intro="Mid-tier civil contractors need an environmental capability but rarely have enough work for a full-time environmental officer. The retainer gives you a principal-level environmental scientist on call: tender reviews, CEMPs, incident response, regulator contact and site inspections, with one number to call and priority turnaround.",
  bullets=["Monthly base fee for standing availability, advice and document review",
           "Priority delivery of CEMPs, audits, investigations and approvals at agreed drawdown rates",
           "Tender and contract environmental clause review before you price the job",
           "Incident and regulator response support, including first-call attendance",
           "Environmental inductions and toolbox content for your crews",
           "Limited to a small number of contractors so response times stay fast"],
  who="NT civil contractors with regular NT Government, Defence or council work who want the compliance capability of a larger firm at a fraction of the cost of an employee.",
  pricing="Monthly retainer with defined inclusions and agreed drawdown rates for deliverables. Three-month minimum.",
  faqs=[("How is this different from hiring an environmental officer?","You get senior, insured, sign-off-capable expertise for less than a junior salary, with no recruitment, leave or supervision. The trade-off is that availability is shared across a small number of clients."),
        ("What is included in the base fee?","Standing availability, phone and email advice, document and tender review, and a set number of inspection or meeting hours. Larger deliverables are priced at drawdown rates agreed up front."),
        ("Can we start with a single project?","Yes. Many clients start with one CEMP or audit and move to the retainer once the second project arrives.")]),
 dict(slug="cultural-heritage-aapa", nav="Cultural Heritage",
  title="Cultural Heritage & AAPA Clearance Coordination NT",
  h1="Cultural heritage assessment and AAPA clearance coordination",
  desc="Cultural heritage assessment, Aboriginal Areas Protection Authority (AAPA) certificate coordination, Traditional Owner engagement and archaeological survey support for projects in the NT.",
  intro="Sacred sites and heritage obligations apply to almost every ground-disturbing project in the Northern Territory. Bell Enviro coordinates AAPA Authority Certificates, heritage assessments and Traditional Owner engagement so that works are cleared before the excavator arrives, not after a stop-work notice.",
  bullets=["AAPA Authority Certificate applications and clearance survey coordination",
           "Heritage due diligence under the NT Heritage Act 2011",
           "Traditional Owner and land council engagement and consultation records",
           "Archaeological survey coordination with qualified archaeologists",
           "Cultural heritage management plans and unexpected finds procedures for CEMPs"],
  who="Civil contractors and developers working on Crown land, Aboriginal land, remote community projects and greenfield sites anywhere in the NT.",
  pricing="Scoped per project; AAPA and specialist fees at cost.",
  faqs=[("Do I need an AAPA certificate?","An Authority Certificate is not mandatory but provides a legal defence against prosecution for damaging a sacred site. Most NT Government and Defence contracts require one before ground disturbance."),
        ("How long does an AAPA certificate take?","Allow several months. Applications are lodged early in project planning, which is why Bell Enviro raises heritage in the first conversation about any project."),
        ("Do you run the consultation yourselves?","Bell Enviro coordinates consultation through AAPA and land councils and engages qualified anthropologists and archaeologists where the project requires specialist surveys.")]),
 dict(slug="compliance-registers", nav="Compliance registers",
  title="Compliance, Stockpile & Incident Registers for NT Civil Contractors",
  h1="Compliance, stockpile and incident registers",
  desc="Practical obligations, stockpile and incident register systems for mid-tier civil contractors, set up and maintained by Bell Enviro so compliance evidence is ready when the auditor or principal asks.",
  intro="Most compliance failures on civil sites are record-keeping failures: the control was in place, but nobody can prove it. Bell Enviro sets up simple, field-usable registers for approval obligations, stockpiles and incidents, trains your supervisors to use them, and keeps them honest through periodic review. A hosted version is being piloted with an NT head contractor.",
  bullets=["Obligations register mapping every approval, licence and contract condition to an owner and evidence",
           "Stockpile register with classification, source, volume and disposal pathway for each stockpile",
           "Incident and non-conformance register with investigation and close-out tracking",
           "Monthly compliance status reporting for principals and superintendents",
           "Audit-ready evidence packs at project completion"],
  who="Civil contractors delivering projects with environmental approval conditions, especially those handling fill, contaminated or PFAS-impacted material, or working under NT Government and Defence contracts.",
  pricing="Set-up fee per project plus optional monthly maintenance. Register the interest for the hosted version via the contact page.",
  faqs=[("Is this software?","Today it is a structured system delivered in tools your site team already uses, set up and reviewed by Bell Enviro. A hosted version is in pilot; contact Bell Enviro to register interest."),
        ("Why a stockpile register?","Regulators and principals increasingly ask where every cubic metre of material came from and went. A stockpile register answers that in minutes instead of a week of searching dockets.")]),
]

REGIONS = [
 dict(slug="darwin-palmerston-rural", nav="Darwin, Palmerston & Rural",
  title="Environmental Consultant Darwin, Palmerston & Rural Area NT",
  h1="Environmental consultant for Darwin, Palmerston and the rural area",
  desc="Darwin-based environmental consultant servicing Darwin, Palmerston, Humpty Doo, Howard Springs, Berry Springs, Noonamah, Coolalinga and the Litchfield rural area. Contaminated land, PFAS, CEMPs, audits and approvals.",
  places="Darwin city and northern suburbs, East Arm and Berrimah industrial precincts, Darwin International Airport and RAAF Base precincts, Palmerston and its new suburbs, Humpty Doo, Howard Springs, Coolalinga, Berry Springs, Noonamah, Virginia, Bees Creek, Darwin River and the Litchfield municipality, Cox Peninsula and Dundee.",
  body="This is Bell Enviro's home ground. Being based in the rural area means same-day site attendance across Darwin, Palmerston and Litchfield, no travel charges within the greater Darwin region, and first-hand knowledge of local conditions: Wet-season drainage, acid sulfate soils around the harbour and lowlands, PFAS investigation areas near the airport and base, and the legacy industrial land at East Arm, Berrimah and Winnellie.",
  work=["Subdivision and roads earthworks CEMPs and ESCPs in Palmerston and Litchfield growth areas",
        "PSIs and DSIs for industrial land transactions at East Arm, Berrimah and Winnellie",
        "Waste classification and PFAS screening for airport precinct and Defence-adjacent works",
        "Quarry and extractive compliance in the Darwin rural area",
        "Weed hygiene declarations and clearance for rural area civil works"]),
 dict(slug="top-end", nav="Top End",
  title="Environmental Consultant Top End NT | Katherine, Jabiru, Arnhem Land, Tiwi",
  h1="Environmental consultant for the Top End",
  desc="Remote-capable environmental consultant for the Top End of the Northern Territory: Katherine, Kakadu and Jabiru, West and East Arnhem Land, Nhulunbuy, the Tiwi Islands, Daly River and the Victoria River district.",
  places="Katherine and the Katherine region, Pine Creek and Adelaide River, Kakadu and Jabiru, West Arnhem including Maningrida and Gunbalanya, East Arnhem including Nhulunbuy and Galiwin'ku, the Tiwi Islands, Wadeye and the Daly River region, Timber Creek and the Victoria River district.",
  body="Remote Top End projects fail on logistics more than science. Bell Enviro has delivered compliance auditing and CEMP implementation for water and distribution network upgrades in Jabiru and is set up for remote mobilisation: self-sufficient field kit, sample cold-chain to Darwin laboratories, and the permits and inductions that Aboriginal land and Kakadu require. Fieldwork is planned around the Dry season, with authoring and reporting through the Wet.",
  work=["CEMP implementation and compliance auditing for remote community infrastructure upgrades",
        "Contaminated land and fuel storage investigations at remote facilities and community sites",
        "Weed hygiene and biosecurity planning for mobilising plant into Arnhem Land and the Tiwi Islands",
        "AAPA and Traditional Owner engagement coordination for works on Aboriginal land",
        "Environmental approvals support for extractive and infrastructure projects in the Katherine region"]),
 dict(slug="northern-territory-kimberley", nav="NT & Kimberley",
  title="Environmental Consultant Northern Territory & Kimberley WA",
  h1="Environmental consultant across the Northern Territory and the Kimberley",
  desc="Environmental consulting across the Northern Territory and north-eastern Western Australia, including Tennant Creek, Alice Springs, the Barkly, Kununurra, Wyndham, Halls Creek and the East Kimberley.",
  places="Tennant Creek and the Barkly, Alice Springs and Central Australia, the Gulf region and Borroloola, and across the border to Kununurra, Wyndham, Lake Argyle, Halls Creek, Fitzroy Crossing and the East Kimberley.",
  body="For projects outside the Top End, Bell Enviro offers a Darwin-based alternative to flying a team from Perth, Adelaide or Brisbane. For East Kimberley work the drive from Darwin is shorter than the flight from Perth, and the environmental and cultural context, Wet season, savanna, Aboriginal land and remote logistics, is the same one Bell Enviro works in every week. Work in Western Australia is delivered under WA's Contaminated Sites Act 2003 and Environmental Protection Act 1986 with the relevant DWER guidelines.",
  work=["Contaminated land investigations and waste classification for mining support, pastoral and infrastructure sites",
        "CEMPs and environmental inspections for road, water and community infrastructure projects",
        "PFAS screening at airstrips, depots and fire training sites",
        "Environmental audits of remote operations for principals and financiers",
        "Approvals pathway scoping for NT and WA proponents"]),
]

GUIDES = [
 dict(slug="do-i-need-a-cemp-for-nt-government-works", title="Do I need a CEMP for NT Government or Defence civil works?",
  desc="When a Construction Environmental Management Plan is required on NT Government, Defence and council contracts, what it must contain, and how to get it approved quickly.",
  body="""<p>Almost all NT Government (DIPL, Power and Water, Department of Housing), Defence estate and local council construction contracts include an environmental management clause requiring the contractor to prepare and implement a Construction Environmental Management Plan before site establishment. Private principals increasingly require one too, because their own approvals say so.</p>
<h2>What triggers the requirement</h2>
<ul><li>A contract clause (commonly in the general conditions or the specification's environmental section) requiring an approved CEMP before commencement.</li><li>A development permit or NT EPA approval condition that is passed down to the contractor.</li><li>Works on or near waterways, Aboriginal land, Kakadu, Defence land or sites with known contamination.</li></ul>
<h2>What a superintendent expects to see</h2>
<ul><li>Site-specific environmental risks (not a generic risk table), including Wet-season erosion, dust, weeds, fuel and chemical storage, waste and stockpiles, heritage and fauna.</li><li>Controls tied to the contractor's actual methodology and plant.</li><li>An Erosion and Sediment Control Plan, usually with a drawing.</li><li>Weed hygiene procedures and vehicle wash-down declarations.</li><li>Monitoring, inspection and incident reporting procedures with named responsibilities.</li><li>Evidence of inductions and training.</li></ul>
<h2>How to get it approved first time</h2>
<p>Send the environmental consultant the full contract environmental clauses, the specification, the approval conditions and your methodology. Plans rejected by superintendents are almost always generic ones that do not reference the contract. A plan built from the contract is typically approved in one round.</p>
<p>Bell Enviro delivers contract-ready CEMPs for NT civil works at a fixed price, usually within five to ten business days. See <a href="/services/construction-environmental-management-plan/">CEMPs and ESCPs</a>.</p>"""),
 dict(slug="psi-vs-dsi-contaminated-land-nt", title="PSI vs DSI: which contaminated land assessment do you need in the NT?",
  desc="The difference between a Preliminary Site Investigation and a Detailed Site Investigation under the ASC NEPM, when each is needed in the Northern Territory, and what they cost.",
  body="""<p>Contaminated land assessment in the Northern Territory follows the National Environment Protection (Assessment of Site Contamination) Measure 1999 (ASC NEPM), which NT EPA adopts as its standard. The NEPM sets out a staged approach.</p>
<h2>Preliminary Site Investigation (PSI)</h2>
<p>A PSI answers one question: is contamination plausible at this site? It reviews land titles and historical aerial photographs, government records, previous reports and interviews, then walks the site to look for evidence. The output is a conceptual site model and a conclusion on whether further investigation is needed. A PSI may include limited sampling where it helps answer the question early.</p>
<p>Typical triggers: land purchase due diligence, development applications where the planning authority asks about contamination, rezoning to a more sensitive use, and decommissioning of fuel storage.</p>
<h2>Detailed Site Investigation (DSI)</h2>
<p>A DSI collects and analyses soil, groundwater and sometimes vapour samples to confirm whether contamination exists, how far it extends and whether it poses a risk to the intended land use. It is designed from the PSI's conceptual site model using a sampling and analysis quality plan, and reports against NEPM investigation levels. Where risk is identified, it leads to a remediation action plan or site management plan.</p>
<h2>Which one do you need?</h2>
<ul><li>No history of contaminating activity and a planning authority asking a general question: PSI.</li><li>Known or suspected contamination, a PSI recommending further work, or an auditor involved: DSI.</li><li>Unexpected finds during civil works (staining, odours, buried drums, fill of unknown origin): targeted investigation and waste classification, often expedited.</li></ul>
<h2>Cost and timing in Darwin</h2>
<p>Bell Enviro delivers PSIs at a fixed price in two to three weeks, and DSIs at a fixed price for design, fieldwork and reporting with laboratory analysis at cost. See <a href="/services/contaminated-land-assessment/">contaminated land assessment</a>.</p>"""),
 dict(slug="pfas-testing-civil-works-darwin", title="PFAS testing for civil works around Darwin: what contractors need to know",
  desc="Where PFAS is a concern for civil works in Darwin, when excavated soil needs testing, and how the PFAS NEMP affects reuse and disposal of material.",
  body="""<p>PFAS (per- and polyfluoroalkyl substances) are the firefighting foam chemicals found in soil and groundwater around airports, Defence bases and fire training grounds. Around Darwin, investigation areas have been declared around RAAF Base Darwin and Darwin International Airport and extend into surrounding suburbs and drainage lines. Legacy industrial sites and landfills can also be affected.</p>
<h2>When excavated material needs PFAS testing</h2>
<ul><li>Works inside or downstream of a declared PFAS investigation or management area.</li><li>Material is leaving site for reuse or disposal and the receiving facility asks for PFAS results (increasingly standard).</li><li>Dewatering will discharge groundwater to stormwater or land.</li><li>The contract or CEMP requires it.</li></ul>
<h2>What the PFAS NEMP means on site</h2>
<p>The PFAS National Environmental Management Plan sets the criteria for reuse, management and disposal of PFAS-impacted soil and water. In practice for Top End contractors this means: test before you move material; prefer on-site reuse under a management plan because licensed disposal options for PFAS waste in the NT are limited; and manage dewatering so that impacted groundwater is not spread.</p>
<h2>Sampling matters</h2>
<p>PFAS is present in waterproof clothing, sunscreen, some sample containers and many field items. Sampling must use PFAS-free equipment and protocols or the results are meaningless. Use a consultant who runs NEMP-compliant protocols and NATA-accredited laboratories.</p>
<p>Bell Enviro provides PFAS screening, waste classification and management plans for civil works across Darwin and the NT. See <a href="/services/pfas-investigation/">PFAS investigation</a>.</p>"""),
 dict(slug="weed-hygiene-declaration-nt", title="Weed hygiene declarations for NT civil works: what is required",
  desc="What a weed hygiene declaration is, when NT Government and land council contracts require one, and how to set up wash-down and inspection procedures that pass audit.",
  body="""<p>The NT Weeds Management Act 2001 places a duty on everyone to prevent the spread of declared weeds, and NT Government, Defence, land council and many private contracts turn that duty into a documented requirement: a weed hygiene declaration for plant and vehicles entering site, and a weed management procedure in the CEMP.</p>
<h2>What a weed hygiene declaration covers</h2>
<ul><li>Identification of the machine or vehicle and where it has come from.</li><li>Confirmation that it has been cleaned (wash-down or blow-down) to remove soil, seed and plant material, with the location and date.</li><li>Inspection by a competent person and sign-off.</li></ul>
<h2>Where it bites</h2>
<p>Mobilising plant to Arnhem Land, the Tiwi Islands, Kakadu, Groote Eylandt and pastoral properties often requires declarations and inspections before the barge or at the property boundary. Gamba grass, mission grass and mimosa are the high-profile risks in the Top End; the Kimberley adds its own declared species.</p>
<h2>Setting it up</h2>
<p>A workable procedure needs a declaration form, a wash-down location and method, an inspection checklist, a register of declarations, and a toolbox talk so operators know why it matters. Bell Enviro provides these as part of CEMPs and can conduct pre-mobilisation inspections. See <a href="/services/construction-environmental-management-plan/">CEMPs and ESCPs</a>.</p>"""),
]

# ---------------------------------------------------------------- helpers
def esc(s): return html.escape(s, quote=True)

def ld(obj): return '<script type="application/ld+json">'+json.dumps(obj, ensure_ascii=False)+'</script>'

ORG = {"@type":"ProfessionalService","@id":BASE+"/#org","name":"Bell Enviro","url":BASE+"/",
  "logo":BASE+"/assets/logo.png","image":BASE+"/assets/logo.png","telephone":PHONE_INTL,"email":EMAIL,
  "description":"Principal-delivered environmental consultancy for civil contractors and developers in Darwin and the Northern Territory: contaminated land, PFAS, CEMPs, audits, approvals and cultural heritage.",
  "address":{"@type":"PostalAddress","addressLocality":"Humpty Doo","addressRegion":"NT","postalCode":"0836","addressCountry":"AU"},
  "geo":{"@type":"GeoCoordinates","latitude":-12.58,"longitude":131.13},
  "areaServed":[{"@type":"City","name":"Darwin"},{"@type":"City","name":"Palmerston"},{"@type":"AdministrativeArea","name":"Litchfield Municipality"},
                {"@type":"Place","name":"Top End, Northern Territory"},{"@type":"State","name":"Northern Territory"},{"@type":"Place","name":"Kimberley, Western Australia"}],
  "founder":{"@type":"Person","@id":BASE+"/about/#chris","name":"Chris Bell","jobTitle":"Principal Environmental Scientist"},
  "priceRange":"$$","knowsAbout":["Contaminated land assessment","PFAS investigation","Construction environmental management plans","Environmental auditing","Environmental approvals Northern Territory","Cultural heritage AAPA"],
  "sameAs":[]}

def layout(path, title, desc, body, extra_ld=None, nav_active=None):
    canonical = BASE + path
    lds = [dict(ORG, **{"@context":"https://schema.org"})] if path=="/" else []
    if extra_ld: lds += extra_ld
    svc_links = "".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["nav"])}</a></li>' for s in SERVICES)
    reg_links = "".join(f'<li><a href="/regions/{r["slug"]}/">{esc(r["nav"])}</a></li>' for r in REGIONS)
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Bell Enviro">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{BASE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="AU-NT"><meta name="geo.placename" content="Darwin">
<link rel="icon" href="/assets/favicon.png" type="image/png">
<link rel="stylesheet" href="/assets/style.css">
{''.join(ld(x) for x in lds)}
</head>
<body>
<header class="top">
 <div class="wrap bar">
  <a class="logo" href="/"><img src="/assets/logo.png" alt="Bell Enviro" width="56" height="56"><span><b>BELL</b> <i>ENVIRO</i></span></a>
  <nav aria-label="Main">
   <input type="checkbox" id="m" hidden><label for="m" class="burger" aria-label="Menu">☰</label>
   <ul>
    <li class="dd"><a href="/services/">Services</a><ul>{svc_links}</ul></li>
    <li class="dd"><a href="/regions/">Regions</a><ul>{reg_links}</ul></li>
    <li><a href="/guides/">Guides</a></li>
    <li><a href="/about/">About</a></li>
    <li><a class="btn" href="/contact/">Get a quote</a></li>
   </ul>
  </nav>
 </div>
</header>
<main>
{body}
</main>
<footer>
 <div class="wrap grid3">
  <div><h3>Bell Enviro</h3><p>Principal-delivered environmental consultancy for civil contractors and developers. Darwin-based, Territory-wide, Kimberley-capable.</p>
   <p><a href="tel:{PHONE_INTL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>Humpty Doo NT 0836</p></div>
  <div><h3>Services</h3><ul>{svc_links}</ul></div>
  <div><h3>Regions</h3><ul>{reg_links}</ul><h3>More</h3><ul><li><a href="/guides/">Guides</a></li><li><a href="/about/">About Chris Bell</a></li><li><a href="/contact/">Contact</a></li></ul></div>
 </div>
 <div class="wrap fine"><p>Chris Bell trading as Bell Enviro. Professional Indemnity and Public Liability insurance current. ICN Gateway registered. © Bell Enviro {TODAY[:4]}.</p></div>
</footer>
</body>
</html>"""

def cta(text="Talk to Chris about your project"):
    return f'<div class="cta"><p>{esc(text)}</p><a class="btn big" href="/contact/">Get a fixed-price quote</a> <a class="btn ghost" href="tel:{PHONE_INTL}">Call {PHONE}</a></div>'

def faq_html(faqs):
    items = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in faqs)
    return f'<section class="wrap"><h2>Frequently asked questions</h2>{items}</section>'

def faq_ld(faqs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}

def crumbs(items):
    lst=[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]
    h='<nav class="crumbs wrap" aria-label="Breadcrumb">'+" › ".join(f'<a href="{u}">{esc(n)}</a>' for n,u in items)+'</nav>'
    return h,{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":lst}

def write(path, content):
    p = os.path.join(OUT, path.lstrip("/"))
    if path.endswith("/"): p = os.path.join(p, "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p,"w",encoding="utf-8").write(content)

# ---------------------------------------------------------------- pages
pages = []  # (path, priority)

def home():
    cards = "".join(f'<a class="card" href="/services/{s["slug"]}/"><h3>{esc(s["h1"].split(" — ")[0].split(" (")[0])}</h3><p>{esc(s["desc"].split(". ")[0])}.</p></a>' for s in SERVICES[:7])
    regs = "".join(f'<a class="card" href="/regions/{r["slug"]}/"><h3>{esc(r["nav"])}</h3><p>{esc(r["places"].split(",")[0])} and surrounds</p></a>' for r in REGIONS)
    guides = "".join(f'<li><a href="/guides/{g["slug"]}/">{esc(g["title"])}</a></li>' for g in GUIDES)
    body = f"""
<section class="hero"><div class="wrap">
 <p class="kicker">Environmental consultant · Darwin NT</p>
 <h1>Environmental compliance for NT civil contractors and developers, without the headcount.</h1>
 <p class="lead">Contaminated land and PFAS investigations, CEMPs, environmental audits, approvals and cultural heritage coordination. Fixed prices. Documents regulators accept. Delivered and signed off by the principal, Chris Bell.</p>
 <p><a class="btn big" href="/contact/">Get a fixed-price quote</a> <a class="btn ghost" href="tel:{PHONE_INTL}">Call {PHONE}</a></p>
 <p class="small">Servicing <a href="/regions/darwin-palmerston-rural/">Darwin, Palmerston and the rural area</a>, the <a href="/regions/top-end/">Top End</a>, and the <a href="/regions/northern-territory-kimberley/">wider NT and Kimberley</a>.</p>
</div></section>
<section class="wrap"><h2>Services</h2><div class="cards">{cards}</div></section>
<section class="alt"><div class="wrap"><h2>Why contractors use Bell Enviro instead of a national firm</h2><div class="cols">
 <div><h3>Principal-delivered</h3><p>The person who quotes the job is the person on site and the signature on the report: insured, accountable, and the one who answers the phone.</p></div>
 <div><h3>Fixed prices, defined scope</h3><p>PSIs, CEMPs, audits and approvals packages with scope, deliverables and dates agreed up front. No open-ended hourly surprises.</p></div>
 <div><h3>Built for the Territory</h3><p>Dry-season fieldwork, Wet-season reporting, remote-capable, and working relationships with NT EPA, DEPWS, Defence, AAPA, land councils and Darwin laboratories.</p></div>
 <div><h3>Fast because it is lean</h3><p>Modern tooling handles the paperwork so the expert time goes into the site, the data and the judgement calls. Standard CEMPs in days, not weeks.</p></div>
</div></div></section>
<section class="wrap"><h2>Where we work</h2><div class="cards">{regs}</div></section>
<section class="alt"><div class="wrap"><h2>Sectors</h2><p class="chips"><span>Defence</span><span>Aviation</span><span>Civil &amp; infrastructure</span><span>Construction &amp; demolition</span><span>Land development</span><span>Mining &amp; extractives</span><span>Oil &amp; gas</span><span>Government &amp; community</span></p></div></section>
<section class="wrap"><h2>Guides</h2><ul class="list">{guides}</ul></section>
{cta("Tell Chris what the contract or the site needs and get a scoped price back, usually within two business days.")}
"""
    write("/", layout("/", "Environmental Consultant Darwin NT | Contaminated Land, PFAS, CEMPs, Audits | Bell Enviro",
        "Darwin-based environmental consultant for NT civil contractors and developers. Contaminated land and PFAS investigations, CEMPs, environmental audits, approvals and AAPA coordination. Fixed prices, principal-delivered.", body))
    pages.append(("/",1.0))

def services_index():
    cards = "".join(f'<a class="card" href="/services/{s["slug"]}/"><h3>{esc(s["h1"])}</h3><p>{esc(s["desc"])}</p></a>' for s in SERVICES)
    ch,cl = crumbs([("Home","/"),("Services","/services/")])
    body = f'{ch}<section class="wrap"><h1>Environmental consulting services</h1><p class="lead">Every service is scoped and priced before work starts and delivered by the principal. Pick the one that matches the contract clause or the problem on site.</p><div class="cards">{cards}</div></section>{cta()}'
    write("/services/", layout("/services/","Environmental Consulting Services NT | Bell Enviro","Contaminated land, PFAS, CEMPs, environmental audits, approvals, retainer and cultural heritage services for civil contractors and developers in Darwin and the NT.", body,[cl]))
    pages.append(("/services/",0.8))

def service(s):
    path=f"/services/{s['slug']}/"
    ch,cl = crumbs([("Home","/"),("Services","/services/"),(s["nav"],path)])
    svc_ld={"@context":"https://schema.org","@type":"Service","name":s["h1"],"serviceType":s["nav"],"description":s["desc"],"provider":{"@id":BASE+"/#org"},
            "areaServed":ORG["areaServed"],"url":BASE+path}
    regs=" · ".join(f'<a href="/regions/{r["slug"]}/">{esc(r["nav"])}</a>' for r in REGIONS)
    body=f"""{ch}
<section class="wrap"><h1>{esc(s['h1'])}</h1><p class="lead">{esc(s['intro'])}</p>
<h2>What is included</h2><ul class="ticks">{''.join(f'<li>{esc(b)}</li>' for b in s['bullets'])}</ul>
<h2>Who it is for</h2><p>{esc(s['who'])}</p>
<h2>Pricing</h2><p>{esc(s['pricing'])}</p>
<p class="small">Available in {regs}.</p></section>
{faq_html(s['faqs'])}
{cta()}"""
    write(path, layout(path, s["title"], s["desc"], body,[cl,svc_ld,faq_ld(s["faqs"])]))
    pages.append((path,0.9))

def regions_index():
    cards="".join(f'<a class="card" href="/regions/{r["slug"]}/"><h3>{esc(r["h1"])}</h3><p>{esc(r["desc"])}</p></a>' for r in REGIONS)
    ch,cl=crumbs([("Home","/"),("Regions","/regions/")])
    body=f'{ch}<section class="wrap"><h1>Regions we service</h1><p class="lead">Based in the Darwin rural area, working across the Top End, the Northern Territory and the East Kimberley.</p><div class="cards">{cards}</div></section>{cta()}'
    write("/regions/", layout("/regions/","Regions Serviced | Darwin, Top End, NT & Kimberley | Bell Enviro","Environmental consulting across Darwin, Palmerston and the rural area, the Top End, the wider Northern Territory and the Kimberley region of Western Australia.", body,[cl]))
    pages.append(("/regions/",0.7))

def region(r):
    path=f"/regions/{r['slug']}/"
    ch,cl=crumbs([("Home","/"),("Regions","/regions/"),(r["nav"],path)])
    svcs="".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["h1"])}</a></li>' for s in SERVICES)
    body=f"""{ch}
<section class="wrap"><h1>{esc(r['h1'])}</h1><p class="lead">{esc(r['body'])}</p>
<h2>Areas covered</h2><p>{esc(r['places'])}</p>
<h2>Typical work in this region</h2><ul class="ticks">{''.join(f'<li>{esc(w)}</li>' for w in r['work'])}</ul>
<h2>Services available</h2><ul class="list">{svcs}</ul></section>
{cta()}"""
    write(path, layout(path, r["title"], r["desc"], body,[cl]))
    pages.append((path,0.8))

def guides_index():
    items="".join(f'<a class="card" href="/guides/{g["slug"]}/"><h3>{esc(g["title"])}</h3><p>{esc(g["desc"])}</p></a>' for g in GUIDES)
    ch,cl=crumbs([("Home","/"),("Guides","/guides/")])
    body=f'{ch}<section class="wrap"><h1>Guides for NT contractors and developers</h1><p class="lead">Plain answers to the questions that come up before a project starts.</p><div class="cards">{items}</div></section>{cta()}'
    write("/guides/", layout("/guides/","Environmental Compliance Guides for NT Civil Works | Bell Enviro","Practical guides on CEMPs, contaminated land, PFAS and weed hygiene for civil contractors and developers in the Northern Territory.", body,[cl]))
    pages.append(("/guides/",0.6))

def guide(g):
    path=f"/guides/{g['slug']}/"
    ch,cl=crumbs([("Home","/"),("Guides","/guides/"),(g["title"],path)])
    art={"@context":"https://schema.org","@type":"Article","headline":g["title"],"description":g["desc"],"datePublished":TODAY,"dateModified":TODAY,
         "author":{"@id":BASE+"/about/#chris"},"publisher":{"@id":BASE+"/#org"},"mainEntityOfPage":BASE+path}
    body=f'{ch}<article class="wrap prose"><h1>{esc(g["title"])}</h1><p class="small">By Chris Bell, Principal, Bell Enviro · Updated {TODAY}</p>{g["body"]}</article>{cta()}'
    write(path, layout(path, g["title"]+" | Bell Enviro", g["desc"], body,[cl,art]))
    pages.append((path,0.7))

def about():
    ch,cl=crumbs([("Home","/"),("About","/about/")])
    person={"@context":"https://schema.org","@type":"Person","@id":BASE+"/about/#chris","name":"Chris Bell","jobTitle":"Principal Environmental Scientist","worksFor":{"@id":BASE+"/#org"},
            "email":EMAIL,"telephone":PHONE_INTL,"url":BASE+"/about/","knowsAbout":ORG["knowsAbout"],
            "memberOf":{"@type":"Organization","name":"Environment Institute of Australia and New Zealand"}}
    body=f"""{ch}
<section class="wrap prose"><h1>About Bell Enviro and Chris Bell</h1>
<p class="lead">Bell Enviro is the practice of Chris Bell, an environmental scientist based in the Darwin rural area who works as the environmental capability inside civil contractors' and developers' project teams across the Northern Territory.</p>
<h2>How the practice works</h2>
<p>Every engagement is delivered or directly supervised by Chris. That is deliberate: the defensible value of an environmental consultant is the professional judgement and the signature on the report, so the person quoting the work is the person on site, interpreting the data and signing off. Report production, data handling and document assembly use modern tooling so that expert time is spent on the site, the data and the regulator conversation rather than formatting.</p>
<h2>Experience</h2>
<ul>
<li>Environmental compliance auditing and CEMP implementation for water and distribution network upgrades in Jabiru, under an ongoing retainer with a civil head contractor</li>
<li>Waste classification and environmental assessment for apron expansion works in the Darwin International Airport precinct</li>
<li>Soil quality and contamination investigations for East Arm and Darwin industrial land transactions</li>
<li>Extractive and quarry environmental compliance in the Darwin rural area</li>
<li>Weed hygiene declarations, erosion and sediment control and incident reporting systems for live civil works</li>
<li>Earlier career across Defence, aviation, oil and gas, mining, community development and cultural heritage projects in the NT and internationally</li>
</ul>
<h2>Credentials and cover</h2>
<ul><li>Certified Environmental Practitioner (Site Contamination) application in progress with EIANZ</li><li>Professional Indemnity and Public Liability insurance current</li><li>ICN Gateway registered</li><li>Working knowledge of Commonwealth, NT EPA, Defence, AAPA, ALRA, NLC and NTG frameworks</li></ul>
<h2>Working with subcontractors and partners</h2>
<p>For larger programs Bell Enviro draws on a bench of trusted field technicians, drillers, archaeologists, anthropologists and ecologists, and works with Darwin's NATA-accredited laboratories. Interstate consultancies also engage Bell Enviro for Darwin-based field capacity delivered to their own SAQPs and templates.</p>
</section>{cta("Want to know whether Bell Enviro is the right fit for your project? A ten-minute call usually settles it.")}"""
    write("/about/", layout("/about/","About Chris Bell | Principal Environmental Scientist, Darwin NT","Chris Bell is a Darwin-based environmental scientist delivering contaminated land, PFAS, CEMP, audit and approvals work for NT civil contractors and developers through Bell Enviro.", body,[cl,person]))
    pages.append(("/about/",0.6))

def contact():
    ch,cl=crumbs([("Home","/"),("Contact","/contact/")])
    body=f"""{ch}
<section class="wrap two"><div>
<h1>Contact Bell Enviro</h1>
<p class="lead">Send the contract clause, the site address or the problem, and Chris will come back with a scoped price, usually within two business days.</p>
<p><strong>Chris Bell</strong>, Principal<br><a href="tel:{PHONE_INTL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>Humpty Doo NT 0836<br>Servicing Darwin, Palmerston, the Top End, the NT and the Kimberley</p>
<p class="small">Hours: Monday to Friday, 7:30am to 5:00pm ACST. Urgent incident support outside hours by phone.</p>
</div>
<form class="form" action="/contact.php" method="post">
 <label>Name<input name="name" required maxlength="100"></label>
 <label>Company<input name="company" maxlength="100"></label>
 <label>Email<input name="email" type="email" required maxlength="150"></label>
 <label>Phone<input name="phone" type="tel" maxlength="40"></label>
 <label>Service needed<select name="service">{''.join(f'<option>{esc(s["nav"])}</option>' for s in SERVICES)}<option>Not sure yet</option></select></label>
 <label>Project location<input name="location" maxlength="150" placeholder="e.g. Palmerston, Jabiru, Kununurra"></label>
 <label>Tell Chris about the project<textarea name="message" rows="6" required maxlength="4000"></textarea></label>
 <div class="hp"><label>Leave blank<input name="website" tabindex="-1" autocomplete="off"></label></div>
 <input type="hidden" name="ts" value="">
 <button class="btn big" type="submit">Send enquiry</button>
 <p class="small">Attachments (contract clauses, drawings, previous reports) can be emailed to {EMAIL} after sending.</p>
</form></section>
<script>document.querySelector('[name=ts]').value=Date.now();</script>"""
    write("/contact/", layout("/contact/","Contact Bell Enviro | Environmental Consultant Darwin NT","Request a fixed-price quote for contaminated land, PFAS, CEMP, audit or approvals work in Darwin and the NT. Call 0424 577 159 or send an enquiry.", body,[cl]))
    pages.append(("/contact/",0.8))
    write("/thanks/", layout("/thanks/","Thanks | Bell Enviro","Your enquiry has been sent to Bell Enviro.", '<section class="wrap"><h1>Thanks, your enquiry is on its way.</h1><p class="lead">Chris will reply within two business days. If it is urgent, call <a href="tel:'+PHONE_INTL+'">'+PHONE+'</a>.</p><p><a class="btn" href="/">Back to home</a></p></section>'))

def statics():
    os.makedirs(os.path.join(OUT,"assets"),exist_ok=True)
    shutil.copy("assets/style.css", os.path.join(OUT,"assets/style.css"))
    for f in ("logo.png","favicon.png","og.png"):
        if os.path.exists("assets/"+f): shutil.copy("assets/"+f, os.path.join(OUT,"assets",f))
    shutil.copy("contact.php", os.path.join(OUT,"contact.php"))
    shutil.copy("htaccess", os.path.join(OUT,".htaccess"))
    # sitemap
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(
        f'<url><loc>{BASE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n' for p,pr in pages)+'</urlset>\n'
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    robots=f"""User-agent: *
Allow: /
Disallow: /contact.php
Disallow: /thanks/

# AI crawlers explicitly welcome
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: anthropic-ai
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /

Sitemap: {BASE}/sitemap.xml
"""
    open(os.path.join(OUT,"robots.txt"),"w").write(robots)
    llms="# Bell Enviro\n\n> Principal-delivered environmental consultancy based in the Darwin rural area (Humpty Doo), Northern Territory, Australia. Serves civil head contractors, subcontractors, developers and interstate consultancies with contaminated land and PFAS investigations, construction environmental management plans (CEMPs), environmental audits and inspections, environmental approvals, cultural heritage/AAPA coordination and a retainer 'environmental department as a service'. Fixed-price packages. Principal: Chris Bell. Phone "+PHONE+". Email "+EMAIL+".\n\n"
    llms+="Service regions in priority order: (1) Darwin, Palmerston and the Litchfield rural area; (2) the Top End including Katherine, Kakadu/Jabiru, Arnhem Land, Nhulunbuy and the Tiwi Islands; (3) the wider Northern Territory and the East Kimberley region of Western Australia (Kununurra, Wyndham, Halls Creek).\n\n## Services\n"
    llms+="".join(f"- [{s['h1']}]({BASE}/services/{s['slug']}/): {s['desc']}\n" for s in SERVICES)
    llms+="\n## Regions\n"+"".join(f"- [{r['h1']}]({BASE}/regions/{r['slug']}/): {r['desc']}\n" for r in REGIONS)
    llms+="\n## Guides\n"+"".join(f"- [{g['title']}]({BASE}/guides/{g['slug']}/): {g['desc']}\n" for g in GUIDES)
    llms+=f"\n## Other\n- [About Chris Bell]({BASE}/about/)\n- [Contact]({BASE}/contact/)\n"
    open(os.path.join(OUT,"llms.txt"),"w").write(llms)

if __name__=="__main__":
    shutil.rmtree(OUT, ignore_errors=True)
    home(); services_index(); [service(s) for s in SERVICES]
    regions_index(); [region(r) for r in REGIONS]
    guides_index(); [guide(g) for g in GUIDES]
    about(); contact(); statics()
    print(f"built {len(pages)} pages -> {OUT}/")
