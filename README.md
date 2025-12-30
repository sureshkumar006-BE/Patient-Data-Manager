🏥 Patient Data Manager with Validation (Python)
📌 Project Overview

This project is a Python-based Patient Data Management System that loads patient records from a CSV file, validates the data using predefined rules, and manages records through a menu-driven command-line interface. It ensures clean data storage, proper error handling, and logging.

✨ Features

Load patient data from CSV

Validate patient details (ID, name, age, diagnosis, date)

Add new patient records with validation

View all patient records

Search patient by ID or name

Update existing patient details

Delete patient records

Export valid data and error reports

Graceful error handling without crashing

📋 Validation Rules

Patient ID: Must follow format P + 3 digits (e.g., P001)

Name: Only letters and spaces (2–50 characters)

Age: Integer between 0 and 120

Diagnosis: One of
Hypertension, Diabetes, Asthma, Migraine, Arthritis, Other

Admission Date: YYYY-MM-DD format and not a future date

🛠️ Technologies Used

Python

CSV File Handling

Regular Expressions (Regex)

Exception Handling

File I/O

Logging

📂 Output Files

valid_patients.csv – Contains only validated patient records

error_report.txt – Contains detailed validation and processing errors

▶️ How to Run

Clone the repository

Place patients.csv in the project directory

Run the Python script

python patient_data_manager.py


Follow the on-screen menu options

📁 Project Structure
├── patient_data_manager.py
├── patients.csv
├── valid_patients.csv
├── error_report.txt
├── README.md

🎯 Use Case

Designed as a technical assessment project to demonstrate Python fundamentals, data validation, error handling, and file processing in a real-world healthcare data scenario.
