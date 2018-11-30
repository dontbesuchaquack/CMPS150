# Author:       Kristlyn Montoya  
# ID/Section:   C00425573 / CMPS-150 Section 01
# Lab #5

# Part I
# ask the user to enter the x coordinate (it can be a float)
x = eval(input("Enter an x-coordinate: "))


# ask the user to enter the y coordinate (it can be a float)

y = eval(input("Enter a y-coordinate: "))

# check for the origin, x-axis OR y-axis & all 4 quadrants
if x == 0 and y == 0:
    location = "the origin"
elif x == 0 or y == 0:
    location = "on an axis"
elif x > 0:
    if y > 0:
        location = "in Quadrant I"
    elif y < 0:
        location = "in Quadrant IV"
    else:
        print("Invalid number")
elif x < 0:
    if y > 0:
        location = "in Quadrant II"
    elif y < 0:
        location = " in Quadrant III"
    else:
        print("Invalid number")
else:
    print("Invalid number")

print("This point is", location)

# Part II
# print a blank line
print()

# pounds/kilograms table

print(" Pounds     Kilograms")
print("---------------------")

count = 5

while count <= 100:
    kilograms = count * .453592
    print(format(count,'5d'),format(kilograms,'12.2f'))

    count += 5 

