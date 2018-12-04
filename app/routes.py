from flask import render_template
from app import app

title = "Puppet Pipelines"

@app.route('/')
@app.route('/index')
def index():
    page = { 'header': 'Welcome to the DevOppsCon in Munich!!', 'body': 'We hope you enjoy your day' }
    return render_template('index.html', title=title, page=page)
