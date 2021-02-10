from functions import walking
import time
answer = input("Would you like to play? (yes/no)\n")
enter = "Press Enter to continue..."
HEXcode = "open"
HEXinput = ""
DoorOpen = False 

if answer.lower().strip() == "yes":
    answer = input("You reach a cross roads, would you like to go left or right?\n").lower().strip()

    if answer == "left":
        answer = input("You encounter a cow, would you like to run or attack\n")

        if answer == "attack":
            print("That was not the greatest idea, you lost")
            input(enter)

        else:
            print("Good choice you made it away safely\n")
            walking()
            print("You come accross a tree with what appears to be a building on top of it and a keypad on a knot, there appears to be a note above it\n")
            time.sleep(3)
            answer = input("Do you read the note or keep moving? (read/move)\n")

            if answer == "read":
                print("The note reads, 'The owner of this base is a man for CTF, open the door and seek Consolation HEX: 6f 70 65 6e'\n")

                while DoorOpen == False:
                    HEXinput = input("Please enter code to unlock the secrets within\n")
                    if HEXinput == HEXcode:
                        DoorOpen = True
                print("The door slides open revealling a ladder that you start to climb\n")
                time.sleep(3)
                


    elif answer == "right":
        answer = input("You find a building, would you like to go inside? (yes/no)\n")

        if answer == "yes":
            answer = input("You enter a room with a tool chest and 2 doors, one leads to the kitchen and the other leads to the garage (chest/kitchen/garage)\n")
        
        else:
            print("You keep walking through the forest\n")
            walking()
            answer = input("You are starving and come across some berries, they look edible (eat/leave)\n")

            if answer == "eat":
                print("You die of poisoning from the Honeysuckle berries")
                input(enter)

            else:
                print("You walk away from the bush hoping for a more reliable food source\n")
                

    else:
        print("You Lost")
        input(enter)

else:
    print("That's too bad")
    input(enter)