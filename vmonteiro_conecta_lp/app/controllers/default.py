from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db#, lm

from app.models.tables import Lead, User
from app.models.forms import LeadForm#, LoginForm

#@lm.user_loader
#def load_user(id):
#	return User.query.filter_by(id=id).first()

@app.route("/index", methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
def index():
	leadform = LeadForm()
	print(leadform.name.data)
	print(leadform.telnumber.data)
	print(leadform.email.data)
	l = Lead(leadform.name.data, leadform.telnumber.data, leadform.email.data)
	db.session.add(l)
	db.session.commit()
	return render_template('index.html',leadform=leadform)

@app.route("/obrigado")
def thanks():
	return render_template('thanks.html')
"""#Bloco de login e logout
#@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		print(user.password)
		print(form.password.data)
		if user and user.password == form.password.data:
			login_user(user)
			return redirect(url_for("index")) #index é nome da função e não o caminho
			flash("Logged in.")
		else:
			flash("Invalid Login.")
	else:
		print(form.errors)
	return render_template('login.html',form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("index"))

"""
#Bloco para teste
"""
@app.route("/add")
def add():
	i = User("teste filho","1234","Tester da Silva Filho","teste.filho@teste.com")
	db.session.add(i)
	db.session.commit()
	print(i)
	return "Add"

@app.route("/sel")
def sel():
	r = User.query.filter_by(username="theomont").first()
	print(r)
	return "Select"

@app.route("/del")
def delete():
	r = User.query.filter_by(username="teste").first()
	print(r)
	db.session.delete(r)
	db.session.commit()
	return "Delete"
"""
