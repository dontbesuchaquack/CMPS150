# Author:           Kristlyn Montoya
# ULID:             C00425573
# Course/Section:   CMPS-150 - Lecture Section X
# Assignment:       pa3
# Date Assigned:    Tuesday, September 18, 2018
# Date/Time Due:    Saturday, September 22, 2018 -- 11:55 pm
#
# Description: This program will compute the shipping cost for a package
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.


# ask the user for the type of package either P or N
pkgType = input("Is the package perishable or non-perishable? Enter: P or N: ")

# ask the user for the weight of the package

weight = eval(input("enter the weight of your package: "))

# calculate tax, then add it to the item cost
# determine the cost of shipping

if pkgType == 'P':
    itemCost = 4.95
    tax = 0.085 * itemCost
    totalCost = itemCost + tax
    if weight > 8:
        shipCost = 15.95
    elif weight > 5:
        shipCost = 9.95
    elif weight > 2:
        shipCost = 5.95
    elif weight >= 0:
        shipCost = 2.95
    else:
        print("invalid")
elif pkgType == 'N':
    itemCost = 1.95
    tax = 0.085 * itemCost
    totalCost = itemCost + tax
    if weight > 8:
        shipCost = 9.95
    elif weight > 5:
        shipCost = 7.95
    elif weight > 2:
        shipCost = 3.95
    elif weight >= 0:
        shipCost = 9.95
    else:
        print("invalid")

shipTotal = totalCost + shipCost

# respond with table of the charges

print("------------------------------")
print("Item Cost:                %s" % itemCost)
print("Tax (8.5%):              ", round(tax,2))
print("Total Cost:               %s" % round(totalCost,2))
print("------------------------------")
print("Package Weight: %slbs" % weight)
print("Shipping Cost:            %s" % shipCost)
print("------------------------------")
print("Total (incl. shipping):  %s" % round(shipTotal,2))





