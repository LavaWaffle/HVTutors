from flask import Blueprint, render_template, request, flash, url_for,  redirect, session
from .xlsxRead import getSheet, getData, getType, getFront 

# defines that this file will contain blue prints
views = Blueprint('views', __name__)

# checks email and redirects user to the proper page
def email(fEmail, onEmail=False):
	# checks if post method is for fEmail
	if str(type(fEmail)) != "<class 'NoneType'>":
		# if user is already on email page, tell them so
		if onEmail:
			return ('flash', ("You already signed up for the email list.", "info"))
		# if the user is not, redirect them
		else:
			# Email would be added to a database here
			return ('redirect', "/emailGratification")
	else:
		return ('pass')

# adds an item to cart in a list
def addToCart(id, time):
	# checks if user has made a cart list, if not it makes a cart lis
	if ('cart' not in session):
		session['cart'] = []	
	# adds item to cart
	session['cart'].append([id, time])

# resets cart 
def resetCart():
	# sets cartlist to a list of length 0
	session['cart'] = []

# home page route
@views.route('/', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		# gets email form data
		directions = email(request.form.get('fEmail'))
		# redirects/sends user depending on return from email func
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':
			pass
			
	# sends user the page
	return render_template("home.html")

# about page route
@views.route('/about', methods=['GET', 'POST'])
def about():
	if request.method == "POST":
		# gets email form data
		directions = email(request.form.get('fEmail'))
		# redirects/sends user depending on return from email func
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':
			pass
	# sends user the page
	return render_template("about.html")

# emailGratification page route
@views.route('/emailGratification', methods=['GET', 'POST'])
def emailGratification():
	if request.method == "POST":
		# gets email form data
		directions = email(request.form.get('fEmail'), True)
		# redirects/sends user depending on return from email func
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':
			pass
			
	# sends user the page
	return render_template('emailGratification.html')

# services page route
@views.route('/services', methods=['GET', 'POST'])
def services():
	if request.method == "POST":
		# gets email form data
		directions = email(request.form.get('fEmail'))
		# redirects/sends user depending on return from email func
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':
			pass

		# gets what item user bought
		id = request.form.get("itemId","")
		# gets what time the user entered
		time = request.form.get("itemTime")
		# adds item to cart
		addToCart(id, time)

	# gets sheet from xlsx
	sheet = getSheet("website/static/serviceData/services.xlsx")
	# gets data from xlsx
	data = getData(sheet)
	# sends user the services
	flash(data, 'data')

	# sends user the page
	return render_template('services.html')

# service sub-page route
@views.route('/services/<subject>', methods=['GET', 'POST'])
def subject(subject):
	if request.method == "POST":
		# gets email form data
		directions = email(request.form.get('fEmail'))
		# redirects/sends user depending on return from email func
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':
			pass
			
		# gets what item user bought
		id = request.form.get("itemId","")
		# gets what time the user entered
		time = request.form.get("itemTime")
		# adds item to cart
		addToCart(id, time)
			
	# gets sheet from xlsx
	sheet = getSheet("website/static/serviceData/services.xlsx")
	# gets data from sheet
	data = getData(sheet)

	# gets subpage from url parameter
	subject = subject.partition("=")[2]
	# gets specific data for the subject
	finalData = getType(data, subject)
	# sends user services
	flash(finalData, "data")

	# sends user the page
	return render_template('services.html')

# cart page route
@views.route('/cart', methods=['GET', 'POST'])
def cart():
	if request.method == "POST":         
		# gets email form data
		directions = email(request.form.get('fEmail'))
		# redirects/sends user depending on return from email func
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':	
			pass
			
		# gets checkout data
		checkOut = (request.form.get('checkOut',''))
		# if user clicked checkout button
		if checkOut.lower() == 'checkout':
			# check if user has a cart
			try:
				# if user has a cart, redirect them to checkout
				if len(session['cart']) > 0:
					return redirect('/checkout')
				# if user doesn't have a cart, tell them they do not
				else:
					flash("You don't have any items in your cart. Come back when you do!","info")
			except KeyError:
				flash("You don't have any items in your cart. Come back when you do!","info")
				
	# gets sheet from xlsx
	sheet = getSheet("website/static/serviceData/services.xlsx")
	# gets data from sheet
	data = getData(sheet)

	# sends user their cart				
	try:
		frontEnd = getFront(data, session['cart'])
		flash(frontEnd[0],"cart")
		flash(frontEnd[1], "sum")
	except Exception:
		pass
		
	# sends user the page
	return render_template('cart.html')
		
# checkout page route
@views.route('/checkout', methods=['GET', 'POST'])
def checkout():
	if request.method == "POST":   
		# gets email form data
		directions = email(request.form.get('fEmail'))
		# redirects/sends user depending on return from email func
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':	
			pass
		
		# gets name data
		firstName = request.form.get('firstName')
		middleName = request.form.get('middleName')
		lastName = request.form.get('lastName')

		# if no name is given
		# gets email data
		fEmail = request.form.get('email')

		# gets location data
		locOption = request.form.get('location') # MCL vs custom
		address = request.form.get('address')

		# gets payment data  
		payment = request.form.get('payment')
		if payment == 'Credit/Debit':
			payment = 'credit'
		else:
			payment = 'paypal'

		# check if user entered data is valid
		# checks if user entered a name
		if len(firstName) == 0 and len(middleName) == 0 and len(lastName) == 0:
			flash('Please enter your name in one of the name boxes', 'error')
		# checks if user entered an email
		elif len(fEmail) == 0:
			flash('Please enter your email in the email box', 'error')
		# checks if user entered a location
		elif locOption == 'custom' and len(address) == 0:
			flash('Please enter your custom location address in the custom location box', 'error')
		# redirects user to the finialize page if they passed all the checks
		else: 
			return redirect(f'/finalizecheckout/paytype={payment}')
	
	# sends user the page
	return render_template('checkout.html')

# finalizecheckout page route
@views.route('/finalizecheckout/<paytype>', methods=['GET', 'POST'])
def finalizecheckout(paytype):
	if request.method == "POST":
		# gets email form data
		directions = email(request.form.get('fEmail'))
		# redirects/sends user depending on return from email func
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':	
			pass
		###### You would get data from form here and send to a db
		return redirect('/checkoutgratification')

	# gets sheet from xlsx
	sheet = getSheet("website/static/serviceData/services.xlsx")
	# gets data from sheet
	data = getData(sheet)

	# sends user their cart
	try:
		frontEnd = getFront(data, session['cart'])
		flash(frontEnd[0],"cart")
		flash(frontEnd[1], "sum")
	except Exception:
		pass

	# gets paytype through parameter in url
	paytype = paytype.partition("=")[2]
	if paytype == 'credit':
		flash(paytype, 'paytype')
	else:
		flash(paytype, 'paytype')

	# sends user the html
	return render_template('finalizeCheckout.html')

# checkout gratification route
@views.route('/checkoutgratification', methods=['GET', 'POST'])
def checkoutgratification():
	if request.method == "POST":         
		directions = email(request.form.get('fEmail'))
		if directions[0] == 'flash':
			flash(directions[1][0], directions[1][1])
		elif directions[0] == 'redirect':
			return redirect(directions[1])
		elif directions[0] == 'pass':	
			pass
	return render_template('checkoutGratification.html')