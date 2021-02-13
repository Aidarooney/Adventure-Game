import time
import os
import sys
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