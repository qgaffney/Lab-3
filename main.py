import csv

def serial_search_csv(file_path, target_value, column_name):

    matching_rows = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[column_name] == target_value:
                matching_rows.append(row)

    return matching_rows

file_path = '/Users/q.gaffney/Lab-3/Resource/budget_data.csv'
target_value = '951227'
column_name = 'Profit/Losses'

result = serial_search_csv(file_path, target_value, column_name)

if result:
    print("Results:")
    for row in result:
        print(row)
else:
    print("No results found.")