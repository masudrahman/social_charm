import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


#from flaskext.mysql import MySQL
 
"""mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'social_charm'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)"""
app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/rate_others')
def rate():
	return render_template('rate_others.html')

@app.route('/rate_others_1')
def rate1():
	return render_template('rate_others_1.html')

@app.route('/rate_others_2')
def rate2():
	return render_template('rate_others_2.html')

@app.route('/rate_others_3')
def rate3():
	return render_template('rate_others_3.html')

@app.route('/rate_others_4')
def rate4():
	return render_template('rate_others_4.html')

@app.route('/rate_others_5')
def rate5():
	return render_template('rate_others_5.html')


@app.route('/save_picture_value', methods=['POST'])
def save_picture_value():
	picture = Picture('https://s3-us-west-1.amazonaws.com/socialcharm-assets/1.jpg')
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