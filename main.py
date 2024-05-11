from LLM_model import *
import streamlit as sc
from PIL import Image
image = Image.open('Img/img.jpg')


def main():
    sc.title('Financial Filings analyser')
    menu = ['Home', 'About']
    choice = sc.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        sc.subheader('Please Enter the Ticker for which you want insights')
        with sc.form(key='ticker'):
            raw_query = sc.text_area("type-here")
            sub_text = sc.form_submit_button(label='YES')
        if sub_text:

            metadata_result = llm_analysis_metadata(raw_query)
            sc.success(metadata_result['input'])
            sc.write(metadata_result['output'])

            metadata_shares = llm_analysis_shares(raw_query)
            sc.success(metadata_shares[0]['input'])
            sc.write(metadata_shares[0]['output'])
            sc.success(metadata_shares[1]['input'])
            sc.write(metadata_shares[1]['output'])

            metadata_assets = llm_analysis_assets(raw_query)
            sc.success(metadata_assets[0]['input'])
            sc.write(metadata_assets[0]['output'])
            sc.success(metadata_assets[1]['input'])
            sc.write(metadata_assets[1]['output'])

            metadata_liablities = llm_analysis_liablities(raw_query)
            sc.success(metadata_liablities[0]['input'])
            sc.write(metadata_liablities[0]['output'])
            sc.success(metadata_liablities[1]['input'])
            sc.write(metadata_liablities[1]['output'])

            metadata_revenue = llm_analysis_revenue(raw_query)
            sc.success(metadata_revenue[0]['input'])
            sc.write(metadata_revenue[0]['output'])
            sc.success(metadata_revenue[1]['input'])
            sc.write(metadata_revenue[1]['output'])

    else:
        sc.subheader('About')
        sc.write('This is the Application built for the task of analysing financial filings, especially 10-K filings of tickers')
        sc.write(
            'Hello, This is Mukundan, a passionate coder and an enthusiat towards LLM and Genai')
        sc.image(image=image)
        sc.write('thanks for the opportunity')
        sc.write('This project was done for the purpose of Evaluation')


    # print(response.get_top_answer())
if __name__ == "__main__":
    main()
