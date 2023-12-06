age = input("What is your current age?")

days_remaining = (90 - int(age)) * 365
months_remaining = (90 - int(age)) * 12
weeks_remaining = (90 - int(age)) * 52

message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left.\n"
print(message)