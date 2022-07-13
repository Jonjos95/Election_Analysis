#The data we need to retrieve

import os
import csv

# Assign a variable to load a file from a path.
file_to_load = os.path.join('C:/Users/Jonjo/OneDrive/Documents/Data Analysis Bootcamp 2022/Week 3 Python/Resources/election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('C:/Users/Jonjo/OneDrive/Documents/Data Analysis Bootcamp 2022/Week 3 Python/Election_Analysis/Analysis/election_analysis.txt')

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# 2. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0



# Open the election results and read the file.
with open(file_to_load) as election_data:

     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     
     # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

     # 1. Add to the total vote count.
        total_votes+= 1

     # Print the candidate name from each row.
        candidate_name = row[2]

     # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
           
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

          # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0


      # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


# Save the results to our text file.

with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
      # Save the final vote count to the text file.
    txt_file.write(election_results)

   # Print each candidate, their voter count, and percentage to the terminal.
   
   # Determine the percentage of votes for each candidate by looping through the counts.
   # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
      # 2. Retrieve vote count of a candidate.
      votes = candidate_votes[candidate_name]
      # 3. Calculate the percentage of votes.
      vote_percentage = float(votes) / float(total_votes) * 100


      #  To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
   
      candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

      # Print each candidate, their voter count, and percentage to the terminal.     
      print(candidate_results)
      #  Save the candidate results to our text file       
      txt_file.write(candidate_results)
            
      #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")  

      # Determine winning vote count and candidate
      # Determine if the votes is greater than the winning count.
      if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
          # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

      winning_candidate_summary = (
         f"-------------------------\n"
         f"Winner: {winning_candidate}\n"
         f"Winning Vote Count: {winning_count:,}\n"
         f"Winning Percentage: {winning_percentage:.1f}%\n"
         f"-------------------------\n")
                          
    print(winning_candidate_summary)
   # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)