#Vinu Harihar
#Guess the Number
import random

x = int(input("Enter an integer between 1 and 100"))
y = random.randint(1, 101)

if x > y:
    print ("Your guess is too high")
    print ("\n")
elif x < y:
    print ("Your guess is too low")
    print ("\n")
else:
    print ("Your guess is correct")
    print ("\n")

while x != y:
    g = input("Guess another number")
    x = int(g)
    if x > y:
        print ("Your guess is too high")
        print ("\n")
    elif x < y:
        print ("Your guess is too low")
        print ("\n")
    else:
        print ("Your guess is correct")
        print ("\n")
    
    