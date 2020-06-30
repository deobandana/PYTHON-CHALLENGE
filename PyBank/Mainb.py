#importing operating system function and csv function
import os 
import os. path
from os import path 
import csv

csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")
total_months = 0

with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimeter=",")

next(csvreader)

for row in csvreader:
 total_months = total_months + 1

print("total_months")