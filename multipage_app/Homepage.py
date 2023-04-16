import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(
    page_title="FreeBreakouts.com"
)

import utils
from styles.st_styles import hide_table_row_index
from configs.constants import company_names

st.title("Check Your Investment!")
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

default_stocks = ['Power Finance Corporation Limited', 'Bank of Baroda', 'Muthoot Finance Limited', 'InterGlobe Aviation Limited', 
                  'RBL Bank Limited', 'Granules India Limited', 'L&T Technology Services Limited', 'Eicher Motors Limited', 
                  'HDFC Life Insurance Company Limited', 'Ambuja Cements Limited']
# Get user inputs
selected_stocks = st.multiselect("Select your stock", options=company_names,  default=default_stocks)
start_date = st.date_input("Start Date", value=pd.to_datetime("2023-01-31", format="%Y-%m-%d"))
end_date = st.date_input("End Date", value=pd.to_datetime("today", format="%Y-%m-%d"))

# convert the dates to string
start = start_date.strftime("%Y-%m-%d")
end = end_date.strftime("%Y-%m-%d")

# Calculate percentage difference for each selected stock
if st.button("Calculate"):
    with st.spinner("Loading data..."):
        result_table_df = utils.calculate_result_table(selected_stocks, start, end)
        format_dict = {'Start Price': '{:.2f}', 'Current Price': '{:.2f}', 'Percentage Change': '{:.2f}'}
        st.table(result_table_df.style.format(format_dict))
        overall_percentage_change = result_table_df['Percentage Change'].sum()
        st.write('Overall Percentage Change: ' + '<span style="color:green;font-weight:bold;">' + str(overall_percentage_change) + '%' + '</span>', unsafe_allow_html=True)




