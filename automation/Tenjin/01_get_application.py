import csv
import time

from selenium.webdriver.common.by import By
from script import switch_to_content_frame, driver, logout
from selenium.webdriver.support.ui import Select

switch_to_content_frame()

# read csv file and extract menus
with open('menus.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Initialize an empty list to store the column data
    menus = []

    # Loop through each row in the CSV file
    for row in reader:        
        menus.append(row[0])

# 2d array to be converted to csv
array_out = [
    ['Menu', 'Application', 'Fields_learnt']
]

# loop through the application options
select = Select(driver.find_element(By.CSS_SELECTOR, 'select#application'))
options = select.options

counter = 1

while counter <= len(menus):
    initial_learnt = 0
    col1 = ''
    col2 = ''
    print(counter, ',', menus[counter])

    for index in range(1, len(options)):
        # select.select_by_index(index)
        option = driver.find_element(By.CSS_SELECTOR, f"select#application option:nth-child({index + 1})")
        option.click()
        getOption = option.get_attribute('innerHTML')
        
        # print(initial_learnt)
        
        

        time.sleep(2)
        # click go
        driver.find_element(By.ID, 'btnSearchFunctions').click()

        time.sleep(2)

        # find search input and pass menu
        search = driver.find_element(By.ID, 'functionsTable_search')
        search.send_keys(menus[counter])

        # get search result
        try:
            # menu name
            result = driver.find_element(By.CSS_SELECTOR, "#functionsTable td:nth-child(2)")
        except:
            # print('No match found')
            continue            
        
        # if result available:
        #   take the application option
        col1 = menus[counter] # function code/menu item
        fields_learnt = driver.find_element(By.CSS_SELECTOR, "#functionsTable > tbody > tr > td:nth-child(7)").get_attribute('innerHTML')
        

        if col1 == result.get_attribute('innerHTML'):
            if fields_learnt != 'N/A':
                no_of_fields = int(fields_learnt) # convert to integer
                if no_of_fields > initial_learnt:
                    initial_learnt = no_of_fields
                    col2 = getOption                 
                
    # insert row to 2d array
    array_out.insert(counter, [col1, col2, initial_learnt])

    # write to csv
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        for row in array_out:
            writer.writerow(row)
    
    # increment counter
    counter = counter + 1

logout()