# this is a python practice project "one-dimension quiz dungeon"

import DungeonSettings as DS
import json
# import os

# ask if player wants to play this game
while True:
    yesOrNo = input("Do you want to play Quiz Dungeon? (y)es/(n)o:")

    if yesOrNo != "y" and yesOrNo != "n":
        print("Please enter y for 'Yes' or n for 'No'.")
        continue
    elif yesOrNo == "n":
        print("You've exit Quiz Dungeon!!")
        quit()
    else:
        break  # yes

# players want to play
# os.system('cmd /k "cls"') # clear the prompt screen
print("Welcome to Quiz Dungeon!!")

# load out the quiz
for room in DS.dungeon:
    print("\nYou have enter a room.")

    if room == "empty":  # a path in front
        print("It is an empty room. You'll move to next room.")

        continue
    elif room == "Exit":
        print("It is an exit. You have passed the Quiz Dungeon.")
        quit()

    # json to object
    data = json.loads(room)

    while True:
        print("\nPress 'Ctrl + C' to Exit Dungeon or answer the question below:")

        answer = input(data['Question'])

        if answer == str(data['Answer']):
            print("Your answer is correct.")
            break
        else:
            print("Your answer is incorrect.")
            continue
