'''
Building dynamic URL in Flask
variable rules and URL building
'''

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask API! created by anuhya'

@app.route('/houserent/<int:total_rent>')  # dynamic URL , varaible rules for int 
def house_rent(total_rent):
    return 'The rent of the house is %d' % total_rent



@ app.route('/checkfesible/<int:rent>')  # dynamic URL , varaible rules for float
def check_rent(rent):
    if rent > 1000:
        result = 'The rent is not that good to pay'
    else:
        result ='The rent is feasible to pay'
    return redirect(url_for('house_rent', total_rent = rent))


if __name__ == '__main__':
    app.run(port=5001 , debug = True ) # runs the application on the development server