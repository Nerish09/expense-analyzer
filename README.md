# Expense Data Analyzer

## Overview

Expense Data Analyzer is a Python-based command-line application that reads expense data from a CSV file and generates meaningful financial insights. The program processes structured data to calculate total spending, average expenses, spending by category, and the highest individual expense. The focus of this project is data handling, logic, and clean code structure rather than a user interface.

This project was built to strengthen core Python skills such as file handling, data aggregation, and modular programming.

---

## Technologies Used

- Python
- CSV file handling
- Standard Python libraries
- Git & GitHub

---

## Features

- Read expense data from a CSV file
- Calculate total expenses
- Calculate average expense amount
- Group and summarize spending by category
- Identify the highest expense with date and category
- Clean, modular code structure with reusable functions

---

## Project Structure

expense-analyzer/
expenses.csv # Sample expense data
analyzer.py # Main program entry point
utils.py # Helper functions for data processing
README.md

## How to Run the Project Locally

### 1. Clone the repository

git clone https://github.com/your-username/expense-analyzer.git
cd expense-analyzer

### 2. Run the analyzer

python3 analyzer.py

The program will read the data from expenses.csv and print the analysis results in the terminal.

Sample Output
Total expenses: $987.50
Average expense: $197.50

Spending by category:
Food: $32.50
Rent: $900.00
Transport: $15.00
Entertainment: $40.00

Highest expense:
Rent - $900.00 on 2024-01-02

### 3. What I Learned

How to read and parse CSV files in Python

Using dictionaries to group and aggregate data

Writing reusable and modular functions

Performing common data analysis tasks such as totals, averages, and maximum value detection

Structuring a Python project for clarity and maintainability

Using Git and GitHub to manage and publish a project

### 4. Future Improvements

Add date-based filtering (monthly or yearly analysis)

Export analysis results to a CSV or text report

Add basic input validation for data files

Extend the analyzer to support larger datasets
