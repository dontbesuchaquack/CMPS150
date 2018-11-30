#  Author:          Your Name
#  ULID/Section:    Your ULID & Section
#  lab12.py 

class Clock:

   def __init__(self, hrsIn, minsIn, secsIn):
      self.__hours = hrsIn
      self.__minutes = minsIn
      self.__seconds = secsIn


   def SetTime(self, newHrsIn, newMinsIn, newSecsIn):
      # write this class method
      self.__hours = newHrsIn
      self.__minutes = newMinsIn
      self.__seconds = newSecsIn

   def GetHours(self):
      return self.__hours

   def GetMinutes(self):
      # write this class method
      return self.__minutes

   def GetSeconds(self):
      # write this class method
      return self.__seconds

   def DisplayTime24(self):
      print("The time is ", end="")
      if (self.__hours < 10):
         print("0", end="")
      print(self.__hours,":", end="")
      if (self.__minutes < 10):
         print("0",end="")
      print(self.__minutes,":", end="")
      if (self.__seconds < 10):
         print("0", end="")
      print(self.__seconds, end="")
      print()
         # finish the rest of this class method
      

   def DisplayTime12(self):
      print("The time is ",end="")
      if (self.__hours < 12):
         # finish the rest of this class method
         tag = "AM"
         if (self.__hours < 10):
            if (self.__hours == 0):
               self.__hours = 12
               print(self.__hours, ":", end="")
               self.__hours = 0
            else:
               print("0", end="")
               print(self.__hours, ":", end="")
         else:
            print(self.__hours, ":", end="")
      elif (self.__hours == 12):
         tag = "PM"
         print(self.__hours, ":", end="")
      else:
         print(self.__hours - 12, ":", end="")
         tag = "PM"
      if (self.__minutes < 10):
         print("0", end="")
      print(self.__minutes,":", end="")
      if (self.__seconds < 10):
         print("0", end='')
      print(self.__seconds, ' ', end="")
      print(tag, end="")
      print()
         
         
         
         
   def ClockTick(self):
      self.__seconds = self.__seconds + 1
      if (self.__seconds == 60):
         self.__seconds = 0
         self.__minutes = self.__minutes + 1
         # finish the rest of this class method
      if (self.__minutes == 60):
         self.__minutes = 0
         self.__hours = self.__hours + 1
         if (self.__hours == 24):
            self.__hours = 0



def main():
   myClock = Clock(0,0,0)     # create a clock with a time of midnight
   myClock.DisplayTime12()    # display it with a 12-hour format
   myClock.DisplayTime24()    # display it with a 24-hour format
   print()

   myClock.SetTime(22,30,5)   # change the time to 10:30:05 PM
   myClock.DisplayTime12()    # display it with a 12-hour format
   myClock.DisplayTime24()    # display it with a 24-hour format
   print()

   myClock.SetTime(11,59,59)  # change the time to 11:59:59 AM
   myClock.DisplayTime12()    # display it with a 12-hour format
   myClock.DisplayTime24()    # display it with a 24-hour format
   print()

   myClock.ClockTick()        # clock tick of 1 second
   myClock.DisplayTime12()    # display new/current time in 12-hour format
   myClock.DisplayTime24()    # display new/current time in 24-hour format
                              
                              
   print()


main()
