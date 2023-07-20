import os
import csv
# print(os.getcwd())
# os.chdir('/Users/crystallucas/UPenn/homework/Module3Python/python-challenge/PyPoll')
# print(os.getcwd())

election_data = "Resources/election_data.csv"

# election_data = os.path.join("Resources","election_data.csv")

# Open and read the csv file
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
     
   #Read the header row first 
    csv_header = next(csv_file)

    total_votes = 0
    candidates = {}

    for row in csv_reader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate] = candidates.get(candidate, 0) + 1

# Calculate the percentage of votes each candidate won
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))

# Find the winner based on popular vote
winner = max(results, key=lambda x: x[2])

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")