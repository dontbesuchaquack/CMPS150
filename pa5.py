# Author:           Kristlyn Montoya
# ULID:             C00425573
# Course/Section:   CMPS 150 - Lecture Section # 001
# Assignment:       pa5
# Date Assigned:    Monday, October 8, 2018
# Date/ Time Due:   Friday, October 12, 2018 -- 11:55 pm
#
# Description:      This program processes text/ string data
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# open the file you are using to read from

infile = open('pa5Data.py', 'r')

#Initialized variables to use in the program (Global Variables)

textline = None
lineCount = 0
vowela = 0
vowele = 0
voweli = 0
vowelo = 0
vowelu = 0

# Main while loop iteration that loops through each line of pa5Data.py
# Set loop condition to stop reading the file when it comes to a blank line

while textline != "":
    textline = infile.readline()
    # Get rid of horizontal white space between iterations
    
    textline = textline.strip()
    
    # re-initialize uppercase variable after each iteration
    
    uppercase = ""
    
    # Nested loop that checks each letter in each line
    # If a letter is uppercase, it gets concatenated as a string in an-
    # -"uppercase" variable
    # If a letter is a vowel, a corresponding vowel counter is updated
    
    for letter in textline:
        if letter.isupper():
            uppercase = uppercase + letter
        if letter in ("a","A"):
            vowela = vowela +1
        elif letter in ("e", "E"):
            vowele = vowele + 1
        elif letter in ("i", "I"):
            voweli = voweli + 1
        elif letter in ("o", "O"):
            vowelo = vowelo + 1
        elif letter in ("u", "U"):
            vowelu = vowelu + 1
    

    # Prints the uppercase letters of each line as a string
    
    print(uppercase)
    
    # Counts a line after each iteration, ONLY if the line read is not an empty space
    
    if textline !="":
        lineCount = lineCount + 1
    
# pretty print statements to output line count, and vowel counts

print("Line Count\n",format(lineCount, '4d'))
print()
print("Vowel Count\n", "a/A:",vowela,'\n', "e/E:",vowele,'\n',"i/I:",voweli,'\n',"o/O:",vowelo,'\n',"u/U:",vowelu)
infile.close()

