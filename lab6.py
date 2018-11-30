# Author:         Kristlyn Montoya  
# ULID/Section:   C00425573 | Section 01 
# Lab #6



# Task #1:  Odd and Even Numbers

# initialize variables

num = 1
count = 0
inch = 1

# repeat loop based on input item NOT being the sentinel value

while num > 0:
    # get first input item
    num = eval(input("Enter a positive integer (non-positive to exit): "))
    if num > 0:
        # process data - determine if input data is odd or even
        if num % 2 == 0:
            print("%s is an even number!" % num)
            # update counter variable
            count = count + 1
        elif num % 2 == 1:
            print("%s is an odd number!" % num)
            # update counter variable
            count = count + 1
    else:
        break

# print the count of positive values entered
print()
print("you entered %s positive numbers" % count)

# print a blank line before moving on to task #2
print()


# Task #2:  Print inches/centimeters table using a for loop
print("Inches \t", "Centimeters")
print("----------------------")
for x in range(3,21,3):
    centimeters = x * 2.54
    print(format(x, "4d"), format(centimeters, '12.2f'))
    
