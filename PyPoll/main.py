import os
import csv

#define variables  
total_votes_cast = 0
candidate_votes = {}
winner = None
vote = 0
vote_percentage = 0.000
max_votes = 0
results = []


#create path to csv file 
file_path = r"PyPoll\Resources\election_data.csv"

#Open and read CVS File
with open(file_path, newline= '' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   #Skip the Header
    header = next(csvfile)


    #iterate every each row in the csv file
    for row in csvreader:
        total_votes_cast +=1
        #get the candidate name from the current row
        candidate = row[2]

        #add the candidate name for 
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
        

    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes/total_votes_cast) * 100
        results.append((candidate, vote_percentage, votes))
  
        if votes > max_votes:
           max_votes = votes
           winner = candidate
    

#print results
print("Election Results")
print("-------------------------")
print(f"Total Votes:{total_votes_cast}")
print("-------------------------")
for candidate, vote_percentage, votes in results:
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
print("-------------------------")
print(f"winner: {winner}")
print("-------------------------")

# Define the output directory and file path
output_dir = os.path.join("PyPoll", "Analysis_Poll")
output_file = os.path.join(output_dir, "results.txt")

# Ensure the directory exists
if not os.path.isdir(output_dir):
    print(f"'{output_dir}' is not a directory or does not exist. Creating it now.")
    os.makedirs(output_dir)
    print(f"Directory '{output_dir}' created.")
else:
    print(f"'{output_dir}' is a directory.")

# Write results to the text file
try:
    with open(output_file, 'w') as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes_cast}\n")
        file.write("-------------------------\n")
        for candidate, vote_percentage, votes in results:
            file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")
    print(f"Results have been written to: {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")