#importing operating system function and csv function
import os
import csv

#veriable Declearation with initial value
candidates = {}
percent = {}
total_voters = []
total_voters = []
total_votes = 0
max_vote= 0
winner =str

#setting Path for input csv and output txt file
csvpath = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("Analysis","PyPoll_Result.txt")

#opening CSV File in read Mode

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader: 

#question 1st solution
        total_votes +=1

#question 2nd 3rd 4th  solution       
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
        
        for keys, value in candidates.items():
            percent[keys] = round((value/total_votes) * 100, 1)

 #question 5th solution           
        for keys in candidates.keys():
            if candidates[keys] > max_vote:
                winner = keys
                max_vote = candidates[keys]

#printing result in console
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for key, value in candidates.items():
    print(key + ": " + str(percent[key]) + "% (" + str(value) + ")")
    print("-------------------------")

print("Winner: " + winner)
print("-------------------------")

#opening text file in write mode and printing result in text file
with open(output_path, mode='w',) as PyPoll_Result:
    PyPoll_Result.write("Election Results \n")
    PyPoll_Result.write("------------------------- \n")
    PyPoll_Result.write("Total Votes: " + str(total_votes) + "\n")
    PyPoll_Result.write("-------------------------- \n")

    for key, value in candidates.items():
        PyPoll_Result.write(key + ": " + str(percent[key]) + "% (" + str(value) + ") \n")
    PyPoll_Result.write("-------------------------- \n")
    PyPoll_Result.write("Winner: " + winner + "\n")
    PyPoll_Result.write("-------------------------- \n")

