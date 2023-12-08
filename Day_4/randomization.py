#Randomisation
import random

randomInteger = random.randint(1, 10)
print (randomInteger)

randomFloat = random.random() * 5 #Prints random floating point numbers [0, 5)
print (randomFloat)

love_score = random.randint(1, 100)
print (f'Your love score is {love_score}')