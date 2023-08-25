from flask import Flask
import futbolPeruano

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to API</p>"
@app.route("/api/v1/")
def dataTable():
    return { 'teams': futbolPeruano.getAllTablePositions() }