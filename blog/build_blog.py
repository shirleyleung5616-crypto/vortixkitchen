# -*- coding: utf-8 -*-
"""
Vortix Kitchen blog generator.

Every blog article is ONE concise pain point. To publish a new pain-point
article, append one dict to ARTICLES below and rerun this script:

    python build_blog.py

It regenerates all article HTML files, blog/index.html and sitemap.xml.
Keep bodies under 400 words, pure client value, no fluff. Design lives in blog.css (unchanged).
"""
import json
import os
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

WA_NUMBER = "8613790093901"
EMAIL = "Shirley20193@163.com"
DATE_ISO = "2026-08-24"
DATE_HUMAN = "Aug 24, 2026"

# Series order used on the blog index.
SERIES = [
    ("returns", "Returns & Quality — why units come back"),
    ("reliability", "Reliability in Tough Markets — why units fail in the field"),
    ("customs", "Customs & Compliance — why containers get held"),
    ("buying", "Buying & Selling — decisions that protect your margin"),
]

ARTICLES = [
    # ---------------- RETURNS / QUALITY ----------------
    {
        "slug": "pain-dead-on-arrival",
        "series": "returns",
        "cat": "RETURNS",
        "footer_label": "Dead on Arrival",
        "image": "page4_img1.jpeg",
        "readtime": "2 min read",
        "title": "Your Cookers Arrive Dead — the IGBT Shortcut Behind 100% Refunds",
        "description": "A dead-on-arrival induction cooker is a 100% refund. The cause is usually a cheap IGBT or bad solder, and the PO line that stops it.",
        "excerpt": "A dead-on-arrival unit is a 100% refund. The cause is usually a cheap IGBT or bad solder — and one line in your PO prevents it.",
        "related": ["pain-cracked-glass", "pain-slow-heating", "pain-igbt-overheat"],
        "cta_title": "Tired of dead-on-arrival units?",
        "cta_text": "Tell us your market and volume — we'll spec a branded IGBT with 100% burn-in and show you the batch test record before you order.",
        "wa_text": "Hi Vortix Kitchen, I keep getting dead-on-arrival cookers in [market]. Can you spec branded IGBT with 100% burn-in and share the test record?",
        "mail_subject": "Dead-on-arrival cookers",
        "mail_body": "Hi Vortix Kitchen, I need cookers that arrive alive. Please advise on branded IGBT, 100% burn-in and batch test records for my market.",
        "body": """<p>A dead-on-arrival cooker is the most expensive return you take: a 100% refund, the freight back, and a buyer who quietly switches supplier. In hot markets it happens more than factories admit.</p>
<p>The cause is almost always the same — an under-specced IGBT module or a poorly soldered board. The factory saves a few cents; you lose the whole sale.</p>
<h2>Put this in your PO</h2>
<p>"IGBT: branded module (Infineon / ST or equivalent); 100% power-on burn-in ≥ 30 min per unit; AOI-inspected soldering; batch burn-in record shipped with the goods."</p>
<p>A supplier who won't write that line has already told you everything.</p>""",
    },
    {
        "slug": "pain-cracked-glass",
        "series": "returns",
        "cat": "RETURNS",
        "footer_label": "Cracked Glass",
        "image": "page4_img1.jpeg",
        "readtime": "2 min read",
        "title": "Cracked Glass on Arrival — Why Cheap Ceramic Glass Is Pure Loss",
        "description": "Cracked glass on arrival is pure loss with no repair and no resale. The fix is grade-A glass and a drop-tested carton specified up front.",
        "excerpt": "Cracked glass on arrival is pure loss: no repair, no resale. The fix is grade-A glass and a drop-tested carton, specified up front.",
        "related": ["pain-dead-on-arrival", "pain-slow-heating", "pain-dusty-fan"],
        "cta_title": "Want glass that survives the box?",
        "cta_text": "Send us your target market and we'll spec tempered microcrystalline glass with a drop-tested sea carton — and show the drop-test record.",
        "wa_text": "Hi Vortix Kitchen, I get cracked-glass returns on arrival. Can you spec grade-A glass with a drop-tested carton?",
        "mail_subject": "Cracked glass on arrival",
        "mail_body": "Hi Vortix Kitchen, please advise on tempered microcrystalline glass and drop-tested carton to stop cracked-glass returns.",
        "body": """<p>Cracked glass on arrival is pure loss — no repair, no resale, just a refund and a dent in your name. The box opens, the cooktop is shattered, and the unit you never sold costs you full price.</p>
<p>The cause is low-grade ceramic glass or a carton that never saw a drop test.</p>
<h2>Put this in your PO</h2>
<p>"Glass: tempered microcrystalline, Schott/Eurokera grade or verified equivalent; sea-freight carton validated by drop test; corner protectors mandatory."</p>
<p>Then ask for the drop-test record. No record means the carton is a guess.</p>""",
    },
    {
        "slug": "pain-slow-heating",
        "series": "returns",
        "cat": "RETURNS",
        "footer_label": "Slow Heating",
        "image": "page2_img8.jpeg",
        "readtime": "2 min read",
        "title": "'It Heats Slowly' Complaints — the Copper-Coil Shortcut Behind the Return",
        "description": "'It doesn't heat properly' triggers a return even when the unit works. The usual culprit is an aluminum-clad heating coil.",
        "excerpt": "'It doesn't heat properly' triggers a return even when the unit works. The culprit is usually an aluminum-clad coil.",
        "related": ["pain-dead-on-arrival", "pain-cracked-glass", "article-cookware-magnetism"],
        "cta_title": "Stop 'slow heating' returns?",
        "cta_text": "Tell us your wattage and we'll spec 100% copper coil with per-batch winding checks — so the unit actually performs.",
        "wa_text": "Hi Vortix Kitchen, customers complain my cookers heat slowly. Can you spec 100% copper coil with verified winding?",
        "mail_subject": "Slow heating complaints",
        "mail_body": "Hi Vortix Kitchen, please advise on 100% copper coil and coil-to-glass tolerance to stop slow-heating returns.",
        "body": """<p>"It doesn't heat properly" triggers a return even when the unit works. The customer isn't wrong about the symptom — they're describing a shortcut in the build.</p>
<p>Aluminum-clad or poorly wound coils lose efficiency and run hot. The cooker struggles to reach temperature, the buyer loses patience, and it comes back.</p>
<h2>Put this in your PO</h2>
<p>"Heating coil: 100% copper; winding spec verified per batch; coil-to-glass gap tolerance checked at QC."</p>
<p>Copper costs more than aluminum-clad. It is also the difference between a unit that performs and one that gets sent back.</p>""",
    },

    # ---------------- RELIABILITY ----------------
    {
        "slug": "pain-igbt-overheat",
        "series": "reliability",
        "cat": "RELIABILITY",
        "footer_label": "IGBT Overheat",
        "image": "page2_img8.jpeg",
        "readtime": "2 min read",
        "title": "Cookers Shut Down Mid-Service — Why a Weak IGBT Kills Sales in Hot Kitchens",
        "description": "In 40C kitchens the IGBT overheats and cuts out mid-service. How to spec a cooker that survives continuous duty.",
        "excerpt": "In 40C kitchens the IGBT overheats and cuts out mid-service. Oversize it and demand a continuous-duty rating.",
        "related": ["pain-dusty-fan", "pain-voltage-spike", "article-product-showcase"],
        "cta_title": "Cookers dying in hot kitchens?",
        "cta_text": "Tell us your market's ambient heat and duty cycle — we'll spec an oversized IGBT and continuous-duty rating built for it.",
        "wa_text": "Hi Vortix Kitchen, my cookers shut down in hot kitchens. Can you spec an oversized IGBT with continuous-duty rating?",
        "mail_subject": "Cookers overheating",
        "mail_body": "Hi Vortix Kitchen, I need cookers that survive 40C kitchens. Please advise on IGBT margin and continuous-duty rating.",
        "body": """<p>In 40°C kitchens your cooker doesn't fail because it's badly made — it fails because the IGBT overheats and cuts out mid-service. The chef notices on night one, and your brand becomes "the one that dies."</p>
<p>The fix is an oversized IGBT with thermal margin, a real aluminum heatsink, and continuous-duty rating — not a fuse that trips.</p>
<h2>Demand this</h2>
<p>"IGBT rated with margin above rated wattage; continuous-duty thermal management validated at 40°C ambient; continuous-duty (not peak-only) rating for commercial use."</p>
<p>For hot markets this single line is what keeps units alive past the first month.</p>""",
    },
    {
        "slug": "pain-dusty-fan",
        "series": "reliability",
        "cat": "RELIABILITY",
        "footer_label": "Dusty Fan",
        "image": "page2_img8.jpeg",
        "readtime": "2 min read",
        "title": "Dust Chokes the Fan — the Silent Killer of Cookers in Tough Markets",
        "description": "Dust chokes the cooling fan and the unit cooks itself. Why a serviceable fan beats a scrapped cooker.",
        "excerpt": "Dust chokes the cooling fan and the unit cooks itself. The fix is a serviceable fan — not a scrapped unit.",
        "related": ["pain-igbt-overheat", "pain-voltage-spike", "article-product-showcase"],
        "cta_title": "Fans clogging with dust?",
        "cta_text": "Send your duty environment and we'll spec a dust-resistant, field-replaceable fan — with spare fans as a line item, not a favor.",
        "wa_text": "Hi Vortix Kitchen, dust kills my cooker fans. Can you spec a serviceable, dust-resistant fan with spare parts?",
        "mail_subject": "Dusty fan failures",
        "mail_body": "Hi Vortix Kitchen, please advise on a dust-resistant serviceable fan and spare-part availability for my market.",
        "body": """<p>In dusty markets the fan intake clogs, airflow drops, and the internals cook themselves. No dramatic failure — just a slow death that shows up as "it stopped after a few months," by which time the buyer has told three friends.</p>
<p>The fix is not a better unit. It is a fan you can replace in the field.</p>
<h2>Demand this</h2>
<p>"Dust-resistant fan, field-replaceable; spare fans listed as a line item, not a favor."</p>
<p>If the only way to swap a $1 fan is to scrap the whole cooker, your customers will blame you — and the next order goes elsewhere.</p>""",
    },
    {
        "slug": "pain-voltage-spike",
        "series": "reliability",
        "cat": "RELIABILITY",
        "footer_label": "Voltage Spikes",
        "image": "page2_img8.jpeg",
        "readtime": "2 min read",
        "title": "One Voltage Spike Fried the Board — the Spec That Protects Your Margin",
        "description": "One grid spike can fry the control board. Surge protection and wide-voltage tolerance turn a warranty claim into a non-event.",
        "excerpt": "One grid spike can fry the board. Surge protection and wide-voltage tolerance turn a warranty claim into a non-event.",
        "related": ["pain-igbt-overheat", "pain-dusty-fan", "article-product-showcase"],
        "cta_title": "One spike fried the board?",
        "cta_text": "Tell us your grid stability and we'll add surge protection plus wide-voltage tolerance, documented — not just claimed.",
        "wa_text": "Hi Vortix Kitchen, voltage spikes fry my cookers. Can you add surge protection and wide-voltage tolerance?",
        "mail_subject": "Voltage spike damage",
        "mail_body": "Hi Vortix Kitchen, please advise on input surge protection and wide-voltage tolerance for unstable grids.",
        "body": """<p>Grids across Central Asia, Southeast Asia and Africa are unstable. One surge or brownout can fry the control board in a single event — and a pattern of "randomly dies" refunds follows.</p>
<p>The fix is surge protection plus wide-voltage tolerance, written into the spec.</p>
<h2>Demand this</h2>
<p>"Input surge protection; wide-voltage tolerance that holds steady through brownouts (no reboot); documented, not claimed."</p>
<p>For unstable grids this one clause is the line between a unit that lasts and a unit that becomes a warranty claim.</p>""",
    },

    # ---------------- CUSTOMS / COMPLIANCE ----------------
    {
        "slug": "pain-ce-sticker",
        "series": "customs",
        "cat": "CUSTOMS",
        "footer_label": "CE Won't Clear",
        "image": "page4_img1.jpeg",
        "readtime": "2 min read",
        "title": "Your CE Sticker Won't Clear Customs — the Assumption That Strands Containers",
        "description": "CE alone will not clear customs in your markets. Name the country and demand a real test report before you order.",
        "excerpt": "CE alone won't clear customs in your markets. Name the country and demand a real test report.",
        "related": ["pain-wrong-plug", "pain-no-local-rep", "article-induction-vs-infrared"],
        "cta_title": "Not sure your paperwork is airtight?",
        "cta_text": "Tell us your target countries and we'll map the certification path and show the real test reports before you commit to a PO.",
        "wa_text": "Hi Vortix Kitchen, I import to [country]. Can you confirm the certification and plug I need before I order?",
        "mail_subject": "Customs clearance check",
        "mail_body": "Hi Vortix Kitchen, please help me avoid a customs hold — which marks and plug do I need for my target markets?",
        "body": """<p>CE is not a global passport. It is the Europe mark — and you don't sell to Europe. Most of your markets want their own: EAC, SNI, SIRIM, TISI, SONCAP, PVoC or NRCS, by country. A missing mark holds the container, and the demurrage bill can exceed your margin.</p>
<h2>Do this</h2>
<p>Name your exact destination country on the PO, then ask for a real test report — issuing lab, report number, date, your exact model — not a photo of a sticker. A CB report to IEC 60335 is the most reusable asset, accepted for faster national approval in Malaysia, Vietnam and South Africa.</p>""",
    },
    {
        "slug": "pain-wrong-plug",
        "series": "customs",
        "cat": "CUSTOMS",
        "footer_label": "Wrong Plug",
        "image": "page4_img1.jpeg",
        "readtime": "2 min read",
        "title": "The Wrong Plug Held Your Whole Container — a $0.30 Decision Made Too Late",
        "description": "The wrong plug can hold your whole container. Lock the plug for your market at tooling — a small decision made in time.",
        "excerpt": "Wrong plug = a held container. Lock the plug at tooling — a $0.30 decision made in time.",
        "related": ["pain-ce-sticker", "pain-no-local-rep", "article-induction-vs-infrared"],
        "cta_title": "Don't let the plug hold your container?",
        "cta_text": "Name your market and we'll lock the correct plug at tooling — written into the spec, not left to chance.",
        "wa_text": "Hi Vortix Kitchen, which plug type do I need for [country]? Can you lock it at tooling?",
        "mail_subject": "Plug type for my market",
        "mail_body": "Hi Vortix Kitchen, please confirm the correct plug type for my market and lock it at tooling.",
        "body": """<p>Voltage is uniform across your markets (220-240V, 50Hz), but plugs are not. Type C/F in Central Asia and much of SEA, Type G in Malaysia and Singapore, Type A/B in Thailand and the Philippines, BS 1363 / SANS 164 in Africa. Some ports treat a wrong-plug shipment as non-compliant and hold the whole container.</p>
<h2>Do this</h2>
<p>Lock the plug for your market at the tooling stage — a $0.30 decision made before production, not a rework after. Write the plug type into the specification, not a verbal agreement. One line on the PO prevents a port hold.</p>""",
    },
    {
        "slug": "pain-no-local-rep",
        "series": "customs",
        "cat": "CUSTOMS",
        "footer_label": "No Local Rep",
        "image": "page4_img1.jpeg",
        "readtime": "2 min read",
        "title": "No Local Rep Named, No Clearance — the Contract Gap That Stalls Perfect Goods",
        "description": "Most certification schemes need a named local representative. Put it in the contract before the container sails.",
        "excerpt": "Most schemes need a named local rep to hold the certificate. Put it in the contract before the container sails.",
        "related": ["pain-ce-sticker", "pain-wrong-plug", "article-induction-vs-infrared"],
        "cta_title": "Avoid the port surprise?",
        "cta_text": "Tell us your destination and we'll confirm the local representative is named in the contract before production starts.",
        "wa_text": "Hi Vortix Kitchen, who holds the certificate locally for [country]? Can you name the rep in the contract?",
        "mail_subject": "Local representative for clearance",
        "mail_body": "Hi Vortix Kitchen, please confirm the local representative requirement for my market and include it in the contract.",
        "body": """<p>Almost every certification scheme in your markets requires a named local entity to hold the certificate — EAC, SNI, SIRIM, SONCAP, NRCS all want a local importer or agent on file. Importers discover this at the port, after the container has sailed.</p>
<h2>Do this</h2>
<p>Confirm the local representative is named in the contract before production, not patched in with a panic email at the port. If your supplier "can't name one," that is the answer you needed before you wired the deposit.</p>""",
    },

    {
        "slug": "pain-nigeria-soncap",
        "series": "customs",
        "cat": "CUSTOMS",
        "footer_label": "Nigeria SONCAP",
        "image": "page4_img1.jpeg",
        "readtime": "2 min read",
        "title": "Your Container Is Stuck at Lagos Port — the SONCAP Step Most Importers Miss",
        "description": "A whole container held at Lagos because SONCAP wasn't done before sailing. The pre-shipment step that clears Nigerian ports.",
        "excerpt": "A whole container held at Lagos because SONCAP wasn't done first. The pre-shipment step that clears Nigerian ports.",
        "related": ["pain-ce-sticker", "pain-no-local-rep", "pain-wrong-plug"],
        "cta_title": "Clearing Nigerian ports without the wait?",
        "cta_text": "Tell us your model and volume — we'll confirm the SONCAP Product and SONCAP Certificate path and supply the test reports before you order.",
        "wa_text": "Hi Vortix Kitchen, I import to Nigeria. Can you confirm the SONCAP documents and test reports I need before ordering?",
        "mail_subject": "Nigeria SONCAP clearance",
        "mail_body": "Hi Vortix Kitchen, please advise on the SONCAP Product Certificate and SONCAP Certificate requirements and the test reports you can provide for Nigeria.",
        "body": """<p>No SONCAP Certificate (SC) = no release at Lagos. Importers lose weeks and their whole margin to demurrage because the step was done after sailing instead of before.</p>
<h2>What SONCAP needs, in order</h2>
<ol>
<li><strong>Product Certificate (PC)</strong> — model-level, up to a year, after testing to Nigerian standards.</li>
<li><strong>SONCAP Certificate (SC)</strong> — shipment-level, after pre-shipment inspection, against the PC. Must be obtained <em>before</em> the container leaves China.</li>
</ol>
<h2>Put this in your PO</h2>
<p>"Supplier to provide IEC 60335 test reports, support PC application, and coordinate pre-shipment inspection for the SC. SC number on all commercial documents."</p>
<p>Work with a factory that can name the accredited body (SGS, Intertek, BV). If they shrug at SONCAP, they have not shipped to your market.</p>""",
    },

    # ---------------- BUYING / SELLING (single-topic, kept) ----------------
    {
        "slug": "article-induction-vs-infrared",
        "series": "buying",
        "cat": "BUYING DECISION",
        "footer_label": "Induction vs Infrared",
        "image": "page2_img8.jpeg",
        "readtime": "3 min read",
        "title": "Induction or Infrared? Pick the Wrong One and You're Stuck with Dead Stock",
        "description": "Bet on the wrong cooker technology and you eat the returns. How cookware habits and margin decide induction vs infrared in your market.",
        "excerpt": "Bet on the wrong technology and you eat dead stock. Match induction or infrared to your market's cookware.",
        "related": ["article-cookware-magnetism", "article-switch-from-gas", "article-product-showcase"],
        "cta_title": "Not sure which mix your market will buy?",
        "cta_text": "Tell us the cookware habits and price tier of your target customers — we'll propose an induction/infrared split and a small test-MOQ.",
        "wa_text": "Hi Vortix Kitchen, my market uses mostly [pot type] pots — should I lead with induction or infrared?",
        "mail_subject": "Induction vs Infrared Mix",
        "mail_body": "Hi Vortix Kitchen, please help me decide the right induction/infrared product mix for my market.",
        "body": """<p>Bet on the wrong cooker technology and a container sits in your warehouse unsold. The only fact that decides the sale in your markets is <strong>cookware</strong>.</p>
<ul>
<li><strong>Induction</strong> heats only magnetic pots (cast iron, magnetic steel). Aluminum, glass and ceramic won't work.</li>
<li><strong>Infrared</strong> heats the glass surface, so it works with <em>any</em> pot.</li>
</ul>
<h2>Choose infrared if</h2>
<p>Your market cooks mostly with aluminum or mixed pots (common across Africa and SE Asia). It removes the "it doesn't work" returns entirely — and it's cheaper to build, a low-MOQ entry SKU.</p>
<h2>Choose induction if</h2>
<p>You're building a premium line: ~90% efficient, cooler surface, a strong safety story for families and energy-conscious buyers. Higher per-unit margin.</p>
<h2>The play most distributors miss</h2>
<p>Carry both. Induction as the premium line, infrared as the universal line that never rejects a customer's existing pots. Together they cover every buyer who walks in.</p>
<h2>3-step market check</h2>
<ol>
<li>Survey the pots your retail partners see — aluminum-dominant → weight infrared.</li>
<li>Decide position: price → infrared; quality/margin → induction; both → carry both.</li>
<li>Test cheap: a small infrared batch validates a new channel before volume.</li>
</ol>""",
    },
    {
        "slug": "article-product-showcase",
        "series": "buying",
        "cat": "COMMERCIAL / FOODSERVICE",
        "footer_label": "Commercial Range",
        "image": "page7_img1.jpeg",
        "readtime": "3 min read",
        "title": "How to Build a Commercial Cooker Range Your Restaurant Clients Actually Reorder",
        "description": "In foodservice the win is the reorder. How to spec a commercial induction range by venue so clients keep coming back.",
        "excerpt": "In foodservice the win is the reorder. Spec by venue so your clients come back.",
        "related": ["pain-igbt-overheat", "pain-dusty-fan", "article-induction-vs-infrared"],
        "cta_title": "Building a commercial cooker range?",
        "cta_text": "Send us your target market and venue mix — we'll propose a ready-to-import bundle with continuous-duty specs and a spare-part list.",
        "wa_text": "Hi Vortix Kitchen, I'm building a commercial cooker range for [venue mix]. Can you propose a bundle and pricing?",
        "mail_subject": "Commercial Cooker Bundle",
        "mail_body": "Hi Vortix Kitchen, I'm building a commercial cooker range and need a product bundle with continuous-duty specs.",
        "body": """<p>In foodservice the win is the reorder, not the first sale. A unit that throttles out during dinner service funds your rival's growth. Spec by venue so clients come back.</p>
<h2>Two mistakes that end the relationship</h2>
<ul>
<li><strong>Peak-power lying:</strong> a "5000W" unit that drops to 3000W can't hold a wok station. The chef notices on night one.</li>
<li><strong>Wrong tool:</strong> a 2000W portable where a 5000W burner was needed, or glass that cracks under all-day use.</li>
</ul>
<h2>Spec by venue</h2>
<ul>
<li>Small restaurant / cafe: 3500W countertop, single zone.</li>
<li>Hotel / buffet: 4000-5000W built-in or twin zone.</li>
<li>Catering / outdoor: portable 2000-3500W, sturdy handle.</li>
<li>Asian wok station: 5000W+ concave-coil unit.</li>
</ul>
<h2>What "commercial grade" must say on paper</h2>
<ul>
<li>Continuous power (2-hour load-test record), not peak-only.</li>
<li>Dual-fan cooling + NTC validated at 40°C ambient.</li>
<li>Reinforced glass, metal housing, industrial IGBT.</li>
<li>Overheat / overvoltage / auto-shutoff mandatory.</li>
<li>Serviceable fan + published spare-part list.</li>
</ul>
<h2>Starter bundle</h2>
<p>A 3500W countertop + a twin-zone 5000W unit covers most of a new client's line on day one — and because both perform, they call you for the second branch.</p>""",
    },
    {
        "slug": "article-cookware-magnetism",
        "series": "buying",
        "cat": "CUSTOMER SUPPORT",
        "footer_label": "Cookware Complaints",
        "image": "page2_img8.jpeg",
        "readtime": "3 min read",
        "title": "Your Customer's Pot Won't Heat? The Cookware Trap Behind Most \"It's Broken\" Complaints",
        "description": "Most induction 'it doesn't work' complaints are the wrong pot, not a defect. How importers pre-empt cookware returns.",
        "excerpt": "Most 'it's broken' induction complaints are the wrong pot. A magnet test on the box stops most returns.",
        "related": ["article-induction-vs-infrared", "pain-slow-heating", "article-switch-from-gas"],
        "cta_title": "Want to cut cookware-related returns?",
        "cta_text": "Tell us your market's dominant cookware type and we'll propose an induction + magnetic-disc bundle plus the box labelling that stops complaints.",
        "wa_text": "Hi Vortix Kitchen, my market uses mostly aluminium pots — how do I avoid 'won't heat' returns?",
        "mail_subject": "Cookware Returns",
        "mail_body": "Hi Vortix Kitchen, please advise how to reduce cookware-related induction returns in my market.",
        "body": """<p>A customer puts an aluminum pot on an induction cooker, nothing heats, and sends it back as "defective." The unit is perfect. The pot is the problem — and across Africa and much of SE Asia, aluminum is the household default. This is the single most common "it's broken" complaint in the trade.</p>
<h2>Why</h2>
<p>Induction only heats ferromagnetic cookware (cast iron, magnetic steel). Aluminum, copper, glass and ceramic don't interact with the field, so the cooker stays cold. It's working as designed; the customer just can't see it.</p>
<h2>Kill the complaint before it starts</h2>
<ol>
<li><strong>Magnet test on the box:</strong> "works with magnetic pots; test with a fridge magnet" turns a return into a 10-second self-check.</li>
<li><strong>Bundle a magnetic disc:</strong> a low-cost steel disc lets any pot work on induction.</li>
<li><strong>Sell infrared where pots are mixed:</strong> it heats any pot, eliminating the category.</li>
<li><strong>Train retail partners:</strong> one line on the shelf card prevents most returns at point of sale.</li>
</ol>
<p>Give every buyer the rule: if a fridge magnet sticks to the pot bottom, it works on induction. Print it, sticker it, put it in the manual.</p>""",
    },
    {
        "slug": "article-switch-from-gas",
        "series": "buying",
        "cat": "SELLING TO YOUR BUYERS",
        "footer_label": "Gas to Induction",
        "image": "page7_img1.jpeg",
        "readtime": "3 min read",
        "title": "Gas to Induction: The Total-Cost Math That Closes the Sale with Your End Customers",
        "description": "Buyers say gas is cheaper until you show total cost of ownership. The math that closes the gas-to-induction sale.",
        "excerpt": "Buyers say gas is cheaper until you show total cost of ownership. The math that closes the gas-to-induction sale.",
        "related": ["article-cookware-magnetism", "article-product-showcase", "article-induction-vs-infrared"],
        "cta_title": "Need a switch-kit to sell induction?",
        "cta_text": "Tell us your buyer type and target market, and we'll bundle a magnetic-disc-equipped induction range plus a one-page TCO sheet.",
        "wa_text": "Hi Vortix Kitchen, I want to sell induction over gas to [buyer type] — can you bundle a switch-kit and TCO sheet?",
        "mail_subject": "Gas-to-Induction Switch Kit",
        "mail_body": "Hi Vortix Kitchen, please help me build a gas-to-induction switch kit (TCO sheet + magnetic disc) for my buyers.",
        "body": """<p>Your buyers hesitate to replace a working gas setup because "gas is cheaper." The sale is won or lost on total cost of ownership — not the sticker price.</p>
<h2>The math to put in front of them</h2>
<ul>
<li><strong>Energy:</strong> induction ~90% efficient vs ~40% for a gas flame. Less energy per meal, real money over a year.</li>
<li><strong>Speed:</strong> faster heat-up and instant response — lower labour cost, faster table turns.</li>
<li><strong>Safety:</strong> no flame, no cylinder, no leak risk — decisive for families and any venue with fire-safety rules. Removing the LPG cylinder is itself a saving where supply is unreliable.</li>
</ul>
<h2>The two honest objections</h2>
<p>Induction needs magnetic cookware, and commercial units need a proper circuit. Both are solved, not fatal: bundle a magnetic disc and spec the right power for the venue. Handle them up front and the "but gas is simpler" argument collapses.</p>
<p>A customer who switches on total-cost math becomes a recurring induction buyer — exactly the account you want.</p>""",
    },
    {
        "slug": "pain-oem-brand",
        "series": "buying",
        "cat": "BUYING DECISION",
        "footer_label": "Launch Your Brand",
        "image": "page7_img1.jpeg",
        "readtime": "2 min read",
        "title": "Launch Your Own Cooker Brand with a China Factory — Without Losing Your Shirt",
        "description": "Want your own induction brand but fear MOQ, deposit and IP risk? The OEM/ODM path that gets importers to market fast.",
        "excerpt": "Want your own cooker brand but fear MOQ, deposit and IP risk? The OEM/ODM path that gets importers to market.",
        "related": ["article-product-showcase", "article-induction-vs-infrared", "pain-ce-sticker"],
        "cta_title": "Ready to build your own brand?",
        "cta_text": "Send us your target market and planned models — we'll propose an OEM/ODM package with MOQ, tooling, certification and QA spelled out.",
        "wa_text": "Hi Vortix Kitchen, I want to launch my own cooker brand. Can you do OEM/ODM with my logo, color and packaging?",
        "mail_subject": "OEM/ODM brand launch",
        "mail_body": "Hi Vortix Kitchen, I want to launch my own induction cooker brand. Please advise on OEM/ODM, MOQ, tooling cost and certification support.",
        "body": """<p>You see cookers selling in your market and think: why isn't my brand on the box? The fear — MOQ, deposit, "will they steal my design?" — is real but manageable.</p>
<h2>OEM vs ODM</h2>
<p><strong>OEM:</strong> take the factory's proven model, add your logo, color and carton. Fastest, lowest risk. <strong>ODM:</strong> co-develop a model — more differentiation, more tooling. Most new brands should start OEM, move to ODM once volume justifies it.</p>
<h2>Five clauses that protect you</h2>
<ol>
<li><strong>MOQ per model</strong> — confirm the real number; a low-MOQ entry SKU lets you test first.</li>
<li><strong>Tooling ownership</strong> — you should own the mold, or have it locked to your brand.</li>
<li><strong>Deposit terms</strong> — 30% / 70% before shipment is normal; 100% upfront is a red flag.</li>
<li><strong>Certification in your name</strong> — SONCAP, EAC, CE under your company, not the factory's.</li>
<li><strong>Pre-shipment inspection</strong> — your right to independent QC before releasing the balance.</li>
</ol>
<p>Get those five in writing and the "scary China factory" becomes a supplier you control.</p>""",
    },
    # ---------------- W2 (2026-08-24) ----------------
    {
        "slug": "pain-kenya-pvoc",
        "series": "customs",
        "cat": "CUSTOMS",
        "footer_label": "Kenya PVoC",
        "image": "page4_img1.jpeg",
        "readtime": "2 min read",
        "title": "Your Kenya Container Is Stuck — the PVoC Step Done After Sailing",
        "description": "A Kenya-bound container held at Mombasa because PVoC/COC wasn't done before sailing. The pre-shipment conformity step that clears KEBS.",
        "excerpt": "A Kenya container held at Mombasa because PVoC wasn't done first. The pre-shipment COC that clears KEBS.",
        "related": ["pain-nigeria-soncap", "pain-ce-sticker", "pain-no-local-rep"],
        "cta_title": "Clearing Kenyan ports without the wait?",
        "cta_text": "Tell us your model and volume — we'll confirm the PVoC/COC path and supply the test reports before you order.",
        "wa_text": "Hi Vortix Kitchen, I import to Kenya. Can you arrange PVoC inspection and provide the COC before shipment?",
        "mail_subject": "Kenya PVoC clearance",
        "mail_body": "Hi Vortix Kitchen, please advise on the PVoC Certificate of Conformity requirements and the test reports you can provide for Kenya.",
        "body": """<p>No PVoC Certificate of Conformity (COC) = no release at Mombasa. Importers lose weeks and their whole margin to demurrage because PVoC was never done before sailing.</p>
<h2>What PVoC needs</h2>
<p>A COC issued by a KEBS-recognised body (SGS, Intertek, BV) after a pre-shipment inspection in China — <em>before</em> the container departs. The inspection checks the actual shipment against your test reports.</p>
<h2>Put this in your PO</h2>
<p>"Supplier to arrange PVoC inspection with a KEBS-recognised body, provide IEC 60335 test reports, and ensure the COC number appears on all shipping documents before vessel departure."</p>
<p>A factory that ships to Kenya can name the inspection body. If they shrug, they have not shipped to your market.</p>""",
    },
    {
        "slug": "pain-voltage-frequency",
        "series": "buying",
        "cat": "SPEC / VOLTAGE",
        "footer_label": "Voltage Match",
        "image": "page2_img8.jpeg",
        "readtime": "2 min read",
        "title": "Half Your Market Can't Use the Cooker — the Voltage Line Most Importers Miss",
        "description": "Ship the wrong voltage and the unit won't run or burns out. How to lock voltage and frequency to your market before production.",
        "excerpt": "Wrong voltage = a container of cookers that won't turn on. Lock the voltage to your market before production.",
        "related": ["pain-voltage-spike", "pain-wrong-plug", "article-induction-vs-infrared"],
        "cta_title": "Not sure which voltage your market needs?",
        "cta_text": "Name your destination countries and we'll lock the correct voltage/frequency — or spec a wide-voltage (100-240V) unit that covers mixed markets.",
        "wa_text": "Hi Vortix Kitchen, my market uses [voltage]. Should I lock voltage or use a wide-voltage unit?",
        "mail_subject": "Voltage spec for my market",
        "mail_body": "Hi Vortix Kitchen, please advise on the correct voltage/frequency for my market and whether a wide-voltage unit fits.",
        "body": """<p>Ship the wrong voltage and the unit won't start or burns out. Your markets run 220-240V at 50Hz — but pockets run 110-120V (Japan, Taiwan, parts of the Americas). Send a 220V unit there and it's dead stock.</p>
<h2>Do this</h2>
<p>Name the exact voltage and frequency on the PO. Uniform 220-240V/50Hz → lock it. Mixed or 110V → spec a wide-voltage unit (100-240V auto-switching) or a dedicated 110V build. One line prevents a container of dead units.</p>""",
        "faq": [
            ("Which of my markets use 110-120V?", "Mostly the Americas (some), Japan (100V, 50/60Hz) and Taiwan (110V/60Hz). Central Asia, Southeast Asia, Africa and the GCC run 220-240V at 50Hz."),
            ("Will a 220-240V cooker work on 110V?", "No - it won't reach power or may not start, and some will overheat. Always match the local voltage or use a wide-voltage (100-240V) unit."),
            ("What does 'wide voltage' mean for cookers?", "A unit with auto-switching input (100-240V, 50/60Hz) that runs safely across both ranges - ideal when you sell into mixed-voltage markets."),
        ],
    },
]


