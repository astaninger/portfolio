from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', ip=request.remote_addr)

@app.route('/projects', methods=["GET"])
def projects():
    pass #return render_template('projects.html')

@app.route('/resume')
def resume():
    pass #return render_template('resume.pdf')
