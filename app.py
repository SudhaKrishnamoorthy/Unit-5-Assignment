import streamlit as st
import pandas as pd
import numpy as np
#supermarket=pd.read_csv('supermarket')
#st.title('Supermarket')
st.markdown("<h1 style='text-align: center; color: red;'>Sudha's Supermarket Dashboard</h1>", unsafe_allow_html=True)
st.subheader('Top 10 Performing Stores by Sales')
supermarket = st.file_uploader("Supermarket", type=['csv'])

if supermarket is not None:
    df=pd.read_csv(supermarket)
    #modified_df = df.drop(columns = [store_area, items_available]
    column_to_sort_by = 'store_sales'
    sorted_df = df.sort_values(by=column_to_sort_by, ascending=False)
    top_10_df = sorted_df.head(10)
st.dataframe(top_10_df)
st.subheader('Lowest 10 Performing Stores by Sales')
supermarket1 = st.file_uploader("Supermarket1", type=['csv'])
if supermarket1 is not None:
    df2=pd.read_csv(supermarket1)
    column_to_sort_by2 = 'daily_customer_count'
    sorted_df2 =df2.sort_values(by=column_to_sort_by2, ascending=True)
    lowest_10_df = sorted_df2.head(10)
st.dataframe(lowest_10_df)
st.subheader('Average store sales ')
supermarket2 = st.file_uploader("Supermarket2", type=['csv'])
if supermarket2 is not None:
    df3=pd.read_csv(supermarket2)
    st.write("supermarket2:")
    st.write(df3)
    selected_column =st.sidebar.selectbox("Select column for average:", df3.columns)
    average = df3[selected_column].mean()
    integer_average =int(average)
    st.sidebar.write(f"Average {selected_column}: {integer_average}")
    
                               