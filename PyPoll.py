# My plan! 
# Start by importing csv & os mod
import csv
import os

#Naming our path w/ variables
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#The Data we need to retrieve
#1. The total number of votes cast
#Set our total votes variable to zero
total_votes = 0

#2. A complete list of candidates who received votes
#Remember that the candidate column is index 2
#Declare blank list to hold the names
candidate_options = []

#4. The total number of votes each candidate won
#blank dictionary for counting per candidate
candidate_votes = {}

#variables for the winners
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#create a filename variable with a path
#Open election results to read
with open(file_to_load) as election_data:
    #Read and analyze data
    file_reader = csv.reader(election_data)
    #Find and print the header row
    headers = next(file_reader)
    for row in file_reader:
        #Add +1 for each vote. 1 row = 1 vote
        total_votes += 1
        #Finding and then listing the names in the candidate list
        candidate_name = row[2]
        #check if name is unique, if so add it to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        #Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
    #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#3. The percentage of votes each candidate won
#For loop to go through the dictionaries
#We need to turn our numbers into floating decimals 
for candidate_name in candidate_votes:
    #retrieve vote count
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    #print the results
    print(f'{candidate_name}: {vote_percentage:.1f}%, ({votes:,})\n')
    #5. The winner of the election based on popular vote
    #loop through the results and compare using conditionals
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true, then new candidate replaces current winner
        winning_count = votes
        winning_percentage = vote_percentage
        #Set winninng candidate to candidate's name
        winning_candidate = candidate_name

#checkpoint prints
#print(f'{total_votes:,}')
#print(candidate_options)
#print(candidate_votes)
#print(f'The winning candidate is {winning_candidate}, with {winning_percentage:.1f}% of the vote ({winning_count:,} votes).')
winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------\n"
)
print(winning_candidate_summary)
#use open() function w/ "w" mode to write data to the file
outfile = open(file_to_save, "w")
#Write some data


#At the end - close the file
#close the files
#election_data.close()
#outfile.close()