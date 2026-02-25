import requests
import sys
import json

QUERY = """
query {
  channel(name: "sofa-framework") {
    packages(first: 200) {
      nodes {
        name
        versions(first: 100) {
          nodes {
            version
            files {
              filename
              size
              sha256
            }
          }
        }
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

data = response.json()

print('data:', data)
packages = data["data"]["channel"]["packages"]["nodes"]

results = []

for pkg in packages:
    if pkg["name"] == "libsofa":
        for version in pkg["versions"]["nodes"]:
            for f in version["files"]:
                results.append({
                    "version": version["version"],
                    "filename": f["filename"],
                    "size": f["size"],
                    "sha256": f["sha256"],
                })

print(json.dumps(results, indent=2))