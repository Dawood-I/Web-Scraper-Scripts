

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_experimental_option("debuggerAddress", "127.0.0.1:9922")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(executable_path='path\chromedriver.exe', chrome_options=options)
"""driver.get('http://melvoridle.com/index.php')"""
"""level = driver.find_element_by_id('skill-progress-level-3').text
level = level[0]
print(level)

level = driver.find_element_by_id('skill-progress-level-3"').text
level = level[0]
print(level)"""
while(True):

    cooksremainig = driver.find_element_by_xpath('//*[@id="cook-count"]')
    print(cooksremainig.text)
    while(cooksremainig.text != "-"):
        time.sleep(0.25)
        cooksremainig = driver.find_element_by_xpath('//*[@id="cook-count"]')

    try:
        driver.find_element_by_id("cook-button-qty-10").click()

    except NoSuchElementException:
        pass
    except ElementNotInteractableException:
        print("occurred at: ", time.clock())
        pass
