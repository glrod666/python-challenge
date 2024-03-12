import csv

# Path to collect data from the Resources folder
file_to_load = 'Resources/election_data.csv'
# Specify the file to write to
output_file = "analysis/election_results.txt"

# Initialize variables
total_votes = 0
candidate_votes = {}
winner = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

# Read the header row
    header = next(reader)

# Loop through the csv
    for row in reader:
        total_votes += 1
    candidate_name = row[2]

if candidate_name not in candidate_votes:
        candidate_votes[candidate_name] = 1
else:
    candidate_votes[candidate_name] += 1

# Save the results to a text file
with open(output_file, "w") as txt_file:
    election_results = (
f"Election Results\n"
f"-------------------------\n"
f"Total Votes: {total_votes}\n"
f"-------------------------\n"
)
    print(election_results, end="")
    txt_file.write(election_results)

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = (votes / total_votes) * 100
    candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

print(candidate_results, end="")
txt_file.write(candidate_results)

if votes > winning_count:
        winning_count = votes
        winner = candidate

winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winner}\n"
f"-------------------------\n"
)
print(winning_candidate_summary)
txt_file.write(winning_candidate_summary)