# Author:           Kristlyn Montoya
# ULID:             C00425573
# Course/Section:   CMPS 150 - Lecture Section # 001
# Assignment:       pa5
# Date Assigned:    Thursday, October 18, 2018
# Date/ Time Due:   Tuesday, October 23, 2018 -- 11:55 pm
#
# Description:      This program will process a file of data using functions
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

# open the file you are using to read from

#main function that holds the sentinel control loop and reads all other functions

def main():
    infile = open('ccNums.py', 'r')
    cardNumber = infile.readline().strip()
    print(format("Credit Card Number", '20s'), "Result")
    print('----------------------------')
    
# Sentinel control loop - loops over the card numbers until it reaches a blank line

    while cardNumber != "":
        number = numCheck(cardNumber)
        sum1 = firstCardSum(cardNumber)
        sum2 = secondCardSum(cardNumber)
        total = sum1 + sum2
        
        #if statement that checks the validity of BOTH the first number of the credit cards,
        #and whether or not the two sums added together are divisible by 100
        
        if total % 10 == 0:
            boolean = True
        else:
            boolean = False
        if number == True and boolean == True:
                number = 'Valid'
        else:
                number = 'Invalid'
        print(format(cardNumber, '20s'), format(number, '10s'))
        cardNumber = infile.readline().strip()
    infile.close()
    
#function that checks the first number in each credit card number that is read
#returns either a true or false value to indicate whether or not it meets
#the requirements
    
def numCheck(cardNumber):
    if cardNumber != "":
        if cardNumber[0] == '6'\
        or cardNumber[0] == '5'\
        or cardNumber[0] == '4'\
        or cardNumber[0] == '3':
            result = True
            return result
        else:
            result = False
            return result
    else:
        pass
    
#function below looks at the left most digit, then every second digit to the right
# after that. The function multiplies each appropriate digit by 2, then
#sums those values and stores the total in a value named "cardSum"

def firstCardSum(cardNumber):
    if cardNumber !='':
        cardSum = 0
        for x in range(0,10,2):
            cardSum = cardSum + eval(cardNumber[x]) * 2
        return cardSum
    else:
        pass
    
# function below looks at the second digit from the left, then every second digit after that,  and
#sums them together. This value is stored in a variable named cardSum2

def secondCardSum(cardNumber):
    if cardNumber !='':
        cardSum2 = 0
        for x in range(1,10,2):
            cardSum2 = cardSum2 + eval(cardNumber[x])
        return cardSum2
    else:
        pass

main()


