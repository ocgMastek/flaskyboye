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
        reports = Report.query.all()
        print("get_all_reports() Result:")
        print(reports)
        return reports
    
    @staticmethod
    def get_report_by_id(id):
        report = Report.query.get(id)
        print("get_report_by_id(id) result")
        print(report)
        return report
    
    @staticmethod
    def add_report(new_report):
        db.session.add(new_report)
        db.session.commit()
        return new_report
    
    @staticmethod
    def update_report(id, edit):
        pass
    
    @staticmethod
    def delete_report():
        pass
    
if __name__ == '__main__':
    db.create_all()
    ReportManager.get_report_by_id(1)
    #ReportManager.add_report(Report({"report_id":2, "date":"10/10/1996", "description":"Some Description"}))
    ReportManager.get_report_by_id(1)
    ReportManager.get_all_reports()
    app.run()