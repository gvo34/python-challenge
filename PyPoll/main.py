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

def add_vote(name,votedict):
  if name in votedict:
    votedict[name] +=1
  else:
    votedict[name] = 1

candidates = {} # {'candidate': votes}
counties = {} # {'county': {candidate': votes}}
total_votes = 0
totals = {}  # {'county':total-votes}

input_data = ('election_data_1', 'election_data_2')

for election_data in input_data:

  voters_file_path = os.path.join('data',election_data+'.csv')  

  with open(voters_file_path,'r') as election_file:
    elections = csv.reader(election_file, delimiter=',')
    next(elections, None) #skip header
    for vote in elections:
      candidate_name = vote[2]
      add_vote(candidate_name, candidates)
      total_votes += 1
      county = vote[1]

      if county in counties:
        add_vote(candidate_name, counties[county])
        totals[county]+=1
      else:
        counties[county]={candidate_name:1}
        totals[county] = 1
  
  # Total number of votes
  print(".................. Elections ..............")
  print("Total number of votes "+str(total_votes))
  print("...........................................")
  #List all candidates
  for c in candidates:
    percentage = (candidates[c]/total_votes)*100
    print(c + " " + str(int(percentage)) +"% ("+ str(candidates[c]) +")")

  max_key = max(candidates,key=candidates.get)
  percentage = (candidates[max_key]/total_votes)*100
  print("...........................................")
  print("Winner is "+max_key + " with "+str(int(percentage))+"%")
  print("...........................................")


  #tally votes
#  for county_votes in counties:
#    max_key = max(counties[county_votes],key=counties[county_votes].get)
#    percentage = (counties[county_votes][max_key]/totals[county_votes])*100
#    print("winner in "+county_votes+ " is " + max_key +" with "+str(int(percentage))+"%") 


  

      

