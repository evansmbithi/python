
# https://github.com/SergeyPirogov/webdriver_manager

import time

from dotenv import dotenv_values

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# create a .env file with USERID and PASSWORD variables for tenjin
config = dotenv_values(".env")

# driver = webdriver.Chrome('chromedriver')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://172.16.20.146:8083/TenjinWeb/")

def login():
    userid = driver.find_element(By.ID, 'txtLoginName')
    userid.send_keys(config['USERID'])

    password = driver.find_element(By.ID, 'txtPassword')
    password.send_keys(config['PASSWORD'])

    login = driver.find_element(By.ID, 'btnLogin')
    login.click()

def switch_to_content_frame():

    login()

    time.sleep(2)

    try:
        driver.find_element(By.ID, 'select2-lstDomain-container').click()        
    except Exception:
        print('Clearing session')
        driver.get(f"http://172.16.20.146:8083/TenjinWeb/TenjinSessionServlet?t=clear_session&paramval={config['USERID']}")
        login()
        driver.find_element(By.ID, 'select2-lstDomain-container').click()

    driver.find_element(By.CSS_SELECTOR, '#select2-lstDomain-results li').click()

    #load project
    driver.find_element(By.ID, 'btnLoadProject').click()

    time.sleep(2)

    # wait until element is found

    # adminPanel
    driver.find_element(By.ID, 'adminPanel').click()

    # application manu
    driver.find_element(By.ID, 'ui-id-4').click()

    time.sleep(2)

    # select function
    driver.find_element(By.CSS_SELECTOR, 'div#ui-id-5 > div:nth-child(2) a').click()


    # switchto content frame
        # Store iframe web element
    iframe = driver.find_element(By.CSS_SELECTOR, ".content > iframe")

        # switch to selected iframe
    driver.switch_to.frame(iframe)
  
# print(menus)

# Content moved to extract_application.py

def logout():

    # leave the frame
    driver.switch_to.parent_frame()

    #logout
    driver.find_element(By.ID, 'logout').click()
    print('🎇 Test completed successfully! 🎇')

    time.sleep(3)
    driver.quit()