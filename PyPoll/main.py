#Import csv module
import os
import csv

#Locate csv file
election_data = os.path.join("PyPoll/Resources/election_data.csv")

#Determine variables, making a list for each one
total_votes = 0
candidate_votes = {}
candidates_list = []

#Reading CSV Module
with open(election_data, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter =',')

    #Skip header row
    header = next(csvreader)

    #Read each row of data after header
    for row in csvreader:
        #Determine the total number of votes
        total_votes += 1

        #Extract candidate name from the row
        candidate_name = row[2]
        
        #Determine cadidate's vote count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1
            candidates_list.append(candidate_name)

# Save the results to a text file
output_file_path = "election_results.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    #Calculate and print the percentage of votes each candidate won
    for candidate in candidates_list:
        percentage = (candidate_votes[candidate] / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})\n")

    #Find the winner based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#Calculate and print the percentage of votes each candidate won
for candidate in candidates_list:
    percentage = (candidate_votes[candidate] / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})")

#Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

#Print the winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")