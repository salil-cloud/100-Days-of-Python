'''
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
'''
print("Welcome to tip calculator\n")
rupee_symbol = "\u20B9"
bill_amount = float(input(f"What is your total bill amount :{rupee_symbol}"))
tip_amount = int(input("What percentage would you like to tip (10/12/20) :"))
spilt = int(input("Total people to split the bill :"))
final_amount = ((tip_amount / 100 * bill_amount + bill_amount)/ spilt)
rounded_final_amount = round(final_amount, 2)
print(f"Your final amount per participant is :{rupee_symbol}{rounded_final_amount}")