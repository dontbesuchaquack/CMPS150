# Author:           Kristlyn Montoya
# ULID:             C00425573
# Course/Section:   CMPS 150 - Lecture Section # 001
# Assignment:       pa8
# Date Assigned:    Tuesday, November 20, 2018
# Date/ Time Due:   Tuesday, November 27, 2018 -- 11:55 pm
#
# Description:      This program will create a file (named pa8_numbers.py) of 10,000
#                   random numbers between one(1) and one hundred(100).
#                   Then, it will create an empty list and append these 10,000 random
#                   numbers in it. Finally, it will compute the average and determine
#                   how many of the numbers are within 10 “above” the average and how
#                   many of the numbers are within 10 “below” the average.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

def average(myList):
    sumNum = sum(myList)
    avg = sumNum/10000
    return avg

def numList():
    myList = []
    infile = open("pa8_numbers.py", 'r')
    for x in range(1,10000):
        myList.append(eval(infile.readline().strip()))
    return myList

def above(myList,avg):
    aboveList = []
    count = 0
    for x in range(len(myList)):
        if myList[x] > avg and myList[x] <= avg + 10:
            aboveList.append(myList[x])
            count = count + 1
    return count

def below(myList,avg):
    belowList = []
    count = 0
    for x in range(len(myList)):
        if myList[x] < avg and myList[x] >= avg - 10:
            belowList.append(myList[x])
            count = count + 1
    return count

def printFunc(avgnum, aList, bList):
    print("Statistics")
    print("------------------------------")
    print(format("Average:", '22s'), format(avgnum, '4.2f'))
    print(format("10 above the average:", '23s'), format(aList,'4d'))
    print(format("10 below the average:", '23s'), format(bList, '4d'))
       
def main():
    
    import random
    
    outfile = open("pa8_numbers.py", "w")

    for i in range(10000):
        data = random.randint(1,100)
        outfile.write(str(data)+"\n")
    outfile.close()

    nList = numList()
    
    avgnum = average(nList)

    aList = above(nList, avgnum)

    bList = below(nList, avgnum)
    
    printFunc(avgnum, aList, bList)
    
main()    
