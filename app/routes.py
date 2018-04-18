from app import app

@app.route('/')
@app.rout('/index')
def index():
    return "Hello World!"
