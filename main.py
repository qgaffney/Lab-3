import csv

with open('Resource'/'budget_data (1).csv', mode='r') as csv.file:
    csvFile = csv.reader(csv.file)
    for lines in csvFile:
        print(lines)