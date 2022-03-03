import os
from random import randint
import pandas as pd
from flask import Flask, abort, request, render_template, redirect, url_for
import json
import mysql.connector 
from flask import jsonify
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

#connect to the database
sysdb = mysql.connector.connect(
    host = config['mysql']['host'],
    user = config['mysql']['user'],
    password = config['mysql']['password'],
    database = config['mysql']['database']
)
mycursor = sysdb.cursor()

#check db connection
def db_connection_check():
    if sysdb.is_connected() == False:
        sysdb.connect()
app = Flask(__name__)


@app.route("/") #根目錄
def home():
    return render_template("home.html")

@app.route("/result", methods=["POST"])
def sendresult():
    types=["japan","korea","china","taiwan","usa","thai","southeast"]
    prefs=[]
    for type in types:
        try:
            prefs.append(request.form.get(type))
        except:
            pass
    calories = request.form.get("calories")
    price = request.form.get("price")
    options = request.form.get("options") 
    return render_template("result.html", calories=calories, prefs=prefs,price=price,options=options)

@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route('/getNameRest', methods=['GET'])
def name_rest():
	print(request.args)
	name_restaurant=request.args.get('name_restaurant')
	print(name_restaurant)
	return render_template('maps.html',name_restaurant = json.dumps(name_restaurant))

# APIs
@app.route("/api/food")

def get_food():
	query66 = 'SELECT * FROM food;'
	mycursor.execute(query66)
	results = mycursor.fetchall()
	data = []
	for result in results:
		data.append(
			{
				"id": result[0],
				"restaurant_id": result[1],
				"food_name": result[2],
				"calories": result[3],
				"food_type": result[4],
				"food_breakfast": result[5],
				"price" : result[6],
			}
		)
	return jsonify(data)

# @app.route("/api/restaurant")
@app.route("/api/restaurant")

def get_restaurant():
	query67 = 'SELECT * FROM restaurant'
	mycursor.execute(query67)
	results1 = mycursor.fetchall()

	data1 = []
	for result1 in results1:
		data1.append(
			{
				"id": result1[0],
				"restaurant_name": result1[1],
				"breakfast": result1[2],
				"restaurant_type":result1[3],
				"address":result1[4],
				"latitude":result1[5],
				"longitude":result1[6],
			}
		)
	return jsonify(data1)

if __name__=="__main__":
    # app.run()
    app.run(host='0.0.0.0', port=80)
