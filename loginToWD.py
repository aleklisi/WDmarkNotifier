from selenium.webdriver.common.keys import Keys
from selenium import webdriver

def getAllMarksFromWebpage(login,password,chrmoedriverPath):

    driver = webdriver.Chrome(chrmoedriverPath)
    driver.get("https://dziekanat.agh.edu.pl/OcenyP.aspx")
    driver.maximize_window()

    loginElem = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder_MiddleContentPlaceHolder_txtIdent")
    loginElem.clear()
    loginElem.send_keys(login)

    passwdElem = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder_MiddleContentPlaceHolder_txtHaslo")
    passwdElem.clear()
    passwdElem.send_keys(password)

    passwdElem.send_keys(Keys.ENTER)
    result = []

    for i in range(2,22):
        for j in range(4,7):
            xpath = '//*[@id="ctl00_ctl00_ContentPlaceHolder_RightContentPlaceHolder_dgDane"]/tbody/tr[{0}]/td[{1}]'.format(i,j)
            cell = driver.find_element_by_xpath(xpath)
            result += [cell.text]

    driver.quit()

    return result

