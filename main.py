from website import create_app
#https://pypi.org/project/Flask-Toastr/



app = create_app()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=6080, debug=True)