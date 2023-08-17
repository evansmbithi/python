import time
import sys

sys.stdout.reconfigure(encoding='utf-8') 
# print(sys.getfilesystemencoding())
# print(sys.getdefaultencoding())
# print(sys.stdout.encoding)

from functions import *
from dotenv import dotenv_values

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

# create a .env file with USERID and PASSWORD variables for tenjin
config = dotenv_values(".env")

try:
    driver = webdriver.Chrome('chromedriver') # check for webdriver locally
except:
    print('chromedriver not found locally')
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True) # prevent browser from closing indefinitely
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = chrome_options)

driver.maximize_window()
driver.implicitly_wait(5) # seconds

# default_frame = driver.switch_to.default_content()

def switch_to_iframe_by_xpath(val):
    driver.implicitly_wait(3) # seconds
    try:
        wait = WebDriverWait(driver, 10)
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, val)))
        # iframe = driver.find_element(By.XPATH,val)
        driver.switch_to.frame(iframe)
        return True
    except:
        print(f'Frame \'{val}\' NOT FOUND!!')
        return False
    finally:
        time.sleep(3)

def switch_to_iframe(val):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it(val))
        return True
    except:
        print(f'Frame \'{val}\' NOT FOUND!!')
        return False
    finally:
        time.sleep(3)

def reset_session():
    driver.get("https://finacle-preprod.co-opbank.co.ke/fininfra/ui/SSOLogin.jsp")
    
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.frame_to_be_available_and_switch_to_it('loginFrame'))
    found_frame = False
    while found_frame != True:
        found_frame = switch_to_iframe('loginFrame')
        if credentials_found(config) != True:
            # exit()
            break    

    login()
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        
        driver.switch_to.alert.accept()
        login()
        return True
    except:
        print('Login Alert')
        return False  

def credentials_found(env):
    try:
        user = env['USERID']
        return True
    except:
        return False

def login(): 
    try:
        wait = WebDriverWait(driver, 10)
        userid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#usertxt.txtbox')))
        try:
            userid.send_keys(config['USERID'])
        except:
            print('Please configure USERID')
            
    except:
        print('User text field NOT FOUND!!')
        relogin()

    password = driver.find_element(By.ID, 'passtxt')
    try:
        password.send_keys(config['PASSWORD'])
    except:
        print('Please configure PASSWORD')
        exit() # terminate run
    time.sleep(3)

    login = driver.find_element(By.ID, 'Submit')
    login.click()
    time.sleep(3)

def relogin():
    try:
        wait = WebDriverWait(driver, 10)
        loginbtn = wait.until(EC.element_to_be_clickable((By.NAME, 'Submit2')))
        print(loginbtn)
        loginbtn.click()
        login()
    except:
        print('Unable to login')
        reset_session()
        
def search_menu(menu):
    # time.sleep(3)
    try:
        driver.switch_to.default_content()    
    except:
        print('Unable to switch to default content')

    switch_to_iframe('loginFrame')

    try:                
        wait = WebDriverWait(driver, 10)
        userid = wait.until(EC.visibility_of_element_located((By.ID, 'menuSelect')))
        userid.send_keys(validate_search(menu))
        time.sleep(2)
        userid.send_keys(Keys.ENTER)
    except:
        print('Searcher NOT FOUND!!')
        relogin()
    # finally:
    #     time.sleep(10)

def in_formArea():
    switch_to_iframe_by_xpath("//iframe[@name='Core_FINPROD']")
    switch_to_iframe_by_xpath("//iframe[@name='UX']")
    switch_to_iframe_by_xpath("//iframe[@name='formArea']")
    return True


def error_on_acc(acc_no):
    if in_formArea():    
        try:
            wait = WebDriverWait(driver, 10)
            userid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#_disbursedet_finRow1 input#_acctNum"))) 
            # userid = driver.find_element(By.ID, "_acctNum")
            userid.send_keys(validate_search(acc_no))
        except:
            print('Acc input NOT FOUND!!')

        try:
            wait = WebDriverWait(driver, 10)
            go_btn = wait.until(EC.element_to_be_clickable((By.ID, '_disbursedet_BGo')))
            # go_btn = driver.find_element(By.ID, "_disbursedet_BGo")
            go_btn.click()
        except:
            print('Go btn NOT FOUND!!')

        try:
            driver.switch_to.parent_frame()
            wait = WebDriverWait(driver, 10)
            error_display = wait.until(EC.visibility_of_element_located((By.ID, 'errorPane_Pld')))
            return error_display.get_attribute('class')
        except:
            # print(acc_no)   
            return ''  
            
    else:
        print('You are probably not in FormArea!!')

def available_balance():
    switch_to_iframe_by_xpath("//iframe[@name='formArea']")    
    try:
        wait = WebDriverWait(driver, 10)
        userid = wait.until(EC.visibility_of_element_located((By.ID, "_avlForDisb_text"))) 
        return userid.get_attribute('innerHTML')
    except:
        print('Available balance NOT FOUND!!')

def logout():
    # time.sleep(3600)
    time.sleep(3)
    try:
        driver.switch_to.default_content()    
    except:
        print('Unable to switch to default content')
    
    switch_to_iframe('loginFrame')
   
    try:
        wait = WebDriverWait(driver, 10)
        logout_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@title='Logout']")))
        logout_btn.click()
    except:
        print('Logout btn NOT FOUND')
    
    
    # Handle logout alert
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        time.sleep(2)
        driver.switch_to.alert.accept()
        # return True
    except:
        print('Logout alert NOT HANDLED!')
        # return False 
    print('🎇Logged out successfully🎇!') 
    # time.sleep(3)
    driver.quit()
    exit()


    ####### REF #######
    # https://github.com/SergeyPirogov/webdriver_manager

    # change stdout encoding
    # http://xahlee.info/python/python_io_encoding.html
    # https://stackoverflow.com/questions/4374455/how-to-set-sys-stdout-encoding-in-python-3