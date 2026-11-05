# Site copy for bellenviro.au. Edit here, then run build.py.
# Voice: plain, direct, NT-specific. Bell Enviro / Chris as the subject, not "we".

SERVICES = [
 dict(slug="contaminated-land-assessment", nav="Contaminated Land",
  title="Contaminated Land Assessment Darwin NT | PSI & DSI",
  h1="Contaminated land assessment: PSI and DSI",
  desc="Preliminary and detailed site investigations (PSI/DSI) in Darwin, Palmerston and across the NT. Done to the ASC NEPM, fixed price, written and signed by the person who did the work.",
  intro="Buying a block, lodging a DA, pulling out an old fuel tank, or hit something that smells wrong in a trench. These are the jobs that need a site investigation. Bell Enviro does them to the ASC NEPM and NT EPA guidelines, with NATA-accredited labs, and writes the report in a way that the regulator, the auditor and the bank can all use.",
  bullets=["Preliminary Site Investigation (PSI): site history, records, walkover, conceptual site model",
           "Detailed Site Investigation (DSI): soil, groundwater and vapour sampling, designed to answer the actual question",
           "Waste classification for fill and excavated material (VENM, ENM, contaminated fill)",
           "Fuel tank decommissioning: validation sampling and the paperwork to close it out",
           "Acid sulfate soil assessment and management plans",
           "Validation and clearance reports for auditors and the NT EPA"],
  who="People buying or developing land in Darwin and Palmerston, civil contractors who have found something unexpected mid-job, Defence and airport precinct works, and interstate consultancies that need someone on the ground in Darwin.",
  pricing="PSIs are a fixed price. DSIs are a fixed price for the design, fieldwork and report, with lab fees at cost. The scope is agreed before anything starts.",
  faqs=[("Do I need a PSI or a DSI?","Start with a PSI. It works out whether contamination is likely from the site's history and a walkover. If it finds a reason for concern, a DSI goes out and samples to confirm it and map how far it goes. Most land deals and DAs only ever need the PSI."),
        ("Will the NT EPA accept the report?","Reports are written to the ASC NEPM and NT EPA contaminated land guidelines. That is what the EPA and the contaminated land auditors assess against."),
        ("How long does a PSI take in Darwin?","Usually two to three weeks, mostly waiting on title searches and records. A DSI depends on lab turnaround, which is five to ten business days after sampling.")]),
 dict(slug="pfas-investigation", nav="PFAS",
  title="PFAS Testing & Investigation Darwin NT | Soil, Water, Defence Precincts",
  h1="PFAS testing, investigation and management",
  desc="PFAS testing of soil, groundwater and surface water in Darwin and the NT, done to the PFAS NEMP. Sampling, waste classification and management plans for civil works near the airport, RAAF base and East Arm.",
  intro="PFAS is the firefighting foam chemical. Around Darwin it sits in the soil and groundwater near the airport, the RAAF base, old fire training grounds and some legacy industrial land, and it has moved along the drains from there. If you are digging in those areas the material may need testing before it leaves site. Bell Enviro runs PFAS sampling to the PFAS National Environmental Management Plan with the right PFAS-free kit and NATA-accredited labs.",
  bullets=["PFAS screening added to a PSI or DSI",
           "Soil, groundwater, surface water and sediment sampling to NEMP protocols",
           "Waste classification and a disposal or reuse pathway for excavated material",
           "PFAS management plans for civil works in affected precincts",
           "Advice on dewatering and stockpiles when PFAS-impacted water or soil turns up"],
  who="Civil contractors working near Darwin International Airport, RAAF Base Darwin, East Arm and other PFAS areas. Developers buying old industrial land. Project managers who need to know where the dirt can go.",
  pricing="Fixed price for the investigation design, fieldwork and report. Lab fees at cost.",
  faqs=[("Where is PFAS a problem around Darwin?","The airport and RAAF base precincts and the suburbs and drains downstream of them, plus any site where firefighting foam was used or stored. If you are excavating in those areas, assume you need to test before material leaves site."),
        ("Can PFAS-impacted soil be reused on site?","Often, yes, under a management plan consistent with the PFAS NEMP. Off-site disposal needs classification and a licensed facility, and there are not many of those in the NT, so on-site reuse is usually the practical answer."),
        ("How much does PFAS testing cost in Darwin?","More than a standard contamination suite. The samples go to specialist labs interstate, so a single soil or water sample is a few hundred dollars including the sampling. Bell Enviro quotes the whole program with the sample numbers the NEMP requires for your purpose."),
        ("What sampling precautions are needed?","PFAS is in waterproof clothing, sunscreen, some sample containers and a lot of normal field gear. If the sampling is not done with PFAS-free equipment and proper decontamination, the results are meaningless. Bell Enviro's protocols follow the NEMP.")]),
 dict(slug="construction-environmental-management-plan", nav="CEMPs & ESCPs",
  title="Environmental Management Plans NT | CEMPs & Erosion and Sediment Control Plans",
  h1="Environmental management plans (CEMPs) and ESCPs",
  desc="Contract-ready CEMPs, erosion and sediment control plans, weed hygiene and dust and noise plans for NT Government, Defence and council civil works. Fixed price, usually within five to ten business days.",
  intro="On most NT Government, Defence and council civil jobs the CEMP has to be approved before you can set up on site. A generic plan with the contract name swapped in gets sent back. Bell Enviro writes the plan from the actual contract clauses, the site and your methodology, so the superintendent approves it first time and your crew can actually follow it.",
  bullets=["CEMPs to NTG, Defence and council specifications",
           "Erosion and Sediment Control Plans that allow for a Top End Wet season",
           "Weed hygiene and management: plans, declarations and wash-down procedures",
           "Dust, noise, vibration and water quality management",
           "Incident and non-conformance procedures that a site supervisor will actually use",
           "Help running the plan: inductions, inspections and monitoring"],
  who="Civil head contractors and subcontractors on roads, water and sewer, subdivisions, airfield, Defence estate and remote community work across the NT.",
  pricing="Fixed price per plan, scoped to the contract. Site support at a day rate or under a retainer.",
  faqs=[("Do I need a CEMP for NT Government civil works?","Almost always. NTG, Defence and council construction contracts require one before site establishment, and most need the superintendent to approve it. Check the environmental clauses in your contract, or send them to Bell Enviro to check."),
        ("How quickly can you turn a CEMP around?","A standard civil works CEMP is normally five to ten business days from receiving the contract documents and your methodology. Faster is possible if the job is urgent."),
        ("Can you also implement the CEMP on site?","Yes. Inspections, monitoring, incident support and close-out reporting, either per visit or under a retainer.")]),
 dict(slug="environmental-auditing-compliance", nav="Auditing & Compliance",
  title="Environmental Compliance Audits & Inspections Darwin NT",
  h1="Environmental audits, inspections and compliance",
  desc="Independent environmental audits, site inspections, monitoring programs and incident systems for civil works in Darwin and across the NT. Findings written as actions, not pages of observations.",
  intro="An audit should tell you what is wrong, who fixes it and by when. Bell Enviro audits against your approvals, licences, CEMP and contract conditions, following ISO 19011, and writes the findings as a short action list rather than a long report nobody reads.",
  bullets=["Compliance audits against approvals, licences, CEMPs and contract conditions",
           "Regular site inspections on live civil works",
           "Monitoring programs: water, dust, noise, stockpiles, sediment controls",
           "Incident and non-conformance systems your own people can run",
           "Retrospective compliance reviews when the records have gaps",
           "Close-out and completion reports at handover"],
  who="Head contractors who want an independent look before the principal's auditor arrives. Principals and project managers who want to know how the contractor is going. Operators holding NT EPA licences or approvals.",
  pricing="Fixed price per audit or inspection program, or a day rate.",
  faqs=[("What does an environmental audit involve?","A read of your approvals and plans, a site walk, a chat with the site staff, and a report listing what conforms, what doesn't, and what to do about it."),
        ("How often should a civil site be inspected?","Weekly during earthworks and through the Wet. Fortnightly or monthly once the site has stabilised. A lot of contracts set the frequency."),
        ("Our records have gaps. Can that be fixed?","Bell Enviro can rebuild monitoring, inspection and incident records from whatever evidence exists, say plainly where the gaps are, and set up a system so it doesn't happen again.")]),
 dict(slug="environmental-approvals", nav="Approvals",
  title="Environmental Approvals NT | NT EPA Referrals, Licences, Land Clearing Permits",
  h1="Environmental approvals, NT EPA referrals and permits",
  desc="NT EPA referrals, environment protection licences, land clearing and water permits, and approvals advice for projects in Darwin, the Top End and the NT.",
  intro="The NT has its own Environment Protection Act, Water Act, Planning Act and Weeds Management Act, plus the Commonwealth EPBC Act on top. Working out which ones apply to a project, and in what order, is half the job. Bell Enviro scopes the approvals a project actually needs, prepares the applications and deals with the agency.",
  bullets=["Approvals scoping: which Acts, which agency, how long",
           "NT EPA referrals and environmental impact assessment support",
           "Environment protection licences for extractives, waste and industrial sites",
           "Land clearing permits, water extraction and discharge licences",
           "Environmental reports for development applications, and conditions compliance afterwards",
           "EPBC Act self-assessment and referrals"],
  who="Developers, quarry and extractive operators, civil contractors who have taken on the approvals obligations, and interstate proponents who don't know the NT system.",
  pricing="Fixed price for scoping and standard applications. Larger assessments are scoped per project.",
  faqs=[("Does my project need an NT EPA referral?","Only if it could have a significant impact on the environment. Most civil jobs don't. Extractives, large clearing and work in sensitive areas might. A short scoping review answers it early, before it becomes a program problem."),
        ("How long do NT environmental approvals take?","Simple licences and permits take weeks. An EPA assessment takes many months. The biggest time saver is starting the scoping early."),
        ("Can you deal with the agency for me?","Yes. Bell Enviro deals with the NT EPA, DEPWS, the Development Consent Authority and AAPA on clients' behalf all the time.")]),
 dict(slug="environmental-department-as-a-service", nav="Retainer",
  title="Environmental Department as a Service | Retainer for NT Civil Contractors",
  h1="Your environmental department, as a service",
  desc="A monthly retainer that gives NT civil contractors an environmental scientist on call for advice, document reviews, incident response and priority delivery of CEMPs, audits and investigations, without hiring one.",
  intro="Most mid-sized civil contractors need an environmental person but not a full-time one. The retainer gives you Chris on call: tender reviews, CEMPs, incidents, regulator calls and site inspections, with one number to ring and your jobs at the front of the queue.",
  bullets=["Monthly base fee covering availability, advice and document reviews",
           "CEMPs, audits, investigations and approvals delivered at agreed rates, ahead of non-retainer work",
           "Environmental clause review on tenders before you price them",
           "Incident and regulator response, including first-call attendance",
           "Inductions and toolbox material for your crews",
           "Only a handful of contractors at a time, so response stays fast"],
  who="NT civil contractors with steady NTG, Defence or council work who want the environmental capability of a bigger firm without the salary.",
  pricing="Monthly retainer with set inclusions and agreed rates for deliverables. Three-month minimum.",
  faqs=[("How is this different from hiring an environmental officer?","You get senior, insured, sign-off-capable expertise for less than a junior's salary, with no recruitment, leave or supervising. The trade-off is that Chris is shared with a small number of other clients."),
        ("What's in the base fee?","Availability, phone and email advice, document and tender reviews, and a set number of hours for inspections or meetings. Bigger deliverables are priced at rates agreed up front."),
        ("Can we start with one project?","Yes. Most retainer clients started with one CEMP or audit and moved across when the second job came in.")]),
 dict(slug="cultural-heritage-aapa", nav="Cultural Heritage",
  title="Cultural Heritage & AAPA Clearance Coordination NT",
  h1="Cultural heritage and AAPA certificates",
  desc="AAPA Authority Certificate applications, heritage due diligence, Traditional Owner engagement and archaeological survey coordination for projects anywhere in the NT.",
  intro="Sacred sites law applies to every bit of ground in the Territory, whatever the tenure. Most government and Defence contracts want an AAPA certificate before you break ground, and the certificate takes months. Bell Enviro gets the AAPA application in early, handles the heritage due diligence and the consultation, and brings in archaeologists or anthropologists when a job needs them.",
  bullets=["AAPA Authority Certificate applications and clearance coordination",
           "Heritage due diligence under the NT Heritage Act 2011",
           "Traditional Owner and land council engagement, with consultation records",
           "Archaeological surveys through qualified archaeologists",
           "Heritage management plans and unexpected finds procedures for your CEMP"],
  who="Civil contractors and developers on Crown land, Aboriginal land, remote community projects and greenfield sites anywhere in the NT.",
  pricing="Scoped per project. AAPA fees and specialist fees at cost.",
  faqs=[("Do I need an AAPA certificate?","It isn't compulsory, but it's the only legal defence if works damage a sacred site, and most NT Government and Defence contracts require one before ground disturbance."),
        ("How long does an AAPA certificate take?","Months. Which is why Bell Enviro raises it in the first conversation about any project."),
        ("Do you run the consultation yourselves?","Consultation goes through AAPA and the land councils. Bell Enviro coordinates it and engages qualified anthropologists and archaeologists when the project needs a specialist survey.")]),
 dict(slug="compliance-registers", nav="Compliance registers",
  title="Compliance, Stockpile & Incident Registers for NT Civil Contractors",
  h1="Compliance, stockpile and incident registers",
  desc="Simple obligations, stockpile and incident registers for civil contractors, set up and kept honest by Bell Enviro so the evidence is there when the auditor or the principal asks.",
  intro="Most compliance failures on civil sites aren't about the controls. The control was there. Nobody can prove it. Bell Enviro sets up plain registers for approval obligations, stockpiles and incidents, trains the supervisors to keep them, and checks them periodically. A hosted version is being trialled with an NT head contractor.",
  bullets=["Obligations register: every approval, licence and contract condition, with an owner and the evidence",
           "Stockpile register: classification, source, volume and where each pile went",
           "Incident and non-conformance register with investigation and close-out tracking",
           "Monthly compliance status for the principal or superintendent",
           "An audit-ready evidence pack at completion"],
  who="Civil contractors on projects with approval conditions, particularly anyone handling fill, contaminated or PFAS-impacted material, or working under NTG and Defence contracts.",
  pricing="Set-up fee per project, plus optional monthly maintenance. Register interest in the hosted version through the contact page.",
  faqs=[("Is this software?","Right now it's a structured system in tools your site team already uses, set up and reviewed by Bell Enviro. A hosted version is in trial. Get in touch if you want to be part of it."),
        ("Why a stockpile register?","Because regulators and principals now ask where every cubic metre came from and went. A stockpile register answers that in minutes instead of a week of digging through dockets.")]),
 dict(slug="asbestos-hazmat-darwin", nav="Asbestos & hazmat",
  title="Asbestos Testing, Registers & Hazmat Surveys Darwin NT",
  h1="Asbestos testing, registers and hazmat surveys",
  desc="Asbestos sampling with NATA-accredited identification, asbestos registers and management plans, pre-demolition hazmat surveys and Class B clearance inspections in Darwin, Palmerston and the NT. Licensed assessors brought in for friable and Class A work.",
  intro="Most Darwin buildings from before 1990, and a lot of the post-Tracy rebuild, have asbestos in them. Before you renovate, demolish, dig near an old slab or buy a commercial building, find out what's there. Bell Enviro samples suspect materials and sends them to a NATA-accredited lab, writes asbestos registers and management plans that meet NT WHS requirements, and does pre-demolition hazmat surveys. Chris has substantial hazmat experience and handles non-friable (Class B) work directly. For friable asbestos and Class A removals Bell Enviro brings in a licensed asbestos assessor or occupational hygienist and manages the job end to end.",
  bullets=["Asbestos identification: sampling of suspect materials, NATA-accredited lab analysis, written result",
           "Asbestos registers and management plans for workplaces under the NT WHS Regulations",
           "Pre-demolition and pre-refurbishment hazmat surveys: asbestos, lead paint, synthetic mineral fibre, PCBs, ozone-depleting substances",
           "Asbestos in soil: assessment, sampling and waste classification on civil sites",
           "Clearance inspections and certificates for non-friable (Class B) removals",
           "Licensed assessors and hygienists arranged for friable (Class A) removals, air monitoring and clearance",
           "Scoping, specifying and supervising removal contractors"],
  who="Renovators and property buyers in Darwin and Palmerston, builders and demolition contractors, body corporates and commercial property managers who need a register, and civil crews who have found asbestos fragments in fill.",
  pricing="Fixed per-sample price for identification, lab included. Registers and surveys are quoted on building size. Clearance inspections at a fixed rate per visit.",
  faqs=[("How much does asbestos testing cost in Darwin?","A single suspect material, with NATA lab analysis and a written result, is a fixed per-sample price. A typical house with a handful of samples is quoted as a package. Ask Bell Enviro for current rates."),
        ("How long do asbestos results take?","Two to three business days from the lab receiving the samples. Same-day or next-day is available at extra cost if demolition is waiting or there's been an incident."),
        ("Do I legally need an asbestos register?","Yes, for any workplace building built before 31 December 2003 where asbestos is or might be present. For a house it's not compulsory, but get one before renovating. A lot of builders won't quote without it."),
        ("Who can do a clearance inspection in the NT?","For non-friable (Class B) removals, a competent person independent of the removalist. For friable (Class A), a licensed asbestos assessor. Bell Enviro does the first directly and brings in a licensed assessor for the second."),
        ("We've found asbestos in soil on site. Now what?","Stop work in that area and get it assessed. Bell Enviro samples and classifies the material, advises on management or disposal under the ASC NEPM and NT EPA requirements, and documents the clearance so work can restart.")]),
 dict(slug="soil-testing-darwin", nav="Soil testing",
  title="Soil Testing Darwin NT | Contamination, Waste Classification, PFAS",
  h1="Soil testing in Darwin and the Top End",
  desc="Soil sampling and testing in Darwin, Palmerston and the rural area: contamination screening, waste classification of fill and excavated material, PFAS, acid sulfate soils and asbestos in soil. NATA labs, results explained.",
  intro="Soil testing only helps if the right things are tested for, the samples are taken properly and someone explains what the numbers mean. Bell Enviro designs the sampling, collects it, uses NATA-accredited labs in Darwin and interstate, and tells you in plain terms what the results mean for your block, your disposal docket or your DA.",
  bullets=["Contamination screening for a property purchase, DA or rezoning",
           "Waste classification of fill, excavated material and stockpiles for disposal or reuse",
           "PFAS soil testing to NEMP protocols",
           "Acid sulfate soil testing (field pH and lab chromium-reducible sulfur)",
           "Asbestos in soil screening and quantification",
           "Hydrocarbons, metals, pesticides and nutrients, interpreted against ASC NEPM and NT EPA criteria",
           "Agricultural and horticultural soil testing on request"],
  who="Landowners and buyers in Darwin, Palmerston and the Litchfield rural area, builders and civil contractors classifying material, and project managers dealing with an unexpected find.",
  pricing="Fixed price per sampling visit plus lab fees at cost. The analysis suite is agreed before sampling so there are no surprises on the invoice.",
  faqs=[("How much does soil testing cost in Darwin?","A basic contamination screen on one sample for metals and hydrocarbons is in the low hundreds including the lab. Classifying a stockpile depends on its volume, because the NEPM and NT EPA set a minimum number of samples per cubic metre. Bell Enviro quotes the whole program up front."),
        ("Can I collect the samples myself?","You can, but labs and regulators only rely on results where the method, containers and chain of custody are documented. Badly collected samples are the most common reason results get thrown out, and a sampling visit is usually cheaper than doing it twice."),
        ("Which lab do you use?","NATA-accredited labs with Darwin receipt for standard suites, and specialist interstate labs for PFAS and asbestos quantification. The lab certificate comes attached to the report.")]),
 dict(slug="water-testing-darwin", nav="Water testing",
  title="Water Testing Darwin NT | Bore Water, Surface Water, Dewatering & Discharge",
  h1="Bore water, surface water and discharge testing in Darwin",
  desc="Bore water, groundwater, surface water, dewatering and discharge sampling in Darwin, Palmerston and the rural area, with NATA-accredited analysis and results explained against drinking water, irrigation and NT EPA criteria.",
  intro="Rural area houses run on bores. Civil sites pump out groundwater. Approvals want the creek monitored. Bell Enviro samples bores, monitoring wells and surface water properly, with purging, field parameters and chain of custody, and reports the results against the criteria that apply: the Australian Drinking Water Guidelines for a household, ANZG guidelines and licence limits for a discharge.",
  bullets=["Bore water testing for drinking, stock and irrigation use in the Darwin rural area",
           "Groundwater monitoring well sampling for contaminated land and PFAS investigations",
           "Dewatering and construction discharge sampling against NT EPA and licence criteria",
           "Surface water and sediment monitoring for CEMPs and approvals",
           "Field parameters: pH, conductivity, dissolved oxygen, turbidity",
           "Plain-English results"],
  who="Rural area homeowners and buyers on bore water, civil contractors with dewatering or discharge conditions, and developers with water monitoring obligations.",
  pricing="Fixed price per sampling visit plus lab fees at cost. Monitoring programs priced per round.",
  faqs=[("How much is bore water testing in Darwin?","A standard household suite (bacteria, metals, major ions, nitrate) including sampling and lab is a fixed package. Ask for the current price. Results are reported against the Australian Drinking Water Guidelines."),
        ("How often should I test my bore?","Bacteria at least yearly, and after flooding, works near the bore, or any change in taste or colour. A full chemistry suite every few years or when buying the property."),
        ("Can you test dewatering water before we discharge?","Yes. Bell Enviro samples for the parameters in your discharge condition with fast turnaround, and can set up the ongoing monitoring the condition requires.")]),
]

