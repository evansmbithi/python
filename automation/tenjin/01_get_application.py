import csv
import time
import datetime
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from script import switch_to_content_frame, driver, validate_search, logout

switch_to_content_frame()

#=====OLD=====
# read csv file and extract menus
# with open('menus.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')

#     # Initialize an empty list to store the column data
#     menus = []

#     # Loop through each row in the first column
#     for row in reader:        
#         menus.append(row[0])

#====NEW=====
input = 'menus.csv'
try:
    df = pd.read_csv(input)
except:
    print(f"Please create '{input}' with column 'MENUS'")
    
menus = df['MENUS'].unique() # remove duplicates
# menus = data.insert(0,'MENUS')
# print(menus)

# 2d array to be converted to csv
array_out = [
    ['Menu', 'Application', 'Fields_learnt']
]

# loop through the application options
select = Select(driver.find_element(By.CSS_SELECTOR, 'select#application'))
options = select.options

counter = 1
row_number = 1 # starts from first row

# Log results
with open('log.txt', 'a+') as logs: # 'a+' Append to existing. Creates a new file, if none exists
    log_date = f"\n=================={datetime.datetime.now()}=======================\n"
    log_header = "\nMENU\t\tAPPLICATION\t\tFIELDS_LEARNT\n"
    logs.write(log_date)
    logs.write(log_header)

    while counter <= len(menus):
        menu = menus[counter-1]
        initial_learnt = 0
        search_input = ''
        col2 = ''
        try:
            print(counter, ',', menu)
        except IndexError:
            print('Process Complete')
            break

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

            row_number = 1
            search_input = validate_search(menu) # function code/menu item

            # find search input and pass menu
            search = driver.find_element(By.ID, 'functionsTable_search')
            search.send_keys(search_input)

            #Do...While loop

            # get search result
            # try:
            #     # menu name
            #     result = driver.find_element(By.CSS_SELECTOR, "#functionsTable td:nth-child(2)")
            # except:
            #     # print('No match found')
            #     continue            
            
            # # if result available:
            # # capture fields learnt
            # fields_learnt = driver.find_element(By.CSS_SELECTOR, f"#functionsTable > tbody > tr:nth-child({row_number}) > td:nth-child(7)").get_attribute('innerHTML')
            
        
            # while search_input != result.get_attribute('innerHTML'):
                
            #     # get search result
            #     try:
            #         # menu name
            #         result = driver.find_element(By.CSS_SELECTOR, f"#functionsTable > tbody > tr:nth-child({row_number+1}) > td:nth-child(2)")
            #     except:
            #         # print('No match found')
            #         continue            
                
            #     # if result available:
            #     #   take the application option
            #     fields_learnt = driver.find_element(By.CSS_SELECTOR, f"#functionsTable > tbody > tr:nth-child({row_number+1}) > td:nth-child(7)").get_attribute('innerHTML')

            # loop through child elements of results tbody
            parent_node = driver.find_element(By.CSS_SELECTOR, f"#functionsTable > tbody")
            
            # child_nodes = parent_node.find_elements(By.XPATH, "./child::*")
            child_nodes = parent_node.find_elements(By.XPATH, "./tr")

            # print(len(child_nodes))


            for item in child_nodes:

                # get search result
                try:
                    # menu name
                    # result = driver.find_element(By.CSS_SELECTOR, "#functionsTable td:nth-child(2)")
                    result = driver.find_element(By.CSS_SELECTOR, f"#functionsTable > tbody > tr:nth-child({row_number}) > td:nth-child(2)")
                                    
                except:
                    # print('No match found')
                    continue            
                
                # if result available:
                # capture fields learnt
                fields_learnt = driver.find_element(By.CSS_SELECTOR, f"#functionsTable > tbody > tr:nth-child({row_number}) > td:nth-child(7)").get_attribute('innerHTML')

                row_number = row_number+1 # loop through each child row in results
                
                print(result.get_attribute('innerHTML'), " ", getOption, " ", fields_learnt) # view results of search
                
                log = f"{result.get_attribute('innerHTML')}\t\t{getOption}\t\t{fields_learnt}\n"
                logs.write(log) # write results to log.txt

                if search_input == result.get_attribute('innerHTML'):
                    if fields_learnt != 'N/A':
                        no_of_fields = int(fields_learnt) # convert to integer
                        if no_of_fields > initial_learnt:
                            initial_learnt = no_of_fields
                            col2 = getOption                
                
        # insert row to 2d array
        array_out.insert(counter, [search_input, col2, initial_learnt])

        # write to csv
        with open('output.csv', mode='w', newline='') as file:
            writer = csv.writer(file)

            for row in array_out:
                writer.writerow(row)
        
        # increment counter
        counter = counter + 1

logout()