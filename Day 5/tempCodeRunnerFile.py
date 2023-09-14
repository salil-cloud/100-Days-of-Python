#Write your code below this row 👇
for n in range(0, 101) :
    if n%3 == 0 or n%5 ==0 :
        if n%3 == 0 and n%5 == 0 :
            print("FizzBuzz")
        elif n%3 == 0 :
            print("Fizz")
        else :
            print("Buzz")
    else :
        print(n)
