from flask import Flask

app=Flask(__name__)

@app.route('/hello')
def home():
    return "Hello World"

@app.route('/')
def home2():
    return "Hello home World"


app.run(port=5000)