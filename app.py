from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Nikhil Bhalala\'s HW3'

