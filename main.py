from functions import walking
from functions import terminal
import time
answer = input("Would you like to play? (yes/no)\n")
enter = "Press Enter to continue..."
HEXcode = "open"
HEXinput = ""
DoorOpen = False
riddle = "map" 
Break = False



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
                terminal("Welcome to Farmers terminal (not associated with Farmer)")


    elif answer == "right":
        answer = input("You find a building, would you like to go inside? (yes/no)\n")

        if answer == "yes":
            answer = input("You enter a room with a tool chest and 2 doors, one leads to the kitchen and the other leads to the garage (chest/kitchen/garage)\n")
            time.sleep(1)
            if answer ==  "chest":
                print("You walk over towards the chest and open it, there is a crowbar inside (This can be used to access rooms that are locked)")

            elif answer == "garage":
                print("You walk ovr to a door on the other side of the building that appears to lead to some sort of garage.\n")
                print("The door appears to be locked by some sort of keypad")

            else:
                print("You walk over to a door witha sign above it reading, 'In this kitchen we dance' You make the educated guess that it leads to the kitchen\n")
                time.sleep(1)
                print("You push open the door revealing another room, but not a kitchen, this room has a soletary computer in it\n")
                time.sleep(1)
                print("You notice that there is a terminal open on it, you move to get a closer look")
                terminal("Welcome to Farmers terminal (Not associated in any way with Farmers) ©I dont have the capacity to make a name for the company\n")
                terminal("This terminal comes equiped with one program and it is a riddle, this riddle is the code to unlock the garage door\n")     
                while Break == False:
                    terminal("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?\n")
                    answer = input("")
                    if answer == (riddle):
                        Break = True
                        terminal("Congratulations you solved the riddle, the code for the door is '1238'\n")
                    else:
                        terminal("Please Try again that was not the answer, you mustn't be Jack\n")
                    
        
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