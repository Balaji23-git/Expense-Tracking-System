import streamlit as st
from datetime import datetime
import requests
import pandas as pd

api = 'http://localhost:8000/'

def analytics_Month():
    analytics_Month = requests.get(f'{api}//analytics/month/')
    if analytics_Month.status_code == 200:
        data = analytics_Month.json()
    else:
        st.error('Error in loading data')

    # Convert to DataFrame
    df = pd.DataFrame(data)

    df['total'] = df['total'].map(lambda x: f"{x:.2f}")

    st.subheader('Expense Breakdown by Month')
    st.bar_chart((df.set_index("month")['total']).astype(float))
    st.table(df)
