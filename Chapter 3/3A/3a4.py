import os
os.system('cls||clear')

#code starts here

paid = float(input())
tax = paid * 0.12
tip = (paid - tax) * 0.10
fee = paid - (tip + tax)
print(f"Tax:, {tax:.2f}")
print(f"Emergency Fund:, {tip:.2f}")
print(f"Accommodation:, {fee:.2f}")
