'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
'''

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height = float(height)
weight = float(weight)

# Calculate BMI
bmi = weight / (height ** 2)

# Convert BMI to an integer if needed
bmi_integer = int(bmi)

print(bmi_integer)
