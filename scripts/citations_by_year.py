import ads
import requests
import matplotlib.pyplot as plt
from collections import defaultdict
import os
import json

# === Read ORCID and API token from environment variables ===
ORCID_ID = os.getenv("ADS_ORCID")
ADS_DEV_KEY = os.getenv("ADS_DEV_KEY")

if not ORCID_ID or not ADS_DEV_KEY:
    raise ValueError("Both ADS_ORCID and ADS_DEV_KEY must be set in the environment.")

ads.config.token = ADS_DEV_KEY

# === Step 1: Get all bibcodes ===
print("Querying NASA ADS for publications...")
bibcodes = []
for paper in ads.SearchQuery(q=f"orcid:{ORCID_ID}", fl=["bibcode"], rows=200):
    bibcodes.append(paper.bibcode)

print(f"Found {len(bibcodes)} papers.")

# === Step 2: Query citation histogram ===
headers = {"Authorization": f"Bearer {ADS_DEV_KEY}"}
refereed_citations = defaultdict(int)
nonrefereed_citations = defaultdict(int)

print("Downloading citation data by year...")
for i, bibcode in enumerate(bibcodes, 1):
    url = f"https://api.adsabs.harvard.edu/v1/metrics?bibcode={bibcode}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to get metrics for {bibcode}")
        continue
    hist = response.json().get("citation histogram", {})
    for year, count in hist.get("refereed", {}).items():
        refereed_citations[int(year)] += count
    for year, count in hist.get("nonrefereed", {}).items():
        nonrefereed_citations[int(year)] += count

# === Step 3: Align years and prepare data
all_years = sorted(set(refereed_citations) | set(nonrefereed_citations))
ref_counts = [refereed_citations.get(y, 0) for y in all_years]
nonref_counts = [nonrefereed_citations.get(y, 0) for y in all_years]

# === Step 4: Save citation data to _data/citations_by_year.json
data_output_dir = os.path.join("_data")
os.makedirs(data_output_dir, exist_ok=True)
json_output_path = os.path.join(data_output_dir, "citations_by_year.json")

with open(json_output_path, "w") as f:
    json.dump({
        "years": all_years,
        "refereed": ref_counts,
        "nonrefereed": nonref_counts
    }, f, indent=2)

print(f"Citation data saved to {json_output_path}")

# === Step 5: Plot and save SVG to assets/images/
image_output_dir = os.path.join("assets", "images")
os.makedirs(image_output_dir, exist_ok=True)
plot_path = os.path.join(image_output_dir, "citations_by_year.svg")

plt.figure(figsize=(10, 6))
plt.plot(all_years, ref_counts, label="Refereed", color="cornflowerblue", linestyle="-", linewidth=2)
plt.plot(all_years, nonref_counts, label="Non-Refereed", color="lightgreen", linestyle="--", linewidth=2)
plt.title("Citations per Year by Type (NASA ADS)")
plt.xlabel("Year")
plt.ylabel("Citations")
plt.legend()
plt.tight_layout()
plt.savefig(plot_path, format="svg")
print(f"Plot saved to {plot_path}")
