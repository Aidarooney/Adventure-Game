answer = input("Would you like to play? (yes/no)\n")

if answer.lower().strip() == "yes":
    answer = input("You reach a cross roads, would you like to go left or right?\n").lower().strip()

    if answer == "left":
        answer = input("You encounter a cow, would you like to run or attack\n")

        if answer == "attack":
            print("That was not the greatest idea, you lost")
            input("Press Enter to continue...")

        else:
            print("Good choice you made it away safely")

    elif answer == "right":
        answer = input("You find a building, would you like to go inside? (yes/no)")


    else:
        print("You Lost")
        input("Press Enter to continue...")

else:
    print("That's too bad")
    input("Press Enter to continue...")