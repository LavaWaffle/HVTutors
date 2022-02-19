# imports create_app func website folder
from website import create_app
#https://pypi.org/project/Flask-Toastr/

# creates an app using create_app func
app = create_app()

# if this file is the main file, run the app
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)