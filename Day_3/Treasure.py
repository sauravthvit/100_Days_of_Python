#Printing the introducotry line
print("Welcome to Treasure Island.\nYour mission is to find the treasure\n")
#Taking input from user for the first question
answer = input('You are at a cross road. Where do you want to go? Choose "left" or "right"\n')
#Keeping the answer in lowercase for ease of the user
answer = answer.lower()
if answer == "left":
    answer1 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    answer1 = answer1.lower()
    if answer1 == "wait":
        answer2 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which door you want to open? Red / Blue / Yellow\n')
        answer2 = answer2.lower()
        if (answer2 == "red") or (answer2 == "blue"):
            print("You win!\n")            
    else:
        print("Game over!\n")
else:
    print("Game Over!\n")