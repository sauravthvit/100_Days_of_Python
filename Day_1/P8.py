print("Welcome to the tip calculator/n")
total_bill = float(input("What was the total bill ? $ "))
tip_percentage = int(input("What percentage would you like to give - 10, 12 or 15 ? "))
number_of_people = int((input("How many people to split the bill ? ")))
tip = tip_percentage / 100 * total_bill
payment = total_bill + tip
each_payment = "{:.2f}".format(payment / number_of_people)

print(f"Each person should pay ${each_payment}")