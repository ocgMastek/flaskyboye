import flask
import sqlalchemy


app = flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:root@localhost:3306/python_projet'
db  = sqlalchemy(app)

class Patient(db.Model):
    __tablename__="patients"
    patient_id=db.Column(db.Integer, primary_key=True)
    name=db.Column('name',db.String(45))
    age=db.Column(db.Integer)
    area=db.Column('area',db.String(45))
    
    def __init__(self,params):
        self.name=params["name"]
        self.age=params["age"]
        self.age=params["area"]
        pass
    
    def __str__(self):
        return "Id:"+str(self.patient_id)+" Name:"+self.name+" Age:"+str(self.age)+" Area:"


if __name__ == '__main__':
    db.create_all() #create the schema using the alchemy content
    # #example_Patient()
    # app.run(port=7700)
    # pass