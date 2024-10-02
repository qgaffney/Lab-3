#Import OS module
import os

#Import module to read CSV
import csv

def linear_search(arr, target):
    for index in range (len(arr)):
        if arr[index] == target
        return index
    
    return -1

#Set path for source file
CSV_PATH = os.path.join ('Resource', 'budget_data (1).csv')

#Open and read CSV
os.chdir(os.path.dirname(os.path.realpath(__file__)))
data=[]
with open(CSV_PATH) as csvfile:

#Specify delimiter and CSV reader
    csvreader = csv.reader(csvfile, delimiter=",")

#Read header row, store it
    csv_header = next(csvreader)

col = [x[0] for x in data]