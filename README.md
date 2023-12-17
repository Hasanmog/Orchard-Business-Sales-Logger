# Orchard Business Sales Logger

## Overview

In the dynamic world of business, the importance of logging cannot be overstated. Keeping track of every transaction, big or small, provides invaluable insights into the health and trajectory of a business. It's like having a detailed map during a treasure hunt; each logged sale leads you closer to the treasure of success and sustainability.

This repository houses a unique codebase specifically tailored for logging sales in an orchard business. Whether you're dealing with different types of oranges and avocados, our sales logger is your digital ledger, ensuring that every juicy detail of your transactions is captured efficiently and effectively.

## Repository Structure

- `entries.py`: Contains functions that prompt the user for sales entry data. It is the interface through which all sales data is collected.
- `storing.py`: Responsible for storing the collected data into an SQLite database. It acts as the data layer of our application, ensuring data persistence.
- `main.py`: This is the heart of our application, tying together the functionalities of entries and storing. It orchestrates the user input process, data storage, and overall flow of the sales logging.
- `requirements.txt`: A list of Python packages that are required to run this application. Use `pip install -r requirements.txt` to install all dependencies.
- `sqlite_to_excel.py`: A utility script that converts the logged sales data from the SQLite database to an Excel file, facilitating easy data analysis and reporting.

## Getting Started

To get started with the Orchard Business Sales Logger, clone this repository and install the required packages listed in `requirements.txt` using the following command:

```bash
pip install -r requirements.txt

# Run main.py to start logging your sales data:

python main.py

# For converting your logged data to an Excel spreadsheet, run:

python sqlite_to_excel.py
