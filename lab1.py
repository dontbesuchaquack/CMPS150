#Author: Kristlyn Montoya
#ULID/Section: C00425573 CMPS-150-01

#get user input
myCity = input("Enter your home town: ")
speed = eval(input("Enter the speed of a vehicle at mph: "))
hours = eval(input("Enter the hours a vehicle traveled: "))

#compute distance vehicle traveled
distance = speed * hours

#print output
print()
print("Your home town is:", myCity)
print("The vehicle traveled", distance, "miles!")
