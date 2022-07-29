import os
os.system('cls||clear')

# Code starts here

n = int(input())
if n > 1:
    for i in range(2, n//2):
        if(n % i) == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Neither")


#----Prime?------
#Write a program that asks the user for a number and then displays whether or not it is prime.
# In a loop where you test the possible dividers of the number, you can conclude that the number 
# is not prime as soon as
#you encounter a number other than 1 or itself that divides it.
#however, you can only conclude that it actually is prime after you have tested all possible dividers.
