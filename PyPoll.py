# My plan! 
# Start by importing csv mod
import csv
import os
#Naming our path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open election results to read
with open(file_to_load) as election_data:
    #Read and analyze data
    file_reader = csv.reader(election_data)
    #Find and print the header row
    headers = next(file_reader)
    print(headers)


#create a filename variable with a path

#use open() function w/ "w" mode to write data to the file
outfile = open(file_to_save, "w")
#Write some data




#The Data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#At the end - close the file
#close the files
#election_data.close()
#outfile.close()