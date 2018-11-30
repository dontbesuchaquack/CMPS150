# pa9  --  starter code  --  Fall 2018
#
# put all of your
# header documentation here
#

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
    infile = open("pa9-items.py")

    ProdList = []
    ServList = []
    
    PorS = infile.readline().strip()
    s = infile.readline().strip()
    num = eval(infile.readline())

    while num != 0:
        if PorS == "P":
            myProd = Product(s, num)
            # append the new object into the Product List
            ProdList.append(myProd)
        elif PorS == "S":
            myServ = Service(s, num)
            # append the new object into the Service List
            ServList.append(myServ)
        else:
            print("Invalid item code")

        PorS = infile.readline().strip()
        s = infile.readline().strip()
        num = eval(infile.readline())

    infile.close()

    print()
    print("Products: ")
    
    for i in range(len(ProdList)):
        print(format(ProdList[i].GetName(),">20s"),'Per Unit Charge:', '$', ProdList[i].GetCost())
              
              
    print("Services: ")
              
    for i in range(len(ServList)):
        print(format(ServList[i].GetDescription(),">20s"),'Per Hour Charge:', '$', ServList[i].GetRate())
        
    print("----------------------------------------------")
    print("Type")
    print("----------------------------------------------")

    infile = open("pa9-purchases.py")

    category = infile.readline().strip()
    item = infile.readline().strip()
    num = eval(infile.readline())
    bquantity = 0
    gquantity = 0
    fquantity = 0
    chours = 0
    phours = 0
    ehours = 0
    
    
    while num != 0:
        if category == 'P':
            for i in range(len(ProdList)):
                if item == ProdList[i].GetName():
                    print(format(item, '12s'), format(num,'2d'))
                    if item == "Batteries":
                        bquantity = bquantity + num
                        ProdList[i].SetQuantity(bquantity)
                    if item == "Glue":
                        gquantity = gquantity + num
                        ProdList[i].SetQuantity(gquantity)
                    if item == "Filters":
                        fquantity = fquantity + num
                        ProdList[i].SetQuantity(fquantity)
                    
        else:
            for i in range(len(ServList)):
                if item == ServList[i].GetDescription():
                    print(format(item, '12s'), format(num,'2d'))
                    if item == "Car Washing":
                        chours = chours + num
                        ServList[i].SetHours(chours)
                    if item == "Painting":
                        phours = phours + num
                        ServList[i].SetHours(phours)
                    if item == "Electrical":
                        ehours = ehours + num
                        ServList[i].SetHours(ehours)



        category = infile.readline().strip()
        item = infile.readline().strip()
        num = eval(infile.readline())

    print("----------------------------------------------")
    print("Product Totals")
    for x in range(len(ProdList)):
        print("\t",format(ProdList[x].GetName(), '16s'), \
        format(ProdList[x].GetQuantity(), '2d'), '\t$', \
        format(ProdList[x].GetTotalCost(), '6.2f'))
    


    print("Service Totals")
    for x in range(len(ServList)):
        print("\t",format(ServList[x].GetDescription(), '16s'), \
        format(ServList[x].GetHours(), '2d'), '\t$', \
        format(ServList[x].GetTotalCost(), '6.2f'))


    print()
        

    infile.close()

main()
