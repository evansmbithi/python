import sys
sys.path.append('.\\app') # assumes app contents are in this directory

from functions import remove_csv_duplicates,capture_csv
from script import logout,search_menu,error_on_acc,reset_session,available_balance
import pandas as pd

reset_session()

input = "./PLD/data/input.csv"
tried = "./PLD/data/tried_acc.csv"
zero_bal = "./PLD/data/zero_bal.csv"
pld_acc = "./PLD/pld_acc.csv"

# input = path_to_csv('input') # "./PLD/data/input.csv"
# tried = path_to_csv('tried_acc')
# pld_acc = path_to_csv('pld_acc')

# read the CSV file into a pandas DataFrame
try:
    df = pd.read_csv(input)
except:
    print(f"Please create '{input}' with column 'ACC'")
    logout()

# extract the "Menu" column into an array
# account = df['ACC'].values
account = df['ACC'].unique() # remove duplicates

# print(account)

for counter in range(0, len(account)):
    search_menu('PLD')

    # if error class='hidden' pick the account
    # means the account does not have any issue/error
    if error_on_acc(account[counter]) != '':
        if str(available_balance()) == 'KES 0.00': 
            # trash any account with zero balance
            capture_csv(tried,account[counter],"zero bal")
            continue
        else:
            capture_csv(pld_acc,account[counter])
    else:
        capture_csv(tried,account[counter])

remove_csv_duplicates(pld_acc, "acc_no")
remove_csv_duplicates(tried, "acc_no")

logout()

