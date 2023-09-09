'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.
'''
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
remaining_age = 90 - age_int
months_left = remaining_age * 12
weeks_left = remaining_age * 52
days_left = remaining_age * 365
print("\nIf you live upto 90 years then :-")
print(f"\nYou have {days_left} days, {weeks_left} weeks, and {months_left} months left.")