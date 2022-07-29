import os
os.system('cls||clear')

# Code starts here

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())
num7 = int(input())
num8 = int(input())
num9 = int(input())
num10 = int(input())

n = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
highest = 0
lis = []
lowest = 9999999999
for i in n:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    if i % 3 == 0:
        lis.append(i)
        
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"{len(lis)} numbers divisible by 3")

#------Min Max Diversity-----
#Write a program that asks the user for ten numbers, 
# and then prints the largest, the smallest, 
# and how many are divisible by 3.





