import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import allure


@pytest.fixture(scope="class")
def setup(request):
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    dev_url = 'https://dev.xxx.xxx.com'
    driver = webdriver.Chrome(path_dir + '/chromedriver')
    print("initial")
    driver.get('https://login.microsoftonline.com')
    driver.find_element_by_xpath("//input[@type='email']").send_keys("test@test.com")
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(5)
    driver.find_element_by_id('username').send_keys('test@test.com')
    driver.find_element_by_id('password').send_keys('test@test.com')
    driver.find_element_by_css_selector("a[title='登录']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(5)
    driver.get(dev_url)
    time.sleep(15)
    request.cls.driver = driver
    request.cls.dev_url = dev_url

    yield driver
    print("quit")
    driver.close()






