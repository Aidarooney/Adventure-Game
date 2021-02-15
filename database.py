import mysql.connector
from mysql.connector.cursor import MySQLCursorNamedTuple

Username = "Username"
Password = "Password"

mydb = mysql.connector.connect(
    username = Username,
    password = Password,
    host = "db-mysql-lon1-55425-do-user-8454104-0.b.db.ondigitalocean.com",
    port = "25060",
    database = "defaultdb",
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")