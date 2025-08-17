# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend (using pytest).
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
2. **Install dependencies:**
   ```commandline
   pip install -r requirements.txt
   ```
3. **Run the FastAPI server:**
   ```commandline
   uvicorn server.server:app --reload
   ```
4. **Run the Streamlit app:**
   ```commandline
   streamlit run frontend/app.py
   ```
5. **Run Tests:**
   ```commandline
   pytest tests/
   ```

## Features

- Add, update, delete, and view expenses by date.
- View expense analytics by category (with percentages and bar chart).
- View monthly expense analytics with totals and bar chart.
- Backend powered by FastAPI with logging enabled.
- Frontend built with Streamlit for interactive visualization.
- MySQL database integration for persistent storage.
- Automated test cases for both frontend and backend using **pytest**.

## Tech Stack

- **Python** – Core programming language  
- **FastAPI** – Backend framework for APIs  
- **Streamlit** – Frontend for visualization  
- **MySQL** – Database for storing expenses  
- **Logging** – For monitoring and debugging  
- **Pytest** – For automated testing  

## Database Schema

**expenses** table:
- `id` (INT, Primary Key, Auto Increment)
- `expense_date` (DATE)
- `category` (VARCHAR)
- `amount` (DECIMAL)
- `notes` (TEXT)

## Usage

1. Navigate to **Add/Update** tab to manage daily expenses.  
2. Go to **Analytics by Category** tab, select start & end date, and view category-wise breakdown with percentages and charts.  
3. Use **Analytics by Month** tab to get month-wise totals and visualize spending trends.  

## Screenshots

### 1. Add / Update Expenses
![Add Update](app_frontend_UI.png)

### 2. Analytics by Category
![Category Analytics](Category_analytics_ui_demo.png)

### 3. Analytics by Month
![Monthly Analytics](Analytics_By_month_ui_demo.png)

## Future Improvements

- User authentication (login system).  
- Export analytics as CSV/Excel.  
- Add pie charts for category percentage visualization.  
- Support multiple currencies.  
- Deploy on cloud (Streamlit Cloud / Heroku / AWS).  

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


