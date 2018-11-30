# lab3.py

# Author:        Kristlyn Montoya
# ULID/Section:  C00425573 / Section 001
 
 
# print a couple of blank lines before the program begins
# asking for input
print()
print()


# ask the user for the radius of the pizza (in inches)  
# if the radius is positive, compute the area of the pizza (in square inches)
# then ask for the price of the pizza & compute the price of the pizza per square inch
# NOTE: print the price NOT rounded, then rounded to 2 decimal places
# if the radius is <= zero, print an error message


radius = eval(input("Enter the radius of your pizza: "))

if radius > 0:
    area = 3.14159 * radius ** 2
    price = eval(input("How much is the pizza?: "))
    pricePerSqin = price / area
    print("Price per square inch = $ %s" % pricePerSqin)
    print("Price per square inch = $ " + format(pricePerSqin, '3.2f') + " " + "(rounded)")
    
else:
    print("That number is too low! Try again.")


# print a couple of blank lines before the next section of code begins
# asking for input
print()
print()



# ask the user to enter a 3-letter word
# you are allowed only ONE input statement

word = input("Enter a 3-letter word: ")

# print the ASCII code (a number) for each letter of the word just input

print("%s =" % word[0], ord(word[0]))
print("%s =" % word[1], ord(word[1]))
print("%s =" % word[2], ord(word[2]))




# print a couple of blank lines when the program is done
print()
print()