def by_slug():
    return {a["slug"]: a for a in ARTICLES}


def wa_url(a):
    return "https://wa.me/%s?text=%s" % (WA_NUMBER, quote(a["wa_text"]))


def mail_url(a):
    return "mailto:%s?subject=%s&body=%s" % (
        EMAIL, quote(a["mail_subject"]), quote(a["mail_body"]))


def jsonld(a):
    ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["description"],
        "image": "https://vortixkitchen.com/product_images/" + a["image"],
        "datePublished": DATE_ISO,
        "dateModified": DATE_ISO,
        "author": {"@type": "Organization", "name": "Vortix Kitchen"},
        "publisher": {
            "@type": "Organization",
            "name": "Foshan Vortix Co., LTD",
            "logo": {"@type": "ImageObject",
                     "url": "https://vortixkitchen.com/product_images/" + a["image"]},
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": "https://vortixkitchen.com/blog/" + a["slug"] + ".html",
        },
    }
    return json.dumps(ld, indent=2, ensure_ascii=False)


def faqld(a):
    if "faq" not in a or not a["faq"]:
        return ""
    ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}}
            for q, ans in a["faq"]
        ],
    }
    return json.dumps(ld, indent=2, ensure_ascii=False)


ARTICLE_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE__ | Vortix Kitchen</title>
    <meta name="description" content="__DESC__">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="blog.css">
    <link rel="canonical" href="__CANON__">
    <meta property="og:type" content="article">
    <meta property="og:title" content="__TITLE__">
    <meta property="og:description" content="__DESC__">
    <meta property="og:image" content="https://vortixkitchen.com/product_images/__IMAGE__">
    <meta property="og:url" content="__CANON__">
    <meta name="twitter:card" content="summary_large_image">
    <script type="application/ld+json">
