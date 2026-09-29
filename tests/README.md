# Currency Converter

## Overview

The Currency Converter is a Python-based command-line application
that allows users to convert amounts between multiple international
currencies using predefined exchange rates.

The application also allows users to view available currencies,
validate input, and maintain a history of previous conversions.

## Features

- Convert between multiple currencies
- View available currencies
- Display currency names
- Validate user input
- Handle invalid currency codes
- Prevent zero and negative amounts
- Save conversion history
- View previous conversions
- Modular Python implementation
- Automated testing

## Technologies Used

- Python 3
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Exception Handling
- CSV File Handling
- Modular Programming
- Pytest

## Project Structure

Currency_Converter_Project/
│
├── main.py
├── converter.py
├── currencies.py
├── validator.py
├── history.py
├── display.py
│
├── tests/
│   └── test_converter.py
│
├── data/
│   └── conversion_history.csv
│
├── README.md
├── statement.md
├── project_report.md
├── requirements.txt
└── .gitignore

## How to Run

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Open the Project

Open the project folder in VS Code or a terminal.

### Step 3: Run the Program

Run:

python main.py

## How to Use

After starting the program, the following menu is displayed:

1. Convert Currency
2. View Available Currencies
3. View Conversion History
4. Exit

Select an option by entering its corresponding number.

## Testing

The project contains automated tests for the currency conversion functions.

Run the tests using:

python -m pytest

The tests check:

- USD to INR conversion
- INR to USD conversion
- Same-currency conversion
- Invalid currency handling

## Input Validation

The program checks that:

- The entered amount is a valid number.
- The amount is greater than zero.
- The FROM currency is supported.
- The TO currency is supported.

## Conversion Method

The program uses USD as the reference currency.

Amount in USD = Amount / FROM currency rate

Converted Amount = Amount in USD × TO currency rate

## Future Enhancements

- Live exchange-rate API
- Graphical User Interface
- Database storage
- Currency search functionality
- Historical exchange-rate charts

## Author
HADI HASAN
VIT BHOPAL