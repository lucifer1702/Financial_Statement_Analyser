# first line: 12
@lru_cache(maxsize=20000)
@memory.cache## adjust the cache size accordingly to the data
def load_data():
 
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


    
    company_data['cik_str']=company_data['cik_str'].astype(str).str.zfill(10) 
    df=HashableDataFrame(company_data)

    print(company_data.iloc[0:10,:]) ## to check the data
    
    return df
