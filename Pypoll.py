#The data we need to retrieve

import os
import csv

# Assign a variable to load a file from a path.
file_to_load = os.path.join("week 3 python","Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("week 3 python","election_analysis","analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     
     # Read and print the header row.
    headers = next(file_reader)
    print(headers)