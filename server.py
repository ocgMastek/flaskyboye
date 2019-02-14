from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import jsonpickle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:root@localhost:3306/python_projet'
db  = SQLAlchemy(app)

class patient_report(db.Model):
    __tablename__="patient_reports"
    report_id=db.Column(db.Integer, primary_key=True)
    report_text=db.Column(db.String(250))
    
    patient_id=db.Column(db.Integer, db.ForeignKey("patients.patient_id"), nullable=False)

    def __init__(self,params):
        self.report_text=params["report_text"]
        pass

    def __str__(self):
        return "Report"

class Patient(db.Model):
    __tablename__="patients"
    patient_id=db.Column(db.Integer, primary_key=True)
    name=db.Column('name',db.String(45))
    age=db.Column(db.Integer)
    area=db.Column('area',db.String(45))
    gender=db.Column('gender',db.String(10))
    dob=db.Column('dob',db.String(10))
    
    reports = db.relationship("patient_report", backref=db.backref("patient", lazy=True))
    
    def __init__(self,params):
        #self.patient_id=int(params["patient_id"])
        self.name=params["name"]
        self.age=int(params["age"])
        self.area=params["area"]
        self.gender=params["gender"]
        self.dob=params["dob"]
        pass    
    
    def __str__(self):
        #return "Id:"+str(self.patient_id)+" Name:"+self.name+" Age:"+str(self.age)+" Area:"+ self.area
        return "Name: "+self.name+" Age: "+str(self.age)+" Area: "+ self.area + " Gender: " + self.gender + " dob: " + self.dob


@app.route('/')
def return_template():
    
    return render_template('home.html',result=Patient.query.all())

@app.route('/patient', methods=['GET'])
def register_form():
    if request.method == 'GET':
        return render_template('patients.html')
    
@app.route('/lab-manager', methods=['GET'])
def lab_manager():
    if request.method == 'GET':
        return render_template('lab-manager.html',patients=Patient.query.all(),reports=patient_report.query.all())
        
@app.route('/patient/report', methods=['GET'])
def make_report():
    if request.method == 'GET':
        return render_template('record.html')


@app.route('/patient/savereport', methods=['POST'])
def save_report():
    if request.method == "POST":
        new_report = patient_report({"report_text":request.form.get("report_text")})
        #print(new_report)
        patient_id = request.form.get("patient_id")
        patient = Patient.query.filter_by(patient_id=patient_id).first()
        patient.reports.append(new_report)
        #db.session.add(patient)
        db.session.add(new_report)
        db.session.commit()
    return redirect('/patient/report')
    #return render_template('record.html')


@app.route('/patient/register', methods=['POST'])
def register_patient():
    if request.method == 'POST':
        #fullrequest = request.form
        new_patient = Patient({"name":request.form.get("name"),
                                "age":int(request.form.get("age")),
                                "area":request.form.get("area"),
                                "gender":request.form.get("gender"),
                                "dob":request.form.get("dob")
                                 })
        print(new_patient)
        db.session.add(new_patient)
        db.session.commit()
        return redirect("/patient")
    
@app.route('/lab-manager/delete', methods=['POST'])
def delete_patient():
    patient_id = request.form.get("patient_id")
    patient = Patient.query.filter_by(patient_id=patient_id).first()
    print(patient.patient_id)
    db.session.delete(patient)
    db.session.commit()
    return redirect("/lab-manager")

@app.route('/lab-manager/delete-report', methods=['POST'])
def delete_report():
    report_id = request.form.get("report_id")
    report = patient_report.query.filter_by(report_id=report_id).first()
    patient_id = report["patient_id"] #Error happening here
    patient = Patient.query.filter_by(patient_id=patient_id).first()
    patient.reports.remove(report)
    db.session.delete(report)
    db.session.add(patient)
    db.session.commit()
    return redirect("/lab-manager")
    