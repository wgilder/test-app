from flask import render_template
from app import app

title = "Puppet PEX"

@app.route('/')
@app.route('/index')
def index():
    page = { 'header': 'Welcome to the Puppet Enterprise Exchange!', 'body': 'We hope you enjoy your day' }
    return render_template('index.html', title=title, page=page)