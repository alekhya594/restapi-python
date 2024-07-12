from flask import Flask
app = Flask(__name__)
@app.route("/")
def welcome():
    return "this is my first app  program"

@app.route("/home")
def home():
    return "this is  home  my frist page"


from controller import *