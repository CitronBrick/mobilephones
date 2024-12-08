from flask import Flask,request,redirect,url_for, render_template,flash, get_flashed_messages
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'wlerj2i3j4525j#@#@$'


class Mobile:

	def __init__(self, name, price, freq, ram, mem):
		self.name = name
		self.price = price
		self.freq = freq
		self.ram = ram 
		self.mem = mem


mobile_list = [
	Mobile( "Pixel", 15, 20, 16, 64),
	Mobile( "Redmi", 19,  25, 8, 32),
	Mobile( "A3", 500, 36, 32,128)
]


@app.route("/")
def hello_world():
	return "<h1>Hello World</h1>"


@app.route("/name/<name>")
def hello(name):
	return f"<h1>{name} Bonjour</h1>"

@app.route("/voiture")
def voiture():
	return dict({"wheels":4, "seats": 4, "color":"red"})

@app.route("/mobiles")
def mobiles():
	return render_template('mobiles.html',mobiles=mobile_list)

@app.route("/mobile/<name>")
def mobile(name):
	mobile = None
	for m in mobile_list:
		if m.name == name:
			mobile = m
	return render_template('mobile.html',mobile=mobile)


@app.route("/login", methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['nom'] 
		if username  and request.form['pwd']:
			return redirect(url_for("hello",name=username))
		else:
			flash('login error using ' + username)
			return render_template('login.html')
	else:
		return render_template('login.html')