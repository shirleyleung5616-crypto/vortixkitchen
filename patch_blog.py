# -*- coding: utf-8 -*-
import re, os

HERE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(HERE, "blog", "build_blog.py")
with open(path, "r", encoding="utf-8") as f:
    s = f.read()

# 1) Remove pain-preshipment-check (user called it fluff / not needed)
pat = re.compile(r'\n    \{\n        "slug": "pain-preshipment-check".*?\n    \},', re.DOTALL)
s2 = pat.sub('', s, count=1)
if s2 == s:
    print("WARN: preshipment block not found, nothing removed")
s = s2

# 2) Insert two new reliability articles before the CUSTOMS comment
new_block = '''    # ---------------- RELIABILITY (configurable builds) ----------------
    {
        "slug": "pain-cooling-fans",
        "series": "reliability",
        "cat": "RELIABILITY",
        "footer_label": "Cooling Fans",
        "image": "page2_img8.jpeg",
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
        "image": "page2_img8.jpeg",
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
    # ---------------- CUSTOMS / COMPLIANCE ----------------'''

marker = "    # ---------------- CUSTOMS / COMPLIANCE ----------------"
if marker not in s:
    print("WARN: customs marker not found")
else:
    s = s.replace(marker, new_block, 1)
    print("inserted 2 new articles before CUSTOMS marker")

with open(path, "w", encoding="utf-8") as f:
    f.write(s)
print("patched build_blog.py")
