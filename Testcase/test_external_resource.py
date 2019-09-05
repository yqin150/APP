import pytest,allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
@allure.feature("Test external resource")

class TestAccess:

    @allure.story("user can see external resource in front page")
    @allure.description("external resource is belowed in recommend pgae")
    def test_accessTableau(self):
        self.driver.get(self.dev_url + '/reports/recommended')
        locator = (By.XPATH, '//div[1]/h1')
        WebDriverWait(self.driver, 25).until(EC.presence_of_element_located(locator))
        centerText = self.driver.find_element_by_xpath('//div[3]/div[3]/h1').text
        print(centerText)
        assert 'External Resource' in centerText




