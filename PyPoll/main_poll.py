import csv

pypoll_path = '.\Resources\election_data.csv'
output_path = '.\\analysis\output.txt'
#poll_data store all data.
poll_data = []
Candidate_list = []
#Candidate_raw used to count vote
Candidate_raw = []
# load csv to dict and list for further process
with open(pypoll_path,encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    i = 0 
    Candidate_list_current = ''
    for row in csv_reader:
        if i > 0:
            poll_data.append(row)
            Candidate_raw.append(row[2])
            #find unique Candidate
            if row[2] not in Candidate_list:
                Candidate_list.append(row[2])
        i = i + 1 

total_votes = len(poll_data)
Candidate_string = ''
winner = ''
winner_vote_count = 0
for i in range(len(Candidate_list)):
    # get vote count and percentage
    vote_count = Candidate_raw.count(Candidate_list[i])
    vote_percent = str(round((vote_count/total_votes*100),3))+'%'
    #format string for output
    Candidate_string = Candidate_string + Candidate_list[i] + ' : ' + vote_percent + ' (' + str(vote_count) + ')' +'\n'
    # find winner
    if vote_count > winner_vote_count:
        winner_vote_count = vote_count
        winner = Candidate_list[i]

#write to files
with open(output_path, 'w') as f:
    output = f'''Election Results
----------------------------
Total Votes: {total_votes}
-------------------------
{Candidate_string}
-------------------------
Winner: {winner}
-------------------------
                '''
    #print and output to file
    print(output)
    f.write(output)


