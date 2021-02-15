import mysql.connector
from mysql.connector.cursor import MySQLCursorNamedTuple

Username = "Username"
Password = "Password"
Host = "Host"
Port = "Port"

mydb = mysql.connector.connect(
    username = Username,
    password = Password,
    host = Host,
    port = Port,
    database = "defaultdb",
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")