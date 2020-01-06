from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = r'C:\develop\chromedriver.exe'


def test0():
    driver = webdriver.Chrome(executable_path=driver_path)

    driver.get("http://www.python.org")

    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)


def test1():
    driver = webdriver.Chrome()
    driver.get("https://xa.zu.anjuke.com/?kw=%E5%90%89%E6%BA%90%E7%BE%8E%E9%83%A1&k_comm_id=275154")
    try:

        for i in range(10):
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.aNxt")))
            element.click()

    finally:
        driver.quit()


def test2():
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("http://www.python.org")

    driver.find_element_by_id("id")
    driver.find_element(By.ID, 'id')

    driver.find_element_by_name('name')
    driver.find_element(By.NAME, 'name')

    driver.find_element_by_class_name('class name')
    driver.find_element(By.CLASS_NAME, 'class name')

    driver.find_element_by_css_selector('css')
    driver.find_element(By.CSS_SELECTOR, 'css')

    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    test0()
