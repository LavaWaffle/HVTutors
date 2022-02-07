from flask import Blueprint, render_template, request, flash, url_for,  redirect, session


# defines that this file will contain blue prints
views = Blueprint('views', __name__)

def email(fEmail, onEmail=False):
	if onEmail:
		return ('flash', ("You already signed up for the email list", "info"))
	else:
		if str(type(fEmail)) != "<class 'NoneType'>":
			# Email would be added to a database here
			return ('redirect', "/emailGratification")

@views.route('/', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		directions = email(request.form.get('fEmail'))
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
			
	return render_template("home.html")

@views.route('/about', methods=['GET', 'POST'])
def about():
	return render_template("about.html")


@views.route('/emailGratification')
def emailGratification():
	return render_template('emailGratification.html')