REGIONS = [
 dict(slug="darwin-palmerston-rural", nav="Darwin, Palmerston & Rural",
  title="Environmental Consultant Darwin, Palmerston & Rural Area NT",
  h1="Darwin, Palmerston and the rural area",
  desc="Darwin-based environmental consultant covering Darwin, Palmerston, Humpty Doo, Howard Springs, Berry Springs, Noonamah, Coolalinga and the Litchfield rural area. Contaminated land, PFAS, asbestos, CEMPs, audits and approvals.",
  places="Darwin city and the northern suburbs, East Arm and Berrimah, the airport and RAAF base precincts, Palmerston and its new suburbs, Humpty Doo, Howard Springs, Coolalinga, Berry Springs, Noonamah, Virginia, Bees Creek, Darwin River and the rest of Litchfield, Cox Peninsula and Dundee.",
  body="This is home. Bell Enviro is based in Humpty Doo, so site attendance across Darwin, Palmerston and Litchfield is same-day and there's no travel charge within the greater Darwin area. It also means local knowledge that doesn't come from a desktop: Wet-season drainage, acid sulfate soils around the harbour and the lowlands, the PFAS areas near the airport and base, and the legacy industrial land at East Arm, Berrimah and Winnellie.",
  work=["CEMPs and ESCPs for subdivision and road earthworks in the Palmerston and Litchfield growth areas",
        "PSIs and DSIs for industrial land deals at East Arm, Berrimah and Winnellie",
        "Waste classification and PFAS screening for airport precinct and Defence-adjacent works",
        "Quarry and extractive compliance in the rural area",
        "Asbestos registers and sampling for Darwin and Palmerston properties",
        "Weed hygiene declarations and inspections for rural area civil works"]),
 dict(slug="top-end", nav="Top End",
  title="Environmental Consultant Top End NT | Katherine, Jabiru, Arnhem Land, Tiwi",
  h1="The Top End",
  desc="Remote-capable environmental consultant for the Top End: Katherine, Kakadu and Jabiru, West and East Arnhem Land, Nhulunbuy, the Tiwi Islands, Daly River and the Victoria River district.",
  places="Katherine and the Katherine region, Pine Creek and Adelaide River, Kakadu and Jabiru, West Arnhem including Maningrida and Gunbalanya, East Arnhem including Nhulunbuy and Galiwin'ku, the Tiwi Islands, Wadeye and the Daly, Timber Creek and the Victoria River district.",
  body="Remote Top End jobs fail on logistics, not science. Bell Enviro has done the compliance auditing and CEMP implementation for water and distribution upgrades in Jabiru and is set up for remote work: self-contained field kit, sample cold chain back to the Darwin labs, and the permits and inductions that Aboriginal land and Kakadu need. Fieldwork gets planned around the Dry. Reporting happens in the Wet.",
  work=["CEMP implementation and compliance auditing for remote community infrastructure upgrades",
        "Contaminated land and fuel storage investigations at remote facilities and communities",
        "Weed hygiene and biosecurity planning for moving plant into Arnhem Land and the Tiwi Islands",
        "AAPA and Traditional Owner engagement for works on Aboriginal land",
        "Approvals support for extractive and infrastructure projects around Katherine"]),
 dict(slug="northern-territory-kimberley", nav="NT & Kimberley",
  title="Environmental Consultant Northern Territory & Kimberley WA",
  h1="The rest of the NT and the Kimberley",
  desc="Environmental consulting across the Northern Territory and north-east WA: Tennant Creek, Alice Springs, the Barkly, Kununurra, Wyndham, Halls Creek and the East Kimberley.",
  places="Tennant Creek and the Barkly, Alice Springs and Central Australia, the Gulf and Borroloola, and over the border to Kununurra, Wyndham, Lake Argyle, Halls Creek, Fitzroy Crossing and the East Kimberley.",
  body="For work outside the Top End, Bell Enviro is the Darwin-based alternative to flying a team in from Perth, Adelaide or Brisbane. Kununurra is a shorter drive from Darwin than it is a flight from Perth, and the country is the same: Wet season, savanna, Aboriginal land, long distances. WA jobs are done under the Contaminated Sites Act 2003 and the Environmental Protection Act 1986 with the DWER guidelines.",
  work=["Contaminated land investigations and waste classification at mining support, pastoral and infrastructure sites",
        "CEMPs and site inspections for road, water and community infrastructure projects",
        "PFAS screening at airstrips, depots and fire training sites",
        "Environmental audits of remote operations for principals and financiers",
        "Approvals scoping for NT and WA proponents"]),
]

