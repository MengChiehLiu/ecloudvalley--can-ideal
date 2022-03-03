import os
from random import randint
import pandas as pd
from flask import Flask, abort, request, render_template, redirect, url_for
import mysql.connector 
from flask import jsonify
import configparser
from numpy import quantile
import json
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

def main_function(food,price,calories):
    for pr in range(50):
        p = 0
        # b = calories*defalut_percentage[key][0]
        df_b = food[(food["food_breakfast"]=="Y") | (food["food_breakfast"]=="A")]
        # print(df_b)
        # print(len(df_b))
        df_b = df_b[df_b["calories"]>= quantile(df_b["calories"].tolist(),0.75)]
        # print(len(df_b))
        df_b_1 = df_b.sample().reset_index()
        p += int(df_b_1["price"])
        # print(df_b_1)
        part1 = int(df_b_1["calories"])
        remain = calories - part1
        # print(remain)
        food1 = food[food["restaurant_name"]!= df_b_1["restaurant_name"][0]]
        s=10000
        for times in range(100):
            df_l = food1[food1["food_breakfast"]!="Y"]
            df_d = food1[food1["food_breakfast"]!="Y"]
            df_l_0 = df_l.sample().reset_index()
            df_d = df_d[df_d["restaurant_name"]!= df_l_0["restaurant_name"][0]]
            df_d_0 = df_d.sample().reset_index()
            t = abs(int(df_l_0["calories"])+int(df_d_0["calories"])-remain)
            if t < s:
                s = t
                df_l_1 = df_l_0
                df_d_1 = df_d_0
                part2 = int(df_l_0["calories"])+int(df_d_0["calories"])
        p += int(df_l_1["price"])
        p += int(df_d_1["price"])
        if p < price:
            total_consume=part1+part2
            return df_b_1,df_l_1,df_d_1,total_consume



app = Flask(__name__)


@app.route("/") #根目錄
def home():
    return render_template("home.html")

@app.route("/result", methods=["POST"])
def sendresult():
    # food = pd.read_csv("food.csv")
    # restaurant = pd.read_csv("restaurant.csv")
    query66 = 'SELECT * FROM food;'
    food = pd.read_sql(query66, sysdb)
    query67 = 'SELECT * FROM restaurant'
    restaurant = pd.read_sql(query67, sysdb)
    food = food.merge(restaurant, left_on='restaurant_id', right_on='id')
    types=["japan","korea","china","taiwan","usa","thai","southeast"]
    prefs=[]
    for type in types:
        try:
            prefs.append(request.form.get(type))
        except:
            pass
    table = zip(types,prefs)
    calories = request.form.get("calories")
    price = request.form.get("price")
    options = request.form.get("options") 
    a,b,c,total_consume = main_function(food,int(price),int(calories))
    # my_list = a.columns.values.tolist()
    a1=a["restaurant_name"][0]
    a_name = a["restaurant_name"][0]
    a_f_name = a["food_name"][0]
    a_calories = a["calories"][0]
    a_price = a["price"][0]
    b_name = b["restaurant_name"][0]
    b_f_name = b["food_name"][0]
    b_calories = b["calories"][0]
    b_price = b["price"][0]
    c_name = c["restaurant_name"][0]
    c_f_name = c["food_name"][0]
    c_calories = c["calories"][0]
    c_price = c["price"][0]
    a_pic = a["img_url"][0]
    b_pic = b["img_url"][0]
    c_pic = c["img_url"][0]
    a_web = a["info_url"][0]
    b_web = b["info_url"][0]
    c_web = c["info_url"][0]

    return render_template("result.html",calories=calories,price=price,options=options,table=table,
    total_consume=total_consume,
    a_name=a_name,b_name=b_name,c_name=c_name,a_f_name=a_f_name,
    b_f_name=b_f_name,c_f_name=c_f_name,
    a_calories=a_calories,b_calories=b_calories,c_calories=c_calories,
    a_price=a_price,b_price=b_price,c_price=c_price,
    a_pic=a_pic,b_pic=b_pic,c_pic=c_pic,
    a_web=a_web,b_web=b_web,c_web=c_web)

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


if __name__=="__main__":
    app.run(debug=True)