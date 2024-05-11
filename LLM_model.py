"""
we will use the LLM model to gain some insights about the company's 10-k fillings
now given that we have the company's data for;
1. the metadata of the 10-k fillings
2.the facts about the 10-k fillings(assests,liabilities,revenues,operating expenses,net income and shares)

we will now use this and the LLM model to get insights about CAGR ananlysis,Profitablity analysis,Liquidity analysis and Risk assesment
"""

from Edgar_data_prep.edgar_CIK import get_ticker_cik
from Edgar_data_prep.edgar_CIK_ticker import metadata_10k_filings, facts_10k_filings
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import retrieval_qa
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings


import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_KEY")

index_creator = VectorstoreIndexCreator()

# we will use this fuction to create the dataframe agent for all the databases combined
""" Due TO TOKEN LIMITATIONS AND THE FACT THAT THE MODEL STARTS TO HALLUCINATE WHEN ALL THE 
DATASETS ARE GIVEN AS A COMBINED DATASET, WE WILL USE THE DATASETS INDIVIDUALLY TO GET THE RESULTS"""
# ISSUE 2 MAJOR SOLVING REQUIRED IN THE FUTURE

#


def llm_analysis_metadata(ticker):
    df_metadata = metadata_10k_filings(ticker)
    agent = create_pandas_dataframe_agent(
        OpenAI(temperature=0.1), [df_metadata], verbose=True)
    query = "summarize the metadata of the 10-k fillings and give insights about the company"
    response = agent(query)
    return response


def llm_analysis_shares(ticker):
    df_shares, _, _, _, _, _ = facts_10k_filings(ticker)
    agent = create_pandas_dataframe_agent(
        OpenAI(temperature=0.1), [df_shares], verbose=True)
    query1 = "summarize the volatilty of shares of the company"
    response1 = agent(query1)
    query2 = "What is the CAGR of the company"
    response2 = agent(query2)
    return response1, response2


def llm_analysis_assets(ticker):
    df_shares, _, _, _, _, _ = facts_10k_filings(ticker)
    agent = create_pandas_dataframe_agent(
        OpenAI(temperature=0.1), [df_shares], verbose=True)
    query1 = "how much is the company's assests"
    response1 = agent(query1)
    query2 = "is the company profitable"
    response2 = agent(query2)
    return response1, response2


def llm_analysis_liablities(ticker):
    _, df_liablities, _, _, _, _ = facts_10k_filings(ticker)
    agent = create_pandas_dataframe_agent(
        OpenAI(temperature=0.1), [df_liablities], verbose=True)
    query1 = "how much is the company's liablities"
    response1 = agent(query1)
    query2 = "is the company going on a loss"
    response2 = agent(query2)
    return response1, response2

#


def llm_analysis_revenue(ticker):
    _, df_liablities, _, _, _, _ = facts_10k_filings(ticker)
    agent = create_pandas_dataframe_agent(
        OpenAI(temperature=0.1), [df_liablities], verbose=True)
    query1 = "how much is the company's revenues"
    response1 = agent(query1)
    query2 = "what is the rate at which the revenues have grown"
    response2 = agent(query2)
    return response1, response2
