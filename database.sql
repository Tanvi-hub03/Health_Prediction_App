
CREATE DATABASE health_prediction;

USE health_prediction;

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    dob DATE,
    email VARCHAR(100),
    glucose FLOAT,
    haemoglobin FLOAT,
    cholesterol FLOAT,
    remarks TEXT

);