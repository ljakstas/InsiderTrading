# -*- coding: utf-8 -*-
"""

SEC Filing Scraper
@author: AdamGetbags

"""

# import modules
import requests
import pandas as pd

# create request header
headers = {'User-Agent': "lukasjakstas@yahoo.com"}

# get all companies data
companyTickers = requests.get(
    "https://www.sec.gov/files/company_tickers.json",
    headers=headers
    )

# review response / keys
print(companyTickers.json().keys())

company_dict = companyTickers.json()
target_cik = 1616543
target_index = None

for key, value in company_dict.items():
    if value.get('cik_str') == target_cik:
        target_index = key
        break

# Print the result
if target_index is not None:
    print(f"Index for 'cik_str' == {target_cik}: {target_index}")
    print(f"Entry: {company_dict[target_index]}")
else:
    print(f"'cik_str' == {target_cik} not found in the data.")