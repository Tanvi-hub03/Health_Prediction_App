<<<<<<< HEAD
# Health Prediction System

## Project Overview

Health Prediction System is a Flask-based web application developed using Python and MySQL. The application allows users to manage patient blood test records and predict possible health risks based on Glucose, Haemoglobin, and Cholesterol values.

The system provides complete CRUD functionality, input validation, patient search, CSV export, and health risk prediction remarks generated from patient test values.

---

## Features

* Add Patient Record
* View Patient Records
* Update Patient Details
* Delete Patient Records
* Search Patient by Name
* Export Patient Data to CSV
* Health Risk Prediction Remarks
* Email Address Validation
* Date of Birth Validation (Future Date Restriction)
* Numeric Blood Test Value Validation
* MySQL Database Integration

---

## Technologies Used

### Frontend

* HTML
* CSS
* Bootstrap 5

### Backend

* Python
* Flask

### Database

* MySQL

### Health Prediction

* Rule-Based Health Risk Prediction
* External AI (Google Gemini API) Ready Structure

---

## Database

### Database Name

health_prediction

### Table Name

patients

### Fields

* ID
* Full Name
* Date of Birth
* Email Address
* Glucose
* Haemoglobin
* Cholesterol
* Remarks

---

## Project Structure

Health_prediction_System/

├── app.py

├── database.sql

├── requirements.txt

├── README.md

└── templates/

    ├── index.html

    ├── add_patient.html

    └── edit_patient.html

---

## Installation and Setup

### 1. Clone the Repository

git clone <repository-url>

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Create Database

Run the database.sql script in MySQL.

### 4. Configure Database Credentials

Update MySQL username, password, and database name in app.py.

### 5. Run the Application

python app.py

### 6. Open Browser

http://127.0.0.1:5000

---

## Validation Implemented

* Valid Email Address Format
* Date of Birth Cannot Be a Future Date
* Glucose Must Be Numeric
* Haemoglobin Must Be Numeric
* Cholesterol Must Be Numeric

---

## Future Enhancements

* User Authentication System
* Dashboard Analytics
* PDF Report Generation
* Email Notifications
* Advanced AI-Based Health Prediction
* Integration with External Healthcare APIs

---

## Author

Tanvi Jain
M.Sc. Computer Science
=======

>>>>>>> e68682f43dc9622e05a7445fb801c13abb7f3228
