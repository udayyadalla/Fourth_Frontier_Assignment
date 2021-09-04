import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
from elementactions import elementactions
from selenium import webdriver
from Variables import Variables
from Map import Map



class MyOperations:

    def __init__(self):
        chromedriver = Variables.data['ChromeDriverPath']
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.webactions = elementactions(self.driver)
        self.driver.get("http://google.com")
        self.driver.maximize_window()
        object = self.driver.find_element_by_name("q")
        # Opening automationpractice page here
        self.driver.get("http://automationpractice.com/index.php")

    def clickonsignin(self):
        try:
            self.driver.find_element_by_xpath(Map.Locators['signinbtn']).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(Map.Locators['enteremail']).send_keys(Variables.data['emailID'])
            time.sleep(2)
            self.driver.find_element_by_xpath(Map.Locators['createbutton']).click()
            time.sleep(2)
        except Exception as e:
            raise

    def enterpersonalinfo(self):
        try:
            self.driver.implicitly_wait(30)
            self.driver.find_element_by_xpath(Map.Locators['firstname']).click()
            self.driver.find_element_by_xpath(Map.Locators['firstname']).send_keys(Variables.data['firstn'])
            self.driver.find_element_by_xpath(Map.Locators['lastname']).send_keys(Variables.data['lastn'])
            self.driver.find_element_by_xpath(Map.Locators['passwordField']).send_keys(Variables.data['password'])
            self.driver.find_element_by_xpath(Map.Locators['selectdate']).click()
            self.driver.find_element_by_xpath(Map.Locators['selectmonth']).click()
            self.driver.find_element_by_xpath(Map.Locators['selectyear']).click()
            self.driver.find_element_by_xpath(Map.Locators['addressinfo']).send_keys(Variables.data['address'])
            self.driver.find_element_by_xpath(Map.Locators['addresscity']).send_keys(Variables.data['city'])
            self.driver.find_element_by_xpath(Map.Locators['addressstate']).click()
            self.driver.find_element_by_xpath(Map.Locators['addresszip']).send_keys(Variables.data['zipcode'])
            self.driver.find_element_by_xpath(Map.Locators['addressphnum']).send_keys(Variables.data['PhoneNumber'])
            self.driver.find_element_by_xpath(Map.Locators['addressalias']).send_keys(Variables.data['alias'])
            self.driver.find_element_by_xpath(Map.Locators['addressregister']).click()
            textonscreen = self.driver.find_element_by_xpath(Map.Locators['usertext'])
            textele = textonscreen.text
            print("\n\nText of an element is::",textele)
            time.sleep(3)
        except Exception as e:
            raise

    def shut_down(self):
        '''
            closing the browser
        '''
        self.driver.close()


opr = MyOperations()
opr.clickonsignin()
opr.enterpersonalinfo()
opr.shut_down()