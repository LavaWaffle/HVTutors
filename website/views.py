from flask import Blueprint, render_template, request, flash, url_for,  redirect, session
from .xlsxRead import getSheet, getData, getType, getFront 

# defines that this file will contain blue prints
views = Blueprint('views', __name__)

def email(fEmail, onEmail=False):
	# checks if post method is for fEmail
	if str(type(fEmail)) != "<class 'NoneType'>":
		if onEmail:
			return ('flash', ("You already signed up for the email list", "info"))
		else:
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
	if request.method == "POST":
		directions = email(request.form.get('fEmail'))
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])

	return render_template("about.html")


@views.route('/emailGratification', methods=['GET', 'POST'])
def emailGratification():
	if request.method == "POST":
		directions = email(request.form.get('fEmail'), True)
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
			
	return render_template('emailGratification.html')

@views.route('/services')
def services():
	sheet = getSheet("website/static/serviceData/services.xlsx")
	data = getData(sheet)

	flash(data, 'data')

	return render_template('services.html')

