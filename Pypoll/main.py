#This is the Main Code for Pypoll
import os
import csv

filepath = ('C:\\Users\\mrrit\\OneDrive\\Documents\\UofO Data Class\\Wk3_Python\\python-challenge\\PyPoll\\Resources\\election_data.csv')
poll_results_file = None
total_votes = None
candidate_name = None
candidate_num = None
percent = None
winner = None
final_results = None
candidates = []
votes_per_candidate = []
vote_percentages = []

with open(filepath, "r", encoding='utf') as poll_file:
    
    poll_reader = csv.reader(poll_file, delimiter=",")
    next(poll_reader, None)

    for row in poll_reader:
        candidate_name = row[2]

        if candidate_name in candidates:
            candidate_num = candidates.index(candidate_name)
            votes_per_candidate[candidate_num] +=1 
        else:
            candidates.append(candidate_name)
            votes_per_candidate.append(1)

    total_votes = sum(votes_per_candidate[0:(len(candidates))])

    for i in votes_per_candidate:
        percent = (i/total_votes)*100
        vote_percentages.append(percent)

    winner = candidates[votes_per_candidate.index(max(votes_per_candidate))] 
    final_results = zip(candidates, vote_percentages, votes_per_candidate)
    poll_results_file = open("results_file.txt", "w")

    print(f"Election Results \n-------------------------------- \nTotal Votes: {total_votes}")
    for i in final_results:
        print(f"{i[0]}: {round(i[1], 3)}% ({i[2]})")
    print(f"-------------------------------- \nWinner: {winner} \n--------------------------------")

    final_results = zip(candidates, vote_percentages, votes_per_candidate)
    
    print(f"Election Results \n-------------------------------- \nTotal Votes: {total_votes}", file=poll_results_file)
    for i in final_results:
        print(f"{i[0]}: {round(i[1], 3)}% ({i[2]})", file=poll_results_file)
    print(f"-------------------------------- \nWinner: {winner} \n--------------------------------", file=poll_results_file)

    poll_results_file.close()
poll_file.close()