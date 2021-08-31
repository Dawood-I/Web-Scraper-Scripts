



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
#foodhp = int(driver.find_element_by_xpath('//*[@id="combat-food-container"]').text[7:9])
while(True):
    try:
        currentHP = driver.find_element_by_xpath('//*[@id="combat-player-hitpoints-current"]').get_attribute("innerHTML")
        #foodhp = int(driver.find_element_by_xpath('//*[@id="combat-food-container"]').text[7:9])
        totalHP = driver.find_element_by_xpath('//*[@id="combat-player-hitpoints-max"]').get_attribute("innerHTML")
        totalHP = int(totalHP)
        img = driver.find_element_by_xpath('//*[@id="combat-food-container"]/div/button[1]/img').get_attribute("src")
        if img == "https://melvoridle.com/assets/media/skills/combat/food_empty.svg":
           driver.find_element_by_xpath('//*[@id="combat-enemy-options"]/p/button').click()
        if int(currentHP) <= (totalHP-14):
            driver.find_element_by_xpath('//*[@id="combat-food-container"]/div/button[1]').click()
            currentHP = driver.find_element_by_xpath('//*[@id="combat-player-hitpoints-current"]').get_attribute("innerHTML")

    except ValueError:
        pass

