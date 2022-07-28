import os
os.system('cls||clear')

# Code starts here

TargetDonation = int(input())
Puzzles = int(input())
Dolls = int(input())
Bears = int(input())
Plushies = int(input())
Truck = int(input())

price = (Puzzles * 14) + (Dolls * 3) + (Bears * 20.2) + (Plushies * 8.20) + (Truck * 10.65)
total = Puzzles + Dolls + Bears + Plushies + Truck

if total >= 50:
  price -= (price * 0.25)
  
price -= (price * 0.1)
price -= TargetDonation

if price >= 0:
  print(f"Yes! {abs(price):.2f} dollars left.")
else:
  print(f"Not enough money! {abs(price):.2f} dollars needed.")


# -----Toy Kingdom----
#Mike has a toy store in the beautiful city called SE-landia. 
# A toy collector suddenly went in to his shop and ordered in bulk. Mike is excited to accomplish the said
# order to forward his profit in the Children's Village. Help Mike by writing a program that will 
# calculate
#Toy prices:
#Puzzle - 14 Dollars
#Talking doll - 3 Dollars
#Teddy bear - 20.2 Dollars
#Pokemon Plushie - 8.20 Dollars
#Big Toy Truck - 10.65 Dollars
#If the order reaches 50 or more , Mike is willing to give his loving costumer 25% discount from the total 
# price. Out of the total money earned, he must allocate 10% for the store rental. Calculate if the money will
#  be enough for Mike's Donation and output how much money will be left or is needed to reach his goal. 
# (See output)
 
  
