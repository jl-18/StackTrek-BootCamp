import os
os.system('cls||clear')

# Code starts here

month = input()
nights = int(input())
month = month.title()

if month == "May" or month == "October":
  deluxe_price = 100 * nights
  premium_price = 85 * nights
  
  if nights > 14:
    deluxe_price -= deluxe_price * 0.3
    premium_price -= premium_price * 0.1
  elif nights > 7:
    deluxe_price -= deluxe_price * 0.05
    
  print(f"Deluxe: {deluxe_price:.2f} dollars")
  print(f"Premium: {premium_price:.2f} dollars")
    
elif month == "July" or month == "September":
  deluxe_price = 112.50 * nights
  premium_price = 90.58 * nights
  
  if nights > 14:
    deluxe_price -= deluxe_price * 0.2
    premium_price -= premium_price * 0.1
  print(f"Deluxe: {deluxe_price:.2f} dollars")
  print(f"Premium: {premium_price:.2f} dollars")
    
elif month == "June" or "August":
  deluxe_price = 125.66 * nights
  premium_price = 100.50 * nights
  
  if nights > 14:
    deluxe_price -= deluxe_price * 0.2
    premium_price -= premium_price * 0.1
  print(f"Deluxe: {deluxe_price:.2f} dollars")
  print(f"Premium: {premium_price:.2f} dollars")
  
#-------Staycation---
#Staycation is one way for us to escape reality. Teofy was burnt out with a lot of SE requirements that 
#led her to the idea of having a staycation with her family. Hotel SE1121 offers two types of rooms : 
# deluxe and premium
#Since Teofy is madly in love with her course, she wants to write a program that would help her calculate 
# the total cost for her entire stay comparing deluxe and premium room types.
