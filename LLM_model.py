"""
we will use the LLM model to gain some insights about the company's 10-k fillings
now given that we have the company's data for;
1. the metadata of the 10-k fillings
2.the facts about the 10-k fillings(assests,liabilities,revenues,operating expenses,net income and shares)

we will now use this and the LLM model to get insights about CAGR ananlysis,Profitablity analysis,Liquidity analysis and Risk assesment
"""

from Edgar_data_prep.edgar_CIK import get_ticker_cik
from Edgar_data_prep.edgar_CIK_ticker import metadata_10k_filings,facts_10k_filings
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
import os 

##API key
api_key = os.environ.get('OPENAI_API_KEY')
