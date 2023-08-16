import re

# regex = '[^a-zA-Z0-9]'
# regex = '[^a-zA-Z]' 
regex = '[^0-9]' #same as [a-zA-Z]

with open('raw_data.txt', 'r') as input_data:
    extract = input_data.read()
    result = re.sub(regex, ' ', extract)
    nres = result.strip()

    with open('raw_data.txt', 'w') as output:
        output.write(nres)

# RUN python regx\regex.py 