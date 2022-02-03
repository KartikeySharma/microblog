from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user= {'username':'Kartikey'}
	posts= [
		{
			'author': {'username':'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username':'Kartikey'},
			'body': 'Raining in New Delhi!'
		},
		{
			'author': {'username':'Bob'},
			'body': 'Gonna sleep :)'
		}	
	]
	return render_template('index.html',title='Home',user=user,posts=posts)
