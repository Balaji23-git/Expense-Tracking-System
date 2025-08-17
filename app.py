import streamlit as st
from datetime import datetime
import requests
from Analytics_By_Category_UI import analytics_Category
from Analytics_By_Month_UI import analytics_Month
from add_update_UI import add_update

st.header('Expenses Management')

tab1, tab2, tab3 = st.tabs(['Add/Update', 'Analytics By Category', 'Analytics By Month' ])

with tab1:
    add_update()

with tab2:
    analytics_Category()

with tab3:
    analytics_Month()
