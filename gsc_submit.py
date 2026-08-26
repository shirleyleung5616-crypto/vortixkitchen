import json
import time
import jwt
import requests

# Load service account key
with open('gsc_service_account.json') as f:
    key = json.load(f)

# Build JWT for OAuth2 service account
now = int(time.time())
claim = {
    "iss": key["client_email"],
    "scope": "https://www.googleapis.com/auth/webmasters",
    "aud": "https://oauth2.googleapis.com/token",
    "exp": now + 3600,
    "iat": now,
}

signed_jwt = jwt.encode(claim, key["private_key"], algorithm="RS256")

# Get access token
resp = requests.post(
    "https://oauth2.googleapis.com/token",
    data={
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": signed_jwt,
    },
    timeout=30,
)
print(f"Token response: {resp.status_code}")
if resp.status_code != 200:
    print(f"Token error: {resp.text}")
    exit(1)

access_token = resp.json()["access_token"]

# Submit sitemap via GSC API
site_url = "https://vortixkitchen.com/"
sitemap_url = "https://vortixkitchen.com/sitemap.xml"

submit_url = f"https://www.googleapis.com/webmasters/v3/sites/{requests.utils.quote(site_url, safe='')}/sitemaps/{requests.utils.quote(sitemap_url, safe='')}"

resp2 = requests.put(
    submit_url,
    headers={"Authorization": f"Bearer {access_token}"},
    timeout=30,
)

print(f"Submit response: {resp2.status_code}")
if resp2.status_code in (200, 204):
    print("SUCCESS: Sitemap submitted to GSC")
    print(f"  Site: {site_url}")
    print(f"  Sitemap: {sitemap_url}")
else:
    print(f"Submit error: {resp2.text}")
