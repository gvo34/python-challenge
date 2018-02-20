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
voters = []

voters_file_path = os.path.join('data','election_data_1.csv')

with open(voters_file_path,'r') as election_file:
  elections = csv.reader(election_file, delimiter=',')

  for vote in elections:
      voter_id = vote[0]
      voters.append(voter_id)

      voter_county = vote[1]
      counties.append(voter_county)
 
      voter_candidate = vote[2]
      try:
        c_index = candidates.index(voter_candidate)
      except ValueError:
        c_index= -1        

      if c_index != -1:
         candidates_votes[c_index] += 1
      else:
         candidates.append(voter_candidate)
         candidates_votes.append(1)
         candidates_county.append(voter_county)

      

total = len(voters)

percentage = []
for c in candidates_votes:
    p = float(c)
    percentage.append((p/total) *100)  

print("Total candidates tally of :" + str(len(candidates)))
tally = zip(candidates, percentage, candidates_votes)
for c in tally:
    print (c)



for county in set(counties):
     print("County "+county)
print("total votes "+str(len(voters)))

max_votes = max(percentage)
m_index = percentage.index(max_votes)

print("The winner is " + candidates[m_index])




      

