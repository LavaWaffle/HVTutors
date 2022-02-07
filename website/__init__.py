from flask import Flask
# imports toastr
from flask_toastr import Toastr

toastr = Toastr()
GLOBAL_ID = 0

def create_app():
	app = Flask(__name__)
	# encrypts cookies and other website things so it should never be told to anyone
	app.config['SECRET_KEY'] = '1290j90-jvxpo403n9f0sjs0432qsdfdsfdsj;lkdfuj89p34h;ilshdf9p80vh34;zhc90'
	
	# gets all pages from views
	from .views import views
	# registers each page with its url prefix
	app.register_blueprint(views, url_prefix='/')

	# config toast features | DELETE THIS L8R
	# app.config['TOASTR_HIDE_EASING'] = 'swing'
	# initialize toastr on the app within create_app()
	toastr.init_app(app)

	# returns the app to main.py
	return app