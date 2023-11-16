import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mysqlaccount1!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE walnuthillalpines")

print("ALL Done!")