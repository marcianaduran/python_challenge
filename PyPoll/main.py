import os
import csv

output_path = os.path.join('Resources','election_data.csv')

#define empty lists and dictionaries
total_votes = []
candidate_list = []
candidate_votes = {}
candidate_winner = []

#read and save information in lists and dictionaries
with open(output_path,'r') as election_data:

    csv_reader = csv.reader(election_data, delimiter=',')
    csv_header = next(election_data)

    for row in csv_reader:
        total_votes.append(row[2])
        candidate_name = row[2]

        if candidate_name not in candidate_list:
             candidate_list.append(candidate_name)
             candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    print('Election Results')
    print('----------------------------')
# 1. total number of votes cast
    print(f'Total Votes: {len(total_votes)}')
    print('----------------------------')
# 2. complete list of candidates who received votes
# 3. percentage of votes each candidate won
# 4. total number of votes each candidate won
    winner = 0
    for candidate in candidate_votes:
        if candidate_votes[candidate] > winner:
            winner = candidate_votes[candidate]
            candidate_winner = candidate
        print(f'{candidate}: {round(candidate_votes[candidate]/len(total_votes)*100,3)}% ({candidate_votes[candidate]})')
    print('----------------------------')
# 5. winner of the election based on popular vote
    print(f'Winner: {candidate_winner}')
    print('----------------------------')
# 6. file export
output_path = os.path.join('analysis','poll analysis.txt')
with open(output_path,'w') as f:
    f.write('Election Results')
    f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    f.write(f'Total Votes: {len(total_votes)}')
    f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    for candidate in candidate_votes:
        f.write(f'{candidate}: {round(candidate_votes[candidate]/len(total_votes)*100,3)}% ({candidate_votes[candidate]})')
        f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    f.write(f'Winner: {candidate_winner}')
    f.write('\n')
    f.write('----------------------------')

    
