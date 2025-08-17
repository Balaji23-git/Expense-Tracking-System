import mysql.connector
from contextlib import contextmanager
from Backend.logging_setup import get_logging


logger = get_logging('db_helper')

@contextmanager
def get_cursor(commit=False):
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'expense_manager'
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit==True:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_expenses_for_date(expense_date):
    logger.info(f'fetch_expenses_for_date called with date:{expense_date}')
    with get_cursor() as cursor:
        cursor.execute('SELECT * FROM expenses where expense_date = %s',(expense_date,))
        expense = cursor.fetchall()
        return expense


def insert_into_expense(expense_date,amount,catogery,notes):
    logger.info(f'insert_into_expense with date:{expense_date}, amount: {amount}, catogery {catogery}, notes {notes}')
    with get_cursor(commit=True) as cursor:
        cursor.execute('INSERT INTO expense_manager.expenses (expense_date, amount, category, notes)'
                       'VALUES (%s,%s,%s,%s)',(expense_date,amount,catogery,notes))

def delete_form_expense(expense_date):
    logger.info(f'delete_form_expense called with date:{expense_date}')
    with get_cursor(commit=True) as cursor:
        cursor.execute('DELETE FROM expenses WHERE expense_date=%s',(expense_date,))


def fetch_expences_summary(start_date,End_date):
    logger.info(f'fetch_expences_summary called with date between start date:{start_date}, end date: {End_date}')
    with get_cursor() as cursor:
        cursor.execute('''select category, sum(amount) as total from expense_manager.expenses
                          where expense_date between %s and %s
                          group by category''',(start_date,End_date))
        fetch = cursor.fetchall()
        return fetch

def fetch_expences_By_Month():
    logger.info(f'fetch_expences_By_Month called ')
    with get_cursor() as cursor:
        cursor.execute('''select 
                          DATE_FORMAT(expense_date, '%b %Y') AS month,
                          SUM(amount) AS total
                          FROM expense_manager.expenses
                          WHERE YEAR(expense_date) = 2024
                          GROUP BY DATE_FORMAT(expense_date, '%b %Y')
                          ORDER BY MIN(expense_date);
                      ''')
        fetch_month = cursor.fetchall()
        return fetch_month




if __name__=='__main__':
    print(fetch_expenses_for_date('2024-08-07'))
    insert_into_expense('2024=08-23',250,'Food','ate something good on birthday')
    # delete_form_expense('2024-08-07')
    print(fetch_expences_summary('2024-08-01','2024-08-05'))
    print(fetch_expenses_for_date('2024-08-23'))



