import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Password1234!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE TheIridescentMarket")

print('All Done')