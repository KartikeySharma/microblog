from app import app

@app.route('/')
@app.route('/index')
@app.route('/helloworld')
def index():
	return "Hello World!"
