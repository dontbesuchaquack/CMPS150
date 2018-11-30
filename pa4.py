# Author:           Kristlyn Montoya
# ULID:             C00425573
# Course/Section:   CMPS 150 - Lecture Section # 001
# Assignment:       pa4
# Date Assigned:    Friday, September 27, 2018
# Date/ Time Due:   Wednesday, October 3, 2018 -- 11:55 pm
#
# Description:      This program is a sales report for a book company
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# open the file you are using to read from

infile = open("pa4Input.py", 'r')

# create counter placeholder variable that will indicate
# the start and stop of the loop

x = 0

# pretty print statements to help position the rest of
# the information printed in the program

print("Electricity\t", "Water")
print("----------------------")

# While loop that reads two lines from the file each iteration
# the loop calculates the utility bill, then prints. The counter
# on the end adds one to x, to continue running the program

while x < 5:
    electricity = eval(infile.readline())
    electricity = electricity *.08
    water = eval(infile.readline())
    water = water / 1000 * 10.15
    print(format(electricity, "5.2f"),"\t\t",format(water, "5.2f"))
    print()
    x+=1

# close the file once the program is done reading from it
infile.close()
