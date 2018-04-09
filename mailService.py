import smtplib

def sendEmail(user, pwd, recipient, subject, body, login):
    FROMADDR = user
    LOGIN = login
    PASSWORD = pwd
    TOADDRS = [recipient]
    SUBJECT = subject

    msg = body

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(LOGIN, PASSWORD)
    server.sendmail(FROMADDR, TOADDRS, msg)
    server.quit()