import mysql.connector
# import pymysql
# pymysql.connect('can-ideal-db.c8a0ipggxbw5.us-west-2.rds.amazonaws.com',)
sysdb = mysql.connector.connect(
    host = 'can-ideal-db.c8a0ipggxbw5.us-west-2.rds.amazonaws.com',
    user = 'rick',
    password = 'yayuan0215'
)

mycursor = sysdb.cursor()

query1 = "DROP DATABASE IF EXISTS can_ideal;"
query2 = "CREATE DATABASE IF NOT EXISTS can_ideal;"
query3 = "USE can_ideal;"
query4 = "DROP TABLE IF EXISTS restaurant;"
query5 = '''
        CREATE TABLE IF NOT EXISTS restaurant(
            id INT NOT NULL AUTO_INCREMENT,
            restaurant_name VARCHAR(99) NOT NULL,
            breakfast CHAR(1) NOT NULL,
            restaurant_type VARCHAR(99),
            address VARCHAR(99) NOT NULL,
            PRIMARY KEY (id)
        );
'''
query6 = "DROP TABLE IF EXISTS food;"
query7 = '''
        CREATE TABLE IF NOT EXISTS food(
            id INT NOT NULL AUTO_INCREMENT,
            restaurant_id INT NOT NULL,
            food_name VARCHAR(99) NOT NULL,
            calories INT NOT NULL,
            food_type VARCHAR(99) NOT NULL,
            food_breakfast CHAR(1),
            price INT NOT NULL,
            PRIMARY KEY (id),
            FOREIGN KEY (restaurant_id) REFERENCES restaurant(id)
        );
'''

mycursor.execute(query1)
mycursor.execute(query2)
mycursor.execute(query3)
mycursor.execute(query4)
mycursor.execute(query5)
mycursor.execute(query6)
mycursor.execute(query7)
