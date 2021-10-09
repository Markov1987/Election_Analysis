# Add our dependencies.
#To be able to handle CVS Files
import csv 
#To create code without explicity be used with Windonws or Mac.
import os  
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Define votes counter variable. 
total_votes=0

#Define candidates list and dictionary to host total votes per candidate. 
candidate_options=[]
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    
#Count votes.
    for row in file_reader:
        total_votes=total_votes+1

#Get candidates name from each row
        candidate_name=row[2]

#Add candidates name to the list
        if candidate_name not in candidate_options:
            #Add only new candidates
            candidate_options.append(candidate_name)

#Create dictionary's keys and set them to Zero to start votes count.
            candidate_votes[candidate_name]=0

#Start counting votes for each candidate
        candidate_votes[candidate_name]= candidate_votes[candidate_name]+1

#Export results to TXT
    with open(file_to_save,"w") as txt_file:
        election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n")
        print(election_results, end="")
            # Save the final vote count to the text file.
        txt_file.write(election_results)
  

        # Calculate voting percentage
        for candidate_name in candidate_votes:
            votes=candidate_votes[candidate_name]
            vote_percentage=float(votes)/float(total_votes)*100
        #print(f"{candidate_name}: received {vote_percentage:.2f} % of the vote." )

        # Determine winner

            if (votes>winning_count) and (vote_percentage>winning_percentage):
                winning_count=votes
                winning_percentage=vote_percentage
                winning_candidate=candidate_name

            candidate_results= (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #Save the candidate results to our text file.
            txt_file.write(candidate_results)

            
        # Print each row in the CSV file.
            #for row in file_reader:
            #   print(row)
            winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

            # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)
        
        