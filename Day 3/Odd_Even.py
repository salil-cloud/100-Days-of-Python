'''
Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is odd because 59 ÷ 2 = 29.5
'''


# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check?\n "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0 :
    print("\nThis is an even number")
else :
    print("\nThis is an odd number")
