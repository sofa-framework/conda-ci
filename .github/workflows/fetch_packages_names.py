import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--channel", required=True)
parser.add_argument("--package", required=True)
parser.add_argument("--platform", required=True)
parser.add_argument("--python", required=False)

args = parser.parse_args()

if args.python:
  py_str = "py" + args.python.replace(".", "")

QUERY = f"""
{{
  package(channelName: "{args.channel}", name: "{args.package}") {{
    variants(limit: 300, platform: "{args.platform}") {{
      page {{
        filename
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

results = []

if resp_json["data"]["package"]:
  page = resp_json["data"]["package"]["variants"]["page"]


  for pkg in page:
    # if python version is specified, filter only package files
    # that contains the python version substring (e.g. py310)
    if args.python:
      if py_str in pkg["filename"]:
        results.append(pkg["filename"])
    else:
      results.append(pkg["filename"])

print(json.dumps(results))
