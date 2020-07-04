#importing operating system function and csv function
import os 
import csv

#setting Path for input csv and output txt file
csvpath = os.path.join(r'Resources\budget_data.csv')
output_path = os.path.join("Analysis\PyBank_Result.txt")

#veriable Declearation with initial value
total_months = 0
Net_total =0
A = 0
B = 0
greatest_increase=0
greatest_decrease=0
increase_date=None
decrease_date=None
total_Change = 0
counter= 1

#opening CSV File in read Mode
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

# escaping First Row 
     next(csvreader)
     
     for row in csvreader:

          #question 1st solution
          total_months += 1

          #Question 2nd Solution
          Net_total += int(row[1])

          #Question 3rd 4th and 5th Solution
          if counter == 1:
               A = int(row[1])
               
          else :
               B = int(row[1])
               Change = (B-A)
               if greatest_increase < Change :
                  greatest_increase = Change
                  increase_date= (row[0])

               if greatest_decrease > Change:
                  greatest_decrease = Change
                  decrease_date= (row[0])

               total_Change =total_Change + Change
               A = int(row[1])
          counter = counter +1
#assigning output in a single string "Result"     
    
Result=(
     f"Financial Analysis\n"
     f"------------------\n"        
     f"Total Months: {total_months}\n"    
     f"Total : ${Net_total}\n"
     f"Average  Change: ${round((total_Change/(counter-2)),2)}\n"
     f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
     f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")

# Printing Result

print(Result)

#opening Text fle In Write Mode 
with open(output_path, mode='w',) as pybank_result:

#printing result In test file     
     pybank_result.write(Result)

