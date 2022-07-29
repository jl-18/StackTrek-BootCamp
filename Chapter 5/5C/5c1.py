import os
os.system('cls||clear')

# Code starts here


numE = int(input())
m = 0
f = 0

for count in range(1, numE + 1):
  i = input()
  if i == "m":
    m += 1
  elif i =="f":
    f += 1
  else: 
    pass
  
d = 0 

if m < f:
    d = f
elif m > f:
    d = m
else:
    d = m
      
  
for count in range(0, d + 1):
    if m % d == 0 and f % d == 0:
        break
    else:
        d -= 1
        continue

m_ratio = m // d
f_ratio = f // d

print(f"Males: {m}")
print(f"Females: {f}")
if m_ratio == 0:
    print("All females")
elif f_ratio == 0:
    print("All males")
else:
    print(f"{m_ratio}:{f_ratio}")

#-----Diversity-----
#A tech diversity research would like to gather statistics for male vs. female enrollees in 
# software-development related degrees such as IT, CS, and SE.
#The program starts by asking how many enrollees, and proceeds by entering either M or F, case-insensitively. 
# The number of M/F entries depends on the number of enrollees specified as the first input.
#It then reports the number of males to females, and displays the ratio. The ratio must be in reduced form. 
# So for 8 males, 2 females, it must be displayed as 4:1 rather than 8:2. Ratio with zeroes in it doesn't 
# make sense, so if there are no females, output All males, and vice versa.

#How to reduce the ratio?
#Same as reducing fractions! Ratios are fractions. Divide both numbers by their greatest common divisor (GCD).
#How to get the GCD?
#The greatest common divisor of two positive integers, n and m, is the largest number, d, which divides 
# evenly into both n and m. There are several algorithms that can be used to solve this problem, including
#  this very slow but simple one:

#Initialize d to the smaller of m and n.

#While d does not evenly divide m OR d does not evenly divide n do
# Decrease the value of d by 1
# Report d as the greatest common divisor of n and m
