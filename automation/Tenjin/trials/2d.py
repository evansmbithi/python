import csv

arr = [
    ['menu', 'application']
]

arr.insert(2, ['BRTG', 'mbithi'])

print(arr)

# write to csv
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    for row in arr:
        writer.writerow(row)