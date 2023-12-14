#Password generator project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'H', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome to the PyPassword Generator!")
nr_letters = int(input("Enter how many letters would you like in your password?\n"))
nr_symbols = int(input("Enter how many symbols would you like in your password?\n"))
nr_numbers = int(input("Enter how many numbers would you like in your password?\n"))

#Easy Way
# password = "" #In string format

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters) #Chooses nr_letters random
    
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers) #Chooses nr_numbers random
    
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols) #Chooses nr_symbols random
    
# print (password)

#Hard way

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters) #Chooses nr_letters random
    
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers) #Chooses nr_numbers random
    
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols) #Chooses nr_symbols random
    
# print (password_list)
# random.shuffle(password_list)
# print (password_list)

password = ""

for char in password_list:
    password += char
    
print (f"Your password is: {password}")

