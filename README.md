
# Expense Tracker Application

## Description

This is a simple web-based Expense Tracker application built using Flask, Flask-WTF for form handling, and a basic file-based data storage (JSON) for managing expenses. It allows users to add, view, update, and delete their expenses. The application also categorizes expenses into predefined categories and supports multiple accounts (e.g., Wifey's, Husband's, and Common).

## Features

1. Create Expenses: Add new expenses by providing details such as expense name, category, price, account, date, and an optional comment.  
2. View Expenses: See a list of all recorded expenses in a table format.  
3. Edit Expenses: Update an existing expense's details.  
4. Delete Expenses: Remove an expense from the list.  
5. Expense Categories: Predefined categories (e.g., 'Mortgage', 'Bills', 'Food', 'Travel', etc.) to classify expenses.  
6. Account Management: Select the associated account for each expense (Wifey's, Husband's, or Common).  
7. Form Validation: Ensures data integrity with proper validation for price, dates, and other fields.

## Usage

###### Expense List Page

When you open the application, you'll be directed to the list of expenses.
You can add a new expense by filling out the form and clicking Submit.
Expenses are listed with their name, category, price, account, and date.
You can click on an expense to update it or delete it.

###### Expense Details Page

Click on any expense to view and edit its details (Expense Name, Category, Price, Account, Date, and Comment).
After editing, click Save to update the expense.

###### Expense Deletion

You can delete an expense by clicking the Delete button next to an expense.
Deleting an expense will remove it from the list and update the expenses.json file.

## Tech Stack

Backend: Python, Flask  
Frontend: HTML, Jinja2, Bootstrap (for styling)  
Forms: Flask-WTF for handling and validating forms  
Data Storage: JSON file (expenses.json) for storing and loading expense data  
Concurrency: Threading used to handle data safely across multiple operations  

## Installation

###### Prerequisites  

Before running the application, ensure that you have Python 3.x installed on your system.

###### Dependencies

Install required Python packages using pip:  
pip install -r requirements.txt  
Where requirements.txt contains dependencies.

###### Running the Application

1. Clone or download the repository.
2. Navigate to the project folder:
cd path/to/your/project
3. Run the Flask development server:
python app.py
4. Open your browser and go to http://127.0.0.1:5000/ to start using the application.
