import random

names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")
print(names)

names_random = random.choice(names)
print(f'{names_random} is going to pay the bill today.')

#alternare version
num_items = len(names)

random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(f'{person_who_will_pay} is going to pay the bill today')