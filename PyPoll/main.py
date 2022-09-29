#import data
import os
import csv

#set up path
pypollcsv = os.path.join("Resources", 'election_data.csv')
pypolltxt = os.path.join("Analysis", 'election_analysis.txt')

#variables
votes =[]
canidates = []
canidate_votes = {}


with open(pypollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        votes.append(int(row[0]))

        # canidate names 
        canidate_name = (row[2])

        # check canidate name in list 
        if canidate_name not in canidates:
            canidates.append(row[2])    
            canidate_votes[canidate_name] = 0
       
       
        # votes per canidate
        canidate_votes[canidate_name] = canidate_votes[canidate_name] + 1


        


      
#total number of votes
total_votes = len(votes)

 


election_output = (f'\n\nElection Results\n'
f'----------------------------\n'
f'Total Votes: {total_votes}\n'
f'----------------------------\n')





# print results 

with open(pypolltxt, 'w') as f:
    f.write(election_output)

    
    

    # winner over canidate results 
    for canidate in canidate_votes:

        # get canidate votes 
        votes = canidate_votes.get(canidate)

        # percentage of votes 
        percent_votes = votes/total_votes * 100



        # print canidate votes 
        canidate_results = (f'{canidate}: {percent_votes:.3f}% ({votes}) \n')

        # winner 
        



        # save canidate name in text file 
    
        f.write(canidate_results)


