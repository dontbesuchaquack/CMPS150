# Author:           Kristlyn Montoya
# ULID:             C00425573
# Course/Section:   CMPS 150 - Lecture Section # 001
# Assignment:       pa1
# Date Assigned:    Friday, August 31, 2018
# Date/ Time Due:   Thursday, September 6, 2018 -- 11:55 pm
#
# Description:      This program will determine the y-intercept of line,
#                   given a point and a slope.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.


# ask the user for their name, using an input/assignment statement

name = input("Please enter your name: ")

# ask the user for a coordinate on a graph
# HINT:  you can use two input/ assignment statements or one simultaneous
# remember, you must change the string input to a numeric

x,y = eval(input("%s, please provide your x,y coordinates: " % name))


# ask the user for the slope of the line
# remember, you must change the string input to a numeric

slope = eval(input("%s, please provide the slope of your line: " % name))

# determine the y-intercept
# REMEMBER: the formula is y = mx + b, where (x,y) is the coordinate
# you got as input, m is the slope you got as input, and you are solving
# for b, the y-intercept (the value of y when the line crosses the y-axis)
# THAT IS, the LHS must be y-intercept (or 'b'), not y.

yIntercept = y - slope * x

# print output similar to sample run

print("Hello %s!" % name)
print("Your y-intercept is: %d" % yIntercept)

