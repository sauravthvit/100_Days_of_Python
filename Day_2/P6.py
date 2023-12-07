height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height = float(height)
weight = float(weight)

BMI = (weight / (height)**2)

print("Your BMI value is ", (BMI))