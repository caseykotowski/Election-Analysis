# Election Analysis
## Purpose
This purpose of creating this code is to provide an audit of election results. 
The election it was created for was a congressional race in Colorado, but this code should be resuable for elections of all size and across the country.
This is not a vote counting machine, but instead takes the data from voting machines and double checks the results. 
## Election Audit Results
* Total Votes Cast: 369,711
  * `# Initialize a total vote counter.`
    `total_votes = 0`
    `# For each row in the CSV file.
    `for row in reader:
        `# Add to the total vote count
        `total_votes = total_votes + 1

* Votes by County: 
  * County Votes:
    * Jefferson: 10.5% (38,855)
    * Denver: 82.8% (306,055)
    * Arapahoe: 6.7% (24,801)
* Largest County Turn Out: Denver
    `for county_name in votes_by_county:
        `# 6b: Retrieve the county vote count.
       ` county_votes = votes_by_county.get(county_name)
       ` # 6c: Calculate the percentage of votes for the county.
       ` county_votes_percent = county_votes / total_votes * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {county_votes_percent:.1f}% ({county_votes:,})\n")
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_votes > largest_count):
            largest_count = county_votes
            largest_turnout = county_name

* Individual Candidate Results: 
    * Charles Casper Stockham: 23.0% (85,213)
    * Diana DeGette: 73.8% (272,892)
    * Raymon Anthony Doane: 3.1% (11,606)
* Winning Candidate: Diana DeGette with 73.8% of the vote, which is 272,892 votes.

    ` for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

## Election Audit Summary - Repurposing the Code
This code is perfect to run as a check of election results. By just supplying a csv file of the election results - in the same format that this congressional district is already use to - this code will breakdown the results by candidate and county in one click. As long as you have a computer that can run python, this audit takes just a few moments. 


For each election, there are a few minor changes that need to be made to obtain the same results as this example. The title of the CSV file in code will have to be updated, and the location of where the file is changed will have to match. 
The rest of the code is written to loop through as many layers of data as exist. 
This code should work for any amount of candidates, voters, or counties. 

There is one other change that I might offer. I'm curious about how the voter turn out compares to number of registered voters. The total number of registered voters per municipality could be hard coded into the starting variables, or it could be added as a column in the election data. Then we can check what the overall voter turn out is, and check which counties have higher percentages of voter turn out. 

There are small changes that need to be made between elections, as well as some potential audit improvements. But overall this code is simple enough for a beginner to use but powerful enough to provide an accurate check on election results. 
