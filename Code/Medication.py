from TextFileInput import *

class Medication:
    # def __init__(self, expirationDate, medicationName, dayToDispense, timeLowerDispense, timeUpperDispense):
    #     self.medicationName = medicationName
    #     self.dayToDispense = dayToDispense
    #     self.timeLowerDispense = timeLowerDispense
    #     self.timeUpperDispense = ttimeLowerDispense
    #     self.expirationDate = expirationDate

    def __init__(self, pillTextFile):
        self.pillTextFile = pillTextFile
        self.file = open(self.pillTextFile, 'r')
        self.medicationName = self.file.readline()
        self.dayToDispense = self.file.readline()
        self.timeLowerDispense = self.file.readline()
        self.timeUpperDispense = self.file.readline()
        self.expirationDate = self.file.readline()
        self.file.close();


    # def getInfoFromFile():
    #     self.medicationName = self.file.readLine()
    #     self.dayToDispense = self.file.readLine()
    #     self.timeLowerDispense = self.file.readLine()
    #     self.timeUpperDispense = self.file.readLine()
    #     self.expirationDate = self.file.readLine()
    #     self.file.closeFile();

    def PrintInfo(self):
        print("Medication Name:", self.medicationName)
        print("Day to Dispense:", self.dayToDispense)
        print("Time Lower Dispense:", self.timeLowerDispense)
        print("Time Upper Dispense:", self.timeUpperDispense)
        print("Experation Date:", self.expirationDate)