__JSONLD__
    </script>
    <script type="application/ld+json">
__FAQLD__
    </script>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="../index.html" class="logo">
                <div class="logo-icon">V</div>
                <div class="logo-text">Vortix<span>Kitchen</span></div>
            </a>
            <ul class="nav-menu">
                <li><a href="../index.html">Home</a></li>
                <li><a href="../index.html#products">Products</a></li>
                <li><a href="../index.html#quality">Quality</a></li>
                <li><a href="../index.html#oem">OEM/ODM</a></li>
                <li><a href="index.html" class="active">Blog</a></li>
                <li><a href="../index.html#contact" class="nav-cta">Get Quote</a></li>
            </ul>
            <div class="mobile-toggle"><span></span><span></span><span></span></div>
        </div>
    </nav>

    <section class="article-header">
        <div class="wrap">
            <span class="cat">__CAT__</span>
            <h1>__TITLE__</h1>
            <div class="meta"><span>📅 __DATE_HUMAN__</span><span>⏱ __READTIME__</span><span>✍️ Vortix Kitchen</span></div>
        </div>
    </section>
    <img class="article-cover" src="../product_images/__IMAGE__" alt="__TITLE__">

    <article class="article-body">
__BODY__

        <div class="article-cta">
            <div class="cta-box">
                <h3>__CTA_TITLE__</h3>
                <p>__CTA_TEXT__</p>
                <div class="cta-actions">
                    <a class="btn-wa" href="__WA_URL__">💬 WhatsApp Us</a>
                    <a class="btn-mail" href="__MAIL_URL__">✉️ Email Us</a>
                </div>
            </div>
        </div>
    </article>

    <section class="related">
        <h3 class="section-title">More guides for importers</h3>
        <div class="related-grid">
