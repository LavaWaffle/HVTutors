# imports flask
from flask import Flask, render_template
# imports toastr
from flask_toastr import Toastr

# creates toastr object
toastr = Toastr()

# 404 page error handler
def pageNotFound(e):
	return render_template('404.html'), 404

def create_app():
	app = Flask(__name__)
	# encrypts cookies and other website things so it should never be told to anyone
	app.config['SECRET_KEY'] = '1290j90-jvxpo403n9f0sjs0432qsdfdsfdsj;lkdfuj89p34h;ilshdf9p80vh34;zhc90'
	
	# gets all pages from views
	from .views import views
	# registers each page with its url prefix
	app.register_blueprint(views, url_prefix='/')

	# initializes toastr 
	toastr.init_app(app)

	# explains to flask what to display for 404 page errors
	app.register_error_handler(404, pageNotFound)

	# returns the app to main.py
	return app