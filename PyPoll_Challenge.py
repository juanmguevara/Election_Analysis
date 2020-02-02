# The date we need to retrieve

# 1. Create a list for the counties.
# 2. Create a dictionary where the county is the key and the votes cast for each county 
# ...in the election are the values.
# 3. Create an empty string that will hold the county name that had the largest turnout.
# 4. Declare a variable that represents the number of votes that a county received. Hint: 
# # Inside a for loop, add an if statement to check if the county name has already been recorded. 
# # If not, add it to the list of county names.
# 5. Inside the with open() function where you are outputting the file, do the following:
# # Create three if statements to print out the voter turnout results similar to the results 
# # ...shown above.
# # Add the results to the output file.
# # Print the results to the command line.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 1.Counties, create an empty list
counties_options = []
# 2.Votes, create an empty list
county_votes = {}
# 3. Largest votes in the county
winning_county = ""
winning_count1 = 0
winning_percentage1 = 0

#------------------------------------------------------------------------------------------------#
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1       
#------------------------------------------------------------------------------------------------#        
        #Print the county name from each row
        counties_name = row[1]
        # If the county name does not match any existing county...
        if counties_name not in counties_options:
            # Add it to the list of counties.
            counties_options.append(counties_name)
            # Begin tracking that counties vote count.
            county_votes[counties_name]=0
        # Add a vote to that counties count.
        county_votes[counties_name] += 1
#------------------------------------------------------------------------------------------------#
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
            f"\n"
            f"County Votes:\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
#------------------------------------------------------------------------------------------------#
        # Determine the percentage of votes for each county by looping through the counts.
        # Iterate through the county list.
        for county in county_votes:
            # Retrieve vote count of a county.
            votes1 = county_votes[county]
            # Calculate the percentage of votes.
            vote_percentage1 = int(votes1) / int(total_votes) * 100
            # Print each candidate, their voter count, and percentage to the
            # terminal.
            county_results =(f"{county}: {vote_percentage1:.1f}% ({votes1:,})\n")    
            # Print each candidate's voter count and percentage to the terminal.
            print(county_results)
            #  Save the candidate results to our text file.
            txt_file.write(county_results)

            # Determine winning vote count, winning percentage, and county.
            if (votes1 > winning_count1) and (vote_percentage1 > winning_percentage1):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count1 = votes1
                winning_percentage1 = vote_percentage1
                # And, set the winning_county equal to the candidate's name.
                winning_county = county
#------------------------------------------------------------------------------------------------#
        Break1 = (
            f"\n"
            f"-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n")
        print(Break1)
        # Save the winning candidate's results to the text file.
        txt_file.write(Break1)
#------------------------------------------------------------------------------------------------#
        # Determine the percentage of votes for each candidate by looping through the counts.
        # Iterate through the candidate list.
        for candidate in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate]
            # Calculate the percentage of votes.
            vote_percentage = int(votes) / int(total_votes) * 100
            # Print each candidate, their voter count, and percentage to the
            # terminal.
            candidate_results =(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")    
            # Print each candidate's voter count and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate
#------------------------------------------------------------------------------------------------#                
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------")
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)