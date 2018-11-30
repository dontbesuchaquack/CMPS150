#  Author:          Kristlyn Montoya
#  ULID/Section:    C00425573 | Section 1
#  lab13.py 

import random



def swap(myList):
    first = myList[0]
    if len(myList) == 16:
        last = myList[15]
        myList[0] = last
        myList[15] = first
    elif len(myList) == 15:
        last = myList[14]
        myList[0] = last
        myList[14] = first
        

def reverse(myList):
    newList = []
    for i in range( len(myList) - 1, -1, -1) :
        newList.append(myList[i])
    return newList
    
    
def main():
    # create an empty list
    myList = []
    # set up a counting loop to append 15 random integers
    # to the list, ranging from 1 to 25 (inclusive)
    for x in range(0,15):
        num = random.randint(1,26)
        myList.append(num)

    # print the list
    print(myList)
    print()
    # generate one more random integer in the same range
    # append it to list ONLY IF it is not already in the list
    extraNum = random.randint(1,26)
    print('The extra number is:', extraNum)
    print()
    if extraNum not in myList:
        myList.append(extraNum)
        print(extraNum, 'is not currently in the list! ... it has now been added!')
        print()
    else:
        print(extraNum,'is already in the list!')
        print()
    # print the list
    print(myList)
    # call function to swap the first & last element
    swap(myList)
    # print the list
    print(myList)
    print()
    # call function to reverse the list
    reversedList = reverse(myList)
    # print the list
    print(reversedList)

main()
