# -*- coding: utf-8 -*-
"""

SEC Filing Scraper
@author: AdamGetbags

"""

# import modules
import requests
import pandas as pd
import edgar_functions as edgar

# create request header
headers = {'User-Agent': "lukasjakstas@yahoo.com"}

# get all companies data
companyTickers = requests.get(
    "https://www.sec.gov/files/company_tickers.json",
    headers=headers
    )

# review response / keys
print(companyTickers.json().keys())

# format response to dictionary and get first key/value
#SensEntry = companyTickers.json()['3766'] #cik = 1616543

# parse CIK // without leading zeros
#directCik = companyTickers.json()['3766']['cik_str']

#!shorten tickers to edited list.
#isolate form 4

# dictionary to dataframe
#companyData = pd.DataFrame.from_dict(companyTickers.json(),orient='index')

# add leading zeros to CIK
#companyData['cik_str'] = companyData['cik_str'].astype(str).str.zfill(10)

# review data
#print(companyData[3766:3767])
#print(companyData.head(10))

#cik = companyData[3766:3767].cik_str[0]
cik = edgar.cik_matching_ticker("sens")
cik
# get company specific filing metadata
filingMetadata = requests.get(
    f'https://data.sec.gov/submissions/CIK{cik}.json',
    headers=headers
    )

# review json 
print(filingMetadata.json().keys())

filingMetadata.json()['filings']
filingMetadata.json()['filings'].keys()
filingMetadata.json()['filings']['recent']
filingMetadata.json()['filings']['recent'].keys()
# dictionary to dataframe
allForms = pd.DataFrame.from_dict(
             filingMetadata.json()['filings']['recent']
             )

# review columns
allForms.columns
allForms[['accessionNumber', 'filingDate', 'reportDate', 'acceptanceDateTime', 'act', 'form', 'size']].head(50)

# 4 metadata
allForms.iloc[0]
allForms.iloc[1]
allForms.iloc[2]

# get company facts data
companyFacts = requests.get(
    f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',
    headers=headers
    )

#review data
companyFacts.json().keys()
companyFacts.json()['facts']
companyFacts.json()['facts'].keys()

# filing metadata
companyFacts.json()['facts']['dei'][
    'EntityCommonStockSharesOutstanding']
companyFacts.json()['facts']['dei'][
    'EntityCommonStockSharesOutstanding'].keys()
companyFacts.json()['facts']['dei'][
    'EntityCommonStockSharesOutstanding']['units']
companyFacts.json()['facts']['dei'][
    'EntityCommonStockSharesOutstanding']['units']['shares']
companyFacts.json()['facts']['dei'][
    'EntityCommonStockSharesOutstanding']['units']['shares'][0]

# concept data // financial statement line items
companyFacts.json()['facts']['us-gaap']
companyFacts.json()['facts']['us-gaap'].keys()

# different amounts of data available per concept
companyFacts.json()['facts']['us-gaap']['AccountsPayable']
companyFacts.json()['facts']['us-gaap']['Revenues']
companyFacts.json()['facts']['us-gaap']['Assets']

# get company concept data
companyConcept = requests.get(
    (
    f'https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}'
     f'/us-gaap/Assets.json'
    ),
    headers=headers
    )

# review data
companyConcept.json().keys()
companyConcept.json()['units']
companyConcept.json()['units'].keys()
companyConcept.json()['units']['USD']
companyConcept.json()['units']['USD'][0]

# parse assets from single filing
companyConcept.json()['units']['USD'][0]['val']

# get all filings data 
assetsData = pd.DataFrame.from_dict((
               companyConcept.json()['units']['USD']))

# review data
assetsData.columns
assetsData.form

# get assets from 10Q forms and reset index
assets10Q = assetsData[assetsData.form == '10-Q']
assets10Q = assets10Q.reset_index(drop=True)

# plot 
assets10Q.plot(x='end', y='val')