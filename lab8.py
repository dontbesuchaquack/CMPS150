# Author:         Kristlyn Montoya
# ULID/Section:   C00425573 | Section 01
# lab8.py 

#****************** LAB Average  ******************

def labAvg(infile):

    g1 = eval(infile.readline())
    g2 = eval(infile.readline())
    g3 = eval(infile.readline())
    g4 = eval(infile.readline())
    g5 = eval(infile.readline())
    g6 = eval(infile.readline())
    g7 = eval(infile.readline())
    
    print(format("Lab Grades:", '12s'),g1,g2,g3,g4,g5,g6,g7)
    sum = g1+g2+g3+g4+g5+g6+g7 

    avg = sum / 7    # computes avg
    avg = avg / 10 * 100  # computes % (because labs are worth 10 points)
    return avg

#****************** PA Average  ****************** 

def paAvg(infile):

    g1 = eval(infile.readline())
    g2 = eval(infile.readline())
    g3 = eval(infile.readline())
    
    print(format("PA Grades:", '12s'),g1,g2,g3)
    sum = g1+g2+g3

    avg = sum / 3    # computes avg
    avg = avg / 100 * 100  # computes % (because pas are worth 100 points)

    return avg
 
#****************** EXAM Average  ****************** 

def examAvg(infile):

    g1 = eval(infile.readline())
    
    print(format("Exam Grades:", '12s'),g1)
    sum = g1

    avg = sum / 1    # computes avg
    avg = avg / 100 * 100  # computes % (because exams are worth 100 points)

    return avg
 
#****************** MAIN/DRIVER  ******************
def main(): 
    # main will call each of your average functions
    # to compute each components of overall class avg
    # call the function to compute your LAB average
    # put the return value in the variable labAverage 

    infile = open("lab8_grades.py",'r')
    labAverage = labAvg(infile) 

    # call the function to compute your PA average
    paAverage = paAvg(infile)

    # call the function to computer your EXAM average
    examAverage = examAvg(infile)
    # close the file
    infile.close()

    # compute your OVERALL class average using the weights
    # provided on the lab instruction sheet 
    overallAverage =  (labAverage * 0.1) + (paAverage * 0.15) + (examAverage * 0.75)


    # print results
    print("  Lab Average =", format(labAverage, '.2f'), "%")
    print("   PA Average =", format(paAverage, '6.2f'), "%")
    print(" Exam Average =", format(examAverage, '6.2f'), "%")
    print("-------------")
    print("Class Average =", format(overallAverage, '6.2f'), "%")


main() 
