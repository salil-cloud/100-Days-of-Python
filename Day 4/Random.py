#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

random_toss = random.randint(0, 1)

if(random_toss == 0) :
    print("Tails")
else :
    print("Heads")