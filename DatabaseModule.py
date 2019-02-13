from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:root@localhost:3306/python_projet'
db  = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__="patients"
    patient_id=db.Column(db.Integer, primary_key=True)
    name=db.Column('name',db.String(45))
    age=db.Column(db.Integer)
    area=db.Column('area',db.String(45))
    
    def __init__(self,params):
        self.name=params["name"]
        self.age=params["age"]
        self.area=params["area"]
        pass
    
    def __str__(self):
        return "Patient_id:"+str(self.patient_id)+" Name:"+self.name+" Age:"+str(self.age)+" Area:"+str(self.area)


@app.route("/patient-example")    
def example_Patient():
    p=Patient({"name":"New Patient","age":50,"area":"Leeds"})
   
    db.session.add(p)
    db.session.commit()
    patients=Patient.query.all()
    for p in patients:
        print("Patient_id: ",p.patient_id," Name:",p.name," Age:",p.age," Area:",p.age)
        
    return str(patients)


if __name__ == '__main__':
    db.create_all() #create the schema using the alchemy content
    example_Patient()
    app.run(port=7700)
    pass