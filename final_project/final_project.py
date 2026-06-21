
#              US Treasury Fiscal Data
#         Documentation: https://fiscaldata.treasury.gov/api-documentation/ 
# Description: The US Department of the Treasury’s public data API, which provides and updates 178 datasets on federal finances.
# Project idea: Analyze trends in debt held by the US

import json
import requests

# base file, aleardy created
CSV_FILE = "us_debt_trends.csv"
# output file
JSON_FILE = "results.json"
# US Treasury API endpoint.Getting lastest 120 records
API_URL = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?sort=-record_date&page[size]=120"


# Get data from web api
response = requests.get(API_URL)

raw_data = response.json()
api_items = raw_data.get("data", [])

existing_dates = []
# Read existing file
with open(CSV_FILE, "r") as file:
    for line in file:
        line = line.strip()

        if line:
            columns = line.split(",")
            existing_dates.append(columns[0])


matching = []
unmatching = []

# Match API data with existing file data
for item in api_items:
    date = item["record_date"]

    if date in existing_dates:
        matching.append(item)
    else:
        unmatching.append(item)


# Append only new records
with open(CSV_FILE, "a") as file:
    for item in unmatching:
        line = (
            item["record_date"] + "," +
            item["tot_pub_debt_out_amt"] + "," +
            item["debt_held_public_amt"] + "\n"
        )

        file.write(line)
        existing_dates.append(item["record_date"])

# math analysis
all_dates = []
all_total_debts = []

# Read the file for data
with open(CSV_FILE, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line:
            columns = line.split(",")

            all_dates.append(columns[0])
            all_total_debts.append(float(columns[1]))

# max debt in last 120 days
max_debt = max(all_total_debts)
# min debt in last 120 days
min_debt = min(all_total_debts)
#avgerage debt
mean_debt = sum(all_total_debts) / len(all_total_debts)
#debt accumlated from start to end date
net_growth_trend = all_total_debts[0] - all_total_debts[-1]

analysis_dictionary = {
    "summary": {
        "total_days_tracked": len(all_dates),
        "tracked_timeframe": f"From {all_dates[0]} to {all_dates[-1]}"
    },
    "analysis_results_usd": {
        "maximum_debt": max_debt,
        "minimum_debt": min_debt,
        "average_debt": round(mean_debt, 2),
        "latest_debt": all_total_debts[0],
        "debt_120days_ago": all_total_debts[-1],
        "net_debt_growth_in_period": net_growth_trend
    }
}

# Save JSON file
with open(JSON_FILE, "w", encoding="utf-8") as file:
    json.dump(analysis_dictionary, file, indent=4)

print(f"Analysis complete. Results freshly saved to '{JSON_FILE}'.")
