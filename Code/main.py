from Scheduler import *
from TextFileInput import *
from Medication import *

# S1 = Scheduler(2,12,14)
# S2 = Scheduler(0,11,13)
# S3 = Scheduler(0,1,11)

# T1 = TextFileInput("pillInfo.txt")
# print(T1.readLine())
# print(T1.readLine())
# print(T1.readLine())
# print(T1.readLine())



print("Program Running")

M1 = Medication("pillInfo.txt")

M1.PrintInfo()


# print("Can Disense?:", S1.canDispense())
# print("Can Disense?:", S2.canDispense())
# print("Can Disense?:", S3.canDispense())
