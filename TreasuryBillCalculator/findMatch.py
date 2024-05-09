from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import date,timedelta
import time
def findMatch(securityType):
    TBill91 = dict()
    TBill182 = dict()
    TBill364 = dict()

    dictionaryList = [TBill91, TBill182, TBill364]

    types = ['364 DAY BILL', '91 DAY BILL', '182 DAY BILL']
    for i in types:
        for j in dictionaryList:
            if securityType == i:
                TBill91Discount = driver.find_element(By.XPATH, '//table//tr[1]/td[4]').text
                TBill91Interest = driver.find_element(By.XPATH, '//table//tr[1]/td[5]').text
                TBill91.update({"duration": TBillPeriod91})
                TBill91.update({"discount": TBill91Discount})
                TBill91.update({"interest": TBill91Interest})
