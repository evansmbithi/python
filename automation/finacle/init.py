import sys
import subprocess
import os

sys.path.append('.\\app')
from functions import capture_text

def init(args=sys.argv[1]):
    menu = str(args).upper()
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Define paths to the external scripts
    script1_path = os.path.join(current_directory, menu, f"{menu}.py")

    # Run script1.py
    print(f"Running {menu}.py:")
    log = subprocess.run(["python", script1_path], shell=True, capture_output=True, encoding="utf-8")
    print(log.stdout)
    if log.stderr:
        print('An error occurred, please check the logs.')
    capture_text('logs.txt',log.stdout,log.stderr)

init()

####### REF ######
# Python Sub-processes
# https://www.datacamp.com/tutorial/python-subprocess

# encoding
# https://discuss.python.org/t/deprecating-text-option-in-subprocess/14280/2