# Author:         Kristlyn Montoya
# ULID/Section:   C00425573 / Section 01
# Lab #10

def main():
    # open the file
    infile = open("trees.py", 'r')

    # print the column headings
    print("\nJob Type   Hrs/Trees    Cost")
    print("----------------------------")

    # read the first set of data
    job = infile.readline().strip()
    num = eval(infile.readline())


    # initialize any needed variables (maximums)
    maximum = 0
    jtype = 0
    hours = 0
    # sentinel-controlled while loop

    while job != '###':
        
        # assign cost by calling a function (pass the data items read)
        total = cost(job,num)
        
        # print data items read and cost computed by function
        print(format(job, '6s'), format(num, '10d'), format(total, '10d'))

        # update maximums
        
        if total > maximum:
            maximum = total
            jtype = job
            hours = num
            
        

        # read next data set
        job = infile.readline().strip()
        num = eval(infile.readline())


    # print maximums
    print("----------------------------")
    print("\nMost Expensive Job")
    print(format(jtype, '6s'), format(hours, '10d'), format(maximum, '10d'))

    # close file    
    infile.close()

# function to compute the cost of the job
def cost(job,num):
    if job == 'TRIM':
        cost = num * 80
    elif job == 'REMOVE':
        cost = num * 500
    return cost


# call main to begin program
main()


