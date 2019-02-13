from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:root@localhost:3306/python_projet'
db  = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__="patients"
    patient_id=db.Column(db.Integer, primary_key=True)
    name=db.Column('name',db.String(45))
    age=db.Column(db.Integer)
    area=db.Column('area',db.String(45))
    
    def __init__(self,params):
        # self.patient_id=int(params["patient_id"])
        self.name=params["name"]
        self.age=int(params["age"])
        self.area=params["area"]
        pass    
    
    def __str__(self):
        # return "Id:"+str(self.patient_id)+" Name:"+self.name+" Age:"+str(self.age)+" Area:"+ self.area
        return "Name:"+self.name+" Age:"+str(self.age)+" Area:"+ self.area

def hello_world():
    return 'Flask server is running'

@app.route('/')
def return_template():
    return render_template('home.html')

@app.route('/patient', methods=['GET'])
def register_form():
    if request.method == 'GET':
        return render_template('patients.html')

@app.route('/patient/list', methods=['GET'])
def list_patients():
    if request.method == 'GET':
        pass
        

@app.route('/patient/register', methods=['POST'])
def register_patient():
    if request.method == 'POST':
        # fullrequest = request.form
        new_patient = Patient({"name":request.form.get("name"),
                                "age":int(request.form.get("age")),
                                "area":request.form.get("area")
                                 })
        db.session.add(new_patient)
        db.session.commit()
        return 'inserted'  
        
        

    # if request.method == 'GET':
    #     return render_template('patients.html')        
    # elif request.method == 'POST':
    #     return 'sent post'