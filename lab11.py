# Author:         Kristlyn Montoya
# ULID/Section:   C00425573 | Section-01
# Lab #11

import random

class Car:
    def __init__(self, symbolIn, location=0):
        self.symbol = symbolIn
        self.location = location

    def MoveCar(self):
        self.location = self.location + random.randint(1,5)  

    def DisplayCar(self):
        if (self.location > 0):
            for i in range(self.location):
                print('*',end="")
            print(self.symbol)
        else:
            print(self.symbol)   


def main():
    # This main function will create two cars 
    # Then it will "race" them by moving them 5 times 

    myCar = Car("Nona")
    yourCar = Car("Kristlyn")
    
    for i in range(5):

        # move and display the first car created
        myCar.MoveCar()
        myCar.DisplayCar()
        yourCar.MoveCar()
        yourCar.DisplayCar()

    # determine which car "moved" farthest (location data member is larger)
    # and declare/print that it is the "winner"
    
    if myCar.location == yourCar.location:
        print("It's a tie!")
    elif myCar.location > yourCar.location:
        print(myCar.symbol,"is the winner!")
    else:
        print(yourCar.symbol,"is the winner!")    

main()  
