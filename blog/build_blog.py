# -*- coding: utf-8 -*-
"""
Vortix Kitchen blog generator.

Every blog article is ONE concise pain point. To publish a new pain-point
article, append one dict to ARTICLES below and rerun this script:

    python build_blog.py

It regenerates all article HTML files, blog/index.html and sitemap.xml.
Keep bodies under 200 words, pure client value, no fluff. Design lives in blog.css (unchanged).
"""
import json
import os
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

WA_NUMBER = "8613790093901"
EMAIL = "Shirley20193@163.com"
DATE_ISO = "2026-09-02"
DATE_HUMAN = "Sep 2, 2026"

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
        "image": "page5_img1.jpeg",
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
        "body": """<p>A dead-on-arrival cooker is a 100% refund plus return freight — you lose the whole sale.</p>
<p>Cause: under-specced IGBT or poor soldering. The factory saves cents; you lose the margin.</p>
<h2>Put in your PO</h2>
<p>"IGBT: branded module (Infineon/ST); 100% power-on burn-in ≥30 min/unit; AOI soldering; batch burn-in record with shipment."</p>""",
    },
    {
        "slug": "pain-cracked-glass",
        "series": "returns",
        "cat": "RETURNS",
        "footer_label": "Cracked Glass",
        "image": "page7_img2.jpeg",
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
        "body": """<p>Cracked glass on arrival = pure loss. No repair, no resale — full refund and a dent in your name.</p>
<p>Cause: cheap ceramic glass or a carton that never passed a drop test.</p>
<h2>Put in your PO</h2>
<p>"Glass: tempered microcrystalline (Schott/Eurokera grade); sea-freight carton drop-test validated; corner protectors." Ask for the drop-test record.</p>""",
    },
    {
        "slug": "pain-slow-heating",
        "series": "returns",
        "cat": "RETURNS",
        "footer_label": "Slow Heating",
        "image": "page5_img1.jpeg",
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
        "body": """<p>"Doesn't heat properly" triggers a return even when the unit works — it's a build shortcut.</p>
<p>Aluminum-clad or badly wound coils lose efficiency and run hot. The buyer returns it.</p>
<h2>Put in your PO</h2>
<p>"Heating coil: 100% copper; winding spec verified per batch; coil-to-glass gap checked at QC."</p>""",
    },

    # ---------------- RELIABILITY ----------------
    {
        "slug": "pain-igbt-overheat",
        "series": "reliability",
        "cat": "RELIABILITY",
        "footer_label": "IGBT Overheat",
        "image": "page9_img2.jpeg",
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
        "body": """<p>In 40°C kitchens the IGBT overheats and cuts out mid-service. The chef notices on night one; your brand becomes "the one that dies."</p>
<h2>Demand this</h2>
<p>"IGBT rated with margin above rated wattage; continuous-duty thermal management validated at 40°C; continuous-duty rating for commercial use."</p>""",
    },
    {
        "slug": "pain-dusty-fan",
        "series": "reliability",
        "cat": "RELIABILITY",
        "footer_label": "Dusty Fan",
        "image": "page1_img1.jpeg",
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
        "body": """<p>In dusty markets the fan clogs, airflow drops, internals cook. No drama — just "stopped after a few months," by which time the buyer told three friends.</p>
<h2>Demand this</h2>
<p>"Dust-resistant fan, field-replaceable; spare fans listed as a line item." If a $1 fan means scrapping the cooker, customers blame you.</p>""",
    },
    {
        "slug": "pain-voltage-spike",
        "series": "reliability",
        "cat": "RELIABILITY",
        "footer_label": "Voltage Spikes",
        "image": "page8_img1.jpeg",
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
        "body": """<p>Unstable grids across your markets: one surge fries the board, and "randomly dies" refunds follow.</p>
<h2>Demand this</h2>
<p>"Input surge protection; wide-voltage tolerance holding steady through brownouts (no reboot); documented." This clause is the line between a unit that lasts and a warranty claim.</p>""",
    },

    # ---------------- RELIABILITY (configurable builds) ----------------
    {
        "slug": "pain-cooling-fans",
        "series": "reliability",
        "cat": "RELIABILITY",
        "footer_label": "Cooling Fans",
        "image": "page5_img2.jpeg",
        "readtime": "2 min read",
        "title": "Your Cookers Die in the Heat - but You Can Spec 2 or 4 Cooling Fans",
        "description": "In hot markets a single fan can't cool the IGBT and the unit dies mid-service. Spec 2 or 4 fans to your environment and stop the returns.",
        "excerpt": "A single fan can't cool the IGBT in 40C markets - the unit dies. Spec 2 or 4 fans to your duty cycle and stop the returns.",
        "related": ["pain-igbt-overheat", "pain-dusty-fan", "article-product-showcase"],
        "cta_title": "Want cooling sized to your market?",
        "cta_text": "Tell us your ambient heat and daily run hours - we'll build the fan count, inlet filtering and NTC control to match, no over-spec cost.",
        "wa_text": "Hi Vortix Kitchen, my cookers overheat in [market]. Can you build 2-fan or 4-fan cooling to my environment?",
        "mail_subject": "Cooling fan configuration",
        "mail_body": "Hi Vortix Kitchen, please advise on 2-fan vs 4-fan cooling for my market's heat and duty cycle, and the inlet filtering you offer.",
        "body": """<p>In 40C kitchens and warehouses a single cooling fan can't pull heat off the IGBT. It throttles, then dies mid-service - a refund and a bad story you didn't need.</p>
<p>Most factories ship one size for every market. We don't.</p>
<h2>Spec it to your environment</h2>
<ul>
<li><strong>2-fan</strong> - light duty, mild-climate retail and home use.</li>
<li><strong>4-fan</strong> - continuous commercial duty in hot, dusty markets (Central Asia, SE Asia, Africa).</li>
</ul>
<p>Tell us your ambient heat and daily run hours; we build the fan count, inlet filtering and NTC control to match - not a guess.</p>
<p>Right-sized cooling = fewer returns, no over-spec cost. You pay for what your market needs.</p>""",
    },
    {
        "slug": "pain-insect-proof",
        "series": "reliability",
        "cat": "RELIABILITY",
        "footer_label": "Insect-Proof",
        "image": "page9_img1.jpeg",
        "readtime": "2 min read",
        "title": "Cockroaches Fried Your Client's Cooker - the Insect-Proof Build That Stops It",
        "description": "In tropical warehouses insects crawl into the cooker and short the board. A sealed, insect-proof build keeps bugs out and warranty claims down.",
        "excerpt": "Insects crawl into the cooker and short the board - a claim you pay for. A sealed, insect-proof build keeps bugs out.",
        "related": ["pain-igbt-overheat", "pain-dusty-fan", "article-product-showcase"],
        "cta_title": "Shipping to a hot, humid market?",
        "cta_text": "Name your destination and we'll lock the insect-proof build at tooling - sealed enclosure, guarded vents, coated board - standard for SE Asia and Africa.",
        "wa_text": "Hi Vortix Kitchen, I ship to [market] where cockroaches are a problem. Can you build an insect-proof cooker?",
        "mail_subject": "Insect-proof cooker build",
        "mail_body": "Hi Vortix Kitchen, please advise on an insect-proof / cockroach-proof build - sealed enclosure, guarded vents and coated board - for humid markets.",
        "body": """<p>In tropical warehouses and open kitchens, cockroaches and insects crawl into the cooker through every gap - and short the control board. The unit dies, sometimes smokes, and your client blames your brand.</p>
<p>An infestation you never see becomes a warranty claim you pay for.</p>
<h2>Spec the insect-proof build</h2>
<ul>
<li><strong>Sealed enclosure</strong> - gasketed seams insects can't pass.</li>
<li><strong>Guarded vents</strong> - mesh-sealed airflow, bugs blocked.</li>
<li><strong>Coated board</strong> - conformal coating resists creepy-crawly conductivity.</li>
</ul>
<p>Standard in our builds for hot, humid markets (SE Asia, Africa). Ask for it by name and we lock it at tooling.</p>
<p>No board short, no fire risk, no surprise claim.</p>""",
    },
    # ---------------- CUSTOMS / COMPLIANCE ----------------
    {
        "slug": "pain-ce-sticker",
        "series": "customs",
        "cat": "CUSTOMS",
        "footer_label": "CE Won't Clear",
        "image": "page6_img2.jpeg",
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
        "body": """<p>CE is the Europe mark — you don't sell to Europe. Your markets want their own: EAC, SNI, SIRIM, TISI, SONCAP, PVoC, NRCS. A missing mark holds the container; demurrage can exceed your margin.</p>
<h2>Do this</h2>
<p>Name the country on the PO. Ask for a real test report — lab, number, date, model — not a sticker photo. A CB report to IEC 60335 speeds approval in Malaysia, Vietnam, South Africa.</p>""",
    },
    {
        "slug": "pain-wrong-plug",
        "series": "customs",
        "cat": "CUSTOMS",
        "footer_label": "Wrong Plug",
        "image": "page6_img1.jpeg",
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
        "body": """<p>Voltage is uniform (220-240V, 50Hz) but plugs are not: C/F in Central Asia & much of SEA, G in Malaysia/Singapore, A/B in Thailand/Philippines. Wrong-plug shipments get held.</p>
<h2>Do this</h2>
<p>Lock the plug at tooling stage — a $0.30 call before production, not rework after. Write the plug type in the spec.</p>""",
    },
    {
        "slug": "pain-no-local-rep",
        "series": "customs",
        "cat": "CUSTOMS",
        "footer_label": "No Local Rep",
        "image": "page9_img1.jpeg",
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
        "body": """<p>EAC, SNI, SIRIM, SONCAP, NRCS all require a named local entity to hold the certificate. Importers learn this at the port — after sailing.</p>
<h2>Do this</h2>
<p>Name the local rep in the contract before production, not a panic email at the port. If the supplier "can't name one," that's your answer before wiring the deposit.</p>""",
    },

    # ---------------- BUYING / SELLING (single-topic, kept) ----------------
    {
        "slug": "article-induction-vs-infrared",
        "series": "buying",
        "cat": "BUYING DECISION",
        "footer_label": "Induction vs Infrared",
        "image": "page7_img2.jpeg",
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
        "body": """<p>Wrong tech = a container unsold. The decider in your markets is cookware.</p>
<ul>
<li><strong>Induction</strong>: heats only magnetic pots (cast iron, steel). Aluminum/glass/ceramic won't work.</li>
<li><strong>Infrared</strong>: heats the glass — works with any pot.</li>
</ul>
<h2>Pick infrared if</h2>
<p>Aluminum-dominant markets (Africa, SE Asia) — kills "it doesn't work" returns, cheaper, low-MOQ entry.</p>
<h2>Pick induction if</h2>
<p>Premium line: ~90% efficient, cool surface, safety story, higher margin.</p>
<h2>Best play</h2>
<p>Carry both: induction premium, infrared universal. Cover every buyer.</p>""",
    },
    {
        "slug": "article-product-showcase",
        "series": "buying",
        "cat": "COMMERCIAL / FOODSERVICE",
        "footer_label": "Commercial Range",
        "image": "page5_img1.jpeg",
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
        "body": """<p>In foodservice the win is the reorder. A unit that throttles at dinner service funds your rival.</p>
<h2>Spec by venue</h2>
<ul>
<li>Cafe: 3500W countertop.</li>
<li>Hotel/buffet: 4000-5000W twin zone.</li>
<li>Catering: 2000-3500W portable.</li>
<li>Wok station: 5000W+ concave coil.</li>
</ul>
<h2>"Commercial grade" on paper</h2>
<ul>
<li>Continuous power (2-hr load test), not peak-only.</li>
<li>Dual-fan + NTC at 40°C.</li>
<li>Reinforced glass, metal housing, industrial IGBT.</li>
<li>Overheat/overvoltage/auto-shutoff.</li>
<li>Serviceable fan + spare-part list.</li>
</ul>
<p>Starter: 3500W + twin-zone 5000W covers most of a new client's line day one.</p>""",
    },
    {
        "slug": "article-cookware-magnetism",
        "series": "buying",
        "cat": "CUSTOMER SUPPORT",
        "footer_label": "Cookware Complaints",
        "image": "page1_img1.jpeg",
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
        "body": """<p>An aluminum pot on induction = nothing heats = "defective" return. The unit is fine; the pot isn't. Aluminum is the household default across Africa & SE Asia — the #1 "broken" complaint.</p>
<h2>Fix it before sale</h2>
<ol>
<li><strong>Magnet test on the box:</strong> "works with magnetic pots; test with a fridge magnet."</li>
<li><strong>Bundle a magnetic disc</strong> — any pot works.</li>
<li><strong>Sell infrared</strong> where pots are mixed — eliminates the category.</li>
<li><strong>Train retail partners</strong> — one shelf line prevents most returns.</li>
</ol>
<p>Rule for every buyer: if a magnet sticks, it works on induction. Print it.</p>""",
    },
    {
        "slug": "article-switch-from-gas",
        "series": "buying",
        "cat": "SELLING TO YOUR BUYERS",
        "footer_label": "Gas to Induction",
        "image": "page9_img2.jpeg",
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
        "body": """<p>Buyers hesitate: "gas is cheaper." The sale is won on total cost of ownership.</p>
<ul>
<li><strong>Energy:</strong> induction ~90% vs gas ~40%. Real money per year.</li>
<li><strong>Speed:</strong> faster heat, faster table turns, lower labour.</li>
<li><strong>Safety:</strong> no flame, no cylinder, no leak — plus the LPG saving where supply is shaky.</li>
</ul>
<h2>Honest objections</h2>
<p>Induction needs magnetic cookware and a proper circuit — solved, not fatal: bundle a magnetic disc, spec the right power. Handle up front and "gas is simpler" collapses.</p>""",
    },
    {
        "slug": "pain-oem-brand",
        "series": "buying",
        "cat": "BUYING DECISION",
        "footer_label": "Launch Your Brand",
        "image": "page6_img1.jpeg",
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
        "body": """<p>Why isn't your brand on the box? MOQ, deposit, "will they steal my design?" — real but manageable.</p>
<p><strong>OEM:</strong> factory's model plus your logo/carton. Fastest, lowest risk. <strong>ODM:</strong> co-develop — more differentiation, more tooling. Start OEM, move to ODM.</p>
<h2>Five clauses that protect you</h2>
<ol>
<li>MOQ per model — a low-MOQ entry SKU lets you test.</li>
<li>Tooling ownership — you own or lock the mold.</li>
<li>Deposit 30/70; 100% upfront is a red flag.</li>
<li>Certification in your name, not the factory's.</li>
<li>Pre-shipment inspection before balance.</li>
</ol>
<p>Those five in writing = a supplier you control.</p>""",
    },
    # ---------------- W2 (2026-08-24) ----------------
    {
        "slug": "pain-voltage-frequency",
        "series": "buying",
        "cat": "SPEC / VOLTAGE",
        "footer_label": "Voltage Match",
        "image": "page8_img1.jpeg",
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
        "body": """<p>Ship the wrong voltage and the unit won't start or burns out. Your markets run 220-240V/50Hz — but Japan, Taiwan, parts of the Americas run 110-120V. Send 220V there = dead stock.</p>
<h2>Do this</h2>
<p>Name voltage/frequency on the PO. Uniform 220-240V/50Hz to lock it. Mixed/110V to wide-voltage (100-240V) or dedicated 110V build.</p>""",
        "faq": [
            ("Which of my markets use 110-120V?", "Mostly the Americas (some), Japan (100V, 50/60Hz) and Taiwan (110V/60Hz). Central Asia, Russia, Southeast Asia and Africa run 220-240V at 50Hz."),
            ("Will a 220-240V cooker work on 110V?", "No - it won't reach power or may not start, and some will overheat. Always match the local voltage or use a wide-voltage (100-240V) unit."),
            ("What does 'wide voltage' mean for cookers?", "A unit with auto-switching input (100-240V, 50/60Hz) that runs safely across both ranges - ideal when you sell into mixed-voltage markets."),
        ],
    },
    {
        "slug": "pain-safe-payment",
        "series": "buying",
        "cat": "PAYMENT / TRUST",
        "footer_label": "Pay Safely",
        "image": "page9_img2.jpeg",
        "readtime": "2 min read",
        "title": "You Paid 100% Upfront - and the Factory Stopped Replying",
        "description": "Paying a China factory 100% upfront is the fastest way to lose the order. The safe payment structure: 30% deposit, 70% balance against the B/L copy or a passed inspection.",
        "excerpt": "100% upfront = the supplier can vanish. Safe structure: 30% deposit, 70% balance on B/L copy or passed inspection.",
        "related": ["pain-oem-brand", "pain-no-local-rep", "pain-ce-sticker"],
        "cta_title": "Want a payment structure that protects you?",
        "cta_text": "Tell us your order size and market - we'll confirm the deposit ratio, inspection gate, and the exact condition that releases the balance.",
        "wa_text": "Hi Vortix Kitchen, I want to import cookers. What payment terms do you offer - deposit, balance on B/L or inspection?",
        "mail_subject": "Payment terms for cooker import",
        "mail_body": "Hi Vortix Kitchen, please advise on your payment structure - deposit ratio, balance on B/L copy or pre-shipment inspection, and any escrow option.",
        "body": """<p>Paying 100% upfront to a China factory is the fastest way to lose everything - the unit ships late, the spec is wrong, or the supplier stops replying after the wire. The deposit you meant as trust becomes a blank cheque.</p>
<h2>What to put in the PO / contract</h2>
<ol>
<li><strong>Deposit 30%</strong> to start; <strong>balance 70%</strong> against the <strong>B/L copy</strong> or a <strong>passed pre-shipment inspection</strong> - never before.</li>
<li><strong>100% upfront is a red flag.</strong> Walk away.</li>
<li><strong>Pay to a company account</strong> (TT), not a personal WeChat/Alipay.</li>
<li><strong>Verify the supplier</strong> - business license, factory address, a live video call. Use third-party inspection before the balance.</li>
<li><strong>Specify in writing:</strong> model, power, plug, certification, and the inspection standard the balance releases against.</li>
</ol>
<p>Release the last cent only when the goods are verified - not when the factory asks nicely.</p>""",
        "faq": [
            ("Is 100% upfront normal for China cooker factories?", "No. 30% deposit / 70% balance against B/L or inspection is standard for established suppliers. 100% upfront is a red flag."),
            ("What protects me if goods fail inspection?", "With the balance held until passed inspection, you keep leverage - the factory fixes or replaces before you pay the rest."),
            ("TT or escrow for a first order?", "TT to a verified company account with inspection-gated balance is common; escrow adds cost but helps on a large first order with an unknown supplier."),
        ],
    },
    # ---------------- W4 (2026-08-27) ----------------
    {
        "slug": "pain-kazakhstan-eac",
        "series": "customs",
        "cat": "CUSTOMS",
        "footer_label": "Kazakhstan EAC",
        "image": "page7_img1.jpeg",
        "readtime": "2 min read",
        "title": "Your Container Is Held at Khorgos — the EAC Mark Most Central Asia Importers Miss",
        "description": "A Kazakhstan-bound container held at the border because EAC certification wasn't done. The EAC (TR CU) conformity step that clears the Eurasian Economic Union.",
        "excerpt": "A Central Asia container held at the border for missing EAC. The TR CU mark that clears Kazakhstan and the EAEU.",
        "related": ["pain-ce-sticker", "pain-no-local-rep"],
        "cta_title": "Clearing Kazakhstan and EAEU customs without surprises?",
        "cta_text": "Tell us your destination in Central Asia or Russia — we'll confirm the EAC (TR CU) documentation and marking before production.",
        "wa_text": "Hi Vortix Kitchen, I import to Kazakhstan/Russia. Can you provide EAC (TR CU) certification and marking for cookers?",
        "mail_subject": "EAC TR CU certification for Kazakhstan/EAEU",
        "mail_body": "Hi Vortix Kitchen, please advise on EAC (TR CU) certification requirements for induction cookers exported to Kazakhstan and the Eurasian Economic Union.",
        "body": """<p>A container stopped at Khorgos or Almaty = demurrage, missed season, lost customers. The usual cause: no EAC mark.</p>
<p>Kazakhstan, Russia, Belarus, Armenia and Kyrgyzstan share the Eurasian Economic Union. For low-voltage appliances, the EAC mark under TR CU 004 is mandatory. No EAC declaration = customs refusal.</p>
<h2>Put this in your PO</h2>
<ul>
<li><strong>EAC declaration</strong> to TR CU 004/2011, issued by an accredited body in the EAEU.</li>
<li><strong>Local representative</strong> named on the certificate (your importer or an authorised local entity).</li>
<li><strong>EAC mark</strong> on the unit and the carton, plus declaration number on shipping docs.</li>
<li><strong>Model match:</strong> declaration must cover the exact model number and power range you ship.</li>
</ul>
<p>A factory that only offers a CE sticker cannot clear EAEU customs. Ask for the EAC declaration before you pay the deposit.</p>""",
        "faq": [
            ("Is EAC the same as CE for Kazakhstan?", "No. CE is for the EU/EEA. EAC (Eurasian Conformity) is required in the EAEU — Kazakhstan, Russia, Belarus, Armenia, Kyrgyzstan."),
            ("Can we use the factory's EAC certificate?", "Only if the certificate lists your local importer/representative and the exact model. Otherwise customs may reject it."),
            ("How long does EAC declaration take?", "Typically 2–6 weeks after test reports are ready. Plan it before production, not after sailing."),
        ],
    },
    # ---------------- W4 (2026-08-28) ----------------
    {
        "slug": "pain-moq-container-loading",
        "series": "buying",
        "cat": "BUYING DECISION",
        "footer_label": "MOQ & Container Load",
        "image": "page5_img2.jpeg",
        "readtime": "2 min read",
        "title": "Your First MOQ Locks Your Margin — How Many Cookers Fit in a 20ft vs 40ft Container",
        "description": "Wrong first MOQ ties up cash or wastes freight space. The container-loading math and PO clause that protects your first order.",
        "excerpt": "Wrong first MOQ ties up cash or wastes freight space. Use the 20ft/40ft loading math and this PO clause.",
        "related": ["pain-oem-brand", "pain-safe-payment", "article-product-showcase"],
        "cta_title": "Planning your first container?",
        "cta_text": "Send your target models and market — we'll confirm carton dims, units per 20/40ft, and a low-MOQ entry SKU to test.",
        "wa_text": "Hi Vortix Kitchen, I'm planning my first container of cookers. Can you confirm carton dims and how many units fit in 20ft/40ft?",
        "mail_subject": "First container MOQ and loading",
        "mail_body": "Hi Vortix Kitchen, please advise on first-order MOQ, carton dimensions, and how many units fit in a 20ft vs 40ft container for my target models.",
        "body": """<p>Agree the wrong MOQ and you either tie up cash in dead stock or pay air-freight rates for a half-empty box. First orders are where margin is made or lost before the container sails.</p>
<h2>Size your first order with this math</h2>
<ul>
<li><strong>20ft container:</strong> ~300–350 single-burner induction cookers.</li>
<li><strong>40ft HQ container:</strong> ~650–750 single-burner units, or 300–350 double-burner units.</li>
<li><strong>Mixed load:</strong> plan carton outer dims before you commit — a few millimetres per box changes the count.</li>
</ul>
<h2>Put in your PO</h2>
<p>"First order: 20ft trial or 40ft mixed. Supplier confirms carton dimensions and max units per container before deposit. MOQ per model: [X] units. Right to combine SKUs to hit container volume."</p>
<p>Test one model, then fill the rest of the box with proven SKUs. A full container cuts freight cost per unit far more than a bigger discount.</p>""",
        "faq": [
            ("What is a safe first MOQ for a new cooker model?", "For standard models, 100–300 units is a common entry MOQ. A smarter first move is one mixed 20ft container so you test multiple SKUs without overcommitting."),
            ("How many induction cookers fit in a 40ft container?", "A 40ft HQ loads roughly 650–750 single-burner units or 300–350 double-burner units, depending on carton outer dimensions."),
            ("Can I mix SKUs in one container?", "Yes — and you should. Mixing SKUs fills the container, lowers freight cost per unit, and lets you test which models sell before scaling."),
        ],
    },
    {
        "slug": "pain-oem-vs-odm",
        "series": "buying",
        "cat": "BUYING DECISION",
        "footer_label": "OEM vs ODM",
        "image": "page1_img2.jpeg",
        "readtime": "2 min read",
        "title": "OEM or ODM? Pick the Wrong One and You Pay for It Twice",
        "description": "OEM is fast and cheap. ODM is yours — but only if the mold and IP clauses are in writing. The cost and risk gap, and the contract terms that close it.",
        "excerpt": "OEM is fast and cheap. ODM is yours — but only if the mold and IP clauses are in writing. The terms that close the gap.",
        "related": ["pain-oem-brand", "pain-moq-container-loading", "pain-safe-payment"],
        "cta_title": "Choosing between OEM and ODM for your brand?",
        "cta_text": "Tell us your target market, planned models and first-order volume — we'll lay out OEM vs ODM cost, lead time and the contract terms that protect your brand.",
        "wa_text": "Hi Vortix Kitchen, I'm launching my cooker brand. Can you compare OEM vs ODM cost, lead time and the IP/mold clauses I need?",
        "mail_subject": "OEM vs ODM for my brand",
        "mail_body": "Hi Vortix Kitchen, please compare OEM and ODM for my cooker brand — cost, lead time, mold ownership, and the IP clauses I need in the contract.",
        "body": """<p>OEM and ODM are not the same deal — pick the wrong one and you pay for it twice. Once in margin, once in differentiation.</p>
<p><strong>OEM</strong> = factory's existing model, your logo and carton. Low MOQ, fast lead time, lowest tooling cost. You buy speed.</p>
<p><strong>ODM</strong> = co-developed, your mold, your specs. Higher tooling ($3k–$15k), longer lead time, but no competitor sells the same unit.</p>
<h2>Match the choice to your stage</h2>
<ul>
<li><strong>New / cash-tight:</strong> start OEM — test the market, keep cash for marketing.</li>
<li><strong>Established / differentiation needed:</strong> move to ODM — the mold and IP are the moat.</li>
</ul>
<h2>Five clauses before you wire the deposit</h2>
<ol>
<li><strong>Mold ownership</strong> in your name (or paid-in-full, locked at the supplier).</li>
<li><strong>Exclusive design</strong> — supplier cannot resell your model.</li>
<li><strong>Tooling refund</strong> tied to an annual volume (e.g. 5,000 units).</li>
<li><strong>Drawing approval</strong> + pre-production sample sign-off, in writing.</li>
<li><strong>30/70 payment</strong>, balance on passed pre-shipment inspection.</li>
</ol>
<p>Wrong choice for your stage, or missing clauses — that's what kills the margin.</p>""",
        "faq": [
            ("What does OEM mean for a cooker brand?", "OEM: the factory builds an existing model and adds your logo, color, and packaging. Lowest MOQ, fastest lead time, but other buyers can sell the same unit."),
            ("What does ODM mean for a cooker brand?", "ODM: you co-develop the model with the factory. You own (or lock) the mold, the design is exclusive to you, but tooling cost and lead time are higher."),
            ("How much does ODM tooling cost for an induction cooker?", "Typically $3,000–$15,000 depending on the housing mold, glass cut and tooling complexity. Negotiate a refund clause tied to annual volume."),
        ],
    },
    # ---------------- W5 (2026-09-01) ----------------
    {
        "slug": "pain-production-scheduling",
        "series": "buying",
        "cat": "BUYING DECISION",
        "footer_label": "Lead Time & Capacity",
        "image": "page2_img1.jpeg",
        "readtime": "2 min read",
        "title": "Your Big Order Shipped 60 Days Late — the Production Schedule Most Importers Don't Lock",
        "description": "A delayed shipment misses your selling season and ties up cash. How to lock factory capacity and milestones so a big cooker order ships on time.",
        "excerpt": "A delayed shipment misses your selling season and ties up cash. Lock the factory capacity and production milestones before you pay the deposit.",
        "related": ["pain-moq-container-loading", "pain-oem-vs-odm", "pain-safe-payment"],
        "cta_title": "Worried about late shipments on big orders?",
        "cta_text": "Tell us your target volume and delivery window — we'll confirm a locked production slot, milestone schedule and penalty clause before you commit.",
        "wa_text": "Hi Vortix Kitchen, I need a big cooker order delivered by [date]. Can you confirm production capacity, milestones and a late-delivery clause?",
        "mail_subject": "Production schedule and lead time for large order",
        "mail_body": "Hi Vortix Kitchen, I am planning a large order and need to confirm production capacity, milestone schedule and lead time before committing. Please advise.",
        "body": """<p>A 60-day delay doesn't just push delivery — it kills your selling season. By the time cookers arrive, your buyers have bought from someone else, and your cash has been locked for months.</p>
<p>Factories often promise 30 days, then put your order behind bigger clients or run out of key components. The PO date becomes a suggestion.</p>
<h2>Put in your PO</h2>
<ol>
<li><strong>Binding lead time:</strong> "Production completed and ready for loading within [X] days from deposit. Liquidated damages: $[Y] per day late, capped at [Z]%."</li>
<li><strong>Capacity allocation:</strong> "Dedicated production line / confirmed capacity slot for this order; no bumping by other clients."</li>
<li><strong>Milestone schedule:</strong> PCB assembly, coil winding, glass fit, final assembly, QC — each with a confirmed date and photo/video proof.</li>
<li><strong>Component buffer:</strong> Key parts (IGBT, glass, fan) locked in stock before production starts.</li>
<li><strong>Pre-shipment inspection gate:</strong> Balance released only after passed inspection and confirmed booking.</li>
</ol>
<p>Schedule without teeth is just a wish. Lock the line, the milestones and the penalty before you wire the deposit.</p>""",
        "faq": [
            ("What is a normal lead time for a large cooker order?", "Standard models usually need 25-35 days after deposit; custom OEM/ODM often needs 40-55 days after sample approval. Always confirm in writing."),
            ("How do I stop the factory bumping my order for a bigger client?", "Add a capacity-allocation clause to your PO: a confirmed production slot with milestone proof and a daily late penalty. The factory will protect your slot when delay costs money."),
            ("Which production milestones should I demand proof of?", "PCB assembly, coil/glass assembly, final assembly, burn-in/QC and carton loading. Ask for dated photos or short videos before releasing the balance."),
        ],
    },
    # ---------------- W5 (2026-09-02) ----------------
    {
        "slug": "pain-spare-parts-pool",
        "series": "buying",
        "cat": "AFTER-SALES / SPARES",
        "footer_label": "Spare Parts Pool",
        "image": "page5_img2.jpeg",
        "readtime": "2 min read",
        "title": "Your Cooker Died After Warranty - and the Spare Part Doesn't Exist",
        "description": "A 2-year-old cooker dies and the spare part isn't available. The spare-parts clause that turns a warranty claim into a 20-minute fix.",
        "excerpt": "A 2-year-old cooker dies and the spare part isn't available. The clause that turns a warranty claim into a 20-minute fix.",
        "related": ["pain-dusty-fan", "pain-igbt-overheat", "pain-oem-vs-odm"],
        "cta_title": "Want a real spare-parts pool, not a paper warranty?",
        "cta_text": "Name your market and order size - we'll lock a spare-parts price list, supply commitment and lead time into the PO, with a service kit shipped with your order.",
        "wa_text": "Hi Vortix Kitchen, I need a real spare-parts pool and supply commitment for cookers in [market]. Can you lock spares pricing and lead time in the PO?",
        "mail_subject": "Spare parts pool for cooker after-sales",
        "mail_body": "Hi Vortix Kitchen, please advise on a spare-parts price list, 5-year supply commitment, and lead time to build a service pool for my cooker orders.",
        "body": """<p>A 2-year-old cooker dies. The fan is $1, but the factory doesn't stock it. You refund the unit, eat the freight, and your client remembers.</p>
<p>Most factories quote a 1-year warranty - then "no spare parts available" the moment you need one. The warranty exists on paper only.</p>
<h2>Put this in the PO</h2>
<ol>
<li><strong>Spare-parts price list locked at order</strong> - fan, IGBT, control board, glass, knob, NTC, with unit price and MOQ.</li>
<li><strong>Spares kit with shipment</strong> - 2-3% of the order as a service kit, or priced as a separate line.</li>
<li><strong>5-year spares supply commitment</strong> - even for discontinued models, from ship date.</li>
<li><strong>Spares lead time in writing</strong> - e.g. 7-15 days, not "when we have stock."</li>
<li><strong>Exploded diagram + repair manual</strong> - so your local tech fixes it, not a refund.</li>
</ol>
<p>A $1 fan and a 20-minute fix, or a full refund and a lost customer. The PO decides which one.</p>""",
        "faq": [
            ("Do factories actually supply spare parts after warranty?", "Good ones do, with a locked price list and a 5-year supply commitment. If the supplier only offers a warranty card and no spares, the warranty is paper only."),
            ("How big a spare-parts kit should I keep in stock?", "A common rule is 2-3% of order volume for the first 12 months - top-selling SKUs first, trim the long tail. Pre-price the kit at order so it's a line item, not a favour."),
            ("Can I get spare parts years after the model is discontinued?", "Only if the PO says so. Add a 5-year spares supply clause tied to the model number, not 'current production.' Without it, you're at the factory's mercy when you need a part."),
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
            "logo": "https://vortixkitchen.com/product_images/page6_img1.jpeg",
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
