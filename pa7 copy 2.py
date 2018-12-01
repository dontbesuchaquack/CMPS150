# pa7  --  sample solution  --  Fall 2018

class Product:
    def __init__(self, newName, newCost):
        self.__name = newName
        self.__cost = newCost
        self.__quantity = 0

    def GetName(self):
        return self.__name

    def GetCost(self):
        return self.__cost

    def GetQuantity(self):
        return self.__quantity

    def SetQuantity(self, newQuantity):
        self.__quantity = newQuantity

    # Price breaks
    def GetTotalCost(self):
        if self.__quantity > 25:
            return self.__cost * self.__quantity * 0.75
        elif self.__quantity > 10:
            return self.__cost * self.__quantity * 0.9
        else:
            return self.__cost * self.__quantity

class Service:
    def __init__(self, newDescription, newRate):
        self.__description = newDescription
        self.__rate = newRate
        self.__hours = 0

    def GetDescription(self):
        return self.__description

    def GetRate(self):
        return self.__rate

    def GetHours(self):
        return self.__hours

    def SetHours(self, newHours):
        self.__hours = newHours

    def GetTotalCost(self):
        return self.__rate * self.__hours

def main():
    infile = open("pa7-items.py")
    
    PorS = infile.readline().strip()
    s = infile.readline().strip()
    n = eval(infile.readline())

    while n != 0:
        if PorS == "P":
            myProd = Product(s, n)
        elif PorS == "S":
            myServ = Service(s, n)
        else:
            print("Invalid item code")

        PorS = infile.readline().strip()
        s = infile.readline().strip()
        n = eval(infile.readline())

    infile.close()

    print()
    print("Product: ",format(myProd.GetName(),"13s"),"Per Unit Charge:  $",format(myProd.GetCost(),"2d"))
    print("Service: ",format(myServ.GetDescription(),"13s"),"Per Hour Charge:  $",format(myServ.GetRate(),"2d"))
    print("----------------------------------------------")
    print("Type")
    print("----------------------------------------------")

    infile = open("pa7-purchases.py")

    item = infile.readline().strip()
    n = eval(infile.readline())
    
    while n != 0:
        if item == myProd.GetName():
            myProd.SetQuantity(myProd.GetQuantity() + n)
            print(format(item,"10s"),format(n,"3d"))
        elif item == myServ.GetDescription():
            myServ.SetHours(myServ.GetHours() + n)
            print(format(item,"10s"),format(n,"3d"))

        item = infile.readline().strip()
        n = eval(infile.readline())

    print("----------------------------------------------")
    print("Totals")
    print(format(myProd.GetName(),"10s"),format(myProd.GetQuantity(),"3d"), "   $",format(myProd.GetTotalCost(),"6.2f"))
    print(format(myServ.GetDescription(),"10s"),format(myServ.GetHours(),"3d"), "   $",format(myServ.GetTotalCost(),"6.2f"))
    print()
        

    infile.close()

main()
