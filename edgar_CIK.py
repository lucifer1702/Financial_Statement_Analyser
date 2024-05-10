"""
THIS module is used to get the CIK number of all the tickers in edgar-sec and store it in cache for us to use directly.

The process is as follows:
1. an api request to the url
2.returns a json file 
3. use lru-cache module of functools to store the data in cache
4. use the cache to get the data directly

"""
import requests
import pandas as pd 
from functools import lru_cache

headers={"User-Agent":"mukunth1026@gmail.com"}


@lru_cache(maxsize=20000)## adjust the cache size accordingly to the data
def load_data():
    """ This is the function that is used to get the data from the url using the request module
    convert the data into a dataframe and store it in cache
    the decorator lru_cache is used to store the data in cache
    """
    ## making a request to the url
    all_tickers_edgarsec=requests.get(
        "https://www.sec.gov/files/company_tickers.json",
        headers=headers
    )
    # print(all_tickers_edgarsec.json().keys()) ## to check the keys in the json file

    ## converting the json file into a dataframe using the from_dict method
    company_data=pd.DataFrame.from_dict(all_tickers_edgarsec.json(),
                                        orient="index"
    )


    ##we will convert the cik column into string first and then fill the remaining spaces with 0
    ## we are doing this because while sending the request to the url the cik number is 10 digits long and is a string 
    company_data['cik_str']=company_data['cik_str'].astype(str).str.zfill(10) 

    # print(company_data.iloc[0:5,:]) ## to check the data
    #  this returns the company data and the data is in cache 
    return company_data





# load_data() ## to check if the function is working properly 

