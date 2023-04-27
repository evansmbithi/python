import csv
import numpy as np

# Open the CSV file using a with statement
with open('raw.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile, delimiter=',')

    # Initialize an empty list to store the column data
    column_data = []

    # Loop through each row in the CSV file
    for row in reader:        
        column_data.append(row[0])
        # Append the value in the third column to the column_data list
        # column_data.append(row[2])

# Print the column data
# print(column_data)

# my_array = []
# extract 39,999 items from array
# for x in range(0,39999):
#     my_array.append(column_data[x])

# print(my_array)

# reshape the array into a 2D array with 202 rows and 199 columns
my_2d_array = np.array(column_data).reshape((202, 199))

# print the resulting 2D array
# print(my_2d_array)


# write to csv
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    for row in my_2d_array:
        writer.writerow(row)
