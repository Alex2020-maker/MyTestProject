import os 
from selenium import webdriver
import time

# open the browser
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input[@name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@name="email"]')
    input3.send_keys("Smolensk@mail.ru")

    # находим элемент <input type="file">
    
    element = browser.find_element_by_id("file")

    # заполняем элемент путём до загружаемого файла
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

    # находим элемент <input type="file">
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()



finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()