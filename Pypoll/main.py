#This is the Main Code for Pypoll
import os
import csv

#establishing variables
#filepath = '../Resources/election_data.csv' - I could never get this method to work, so I opted for what you see below
filepath = ('C:\\Users\\mrrit\\OneDrive\\Documents\\UofO Data Class\\Wk3_Python\\python-challenge\\PyPoll\\Resources\\election_data.csv')
poll_results_file = None
total_votes = None
candidate_name = None
candidate_num = None
percent = None
winner = None
final_results = None

#establishing empty lists
candidates = []
votes_per_candidate = []
vote_percentages = []

with open(filepath, "r", encoding='utf') as poll_file:
    
    poll_reader = csv.reader(poll_file, delimiter=",")
    next(poll_reader, None)

    for row in poll_reader:
        candidate_name = row[2]

        #adding votes if the candidate is already in the list, else appending new elements to the lists
        if candidate_name in candidates:
            candidate_num = candidates.index(candidate_name)
            votes_per_candidate[candidate_num] +=1 
        else:
            candidates.append(candidate_name)
            votes_per_candidate.append(1)

    #finding the total votes by adding all of the numbers in the 'votes per candidate' list
    total_votes = sum(votes_per_candidate[0:(len(candidates))])

    #finding the vote percentages by dividing votes per candidate by total votes, element by element
    for i in votes_per_candidate:
        percent = (i/total_votes)*100
        vote_percentages.append(percent)

    #the winner had the 'max' number of votes
    winner = candidates[votes_per_candidate.index(max(votes_per_candidate))] 

    #zipping it all together for easier printing    
    final_results = zip(candidates, vote_percentages, votes_per_candidate)
    
    #printing results to terminal
    print(f"Election Results \n-------------------------------- \nTotal Votes: {total_votes}")
    for i in final_results:
        print(f"{i[0]}: {round(i[1], 3)}% ({i[2]})")
    print(f"-------------------------------- \nWinner: {winner} \n--------------------------------")

    #writing results to new text file
    final_results = zip(candidates, vote_percentages, votes_per_candidate)
    poll_results_file = open("pypoll_results_file.txt", "w")
    print(f"Election Results \n-------------------------------- \nTotal Votes: {total_votes}", file=poll_results_file)
    for i in final_results:
        print(f"{i[0]}: {round(i[1], 3)}% ({i[2]})", file=poll_results_file)
    print(f"-------------------------------- \nWinner: {winner} \n--------------------------------", file=poll_results_file)

    poll_results_file.close()
poll_file.close()