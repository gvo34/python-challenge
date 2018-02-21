#You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). 
#Each dataset is composed of three columns: 
#Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv


candidates = []
candidates_votes = []
candidates_county = []
counties = []
counties_votes = []
voters = []




# Add candidate to the list of candidates
def add_candidate(candidate, candidatelist,votes):
  candidatelist.append(candidate)
  cleanlist = list(set(candidatelist))
  if len(cleanlist) != len(candidatelist): #added a new candidate
      votes.append(1)
  return cleanlist

# increase the votecount with matching votelist
def add_vote(vote, votelist, votecount):
      try:  #search if the vote is already in the list
        index = votelist.index(vote)
      except ValueError:
        index = -1  
            # if the vote is in the list, increase the counter
      if index >= len(votecount) or index == -1:
        votecount.append(1)
      else:
        votecount[index] +=1


input_data = ('election_data_1', 'election_data_2')

for election_data in input_data:

  voters_file_path = os.path.join('data',election_data+'.csv')  

  with open(voters_file_path,'r') as election_file:
    elections = csv.reader(election_file, delimiter=',')

    for vote in elections:
      voter_id = vote[0]
      voters.append(voter_id)

      voter_county = vote[1]
      counties = add_candidate(voter_county, counties, counties_votes)

      voter_candidate = vote[2]
      candidates = add_candidate(voter_candidate, candidates, candidates_votes)

      add_vote(voter_candidate, candidates, candidates_votes)
      add_vote(voter_county, counties, counties_votes)

      total = len(voters)


  percentage = []
  for c in candidates_votes:
    p = float(c)
    percentage.append('{:.0%}'.format((p/total)))  

  print("----------------- ELECTIONS from "+election_data+" ------------------------")
  print("Total candidates tally of :" + str(len(candidates)) + " candidates")
  tally = zip(candidates, percentage, candidates_votes)
  for c in tally:
    print (c)

  max_votes = max(candidates_votes)
  m_index = candidates_votes.index(max_votes)

  print(">>>>>>>>>>>>>>>>>>>>>>>>The winner is: " + candidates[m_index])

  print("Voting partocipation is:")
  turnout = zip(counties, counties_votes)
  for t in turnout:
    print(t)

  max_turnout = max(counties_votes)
  t_index = counties_votes.index(max_turnout)

  print("County with the highest turnout is: "+counties[t_index] + " with " + str(max_turnout)+" votes")



      

