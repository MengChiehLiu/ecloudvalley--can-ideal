import mysql.connector
import pandas

#connect to the database
sysdb = mysql.connector.connect(
    host = 'can-ideal-db.c8a0ipggxbw5.us-west-2.rds.amazonaws.com',
    user = 'rick',
    password = 'yayuan0215',
    database = 'can_ideal'
)

mycursor = sysdb.cursor()

# Extract data from restaurant.csv
result_r = pandas.read_csv("restaurant.csv", encoding="big5")
restaurant_name = list(result_r["restaurant_name"])
breakfast= list(result_r["breakfast"])
restaurant_type = list(result_r["restaurant_type"])
address = list(result_r["address"])
for i,j,k,l in zip(restaurant_name,breakfast,restaurant_type,address):
    restaurant_name = i
    breakfast = j
    restaurant_type = k
    address = l
    #insert into restaurant table
    
    query15 = '''
            INSERT INTO restaurant(restaurant_name, breakfast, restaurant_type, address)
            VALUES(%s,%s,%s,%s)
    '''
    mycursor.execute(query15, (restaurant_name, breakfast, restaurant_type, address))
    sysdb.commit()

result_f = pandas.read_csv("food.csv", encoding="big5")
restaurant_id = list(result_f["restaurant_id"])
food_name = list(result_f["food_name"])
calories = list(result_f["calories"])
food_type = list(result_f["food_type"])
price = list(result_f["price"])
food_breakfast = list(result_f["food_breakfast"])
for i,j,k,l,m,n in zip(restaurant_id,food_name,calories,food_type,price,food_breakfast):
    restaurant_id = i
    food_name = j
    calories = k
    food_type = l
    price = m
    food_breakfast = n
    #insert into food table
    
    query16 = '''
            INSERT INTO food(restaurant_id, food_name, calories, food_type, price, food_breakfast)
            VALUES(%s,%s,%s,%s,%s,%s)
    '''
    mycursor.execute(query16, (restaurant_id, food_name, calories, food_type, price, food_breakfast))
    sysdb.commit()
