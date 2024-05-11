"""
we will use the LLM model to gain some insights about the company's 10-k fillings
now given that we have the company's data for;
1. the metadata of the 10-k fillings
2.the facts about the 10-k fillings(assests,liabilities,revenues,operating expenses,net income and shares)
"""

import litellm as ll
from edgar_CIK_ticker import filling_10kmetadata, facts_abt_filling10k


