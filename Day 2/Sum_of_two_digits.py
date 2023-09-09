# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
int_two_digit_number = int(two_digit_number)

# Calculate the sum of the two digits
first_digit = int_two_digit_number // 10
second_digit = int_two_digit_number % 10

sum_of_digits = first_digit + second_digit
print(str(first_digit) + "+" + str(second_digit)+"="+str(sum_of_digits))