from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import date, timedelta
import time


def ratesDownload():
    softAssertion = __import__('softassertions').SoftAssertions

    soft_assert = softAssertion()

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Navigate to a website

    driver.get('https://www.bog.gov.gh/treasury-and-the-markets/treasury-bill-rates/')

    currentDay = date.today()
    prevDay = currentDay - timedelta(days=1)
    DayNow = prevDay.strftime("%d %b %Y")
    TBill91 = dict()
    TBill182 = dict()
    TBill364 = dict()
    rates = {"91": TBill91, "182": TBill182, "364": TBill364}
    element_to_scroll_to = driver.find_element(By.ID, 'table_1_range_from_0')

    def enterDate(dateValue):
        driver.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll_to)
        element_to_scroll_to.send_keys(dateValue)
        element_to_scroll_to.send_keys(Keys.ENTER)
        time.sleep(10)

    display_date = driver.find_element(By.XPATH, '//table//tr[1]/td[1]').text.strip()
    if soft_assert.assert_equal(display_date, DayNow, "The date doesn't match"):
        enterDate(DayNow)
        time.sleep(10)
        TBillPeriod91 = driver.find_element(By.XPATH, '//table//tr[1]/td[3]').text
        TBill91Discount = driver.find_element(By.XPATH, '//table//tr[1]/td[4]').text
        TBill91Interest = driver.find_element(By.XPATH, '//table//tr[1]/td[5]').text
        TBill91.update({"duration": TBillPeriod91})
        TBill91.update({"discount": TBill91Discount})
        TBill91.update({"interest": TBill91Interest})

        TBillPeriod182 = driver.find_element(By.XPATH, '//table//tr[2]/td[3]').text
        TBill182Discount = driver.find_element(By.XPATH, '//table//tr[2]/td[4]').text
        TBill182Interest = driver.find_element(By.XPATH, '//table//tr[2]/td[5]').text
        TBill182.update({"duration": TBillPeriod182})
        TBill182.update({"discount": TBill182Discount})
        TBill182.update({"interest": TBill182Interest})

        TBillPeriod364 = driver.find_element(By.XPATH, '//table//tr[3]/td[3]').text
        TBill364Discount = driver.find_element(By.XPATH, '//table//tr[3]/td[4]').text
        TBill364Interest = driver.find_element(By.XPATH, '//table//tr[3]/td[5]').text
        TBill364.update({"duration": TBillPeriod364})
        TBill364.update({"discount": TBill364Discount})
        TBill364.update({"interest": TBill364Interest})
        return rates


    else:
        element_to_scroll_to.clear()
        element_to_scroll_to.send_keys(Keys.ENTER)
        time.sleep(10)
        latestDate = driver.find_element(By.XPATH, '//table//tr[1]/td[1]').text
        enterDate(latestDate)
        TBillPeriod91 = driver.find_element(By.XPATH, '//table//tr[1]/td[3]').text
        TBill91Discount = driver.find_element(By.XPATH, '//table//tr[1]/td[4]').text
        TBill91Interest = driver.find_element(By.XPATH, '//table//tr[1]/td[5]').text
        TBill91.update({"duration": TBillPeriod91})
        TBill91.update({"discount": TBill91Discount})
        TBill91.update({"interest": TBill91Interest})

        TBillPeriod182 = driver.find_element(By.XPATH, '//table//tr[2]/td[3]').text
        TBill182Discount = driver.find_element(By.XPATH, '//table//tr[2]/td[4]').text
        TBill182Interest = driver.find_element(By.XPATH, '//table//tr[2]/td[5]').text
        TBill182.update({"duration": TBillPeriod182})
        TBill182.update({"discount": TBill182Discount})
        TBill182.update({"interest": TBill182Interest})

        TBillPeriod364 = driver.find_element(By.XPATH, '//table//tr[3]/td[3]').text
        TBill364Discount = driver.find_element(By.XPATH, '//table//tr[3]/td[4]').text
        TBill364Interest = driver.find_element(By.XPATH, '//table//tr[3]/td[5]').text
        TBill364.update({"duration": TBillPeriod364})
        TBill364.update({"discount": TBill364Discount})
        TBill364.update({"interest": TBill364Interest})
        return rates