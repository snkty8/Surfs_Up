from flask import Flask

#Create instance
app = Flask(__name__)

#Create route
@app.route('/')
def hello_world():
    return 'Hello world'


