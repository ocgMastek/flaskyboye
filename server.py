from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import jsonpickle

app = Flask(__name__)

def hello_world():
    return 'Flask server is running'

@app.route('/template')
def return_template():
    return render_template('home.html')

@app.route('/patient', methods=['GET'])
def register_form():
    if request.method == 'GET':
        return render_template('patients.html')

@app.route('/patient/register', methods=['POST'])
def register_patient():
    if request.method == 'POST':
        # fullrequest = request.form
        patient = ({"patient_id":int(request.form.get("patient_id")),
                    "name":request.form.get("name"),
                    "age":int(request.form.get("age")),
                    "area":request.form.get("area")
                    })
                    
        return jsonpickle.encode(patient)
        

    # if request.method == 'GET':
    #     return render_template('patients.html')        
    # elif request.method == 'POST':
    #     return 'sent post'