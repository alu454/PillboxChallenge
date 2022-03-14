class TextFileInput:
    def __init__(self, pillTextFile):
        self.pillTextFile = pillTextFile
        self.file = open(self.pillTextFile, 'r')


    # def openFile(self):
    #     file = open(self.pillTextFile, 'r')
    def closeFile(self):
        self.file.close()
    def readLine(self):
        return self.file.readline()
