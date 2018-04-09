def readPreviousMarks():
    file = open("oceny.txt","r")
    fileContent = file.read()
    file.close()
    return fileContent

def writeNewMarks(txt):
    file = open("oceny.txt", "w")
    file.write(txt)
    file.close()

