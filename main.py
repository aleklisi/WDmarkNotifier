from time import sleep
from loginToWD import getAllMarksFromWebpage
from fileOps import readPreviousMarks, writeNewMarks
from mailService import sendEmail

user = "mysmtp@gmail.com"
pwd = "mypassword"
login = "mysmtp"
recipient = "notifiedmail@mail.com"
subject = "new Subject"
body = """
    Hi,
    this is ecample message.
    Regards,
    me
"""

chrmoedriverPath = 'path/to/chromedriver.exe'

indexNumber = "my index number"
WDpassword = "my WD password"

while(True):
    marksFromWebpage = getAllMarksFromWebpage(indexNumber,WDpassword,chrmoedriverPath)
    stringFromWebpage = " ".join(marksFromWebpage)
    previousMarks = readPreviousMarks()

    if(previousMarks != stringFromWebpage):
        sendEmail(user, pwd,recipient,subject,body, login)
        print("Mail sent!!!")
        writeNewMarks(stringFromWebpage)
        print("FileUpdated")

    sleep(60)
    print("Program still works :)")
