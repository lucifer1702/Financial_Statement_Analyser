"""
this python file is used to get the CIK string of the ticker provided using the edgar-sec website
the steps are as follows 
1. load_data function is used to get the data from the edgar-sec website, this has all the cik values for all the tickers
2. the get_ticker_cik function is used to get the cik value of the ticker provided"""

"""
We try to do Caching of the data using joblib library and we use sha256 hashing to hash the dataframe and then use it in lru cache"
"""

from joblib import Memory
from functools import lru_cache 
import requests
import pandas as pd
from hashdf import HashableDataFrame

headers = {"User-Agent": "mukunth1026@gmail.com"}

# memory=Memory('cachedir/',verbose=0)

# @lru_cache(maxsize=10000)
# @memory.cache
def load_data():

    # making a get request to the url
    all_tickers_edgarsec = requests.get(
        "https://www.sec.gov/files/company_tickers.json",
        headers=headers
    )
    # print(all_tickers_edgarsec.json().keys()) ## to check the keys in the json file

    # converting the json file into a dataframe using the from_dict method
    company_data = pd.DataFrame.from_dict(all_tickers_edgarsec.json(),
                                          orient="index"
                                          )

    company_data['cik_str'] = company_data['cik_str'].astype(str).str.zfill(10)

    # print(company_data.iloc[0:10,:]) ## to check the data

    # return company_data

# used to get the cik value of the ticker
""" the lru cache always misses on the caching, hence we are unable to do caching of the data here. 
Issue #1 to work on in the future
"""

def get_ticker_cik(ticker):

    # we call the load_data function to get the data
     df = load_data()
     # we will get the CIK corresponding to the ticker
     cik = df[df['ticker'] == ticker]['cik_str'].values[0]
     return cik
    

# print(get_ticker_cik("AAPL"))