from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask server is running'

@app.route('/template')
def return_template():
    return render_template('home.html')
    
@app.route('/register', methods=['POST'])
def register_patient():
    if request.method == "POST":
        return 'POST'