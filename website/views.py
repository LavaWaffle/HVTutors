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
	else:
		return ('pass')


def addToCart(id, time):
	if ('cart' not in session):
		session['cart'] = []	
	
	session['cart'].append([id, time])


@views.route('/', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		directions = email(request.form.get('fEmail'))
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':
			pass
			
	return render_template("home.html")

@views.route('/about', methods=['GET', 'POST'])
def about():
	if request.method == "POST":
		directions = email(request.form.get('fEmail'))
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':
			pass

	return render_template("about.html")


@views.route('/emailGratification', methods=['GET', 'POST'])
def emailGratification():
	if request.method == "POST":
		directions = email(request.form.get('fEmail'), True)
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':
			pass
			
	return render_template('emailGratification.html')

@views.route('/services', methods=['GET', 'POST'])
def services():
	# gets data
	sheet = getSheet("website/static/serviceData/services.xlsx")
	data = getData(sheet)

	# sends data to html
	flash(data, 'data')

	if request.method == "POST":
		directions = email(request.form.get('fEmail'))
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':
			pass

		id = request.form.get("itemId","")
		time = request.form.get("itemTime")

		addToCart(id, time)
		print(session['cart'])

	return render_template('services.html')

@views.route('/services/<subject>', methods=['GET', 'POST'])
def subject(subject):
	sheet = getSheet("website/static/serviceData/services.xlsx")
	dataa = getData(sheet)

	subject = subject.partition("=")[2]
	finalData = getType(dataa, subject)
	flash(finalData, "data")

	if request.method == "POST":

		fEmail = request.form.get('fEmail')
		if str(type(fEmail)) != "<class 'NoneType'>":
			# you would add email to a database here
			return redirect('/emailGratification')

		id = request.form.get("itemId","")
		time = request.form.get("itemTime")
		
		addToCart(id, time)
		print(session['cart'])
	
	return render_template('services.html')