from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get(" http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_xpath('//button[text()="Book"]')
button.click()

# to do task

x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_xpath('//input[@class="form-control"]')
input1.send_keys(y)

button = browser.find_element_by_xpath('//button[text()="Submit"]')
button.click()

time.sleep(10)

# закрываем браузер после всех манипуляций

browser.quit()
