import flask
from flask import request, jsonify
import student_generator

app = flask.Flask(__name__)

def function():
    data_file = open("file.txt" , "r")

app.config["DEBUG"] = True

student_dictioanries = student_generator.get_student_dictionaries()

@app.route('/', methods=['GET'])
def index():
    return "<h1> My name is Halil Keles</h1>"

@app.route('/api/students/all', methods=['GET'])

def api_all():
    return jsonify

app.run()

