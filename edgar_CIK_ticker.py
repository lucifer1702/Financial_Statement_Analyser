"""
this file is where we get the actual data from the edgar-sec website for the ticker
we then use it get the fillings for the company
then we use it to get 10-k only fillings of the company
we will then use this data to get some results in the llm module
"""


import requests
from edgar_CIK import load_data ## importing the load_data function from the edgar_CIK.py file
import pandas as pd

