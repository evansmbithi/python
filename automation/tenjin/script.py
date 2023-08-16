
# https://github.com/SergeyPirogov/webdriver_manager

import time

from dotenv import dotenv_values

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create a .env file with USERID and PASSWORD variables for tenjin
config = dotenv_values(".env")

try:
    driver = webdriver.Chrome('chromedriver')
except:
    print('chromedriver not found locally')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://172.16.20.146:8083/TenjinWeb/")

def validate_search(input):
    menu_name = str(input).strip()
    return menu_name

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
        # driver.get(f"http://172.16.20.146:8083/TenjinWeb/TenjinSessionServlet?t=clear_session&paramval={config['USERID']}")
        # login()
        driver.get(f"http://172.16.20.146:8083/TenjinWeb/TenjinSessionServlet?t=clear_session&txtLoginName={config['USERID']}&txtPassword={config['PASSWORD']}")
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
    # driver.find_element(By.CSS_SELECTOR, 'div#ui-id-5 > div:nth-child(2) a').click()
    try:
        wait = WebDriverWait(driver, 10)
        func = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#ui-id-5 > div:nth-child(2) a')))
        func.click()
    except:
        print('Function button took too long')


    # switchto content frame
        # Store iframe web element
    iframe = driver.find_element(By.CSS_SELECTOR, ".content > iframe")

        # switch to selected iframe
    driver.switch_to.frame(iframe)

  
# print(menus)

# Content moved to extract_application.py

def logout():

    # leave the frame
    driver.switch_to.default_content()
    # driver.switch_to.parent_frame()
    time.sleep(10)

    #logout
    try:
        driver.find_element(By.ID, 'logout').click()
    except:
        print('🎇 Test completed successfully! 🎇')

    time.sleep(2)
    driver.quit()