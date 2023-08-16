import time

from selenium.webdriver.common.by import By
from script import switch_to_content_frame, driver, logout
from selenium.webdriver.support.ui import Select
import pandas as pd

# read output file -> fetch Menu,Application columns

# read the CSV file into a pandas DataFrame
df = pd.read_csv('output.csv')

# extract the "Menu" and "Application" columns into arrays
menus = df['Menu'].values
applications = df['Application'].values

# print the arrays
print(menus)
print(applications)

switch_to_content_frame()


for counter in range(0, len(menus)):
    # select application
    # loop through the application options
    select = Select(driver.find_element(By.CSS_SELECTOR, 'select#application'))

    # select the application Option value by visible text
    select.select_by_visible_text(applications[counter])
    # click go
    driver.find_element(By.ID, 'btnSearchFunctions').click()

    time.sleep(2)

    # search menu
    search = driver.find_element(By.ID, 'functionsTable_search')
    search.send_keys(menus[counter])

    time.sleep(3)
    
    # if result contains multiple menus
    # find the menu in question and click download

    row_number = 1 # starts from first row
    col1 = menus[counter] # function code/menu item
    # get search result
    try:
        # menu name
        result = driver.find_element(By.CSS_SELECTOR, "#functionsTable td:nth-child(2)")
    except:
        # print('No match found')
        continue            
    
    # if result available:
    # capture fields learnt
    fields_learnt = driver.find_element(By.CSS_SELECTOR, f"#functionsTable > tbody > tr:nth-child({row_number}) > td:nth-child(7)").get_attribute('innerHTML')

    #Do...While loop
    while col1 != result.get_attribute('innerHTML'):
        row_number = row_number+1
        # get search result
        try:
            # menu name
            result = driver.find_element(By.CSS_SELECTOR, f"#functionsTable > tbody > tr:nth-child({row_number}) > td:nth-child(2)")
        except:
            # print('No match found')
            continue            
        
        # if result available:
        #   take the application option
        fields_learnt = driver.find_element(By.CSS_SELECTOR, f"#functionsTable > tbody > tr:nth-child({row_number}) > td:nth-child(7)").get_attribute('innerHTML')
        
    
    # Click download
    try:
        driver.find_element(By.CSS_SELECTOR, f"#functionsTable > tbody > tr:nth-child({row_number}) > td:nth-child(6) > a").click()
    except:
        print('Download button not found')

    time.sleep(2)

    # go to sub-frame
    iframe = driver.find_element(By.CSS_SELECTOR, "div.subframe > iframe#ttd-options-frame")

    # switch to selected iframe
    driver.switch_to.frame(iframe)

    # click go
    driver.find_element(By.ID, "btnOk").click()

    time.sleep(2)

    # leave the child frame
    driver.switch_to.parent_frame()


logout()