import time
import pyfirmata

#Note Monday is day 0



class Scheduler:

    #Default Constructor takes in the date of the pill, time1 which is the lower bound for pill to be dispensed and upper bound for pill to be disnped
    def __init__(self,userDay,userTime1, userTime2):
        self.userDay = userDay
        self.userTime1 = userTime1
        self.userTime2 = userTime2
        self.current_time = time.localtime(time.time())

    def isRightDay(self):
        if self.userDay == self.current_time.tm_wday:
            return True
        else:
            return False

    def isRightTime(self):
        if self.userTime1 <= self.current_time.tm_hour <= self.userTime2:
            return True
        else:
            return False

    #Checks if can pills given the day, and two time period in which the method returns true
    def canDispense(self):
        if(self.isRightDay() == True and self.isRightTime() == True):
            return True
        else:
            return False
