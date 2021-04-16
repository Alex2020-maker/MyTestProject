from selenium import webdriver
import math
import time

# open the browser
try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # Read the value for the variable x

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x = x_element.text
    y = calc(x)

    # Scroll down the page

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Enter the answer in the text field

    inputAnswer = browser.find_element_by_xpath('//input[@class="form-control"]')
    inputAnswer.send_keys(y)

    # Select checkbox and select robots

    option1 = browser.find_element_by_css_selector('[type="checkbox"]')
    option1.click()

    option1 = browser.find_element_by_css_selector('[value="robots"]')
    option1.click()

    # click button

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
