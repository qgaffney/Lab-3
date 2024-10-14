import csv

def serial_search_csv(filename, target_value, column_name):

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        row_number = 1
        for row in reader:
            if row[column_name] == target_value:
                return row_number
            row_number += 1
    return -1

def binary_search_csv(filename, target_value, column_name):

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        low, high = 0, len(rows) - 1

        while low <= high:
            mid = (low + high) // 2
            if rows[mid][column_name] == target_value:
                return mid + 1
            elif rows[mid][column_name] < target_value:
                low = mid + 1
            else:
                high = mid - 1

    return -1

# Example usage
filename = '/Users/q.gaffney/Lab-3/Resource/budget_data.csv'
target_value = '1141840'
column_name = 'Profit/Losses'

serial_result = serial_search_csv(filename, target_value, column_name)
print("Result of serial search:", serial_result)

binary_result = binary_search_csv(filename, target_value, column_name)
print("Result of binary search:", binary_result)