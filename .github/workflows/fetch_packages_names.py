import requests
import sys
import json

QUERY = """
{
  package(channelName: "sofa-framework", name: "libsofa") {
    variants(limit: 300) {
      page {
        filename
        platform
      }
    }
  }
}
"""

response = requests.post(
    "https://prefix.dev/api/graphql",
    json={"query": QUERY},
)

response.raise_for_status()

resp_json = response.json()

page = resp_json["data"]["package"]["variants"]["page"]
# print("page size: ", len(page))

results = []

for pkg in page:
  # print('----')
  # print('file: ', pkg["filename"])
  # print('platform: ', pkg["platform"])
  results.append([pkg["platform"], pkg["filename"]])

print(json.dumps(results))

# print(json.dumps(results, indent=2))