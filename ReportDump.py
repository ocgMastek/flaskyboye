from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import jsonpickle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:root@localhost:3306/python_projet'
db  = SQLAlchemy(app)

class Report(db.Model):
    __tablename__="reports"
    report_id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(200))
    date=db.Column(db.String(10))
    
    def __init__(self,params):
        self.report_id=params["report_id"]
        self.date=params["date"]
        self.description=params["description"]
        pass    
    
    def __str__(self):
        return "Id:"+str(self.report_id)+" Description:"+self.description+" Date:"+self.date

class ReportManager(object):
    """Class to define db call functions"""
    
    @staticmethod
    def get_all_reports():
        pass
    
    @staticmethod
    def get_report_by_id():
        pass
    
    @staticmethod
    def add_report():
        pass
    
    @staticmethod
    def update_report():
        pass
    
    @staticmethod
    def delete_report():
        pass