# Author:         Kristlyn Montoya
# ULID/Section:   C00425573 | Section - 01
# lab9.py 
 
import math

# Area of a circle
def AC(radius):
    area = math.pi * radius ** 2
    return area 
 
# WRITE ALL THE OTHER FUNCTIONS

# Area of a rectangle

def AR(length, width):
    area = length * width
    return area

def VC(length, width, height):
    volume = length * width * height
    return volume

def SAC(length):
    surfaceArea = 6 * length * length
    return surfaceArea

def VR(length, width, height):
    volume = length * width * height
    return volume

def VS(radius):
    volume = 4/3 * math.pi * radius * radius * radius
    return volume

def SAS(radius):
    surfaceArea = 4 * math.pi * radius * radius
    return surfaceArea
 
def main():

    infile = open("lab9_input.py","r")

    # get calculation type, but wait on dimension(s) because
    # number of dimensions is dependent on type of shape
    shapeType = (infile.readline()).strip()

    while (shapeType != "###"): 

        if (shapeType == "AC"):
            # read only one dimension for a circle
            radius = eval(infile.readline())
            circleArea = AC(radius)
            print(format("Area of a Circle","30s"),format(circleArea,"15.2f"))
 
        # do the processing for all other types of calculations
        elif (shapeType == "AR"):
            length = eval(infile.readline())
            width = eval(infile.readline())
            rectangleArea = AR(length, width)
            print(format("Area of a Rectangle","30s"),format(rectangleArea,"15.2f"))

        elif (shapeType == "VC"):
            length = eval(infile.readline())
            width = eval(infile.readline())
            height = eval(infile.readline())
            cubeVolume = VC(length, width, height)
            print(format("Volume of a Cube","30s"),format(cubeVolume,"15.2f"))
            
        elif (shapeType == "SAC"):
            length = eval(infile.readline())
            cubeSurfaceArea = SAC(length)
            print(format("Surface Area of a Cube","30s"),format(cubeSurfaceArea,"15.2f"))

        elif (shapeType == "VR"):
            length = eval(infile.readline())
            width = eval(infile.readline())
            height = eval(infile.readline())
            rectPrismVolume = VC(length, width, height)
            print(format("Volume of a Rectangular Prism","30s"),format(rectPrismVolume,"15.2f"))

        elif (shapeType == "VS"):
            # read only one dimension for a circle
            radius = eval(infile.readline())
            sphereVolume = VS(radius)
            print(format("Volume of a Sphere","30s"),format(sphereVolume,"15.2f"))

        elif (shapeType == "SAS"):
            # read only one dimension for a circle
            radius = eval(infile.readline())
            sphereSurfaceArea = SAS(radius)
            print(format("Surface Area of a Sphere","30s"),format(sphereSurfaceArea,"15.2f"))

        # get calculation type, but wait on dimension(s)
        shapeType = (infile.readline()).strip()


    # close the file when you exit the while loop 
    infile.close()
    
main() 