__RELATED__
        </div>
    </section>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <span class="logo-text">Vortix<span>Kitchen</span></span>
                <p>Professional induction cooker and infrared cooker manufacturer based in Foshan, China. Delivering quality kitchen appliances to global partners since 2010.</p>
                <div class="footer-social">
                    <a href="https://wa.me/8613790093901" class="social-link" title="WhatsApp">&#128172;</a>
                    <a href="mailto:Shirley20193@163.com" class="social-link" title="Email">&#9993;</a>
                </div>
            </div>
            <div class="footer-column">
                <h4>Articles</h4>
                <ul class="footer-links">
__FOOTER_LINKS__
                </ul>
            </div>
            <div class="footer-column">
                <h4>Company</h4>
                <ul class="footer-links">
                    <li><a href="../index.html#quality">About Us</a></li>
                    <li><a href="../index.html#oem">OEM/ODM</a></li>
                    <li><a href="../index.html#contact">Factory Tour</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h4>Contact</h4>
                <ul class="footer-links">
                    <li><a href="mailto:Shirley20193@163.com">Shirley20193@163.com</a></li>
                    <li><a href="https://wa.me/8613790093901">WhatsApp: +86 137 9009 3901</a></li>
                    <li><a href="../index.html#contact">Foshan, Guangdong, China</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 Foshan Vortix Co., LTD. All Rights Reserved. | Professional Kitchen Appliance Manufacturer</p>
        </div>
    </footer>

    <a href="https://wa.me/8613790093901" target="_blank" class="whatsapp-float" title="Chat on WhatsApp">&#128172;</a>
