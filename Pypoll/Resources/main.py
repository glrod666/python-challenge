import csv
import os

# Path to collect data from the Resources folder
election_data_path = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the csv file
with open(election_data_path) as csvfile:
csvreader:_reader = csv.reader(csvfile, delimiter=',')

# Skip the header
next(csvreader)

# Process each row
for row in csvreader:
    total_votes += 1
    candidate_name = row[2]

    if candidate_name in candidates:
        candidates[candidate_name] += 1
    else:
        candidates[candidate_name] = 1

# Determine the winner and calculate percentages
    for candidate in candidates:
        if candidates[candidate] > winner_votes:
            winner = candidate
        winner_votes = candidates[candidate]
        candidates[candidate] = [candidates[candidate], (candidates[candidate] / total_votes) * 100]

# Create and write to the analysis text file
output_path = os.path.join("election_results.txt")

with open(output_path, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
for candidate, data in candidates.items():
    txt_file.write(f"{candidate}: {data[1]:.3f}% ({data[0]})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, data in candidates.items():
    print(f"{candidate}: {data[1]:.3f}% ({data[0]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")