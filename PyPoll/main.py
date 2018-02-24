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

def add_vote(name,votedict,vote):
  if name in votedict:
    votedict[name] +=vote
  else:
    votedict[name] = vote

def county_vote(countyname, candidatename, counties): 
  if countyname in counties:
    add_vote(candidatename, counties[countyname],1)
  else:
    counties[countyname]={candidatename:1}

def print_votes(total_votes, candidates, counties, report):

  reportfile = os.path.join('output',report+'_report.txt')
  with open(reportfile,'w',newline='') as reprotf:
    # Total number of votes
    print(".................."+report+" Elections ..............")
    print("Total number of votes "+str(total_votes))
    print("...........................................")
    #List all candidates
    for c in candidates:
      percentage = (candidates[c]/total_votes)*100
      print(c + " " + str(int(percentage)) +"% ("+ str(candidates[c]) +")")
      
    max_key = max(candidates,key=candidates.get)
    percentage = (candidates[max_key]/total_votes)*100
    print("...........................................")
    print("Popular vote winner is "+max_key + " with "+str(int(percentage))+"%")
      
    #tally votes
    tally = {} # {'candidate': all_county_votes}
    for county in counties:
      max_candidate = max(counties[county],key=counties[county].get)
      add_vote(max_candidate, tally, counties[county][max_candidate]) # candidate with max votes for each county
    winner = max(tally, key=tally.get)
    print("...........................................")
    print("WINNER: "+winner)
    print("...........................................")
    

def read_elections_report(file_name):
      # read report from a file                                                                                      
      reportfile = os.path.join('output',file_name+'_report.txt')
      with open(reportfile,'r') as reportf:
            lines = reportf.read()
            print(lines)


def PyPoll(datafiles):
  for election_file in datafiles:
    voters_file_path = os.path.join('data',election_file+'.csv')  

    with open(voters_file_path,'r') as election_data:
      elections = csv.reader(election_data, delimiter=',')
      next(elections, None) #skip header

      candidates = {} # {'candidate': votes}
      counties = {}   # {'county': {candidate': votes}}
      total_votes = 0

      for vote in elections:
        candidate_name = vote[2]
        add_vote(candidate_name, candidates,1)
        total_votes += 1
        county = vote[1]
        county_vote(county, candidate_name, counties)
          
    print_votes(total_votes, candidates, counties, election_file)  
    read_elections_report(election_file)
    



input_data = ('election_data_1', 'election_data_2')
PyPoll(input_data)

      

