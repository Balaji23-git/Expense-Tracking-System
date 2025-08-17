import streamlit as st
from datetime import datetime
import requests
import pandas as pd

api = 'http://localhost:8000/'

def analytics_Category():
    co1, co2 = st.columns(2)
    with co1:
        st.write('Start Date')
        select_start_date = st.date_input('Select start date:', datetime(2024, 8, 1), label_visibility="collapsed")

    with co2:
        st.write('end Date')
        select_end_date = st.date_input('Select end date:', datetime(2024, 8, 10), label_visibility="collapsed")

    if st.button("Get Analytics"):
        summary = requests.get(f'{api}/analytics/{select_start_date}/{select_end_date}')
        if summary.status_code == 200:
            summary = summary.json()
        else:
            st.error('error to find summary')

        # Convert to DataFrame
        df = pd.DataFrame(summary)
        total = df['total'].sum()
        df['percentage'] = (df['total'] / total) * 100

        # reset the index after  - reset_index(drop=True)
        df = df.sort_values(by='percentage', ascending=False).reset_index(drop=True)

        # Format as strings with 2 decimals
        df['total'] = df['total'].map(lambda x: f"{x:.2f}")
        df['percentage'] = df['percentage'].map(lambda x: f"{x:.2f}")

        st.subheader('Expense Breakdown by category')
        st.bar_chart(df.set_index("category")['percentage'].astype(float))
        st.table(df)