#integrate html with flask (jinja2)

'''
integrate html with flask 
http verb get and post 
'''

''''
redirect() function is used to redirect the user to the specific URL--dynamic URL
url_for() routes to this url at redirect
render_template() function is used to render the html file in flask
'''

from flask import Flask,redirect,url_for, render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/buyhouse/<int:total_price>')
def buy_house(total_price):
    # return 'The price of the house is ' +str(total_price) + ' You can buy the house'
    return render_template('taking_home.html', total_price = total_price)

@app.route('/notbuyhouse/<int:total_price>')
def not_buy_house(total_price):
    return 'The price of the house is ' +str(total_price) + ' You can not buy the house'

# @ app.route('/checkfesible/<int:rent>')  # dynamic URL , varaible rules for float
# def check_rent(rent):
#     if rent > 1000:
#         result = 'not_buy_house'
#     else:
#         result ='buy_house'
#     return redirect(url_for(result, total_price = rent))

@app.route('/submit', methods = ['POST','GET'])
def submit():
    taking_home = 0
    if request.method == 'POST':
        rent = request.form['rent']
        amenitiesCost = request.form['amenitiesCost']
        pool = request.form['pool']
        bedrooms = request.form['bedrooms']
        taking_home = int(rent) - int(amenitiesCost)
    res = " "
    if taking_home > 1000:
        res = 'not_buy_house'
    else:
        res ='buy_house'
    return redirect(url_for(res, total_price = taking_home))
 
if __name__ == '__main__':
    app.run(port=5001 , debug = True ) # runs the application on the development server