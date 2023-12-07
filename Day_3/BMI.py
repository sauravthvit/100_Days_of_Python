height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have a normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")

print("And your BMI value is", "{:.2f}".format(bmi))