import csv
from flask import Response
from flask import Flask, render_template, request, redirect
from datetime import date
import re
import mysql.connector

# import google.generativeai as genai
# genai.configure(api_key="gemini_api_key")
# model = genai.GenerativeModel("gemini-2.0-flash")
# def generate_health_remark(glucose, haemoglobin, cholesterol):
#     prompt = f"""
#     Analyze these patient blood test values.
#     Glucose: {glucose}
#     Haemoglobin: {haemoglobin}
#     Cholesterol: {cholesterol}
#     Predict possible health risks.
#     Give response in 2-3 short lines only.
#     """
#     response = model.generate_content(prompt)
#     return response.text[:300]


# Generate health prediction remarks based on blood report values
def generate_health_remark(glucose, haemoglobin, cholesterol):

    remarks = []

    if float(glucose) > 180:
        remarks.append("High glucose level. Possible diabetes risk.")

    if float(haemoglobin) < 12:
        remarks.append("Low haemoglobin. Possible anemia risk.")

    if float(cholesterol) > 240:
        remarks.append("High cholesterol. Possible heart disease risk.")

    if len(remarks) == 0:
        return "All values appear within normal range."

    return " ".join(remarks)

app = Flask(__name__)


# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="health_prediction"
)

cursor = db.cursor()

# Search patient by name
@app.route('/')
def index():

    search = request.args.get('search')

    if search:
        query = """
        SELECT * FROM patients
        WHERE full_name LIKE %s
        """
        cursor.execute(
            query,
            ('%' + search + '%',)
        )
    else:
        cursor.execute(
            "SELECT * FROM patients"
        )
    patients = cursor.fetchall()

    return render_template(
        'index.html',
        patients=patients
    )

# Export all patient records to CSV
@app.route('/export')
def export_csv():

    cursor.execute(
        "SELECT * FROM patients"
    )
    patients = cursor.fetchall()
    def generate():
        data = csv.writer(
            open('temp.csv', 'w', newline='')
        )
    output = []

    output.append(
        "ID,Name,DOB,Email,Glucose,Haemoglobin,Cholesterol,Remarks\n"
    )

    for patient in patients:

        row = ",".join(
            [str(col) for col in patient]
        )
        output.append(row + "\n")

    return Response(
        output,
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment;filename=patients.csv"
        }
    )

@app.route('/add', methods=['GET', 'POST'])
def add_patient():

    if request.method == 'POST':
        full_name = request.form['full_name']
        dob = request.form['dob']
        selected_date = date.fromisoformat(dob)

        if selected_date > date.today():
            return "DOB cannot be a future date"

        email = request.form['email']
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            return "Invalid Email Address"
    
        
        try:
             glucose = float(request.form['glucose'])
             haemoglobin = float(request.form['haemoglobin'])
             cholesterol = float(request.form['cholesterol'])
        except:
            return "Glucose, Haemoglobin and Cholesterol must be numeric values"

    
        remarks = generate_health_remark(
            glucose,
            haemoglobin,
            cholesterol
        )

        sql = """
        INSERT INTO patients
        (full_name,dob,email,glucose,haemoglobin,cholesterol,remarks)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        cursor.execute(sql, values)
        db.commit()

        return redirect('/')

    return render_template('add_patient.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):

    if request.method == 'POST':

        full_name = request.form['full_name']
        dob = request.form['dob']
        email = request.form['email']
        glucose = request.form['glucose']
        haemoglobin = request.form['haemoglobin']
        cholesterol = request.form['cholesterol']

        # DOB Validation
        selected_date = date.fromisoformat(dob)

        if selected_date > date.today():
            return "DOB cannot be a future date"

        # Email Validation
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_pattern, email):
            return "Invalid Email Address"

        # Numeric Validation
        try:
            glucose = float(glucose)
            haemoglobin = float(haemoglobin)
            cholesterol = float(cholesterol)
        except:
            return "Glucose, Haemoglobin and Cholesterol must be numeric values"

        remarks = generate_health_remark(
            glucose,
            haemoglobin,
            cholesterol
        )

        sql = """
        UPDATE patients
        SET full_name=%s,
            dob=%s,
            email=%s,
            glucose=%s,
            haemoglobin=%s,
            cholesterol=%s,
            remarks=%s
        WHERE id=%s
        """

        values = (
            full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks,
            id
        )

        cursor.execute(sql, values)
        db.commit()

        return redirect('/')

    cursor.execute(
        "SELECT * FROM patients WHERE id=%s",
        (id,)
    )

    patient = cursor.fetchone()

    return render_template(
        'edit_patient.html',
        patient=patient
    )

@app.route('/delete/<int:id>')
def delete_patient(id):

    cursor.execute(
        "DELETE FROM patients WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)