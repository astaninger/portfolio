from flask import Flask, render_template, request, jsonify, url_for, send_file
from flask_bootstrap import Bootstrap
from os import chdir

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', ip=request.remote_addr)

@app.route('/projects', methods=["GET"])
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return send_file('static/alex_resume_site.pdf')
