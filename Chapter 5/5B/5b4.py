import os
os.system('cls||clear')

# Code starts here


from math import sqrt
flag = True
count = 0;
first_x = 0
first_y = 0
temp_x = 0
temp_y  = 0
area = 0
peri = 0
while flag == True:
    x = input()
    if(x == 'stop'):
        area += (temp_x * first_y) - (temp_y * first_x)
        peri += (sqrt((temp_x - first_x)**2 + (temp_y - first_y)**2))
        flag = False
        continue
    else:
        y = int(input())
        if count == 0:
            first_x = int(x)
            first_y = int(y)
            temp_x = int(x)
            temp_y = int(y) 
            count += 1
        else:
            peri += (sqrt((int(x) - temp_x)**2 + (int(y) - temp_y)**2))
            area += (temp_x * int(y)) - (temp_y * int(x))
            temp_x = int(x)
            temp_y = int(y)
            count += 1

print(f"Perimeter: {peri}")
print(f"Area: {abs(area/2)}")

#-------Polygon-------
#Polygons are a big part of many apps, including the ever useful Google Maps. For the founder of a real 
# estate planning app, StartupIO tasked you to write a program that calculates the perimeter and area of
# any polygon, given the points as input.
#Begin by reading the x and y values for the first point on the perimeter of the polygon from the user.
# Then continue reading pairs of x and y values until the user enters stop for the x-coordinate.
