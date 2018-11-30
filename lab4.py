# Author:         Kristlyn Montoya
# ULID/Section:   C00425573 / CMPS-150 Section # 001
# Lab #4 

# Part I
# Ask the user to enter the lengths of three sides of a triangle
side1,side2,side3 = eval(input("Enter 3 integers for the triangle sides: "))


# Check for "valid" lengths ...
# if valid -- compute perimeter -- else print "invalid"

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print('perimeter:', side1 + side2 + side3)
else:
    print("These numbers are invalid")


# Part II
# Ask the user for a number
print()
number = eval(input("Enter a number: "))


# Determine if the input number is positive, negative or zero
# Respond with your determination

if number < 0:
    print("%s is a negative number" % number)
elif number == 0:
    print("%s equals 0" % number)
elif number > 0:
    print("%s is a positive number" % number)


# Part III
# Ask the user for how many years they have worked for a company
print()
years = eval(input("Enter years worked: "))


# Determine the category of their raise (see handout)
# Respond with your determination

if years > 7:
    print("Raise category: 6%")
elif years >= 6:
    print("Raise category: 5%")
elif years >= 4:
    print("Raise category: 4%")
elif years >= 0:
    print("Raise category: 3%")
