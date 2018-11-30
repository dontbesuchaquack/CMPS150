# Author:         Kristlyn Montoya
# ULID/Section:   C00425573 | Section 01
# Lab #7
 
infile = open("fuel.py","r")
    
print()
print("    Fuel Type        Gallons     Bill")
print("-------------------------------------")  


# this is a count-controlled loop
              
for i in range(1,16):
    # read and process data
    fuelType = infile.readline().strip()
    fuelAmount = eval(infile.readline())
    gallons = fuelAmount
    if fuelType == 'R':
        word = "Regular Unleaded"
        bill = gallons * 2.12
    elif fuelType == 'D':
        word = "Diesel"
        bill = gallons * 2.35
    elif fuelType == 'S':
        word = "Super Unleaded"
        bill = gallons * 2.62
    elif fuelType == 'P':
        word = "Unleaded Plus"
        bill = gallons * 2.36
    else:
        break
 

    # print each line of output
    print(format(word,'20s'),format(gallons,'7.2f'),format(bill,'8.2f'))  


infile.close()