GUIDES = [
 dict(slug="do-i-need-a-cemp-for-nt-government-works", title="Do I need a CEMP for NT Government or Defence civil works?",
  desc="When a Construction Environmental Management Plan is required on NT Government, Defence and council contracts, what has to be in it, and how to get it approved first time.",
  body="""<p>Short answer: almost certainly. NT Government (DIPL, Power and Water, Housing), Defence estate and council construction contracts nearly all have a clause requiring a CEMP before site establishment. Private principals are asking for them too, because their own approval conditions say so.</p>
<h2>What triggers it</h2>
<ul><li>A contract clause, usually in the general conditions or the environmental section of the spec, requiring an approved CEMP before you start.</li><li>A development permit or NT EPA approval condition that gets passed down to the contractor.</li><li>Work near waterways, on Aboriginal land, in Kakadu, on Defence land, or on a site with known contamination.</li></ul>
<h2>What the superintendent wants to see</h2>
<ul><li>Risks specific to this site, not a generic table: Wet-season erosion, dust, weeds, fuel and chemical storage, waste and stockpiles, heritage, fauna.</li><li>Controls that match your actual methodology and plant.</li><li>An Erosion and Sediment Control Plan, normally with a drawing.</li><li>Weed hygiene procedures and vehicle wash-down declarations.</li><li>Monitoring, inspection and incident procedures with names against them.</li><li>Evidence of inductions and training.</li></ul>
<h2>Getting it approved first time</h2>
<p>Send your consultant the full environmental clauses, the spec, the approval conditions and your methodology. Plans get rejected when they are generic and don't reference the contract. A plan written from the contract normally gets through in one round.</p>
<p>Bell Enviro writes contract-ready CEMPs for NT civil works at a fixed price, usually inside five to ten business days. See <a href="/services/construction-environmental-management-plan/">CEMPs and ESCPs</a>.</p>"""),
 dict(slug="psi-vs-dsi-contaminated-land-nt", title="PSI vs DSI: which contaminated land assessment do you need in the NT?",
  desc="The difference between a Preliminary Site Investigation and a Detailed Site Investigation under the ASC NEPM, when each is needed in the NT, and roughly what they cost.",
  body="""<p>Contaminated land assessment in the NT follows the National Environment Protection (Assessment of Site Contamination) Measure 1999, the ASC NEPM, which the NT EPA adopts as its standard. It's a staged process, and you only go to the next stage if the current one says you need to.</p>
<h2>Preliminary Site Investigation (PSI)</h2>
<p>A PSI answers one question: is contamination likely here? It looks at land titles, historical aerial photos, government records, old reports and whoever knows the site, then walks the ground looking for evidence. The result is a conceptual site model and a yes or no on further work. Sometimes a few samples go in at this stage if they'll settle the question early.</p>
<p>Typical triggers: buying land, a DA where the planning authority asks about contamination, rezoning to a more sensitive use, and pulling out fuel storage.</p>
<h2>Detailed Site Investigation (DSI)</h2>
<p>A DSI goes and samples. Soil, groundwater, sometimes vapour, designed from the PSI's site model under a sampling and analysis quality plan and reported against the NEPM investigation levels. If it finds a risk, the next step is a remediation action plan or a site management plan.</p>
<h2>Which one?</h2>
<ul><li>No history of anything nasty and a planning authority asking a general question: PSI.</li><li>Known or suspected contamination, a PSI that recommended more work, or an auditor involved: DSI.</li><li>Something unexpected in a trench (staining, smell, drums, fill of unknown origin): a targeted investigation and waste classification, usually in a hurry.</li></ul>
<h2>Cost and timing in Darwin</h2>
<p>Bell Enviro does PSIs at a fixed price in two to three weeks, and DSIs at a fixed price for the design, fieldwork and report with lab fees at cost. See <a href="/services/contaminated-land-assessment/">contaminated land assessment</a>.</p>"""),
 dict(slug="pfas-testing-civil-works-darwin", title="PFAS testing for civil works around Darwin: what contractors need to know",
  desc="Where PFAS is a problem for civil works around Darwin, when excavated soil needs testing, and what the PFAS NEMP means for reusing or disposing of material.",
  body="""<p>PFAS is the firefighting foam chemical. It's in the soil and groundwater around airports, Defence bases and fire training grounds, and around Darwin the declared investigation areas take in RAAF Base Darwin, Darwin International Airport and the suburbs and drains downstream. Old industrial sites and landfills can have it too.</p>
<h2>When excavated material needs testing</h2>
<ul><li>You're working inside or downstream of a declared PFAS investigation or management area.</li><li>Material is leaving site and the receiving facility wants PFAS results, which is now standard.</li><li>You're dewatering to stormwater or land.</li><li>The contract or the CEMP says so.</li></ul>
<h2>What the PFAS NEMP means on site</h2>
<p>The PFAS National Environmental Management Plan sets the criteria for reusing, managing and disposing of PFAS-impacted soil and water. For a Top End contractor it comes down to this: test before you move it, keep it on site under a management plan where you can because licensed PFAS disposal in the NT is scarce, and don't spread impacted groundwater around with the dewatering.</p>
<h2>Sampling matters</h2>
<p>PFAS is in waterproof clothing, sunscreen, some sample bottles and plenty of ordinary field gear. If the sampling isn't done with PFAS-free equipment, the results are useless. Use someone who runs NEMP protocols and NATA labs.</p>
<p>Bell Enviro does PFAS screening, waste classification and management plans for civil works across Darwin and the NT. See <a href="/services/pfas-investigation/">PFAS testing and investigation</a>.</p>"""),
 dict(slug="weed-hygiene-declaration-nt", title="Weed hygiene declarations for NT civil works: what's required",
  desc="What a weed hygiene declaration is, when NT Government and land council contracts require one, and how to set up wash-down and inspection procedures that stand up at audit.",
  body="""<p>The NT Weeds Management Act 2001 puts a duty on everyone to stop declared weeds spreading. NT Government, Defence, land council and a lot of private contracts turn that into paperwork: a weed hygiene declaration for every bit of plant and every vehicle coming onto site, and a weed section in the CEMP.</p>
<h2>What a declaration covers</h2>
<ul><li>Which machine or vehicle it is and where it has come from.</li><li>That it has been cleaned (wash-down or blow-down) of soil, seed and plant material, where and when.</li><li>Inspection and sign-off by someone competent.</li></ul>
<h2>Where it bites</h2>
<p>Taking plant into Arnhem Land, the Tiwi Islands, Kakadu, Groote Eylandt or onto pastoral stations often means declarations and inspections before the barge or at the boundary. Gamba grass, mission grass and mimosa are the big ones in the Top End. The Kimberley has its own list.</p>
<h2>Setting it up</h2>
<p>You need a declaration form, somewhere and some way to wash down, an inspection checklist, a register of declarations, and a toolbox talk so the operators know why they're doing it. Bell Enviro provides all of this as part of a CEMP and can do pre-mobilisation inspections. See <a href="/services/construction-environmental-management-plan/">CEMPs and ESCPs</a>.</p>"""),
 dict(slug="nt-epa-referral", title="NT EPA referral: when a project needs one and how it works",
  desc="When a project has to be referred to the NT EPA under the Environment Protection Act 2019, how the pre-referral screening tool works, what goes in a referral and how long it takes.",
  body="""<p>Under the NT Environment Protection Act 2019, a proponent has to refer a proposal to the NT EPA if it could have a significant impact on the environment. It's the proponent's call, which is why projects get it wrong both ways: referring when they didn't need to and losing months, or not referring and finding out at the approvals stage.</p>
<h2>Does your project need referring?</h2>
<ul><li>Start with the NT EPA's pre-referral screening tool and the Environmental Factors and Objectives guideline, both on the NT EPA website.</li><li>Usually yes: new or expanded extractive operations, large-scale clearing, industrial sites with significant discharges, major infrastructure in sensitive areas, and anything already flagged by another approval (a mining authorisation, a water licence).</li><li>Usually no: routine civil works in existing corridors, maintenance, subdivision earthworks already covered by a development permit, and small clearing under the permit thresholds.</li></ul>
<h2>What goes in a referral</h2>
<p>The proposal, the receiving environment, the potential impacts against each of the EPA's environmental factors, and how you'll manage them. A good referral is what gets you the outcome most proponents want: a decision that no further assessment is required.</p>
<h2>Timing</h2>
<p>The EPA has roughly four to six weeks to decide on a referral once it's accepted as complete. If they decide to assess, it runs many months. Put both scenarios in the program.</p>
<p>Bell Enviro scopes whether a referral is needed, writes referrals and deals with the NT EPA. See <a href="/services/environmental-approvals/">environmental approvals</a>.</p>"""),
 dict(slug="land-clearing-permit-nt", title="Land clearing permits in the NT: when you need one and how to apply",
  desc="When clearing native vegetation in the NT needs a permit under the Planning Act, what the Land Clearing Guidelines require, the exemptions, and how to put together an application that gets approved.",
  body="""<p>Clearing native vegetation in the NT generally needs a permit from the Development Consent Authority under the Planning Act 1999 and the NT Planning Scheme, assessed against the NT Land Clearing Guidelines. Pastoral land has its own process through the Pastoral Land Board.</p>
<h2>When you need a permit</h2>
<ul><li>Clearing more than the exempt area on a freehold lot. The threshold depends on the zone and in the rural area it's small.</li><li>Clearing within the buffers of watercourses, wetlands, rainforest and monsoon vine thicket, or threatened species habitat.</li><li>Clearing for subdivision, horticulture, industrial development, or new roads and tracks.</li></ul>
<h2>Exemptions that commonly apply</h2>
<p>Fire breaks of the prescribed width, fence lines, clearing within a set distance of a dwelling, and maintaining land that was already cleared. They're specific. Check the current guidelines before relying on one.</p>
<h2>What goes in an application</h2>
<ul><li>A clearing plan on aerial imagery showing the area, what's retained and the buffers.</li><li>A description of the vegetation and habitat, including threatened species and sensitive vegetation checks.</li><li>Erosion and sediment control, weed management and drainage.</li><li>Why you need that much clearing and what else was considered.</li></ul>
<p>Bell Enviro prepares clearing applications and the environmental information behind them, and can bundle the AAPA, weed and erosion requirements that usually come with them. See <a href="/services/environmental-approvals/">environmental approvals</a>.</p>"""),
 dict(slug="aapa-certificate-nt", title="AAPA Authority Certificates: what they are, when you need one and how long they take",
  desc="How AAPA Authority Certificates work in the NT, why most government and Defence contracts require one, how to apply, and what it costs and how long it takes.",
  body="""<p>An Authority Certificate from the Aboriginal Areas Protection Authority, under the NT Aboriginal Sacred Sites Act 1989, sets out the conditions for doing work without damaging or interfering with sacred sites. It's the only legal defence against prosecution under the Act. The Act applies everywhere in the Territory, on any tenure, whether or not a site is registered.</p>
<h2>When you need one</h2>
<ul><li>Most NT Government, Defence, land council and major private contracts require a current certificate before ground disturbance.</li><li>Any project on Aboriginal land, near a registered or recorded site, or in a greenfield area.</li><li>Any job where a stop-work order would hurt.</li></ul>
<h2>The process</h2>
<ol><li>Lodge an application with AAPA describing the works and the exact area, with a map and the activities.</li><li>AAPA consults the custodians, sometimes with a field survey.</li><li>AAPA issues the certificate with conditions: restricted areas, buffers, reporting.</li></ol>
<h2>Timing and cost</h2>
<p>Months. AAPA charges on the size and complexity of the area, and consultation and surveys add time and cost on remote jobs. Applying early with a clear, accurately mapped scope is the single biggest thing you can do to speed it up.</p>
<p>Bell Enviro prepares and manages AAPA applications and heritage due diligence for contractors and developers. See <a href="/services/cultural-heritage-aapa/">cultural heritage and AAPA</a>.</p>"""),
 dict(slug="gamba-grass-management-plan", title="Gamba grass and weed management plans for Darwin rural blocks and civil sites",
  desc="Gamba grass obligations for landholders and contractors around Darwin, what a weed management plan under the NT Weeds Management Act has to contain, and how to meet them without it taking over your life.",
  body="""<p>Gamba grass is a declared weed with its own statutory Weed Management Plan, and that plan puts obligations on every landholder in the declared zone, which takes in Darwin, Palmerston, Litchfield and Coomalie. It burns up to eight times hotter than native grass and is the main reason Top End fire seasons keep getting worse.</p>
<h2>What landholders have to do</h2>
<ul><li>Don't spread it. No moving gamba seed or plants, including in soil, hay, mulch, or on vehicles and machinery.</li><li>Control it on your block, with specific buffer requirements around buildings and boundaries depending on which zone you're in.</li><li>Keep records where the plan asks for them.</li></ul>
<h2>What it means for civil contractors</h2>
<p>Plant leaving gamba-infested sites has to be cleaned, and most NTG and council contracts want weed hygiene declarations and a weed section in the CEMP. Topsoil and fill out of the Darwin rural area is a known way of getting gamba and mission grass into new subdivisions and remote communities.</p>
<h2>What goes in a weed management plan</h2>
<ul><li>A map of what's where, by species and density.</li><li>Priorities: new outbreaks first, then containing the established areas, then the buffers.</li><li>Control methods and timing: spray at the right growth stage early in the Wet, slash before seed set, follow up.</li><li>Hygiene for vehicles, machinery and materials.</li><li>A monitoring and record schedule.</li></ul>
<p>Bell Enviro writes weed management plans for rural blocks, developments and civil jobs, and provides weed hygiene procedures and inspections. See <a href="/services/construction-environmental-management-plan/">CEMPs and ESCPs</a>.</p>"""),
]
