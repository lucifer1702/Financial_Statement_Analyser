"""
this file is where we get the actual data from the edgar-sec website for the ticker
we then use it get the fillings for the company
then we use it to get 10-k only fillings of the company
we will then use this data to get some results in the llm module
"""
import requests
# importing the load_data function from the edgar_CIK.py file
from Edgar_data_prep.edgar_CIK import get_ticker_cik
import pandas as pd

headers = {"User-Agent": "mukunth1702@kgpian.iitkgp.ac.in"}

# used to get the metadata for all the 10k fillings for the ticker


def metadata_10k_filings(ticker):
    # get the cik value of the ticker
    cik = get_ticker_cik(ticker)
    # making a get request to the url
    fillingmetadata = requests.get(
        f"https://data.sec.gov/submissions/CIK{cik}.json", headers=headers)
    # print(fillingmetadata.json().keys()) ## to check the keys in the json file
    # converting into pd dataframe
    allmetadata = pd.DataFrame.from_dict(
        fillingmetadata.json()['filings']['recent'])
    # to get only the 10-k fillings
    metadata_10k = allmetadata[allmetadata['form'] == '10-K']
    return metadata_10k

# this function is used to get the facts about the filling and we are going to retrieve facts about all the 10k fillings the firm has done

# This is the major portion of the fillings where export facts about the filling


def facts_10k_filings(ticker):
    # get the cik number of the ticker
    cik = get_ticker_cik(ticker)
    # making a get request to the url
    facts = requests.get(
        f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", headers=headers)
    # the dei route
    facts_df_dei = pd.DataFrame.from_dict(facts.json(
    )['facts']['dei']['EntityCommonStockSharesOutstanding']['units']['shares'])
    facts_df_dei_10k = facts_df_dei[facts_df_dei['form'] == '10-K']
    # the us gaap route
    # print(facts.json()['facts']['us-gaap'].keys())
    #  this has a bunch of keys lets try and extract th most out of it
    """
  given the field has multiple important keys we will try to extract the most important ones:
  the important keys are as follows: Assets,Liablities,Revenues,OperatingExpenses,NetIncomeLoss
  """
    # hardcoded the dataframe extraction of all the important fields

    facts_df_usgaap1 = pd.DataFrame.from_dict(
        facts.json()['facts']['us-gaap']['Assets']['units']['USD'])
    facts_df_usgaap1_10k = facts_df_usgaap1[facts_df_usgaap1['form'] == '10-K']
    facts_df_usgaap2 = pd.DataFrame.from_dict(
        facts.json()['facts']['us-gaap']['Liabilities']['units']['USD'])
    facts_df_usgaap2_10k = facts_df_usgaap2[facts_df_usgaap2['form'] == '10-K']
    facts_df_usgaap3 = pd.DataFrame.from_dict(
        facts.json()['facts']['us-gaap']['Revenues']['units']['USD'])
    facts_df_usgaap3_10k = facts_df_usgaap3[facts_df_usgaap3['form'] == '10-K']
    facts_df_usgaap4 = pd.DataFrame.from_dict(
        facts.json()['facts']['us-gaap']['OperatingExpenses']['units']['USD'])
    facts_df_usgaap4_10k = facts_df_usgaap4[facts_df_usgaap4['form'] == '10-K']
    facts_df_usgaap5 = pd.DataFrame.from_dict(
        facts.json()['facts']['us-gaap']['NetIncomeLoss']['units']['USD'])
    facts_df_usgaap5_10k = facts_df_usgaap5[facts_df_usgaap5['form'] == '10-K']

    return facts_df_dei_10k, facts_df_usgaap1_10k, facts_df_usgaap2_10k, facts_df_usgaap3_10k, facts_df_usgaap4_10k, facts_df_usgaap5_10k
