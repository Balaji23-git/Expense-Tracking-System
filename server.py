from fastapi import FastAPI
from Backend import db_helper
from datetime import date
from pydantic import BaseModel
from typing import List

app = FastAPI()

class valida(BaseModel):
    amount: float
    category: str
    notes : str

class expenc(BaseModel):
    category: str
    total: float


@app.get('/expense/{expense_date}',response_model = List[valida] )
def get_expense_for_date(expense_date: date):
    value = db_helper.fetch_expenses_for_date(expense_date)
    return value

@app.post('/expense/{expense_date}')
def insert_expense(expense_date:date, expense:List[valida]):
    db_helper.delete_form_expense(expense_date)
    for exp in expense:
        db_helper.insert_into_expense(expense_date,exp.amount,exp.category,exp.notes)
    return f'Data added successfully'

@app.get('/analytics/{start_date}/{end_date}',response_model = List[expenc])
def get_analytatic_for_dates(start_date: date, end_date: date):
    exp_summary = db_helper.fetch_expences_summary(start_date,end_date)
    return exp_summary

@app.get('/analytics/month/')
def get_analytatic_for_month():
    analytatic_for_month = db_helper.fetch_expences_By_Month()
    return analytatic_for_month







