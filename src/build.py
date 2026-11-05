#!/usr/bin/env python3
"""Bell Enviro static site generator. Run: python3 build.py  -> writes ./out/"""
import os, json, shutil, html
from datetime import date

OUT = "out"
BASE = "https://bellenviro.au"
PHONE = "0424 577 159"; PHONE_INTL = "+61424577159"; EMAIL = "chris@bellenviro.au"
TODAY = date.today().isoformat()

from content import SERVICES, REGIONS, GUIDES

# ---------------------------------------------------------------- helpers
def esc(s): return html.escape(s, quote=True)

def ld(obj): return '<script type="application/ld+json">'+json.dumps(obj, ensure_ascii=False)+'</script>'

ORG = {"@type":"ProfessionalService","@id":BASE+"/#org","name":"Bell Enviro","url":BASE+"/",
  "logo":BASE+"/assets/logo.png","image":BASE+"/assets/logo.png","telephone":PHONE_INTL,"email":EMAIL,
  "description":"Environmental consultant in Darwin NT for civil contractors, developers and property owners: contaminated land, PFAS, asbestos and soil testing, CEMPs, audits, NT EPA approvals and AAPA sacred site certificates. Principal-delivered, fixed prices.",
  "address":{"@type":"PostalAddress","addressLocality":"Humpty Doo","addressRegion":"NT","postalCode":"0836","addressCountry":"AU"},
  "geo":{"@type":"GeoCoordinates","latitude":-12.58,"longitude":131.13},
  "areaServed":[{"@type":"City","name":"Darwin"},{"@type":"City","name":"Palmerston"},{"@type":"AdministrativeArea","name":"Litchfield Municipality"},
                {"@type":"Place","name":"Top End, Northern Territory"},{"@type":"State","name":"Northern Territory"},{"@type":"Place","name":"Kimberley, Western Australia"}],
  "founder":{"@type":"Person","@id":BASE+"/about/#chris","name":"Chris Bell","jobTitle":"Principal Environmental Scientist"},
  "priceRange":"$$","knowsAbout":["Contaminated land assessment","PFAS investigation","Construction environmental management plans","Environmental auditing","Environmental approvals Northern Territory","NT EPA referrals","Cultural heritage AAPA","Asbestos identification and registers","Soil and water testing","Flora and fauna surveys","ISO 14001 environmental management systems"],
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
  <div><h3>Bell Enviro</h3><p>Environmental consultant for civil contractors, developers and property owners. Based in Humpty Doo, works across the NT and the Kimberley.</p>
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
    cards = "".join(f'<a class="card" href="/services/{s["slug"]}/"><h3>{esc(s["h1"].split(" — ")[0].split(" (")[0])}</h3><p>{esc(s["desc"].split(". ")[0])}.</p></a>' for s in SERVICES)
    regs = "".join(f'<a class="card" href="/regions/{r["slug"]}/"><h3>{esc(r["nav"])}</h3><p>{esc(r["places"].split(",")[0])} and surrounds</p></a>' for r in REGIONS)
    guides = "".join(f'<li><a href="/guides/{g["slug"]}/">{esc(g["title"])}</a></li>' for g in GUIDES)
    body = f"""
<section class="hero"><div class="wrap">
 <p class="kicker">Environmental consultant · Darwin NT</p>
 <h1>Environmental compliance for NT civil contractors, developers and property owners. No headcount required.</h1>
 <p class="lead">Contaminated land, PFAS, asbestos and soil testing, CEMPs, audits, NT EPA approvals and sacred site clearances (AAPA certificates). Fixed prices agreed up front. Reports the regulator accepts. Chris Bell does the work and signs it.</p>
 <p><a class="btn big" href="/contact/">Get a fixed-price quote</a> <a class="btn ghost" href="tel:{PHONE_INTL}">Call {PHONE}</a></p>
 <p class="small">Servicing <a href="/regions/darwin-palmerston-rural/">Darwin, Palmerston and the rural area</a>, the <a href="/regions/top-end/">Top End</a>, and the <a href="/regions/northern-territory-kimberley/">wider NT and Kimberley</a>.</p>
</div></section>
<section class="wrap"><h2>Services</h2><div class="cards">{cards}</div></section>
<section class="alt"><div class="wrap"><h2>Why use Bell Enviro rather than a national firm</h2><div class="cols">
 <div><h3>One person, start to finish</h3><p>The person who quotes the job is the one on site and the name on the report. Insured, accountable, and the one who picks up the phone.</p></div>
 <div><h3>Fixed prices</h3><p>Scope, deliverables and dates agreed before anything starts. No open-ended hourly bills.</p></div>
 <div><h3>Knows the Territory</h3><p>Fieldwork and reporting all year round, planned around the Wet rather than stopped by it. Remote-capable. Working relationships with the NT EPA, DEPWS, Defence, AAPA, the land councils and the Darwin labs.</p></div>
 <div><h3>Quick, because it's lean</h3><p>The paperwork is automated so the time goes into the site, the data and the judgement calls. A standard CEMP takes days, not weeks.</p></div>
</div></div></section>
<section class="wrap"><h2>Where Bell Enviro works</h2><div class="cards">{regs}</div></section>
<section class="alt"><div class="wrap"><h2>Sectors</h2><p class="chips"><span>Defence</span><span>Aviation</span><span>Civil &amp; infrastructure</span><span>Construction &amp; demolition</span><span>Land development</span><span>Mining &amp; extractives</span><span>Oil &amp; gas</span><span>Government &amp; community</span></p></div></section>
<section class="wrap"><h2>Guides</h2><ul class="list">{guides}</ul></section>
{cta("Send Chris the contract clause or the site address and get a scoped price back, usually within two business days.")}
"""
    write("/", layout("/", "Environmental Consultants Darwin NT | Contaminated Land, PFAS, Asbestos, CEMPs | Bell Enviro",
        "Darwin environmental consultants for civil contractors, developers and property owners. Contaminated land, PFAS, asbestos and soil testing, CEMPs, environmental audits, NT EPA approvals and AAPA coordination. Fixed prices, principal-delivered.", body))
    pages.append(("/",1.0))

def services_index():
    cards = "".join(f'<a class="card" href="/services/{s["slug"]}/"><h3>{esc(s["h1"])}</h3><p>{esc(s["desc"])}</p></a>' for s in SERVICES)
    ch,cl = crumbs([("Home","/"),("Services","/services/")])
    body = f'{ch}<section class="wrap"><h1>Environmental consulting services</h1><p class="lead">Everything is scoped and priced before it starts, and Chris does the work. Pick the one that matches the contract clause or the problem on site.</p><div class="cards">{cards}</div></section>{cta()}'
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
    body=f'{ch}<section class="wrap"><h1>Where Bell Enviro works</h1><p class="lead">Based in Humpty Doo. Works across Darwin, the Top End, the rest of the NT and the East Kimberley.</p><div class="cards">{cards}</div></section>{cta()}'
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
    body=f'{ch}<section class="wrap"><h1>Guides for NT contractors and developers</h1><p class="lead">Straight answers to the questions that come up before a job starts.</p><div class="cards">{items}</div></section>{cta()}'
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
            "email":EMAIL,"telephone":PHONE_INTL,"url":BASE+"/about/","knowsAbout":ORG["knowsAbout"]}
    body=f"""{ch}
<section class="wrap prose"><h1>About Bell Enviro and Chris Bell</h1>
<p class="lead">Bell Enviro is Chris Bell, an environmental scientist in Humpty Doo who works as the environmental capability inside civil contractors' and developers' teams across the NT.</p>
<h2>How the practice works</h2>
<p>Chris does the work or directly supervises it. That's deliberate. What you're paying an environmental consultant for is the judgement and the signature, so the person who quotes the job is the one on site, reading the data and signing the report. The report production and data handling are automated as far as they sensibly can be, which is why the prices are what they are and the turnaround is quick.</p>
<h2>Experience</h2>
<ul>
<li>Environmental compliance auditing and CEMP implementation for water and distribution network upgrades in Jabiru, under an ongoing retainer with a civil head contractor</li>
<li>Waste classification and environmental assessment for apron expansion works in the Darwin International Airport precinct</li>
<li>Soil quality and contamination investigations for East Arm and Darwin industrial land transactions</li>
<li>Extractive and quarry environmental compliance in the Darwin rural area</li>
<li>Weed hygiene declarations, erosion and sediment control and incident reporting systems for live civil works</li>
<li>Asbestos and hazmat surveys, registers and Class B clearances</li>
<li>Flora and fauna surveys and wildlife management plans for clearing, Defence and civil works</li>
<li>Earlier work across Defence, aviation, oil and gas, mining, community development and cultural heritage in the NT and overseas</li>
</ul>
<h2>Credentials and cover</h2>
<ul><li>Environmental professional with over 25 years' experience, most of it in the Northern Territory</li><li>ISO 14001 environmental management systems auditor trained; audits to ISO 19011</li><li>Professional Indemnity and Public Liability insurance current</li><li>ICN Gateway registered</li><li>Working knowledge of Commonwealth, NT EPA, Defence, AAPA, ALRA, NLC and NTG frameworks</li></ul>
<h2>Partners</h2>
<p>Bigger programs draw on a bench of field techs, drillers, archaeologists, anthropologists, ecologists and licensed asbestos assessors that Bell Enviro has worked with before, and on Darwin's NATA-accredited labs. Interstate consultancies also use Bell Enviro as their Darwin field capacity, working to their own SAQPs and templates.</p>
</section>{cta("Not sure if Bell Enviro is the right fit? A ten-minute call usually sorts it out.")}"""
    write("/about/", layout("/about/","About Chris Bell | Principal Environmental Scientist, Darwin NT","Chris Bell is a Darwin-based environmental scientist delivering contaminated land, PFAS, CEMP, audit and approvals work for NT civil contractors and developers through Bell Enviro.", body,[cl,person]))
    pages.append(("/about/",0.6))

