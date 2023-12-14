#Printing each number from 1 to 100 using for loop
for number in range(1, 101):
    #If number is divisible by both 3 and 5 print FizzBuzz
    if (number % 3 == 0) and (number % 5 == 0):
        print ("FizzBuzz")
    #If number is divisible by 3 print Fizz
    elif number % 3 == 0:
        print ("Fizz")
    #If number is divisible by 5 print Buzz
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print(number)