import os
os.system('cls||clear')

# Code starts here

callMins = float(input())
texts = float(input())

print(f"Call minutes: {callMins:.1f}")
print(f"Text messages: {texts:.1f}")

allowed_calls = 60
excessMins = float(callMins - allowed_calls)

if excessMins > 0:
  excessMins *= 6.50
else:
  excessMins = 0
print(f"Excess minute charges: {excessMins:.2f}")

allowed_texts = 100
excessSMS = float(texts - allowed_texts )
if excessSMS >  0:
  excessSMS *= 1
else:
  excessSMS = 0
print(f"Excess SMS charges: {excessSMS:.2f}")

fee = 25.00
print(f"911 fee: {fee:.2f}")

monthly_bill = 799.00
amount = float(excessMins + excessSMS + fee + monthly_bill)
tax = float(amount * 0.05)
print(f"Tax: {tax:.2f}")

total = amount + tax
print(f"Total bill: {total:.2f}")

#---Cellphone Plan -----
#A particular cell phone plan includes 60 minutes of air time and 100 text messages for Php 799 a month. 
# Each additional minute of air time costs Php 6.50 while additional text messages cost Php 1 each. 
# All cell phone bills include an additional charge of Php 25 to support PRRD's 911 call centers, 
# and the entire bill (including the 911 charge) is subject to 5 percent sales tax.
#Write a program that reads the number of call minutes and text messages used in a month from the user. 
# Display the base charge, additional minutes charge (if any), additional text message charge (if any), 
# the 911 fee, tax and total bill amount. Only display the additional minute and text message charges if t
# he user incurred costs in these categories. Ensure that all of the charges are displayed using 2 decimal 
# places (so 15 must display as 15.00, 9.375 must display as 9.38).
