from flask import render_template
from app_entry import entry_point as ep

title = "Puppet Pipelines"

@ep.route('/')
@ep.route('/index')
def index():
    page = { 'header': 'Welcome', 'body': 'We hope you enjoy your day' }
    return render_template('index.html', title=title, page=page)
