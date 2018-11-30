# Author:           Kristlyn Montoya
# ULID:             C00425573
# Course/Section:   CMPS 150 - Lecture Section # 001
# Assignment:       pa2
# Date Assigned:    Monday, September 10, 2018
# Date/ Time Due:   Saturday, September 15, 2018 -- 11:55 pm
#
# Description:      This program will determine the gratuity on a bill,
#                   and print a formatted output table.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.


# ask the user for three(3) sets of customer name, bill amount and gratuity
customer1 = input("Enter a name for customer 1: ")
customer2 = input("Enter a name for customer 2: ")
customer3 = input("Enter a name for customer 3: ")
billAmounts = eval(input("Enter bill amounts for each customer: "))
gratuities = eval(input("Enter gratuity amounts for each customer: "))

# determine gratuity amount for each customer
# gratuity amount is: bill amount * (gratuity/100)
# determine total by summing bill amount and gratuity amount

gratuity1 = billAmounts[0] * (gratuities[0]/100)
gratuity2 = billAmounts[1] * (gratuities[1]/100)
gratuity3 = billAmounts[2] * (gratuities[2]/100)

custTotal1 = gratuity1 + billAmounts[0]
custTotal2 = gratuity2 + billAmounts[1]
custTotal3 = gratuity3 + billAmounts[2]

# print output similar to sample run
#NOTE: money must have 2 decimal places
print("Customer name:\t", customer1, ' ', customer2, ' ', customer3)
print("Bill:\t\t", round(billAmounts[0], 2), '\t', round(billAmounts[1], 2), '\t', round(billAmounts[2], 2))
print("Gratuity:\t", round(gratuity1, 2), '\t', round(gratuity2, 2), '\t', round(gratuity3, 2))
print("Total:\t\t", round(custTotal1, 2), '\t', round(custTotal2, 2), '\t', round(custTotal3, 2))


