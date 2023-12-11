import random

# Rock = 0

rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper = 1

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors = 2

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = int(input('What do you choose? Type "0" for rock, "1" for paper, "2" for scissors\n'))

if user_choice == 0:
    print (rock)
elif user_choice == 1:
    print (paper)
elif user_choice == 2:
    print (scissors)
else:
    print ("Invalid choice")
    
print ("Computer chose: ")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print (rock)
elif computer_choice == 1:
    print (paper)
elif computer_choice == 2:
    print (scissors)

if ((user_choice == 0) and (computer_choice == 1)) or ((user_choice == 2) and (computer_choice == 1)) or ((user_choice == 1) and (computer_choice == 2)):
    print ("You lose")
    
elif (user_choice == computer_choice):
    print ("It\'s a draw")
else:
    print("You win")