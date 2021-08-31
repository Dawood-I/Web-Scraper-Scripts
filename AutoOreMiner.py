from selenium import webdriver

import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_experimental_option("debuggerAddress", "127.0.0.1:9922")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(executable_path='path\chromedriver.exe', chrome_options=options)
"""driver.get('http://melvoridle.com/index.php')"""

"""python_button1 = driver.find_elements_by_xpath('//*[@id="sidebar"]/div[1]/div[2]/div/div/div/div[2]/ul/li[15]/a')
python_button1.click()"""
# click radio button
rune = driver.find_element_by_xpath('//*[@id="mining-ore-8"]/a')
adamant = driver.find_element_by_xpath('//*[@id="mining-ore-7"]/a')
mythril = driver.find_element_by_xpath('//*[@id="mining-ore-6"]/a')
coal = driver.find_element_by_xpath('//*[@id="mining-ore-3"]/a')
def getsize(x):
    if x == "rune":
        x = driver.find_element_by_xpath('//*[@id="mining-rock-hp-8"]').size["width"]
    elif x == "adamant":
        x = driver.find_element_by_xpath('//*[@id="mining-rock-hp-7"]').size["width"]
    return x
for i in range(15000):
    rune.click()
    runesize = getsize("rune")
    adamantsize = getsize("adamant")
    while runesize!=0:
        time.sleep(0.25)
        runesize = getsize("rune")
        adamantsize = getsize("adamant")
    adamant.click()
    while runesize == 0:
        time.sleep(0.25)
        adamantsize = getsize("adamant")
        runesize = getsize("rune")
        if adamantsize == 0:
            mythril.click()
            while adamantsize == 0 and runesize ==0:
                time.sleep(0.25)
                adamantsize =  getsize("adamant")
                runesize = getsize("rune")

