from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    pass #return render_template('projects.html')

@app.route('/resume')
def resume():
    pass #return render_template('resume.pdf')