</body>
</html>
"""


def render_article(a, lookup):
    rel = []
    for s in a["related"]:
        o = lookup[s]
        rel.append("""            <a class="article-card" href="%s.html">
                <img class="thumb" src="../product_images/%s" alt="%s">
                <span class="card-cat">%s</span>
                <h3>%s</h3>
                <div class="card-meta"><span>📅 %s</span><span>⏱ %s</span></div>
            </a>""" % (o["slug"], o["image"], o["title"], o["cat"], o["title"], DATE_HUMAN, o["readtime"]))
    related = "\n".join(rel)

    foot = []
    for o in ARTICLES:
        foot.append('                    <li><a href="%s.html">%s</a></li>' % (o["slug"], o["footer_label"]))
    footer_links = "\n".join(foot)

    return (ARTICLE_TPL
            .replace("__TITLE__", a["title"])
            .replace("__DESC__", a["description"])
            .replace("__CAT__", a["cat"])
            .replace("__IMAGE__", a["image"])
            .replace("__DATE_HUMAN__", DATE_HUMAN)
            .replace("__READTIME__", a["readtime"])
            .replace("__BODY__", a["body"])
            .replace("__CTA_TITLE__", a["cta_title"])
            .replace("__CTA_TEXT__", a["cta_text"])
            .replace("__WA_URL__", wa_url(a))
            .replace("__MAIL_URL__", mail_url(a))
            .replace("__JSONLD__", jsonld(a))
            .replace("__CANON__", "https://vortixkitchen.com/blog/" + a["slug"] + ".html")
            .replace("__FAQLD__", faqld(a))
            .replace("__RELATED__", related)
            .replace("__FOOTER_LINKS__", footer_links))


def render_index(lookup):
    blocks = []
    for key, label in SERIES:
        cards = []
        for a in [x for x in ARTICLES if x["series"] == key]:
            cards.append("""            <a class="article-card" href="%s.html">
                <img class="thumb" src="../product_images/%s" alt="%s">
                <span class="card-cat">%s</span>
                <h3>%s</h3>
                <p class="excerpt">%s</p>
                <div class="card-meta"><span>📅 %s</span><span>⏱ %s</span></div>
                <span class="read-more">Read article →</span>
            </a>""" % (a["slug"], a["image"], a["title"], a["cat"], a["title"], a["excerpt"], DATE_HUMAN, a["readtime"]))
        cls = "" if blocks else " first-series"
        blocks.append('        <h2 class="series-title%s">%s</h2>\n        <div class="article-grid">\n%s\n        </div>' % (cls, label, "\n".join(cards)))
    series_html = "\n".join(blocks)

    foot = []
    for o in ARTICLES:
        foot.append('                    <li><a href="%s.html">%s</a></li>' % (o["slug"], o["footer_label"]))
    footer_links = "\n".join(foot)

    blog_ld = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "Vortix Kitchen Insights",
        "url": "https://vortixkitchen.com/blog/",
        "publisher": {
            "@type": "Organization",
            "name": "Foshan Vortix Co., LTD",
            "logo": "https://vortixkitchen.com/product_images/page2_img8.jpeg",
        },
        "description": "One focused guide per problem importers face — customs holds, returns, reliability, buying decisions and selling induction.",
    }

    tpl = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insights &amp; Guides for Cooker Importers | Vortix Kitchen Blog</title>
    <meta name="description" content="Practical, problem-solving guides for cooker importers: one focused article per real problem — avoiding customs holds, cutting returns, picking the right technology, and selling induction over gas.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="blog.css">
    <style>
        .series-title{font-family:'Playfair Display',Georgia,serif;font-size:27px;color:var(--primary);margin:40px 0 18px;padding-bottom:10px;border-bottom:2px solid var(--accent);}
        .series-title.first-series{margin-top:8px;}
    </style>
    <script type="application/ld+json">
__BLOG_LD__
    </script>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="../index.html" class="logo">
                <div class="logo-icon">V</div>
                <div class="logo-text">Vortix<span>Kitchen</span></div>
            </a>
            <ul class="nav-menu">
                <li><a href="../index.html">Home</a></li>
                <li><a href="../index.html#products">Products</a></li>
                <li><a href="../index.html#quality">Quality</a></li>
                <li><a href="../index.html#oem">OEM/ODM</a></li>
                <li><a href="index.html" class="active">Blog</a></li>
                <li><a href="../index.html#contact" class="nav-cta">Get Quote</a></li>
            </ul>
            <div class="mobile-toggle"><span></span><span></span><span></span></div>
        </div>
    </nav>

    <section class="blog-hero">
        <div class="badge">FOR IMPORTERS & BUYERS</div>
        <h1>Insights &amp; Guides for Cooker Importers</h1>
        <p>One real problem per guide — and how to avoid it. Customs holds, returns, reliability in tough markets, buying decisions and selling induction. Written by a Foshan factory, not a copywriter.</p>
    </section>

    <div class="blog-wrap">
__SERIES__
    </div>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <span class="logo-text">Vortix<span>Kitchen</span></span>
                <p>Professional induction cooker and infrared cooker manufacturer based in Foshan, China. Delivering quality kitchen appliances to global partners since 2010.</p>
                <div class="footer-social">
                    <a href="https://wa.me/8613790093901" class="social-link" title="WhatsApp">&#128172;</a>
                    <a href="mailto:Shirley20193@163.com" class="social-link" title="Email">&#9993;</a>
                </div>
            </div>
            <div class="footer-column">
                <h4>Articles</h4>
                <ul class="footer-links">
__FOOTER_LINKS__
                </ul>
            </div>
            <div class="footer-column">
                <h4>Company</h4>
                <ul class="footer-links">
                    <li><a href="../index.html#quality">About Us</a></li>
                    <li><a href="../index.html#oem">OEM/ODM</a></li>
                    <li><a href="../index.html#contact">Factory Tour</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h4>Contact</h4>
                <ul class="footer-links">
                    <li><a href="mailto:Shirley20193@163.com">Shirley20193@163.com</a></li>
                    <li><a href="https://wa.me/8613790093901">WhatsApp: +86 137 9009 3901</a></li>
                    <li><a href="../index.html#contact">Foshan, Guangdong, China</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 Foshan Vortix Co., LTD. All Rights Reserved. | Professional Kitchen Appliance Manufacturer</p>
        </div>
    </footer>

    <a href="https://wa.me/8613790093901" target="_blank" class="whatsapp-float" title="Chat on WhatsApp">&#128172;</a>
</body>
</html>
"""
    return (tpl
            .replace("__BLOG_LD__", json.dumps(blog_ld, indent=2, ensure_ascii=False))
            .replace("__SERIES__", series_html)
            .replace("__FOOTER_LINKS__", footer_links))


