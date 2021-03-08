import time
import sys
import mysql.connector
from mysql.connector.cursor import MySQLCursorNamedTuple
class bcolors:
    green= '\033[92m'
    ENDC = '\033[0m'

def terminal(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.04)
        else:
            time.sleep(0.02)

        
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  return("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),round(float(sec), 2)))


def walking():
    print("You start walking, you will arrive in:\n")
    print("5\n")
    time.sleep(1)
    print("4\n")
    time.sleep(1)
    print("3\n")
    time.sleep(1)
    print("2\n")
    time.sleep(1)
    print("1\n")
    time.sleep(1)

def loading():
    items = list(range(0, 57))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

        
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def ending(username):
    print("Thank you for playing my game!")
    username = input("Please enter a username:\n")

def leaderboard():
    login = "username"
    Password = "password"
    Host = "host"
    Port = "port"

    mydb = mysql.connector.connect(
        username = login,
        password = Password,
        host = Host,
        port = Port,
        database = "Leaderboard",
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Leaderboard ORDER BY Time asc LIMIT 5")
    result = mycursor.fetchall()

    for row in result: 
        print(row) 

def score(username, timeTaken, today):
    login = "username"
    Password = "password"
    Host = "host"
    Port = "port"

    mydb = mysql.connector.connect(
        username = login,
        password = Password,
        host = Host,
        port = Port,
        database = "Leaderboard",
    )

    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO Leaderboard (Username, Time, Date) VALUES (%s, %s, %s)", (username, timeTaken, today))
    mydb.commit()