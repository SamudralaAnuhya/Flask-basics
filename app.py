from flask import Flask
 # creates WSGI application (common interface between web servers and web applications)
app = Flask(__name__)


#decorator to route the URL to the function
@app.route('/')
def welcome():
    return 'Welcome to the Flask API! created by anuhya samudrla'

@app.route('/anuhya')
def family():
    return 'Welcome to my family'



if __name__ == '__main__':
    app.run(port=5001  ) # runs the application on the development server