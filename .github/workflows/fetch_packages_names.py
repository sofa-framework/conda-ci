import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--channel", required=True)
parser.add_argument("--package", required=True)

args = parser.parse_args()

QUERY = f"""
{{
  package(channelName: "{args.channel}", name: "{args.package}") {{
    variants(limit: 300) {{
      page {{
        filename
        platform
      }}
    }}
  }}
}}
"""

response = requests.post(
    "https://prefix.dev/api/graphql",
    json={"query": QUERY},
)

response.raise_for_status()

resp_json = response.json()

page = resp_json["data"]["package"]["variants"]["page"]

results = []

for pkg in page:
  results.append([pkg["platform"], pkg["filename"]])

print(json.dumps(results))