def render_sitemap():
    urls = ["https://vortixkitchen.com/", "https://vortixkitchen.com/blog/"]
    for a in ARTICLES:
        urls.append("https://vortixkitchen.com/blog/%s.html" % a["slug"])
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        out.append("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>%s</priority>\n  </url>" % (
            u, DATE_ISO, "1.0" if u == urls[0] else ("0.8" if u.endswith("/blog/") else "0.7")))
    out.append("</urlset>")
    return "\n".join(out)


def main():
    lookup = by_slug()
    # sanity: every related slug must exist
    for a in ARTICLES:
        for s in a["related"]:
            if s not in lookup:
                raise SystemExit("Unknown related slug: %s in %s" % (s, a["slug"]))

    for a in ARTICLES:
        html = render_article(a, lookup)
        with open(os.path.join(HERE, a["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", a["slug"] + ".html")

    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_index(lookup))
    print("wrote blog/index.html")

    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(render_sitemap())
    print("wrote sitemap.xml")

    # confirm the old bundled files are removed
    for old in ["article-quality-issues.html", "article-certifications-by-market.html",
                "article-power-wattage-guide.html"]:
        p = os.path.join(HERE, old)
        if os.path.exists(p):
            os.remove(p)
            print("removed", old)


if __name__ == "__main__":
    main()