def contact():
    ch,cl=crumbs([("Home","/"),("Contact","/contact/")])
    body=f"""{ch}
<section class="wrap two"><div>
<h1>Contact Bell Enviro</h1>
<p class="lead">Send the contract clause, the site address or the problem. Chris will come back with a scoped price, usually within two business days.</p>
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
 <p class="small">Got attachments (contract clauses, drawings, old reports)? Email them to {EMAIL} after sending.</p>
</form></section>
<script>document.querySelector('[name=ts]').value=Date.now();</script>"""
    write("/contact/", layout("/contact/","Contact Bell Enviro | Environmental Consultant Darwin NT","Request a fixed-price quote for contaminated land, PFAS, CEMP, audit or approvals work in Darwin and the NT. Call 0424 577 159 or send an enquiry.", body,[cl]))
    pages.append(("/contact/",0.8))
    write("/thanks/", layout("/thanks/","Thanks | Bell Enviro","Your enquiry has been sent to Bell Enviro.", '<section class="wrap"><h1>Thanks. Your enquiry is on its way.</h1><p class="lead">Chris will reply within two business days. If it&#39;s urgent, call <a href="tel:'+PHONE_INTL+'">'+PHONE+'</a>.</p><p><a class="btn" href="/">Back to home</a></p></section>'))

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
