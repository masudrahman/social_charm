import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/rate_others')
def rate():
	return render_template('rate_others.html')

@app.route('/feature_list')
def feature_list():
	return render_template('feature_list.html')

@app.route('/result')
def result():
	return render_template('result.html')

@app.route('/invite')
def invite():
	return render_template('invite.html')

if __name__ == '__main__':
     app.debug = True
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)