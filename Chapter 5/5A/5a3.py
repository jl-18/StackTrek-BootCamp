import os
os.system('cls||clear')

# Code starts here

age = int(input())
goal = float(input())
price = float(input())

money = 0
toy = 0

for i in range(0, age):
    i += 1
    if i % 2 == 0:
        money += 1
    else:
        toy += 1

bday_moneys = 0
for years in range(0,money):
    years += 1
    bday_moneys += 10 * years
    bday_moneys -= 1

total_toy_price = 0
for years in range(0,toy):
    total_toy_price += price

savings = bday_moneys + total_toy_price

if savings < goal:
    print(f"No! you still need {(goal - savings):.2f}")
elif goal < savings:
    print(f"Yes! you still have {savings - goal:.2f} left")

#-----Birthdays------
#Most Chinese people describe themselves as diligent and thrifty. Some believe it's a Chinese value, 
# with being frugal a good approach to life, while others say it's a remnant of the past.
#Shem Young is N years old. For each birthday he receives a present. For each odd birthday 
# (1, 3, 5, …, n) he receives toys, and for each even birthday (2, 4, 6, …, n) he receives money.
#  For his second birthday he received 10 Dollars, and the amount is increased by 10.00 Dollars for 
# each following even birthday (2 -> 10, 4 -> 20, 6 -> 30 etc.). Over the years Shem has secretly 
# saved his money. Shem's naughty brother through the years gets 1.00 Dollar when he receives money as present.
#  Shem has sold his toys which he received over the years and each one for P Dollars and added the sum to the 
# amount of saved money. With the money he wanted to buy a washing machine for X Dollars to help his mother 
# with her household chores. Write a program that calculates how much money he has saved and if it is enough
#  to buy a washing machine.



  
  
  
