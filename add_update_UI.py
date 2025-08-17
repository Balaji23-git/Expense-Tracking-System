import streamlit as st
from datetime import datetime
import requests

api = 'http://localhost:8000/'

def add_update():
    select_date = st.date_input('Add Expense for Date:', datetime(2024,8,1))
    response = requests.get(f'{api}/expense/{select_date}')
    if response.status_code == 200:
        res = response.json()

    else:
        st.errors('No data fund')

    cat = ['Food', 'Rent', 'Shopping', 'Entertainment', 'Other']

    with st.form(key='Expense_table'):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('Amount')

        with col2:
            st.write('category')

        with col3:
            st.write('Note')

        Data = []

        for i in range(5):
            if i<len(res):
                amount = res[i]['amount']
                category = res[i]['category']
                notes = res[i]['notes']

            else:
                amount = 0.0
                category = 'Shopping'
                notes = ''


            col1,col2,col3 = st.columns(3)

            with col1:
                amount_input = st.number_input(label='Amount',min_value= 0.0, step=1.0, value=amount,key=f'amount_{i}', label_visibility="collapsed")

            with col2:
                catogery_input = st.selectbox(label='catogery', options=cat, index=cat.index(category), key=f'category_{i}', label_visibility="collapsed")

            with col3:
                notes_input = st.text_input(label='note', value=notes, key=f'note_{i}', label_visibility="collapsed")

            Data.append({
                'amount': amount_input,
                'category': catogery_input,
                'notes': notes_input
            })


        submit_button = st.form_submit_button()
        if submit_button:
            filtered_data = [Data for Data in Data if Data['amount']>0]
            ret = requests.post(f'{api}/expense/{select_date}', json = filtered_data)
            if ret.status_code==200:
                st.write('Data added successfully')
            else:
                st.errors('Data error')