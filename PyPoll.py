# The date we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidated who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Resources\election_results.csv

# # Import the datetime dependency.
# import datetime
# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# # Print the present time.
# print("The time right now is,", now)

#----------------------------------------------------------------------#

#3.4.3: Open & Read to Files with Python

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    print(election_data)

#----------------------------------------------------------------------#

#3.4.3: Write to Files with Python

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

#---------------------------MakingCodeCleaner--------------------------#

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #Two Methods of adding data:
    #1.)
    #  # Write three counties to the file.
    #  txt_file.write("Arapahoe")
    #  txt_file.write("Denver")
    #  txt_file.write("Jefferson")
    #2.)
    #  # Write three counties to the file.
    #  txt_file.write("Arapahoe, Denver, Jefferson")

    #Newline Escape Sequence
     # Write three counties to the file.
     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#----------------------------------------------------------------------#

#3.4.4: Read the Election Results

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

#----------------------------------------------------------------------#

#3.4.5: Commit Your Code

# 1. Launch the terminal for macOS or GitBash for Windows.
# 2. Enter in terminal: git init 
# 3. Navigate to the Election_Analysis folder.
# 4. Type git status and press Enter.
# 5. Type git add . and press Enter.
# 6. Check the status again with git status and then press Enter.
# 7. Commit the files to be added to the repository by typing git commit -m "Adding the election audit code." and then press Enter.
# 8. Type git push and press Enter to add the file to your repository.
# 9. Refresh your GitHub page to see the repository changes.

#----------------------------------------------------------------------#

# 3.5.1: Get the Total Votes|3.5.2: Get the Candidates in the Election
#                   3.5.3: Get the Candidates’ Votes

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
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

# 3.5.1 # 3. Print the total votes.
# print(total_votes)

# 3.5.2 # Print the candidate list.
# print(candidate_options)

# Print the candidate vote dictionary.
print(candidate_votes)

#----------------------------------------------------------------------#

# 3.5.4: Determine Candidates' Percentage of Votes
   
for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # 3. Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate}: received {vote_percentage:.1f}% of the vote.") 

#----------------------------------------------------------------------#

# 3.5.5: Determine the Winning Candidate

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
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

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
        #  To do: print out the winning candidate, vote count and percentage to
        #   terminal.
        # 4. Print the candidate name and percentage of votes.
        print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
