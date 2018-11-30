#  Author:          Kristlyn Montoya
#  ULID/Section:    C00425573 & Section 01
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
      self.__newSecsIn = secsIn
      

   def GetHours(self):
      return self.__hours

   def GetMinutes(self):
      # write this class method
      return self.__minutes

   def GetSeconds(self):
      # write this class method
      return self.__seconds

   def DisplayTime24(self):
      print("The time is",format(self.__hours,"2d"),": ",end="")
      if (self.__minutes < 10):
         print("0",end="")
         # finish the rest of this class method
      elif self.__minutes % 59 > 1:
         leftoverminutes = self.__minutes % 60
         hours = int(self.__minutes / 60)
         secs = self.GetSeconds
         self.SetTime(hours, leftovermins,secs)
      if (self.__hours > 12):
         
         

   def DisplayTime12(self):
      print("The time is ",format(self.__hours, '2d'), ":",end="")

      if (self.__hours <= 12):
         # finish the rest of this class method

   def ClockTick(self):
      self.__seconds = self.__seconds + 1
      if (self.__seconds == 60):
         self.__seconds = 0
         self.__minutes = self.__minutes + 1
         # finish the rest of this class method



def main():
   myClock = Clock(0,0,0)     # create a clock with a time of midnight
   myClock.DisplayTime12()    # display it with a 12-hour format
   myClock.DisplayTime24()    # display it with a 24-hour format
   print()

   myClock.SetTime(22,30,05)  # change the time to 10:30:05 PM
   myClock.DisplayTime12()    # display it with a 12-hour format
   myClock.DisplayTime24()    # display it with a 24-hour format
   print()

   myClock.SetTime(11,59,59)  # change the time to 11:59:59 AM
   myClock.DisplayTime12()    # display it with a 12-hour format
   myClock.DisplayTime24()    # display it with a 12-hour format
                              # display it with a 24-hour format
   print()

                              # clock tick of 1 second
                              # display new/current time in 12-hour format
                              # display new/current time in 24-hour format
   print()


main()
