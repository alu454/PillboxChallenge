import time
import pyfirmata

current_time = time.localtime(time.time())
#Note Monday is day 0
print("Day of the week:", current_time.tm_wday)
print("Current Hour:", current_time.tm_hour)
print("Minute of the hour:", current_time.tm_min)


def isRightDay(userDay):
    if userDay == current_time.tm_wday:
        return True
    else:
        return False

def isRightTime(userTime1, userTime2):
    if userTime1 <= current_time.tm_hour <= userTime2:
        return True
    else:
        return False

#Checks if can pills given the day, and two time period in which the method returns true
def canDispense(userDay, userTime1, userTime2):
    if(isRightDay(userDay) == True and isRightTime(userTime1, userTime2) == True):
        return True
    else:
        return False

print("Checking Date:", isRightDay(3))
print("Checking Time:", isRightTime(10,14))
print("Can Disense?:", canDispense(2,12,14))
print("Can Disense?:", canDispense(3,10,12))
print("Can Disense?:", canDispense(3,12,14))
