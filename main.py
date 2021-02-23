from functions import walking
from functions import terminal
from functions import time_convert
import time
answer = input("Would you like to play? (yes/no)\n")
enter = "Press Enter to continue..."
HEXcode = "open"
HEXinput = ""
DoorOpen = False
riddle = "map" 
Break = False
fire_answers = "fuel, oxygen, heat"
fire_input = ""



'''
Add these in after bulk of code is completed
time_lapsed = end_time - start_time
end_time = time.time()
start_time = time.time()
time_convert(time_lapsed)
'''




if answer.lower().strip() == "yes":
    answer = input("You reach a cross roads, would you like to go left or right?\n").lower().strip()
    start_time = time.time()

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
                print(r"""
      /\_/\
 /\  / o o \
//\\ \~(*)~/
`  \/   ^ /
   | \|| ||
   \ '|| ||
    \)()-())
                """)
                terminal("Welcome to El Gatos terminal (Not associated in any way with a cat) ©I dont have the capacity to make a name for the company\n")
                terminal("This terminal comes equiped with one program and it is a riddle, this riddle is the code to unlock the garage door\n")     
                while Break == False:
                    terminal("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?\n")
                    answer = input("")
                    if answer == (riddle):
                        Break = True
                        terminal("Congratulations you solved the riddle, the code for the door is '1238'\n")
                    else:
                        terminal("Please Try again that was not the answer\n")
                    
        
        else:
            print("You keep walking through the forest\n")
            walking()
            answer = input("You are starving and come across some berries, they look edible (eat/leave)\n")

            if answer == "eat":
                print("You die of poisoning from the Honeysuckle berries")
                input(enter)

            else:
                print("You walk away from the bush hoping for a more reliable food source\n")
                walking()
                print("You arrive at what appears to be a farm with a small farm house at the top of the hill")
                time.sleep(1)
                print("You start walking towards it with the hope of food and warmth for the night")
                walking()
                answer = input("You knock on the door and it slides open revealing a warm deserted house with a stocked fridge, do you stay the night (yes/no)\n")
                if answer == "yes":
                    print("You lean into the fireplace to start a roaring fire to cook some delicious beans on\n")
                    time.sleep(1)
                    print("You think back to your training as a scout and desperatly try and remember how to light a proper fire\n")
                    fire_input = input("What are the 3 elements required for a good fire?\n")
                    if fire_input == fire_answers:
                        print("You start a roaring fire")
                        time.sleep(1)
                        print("You cook up some steak that you find in the fridge, medium rare\n")
                        time.sleep(3)
                        print("You fall asleep next to the heat of your roaring fire")
                        time.sleep(5)
                        print("The fire got out of control and burned the house down with you in it")
                        input(enter)
                        #Need to add more story here instead of ending it

                else:
                    print("You continue on your way as night closes in and by 3am you still havent found food or shelter, you lean against a tree and slip into a deep sleep")
                    time.sleep(3)
                    print("You die from starvation")
                    input(enter)

    else:
        print("You Lost")
        input(enter)

else:
    print("That's too bad")
    input(enter)
