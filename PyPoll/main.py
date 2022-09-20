import os
import csv


pypollcsv = os.path.join("Resources", 'election_data.csv')
pypolltxt = os.path.join("Analysis", 'election_analysis.txt')

total_votes =[]
canidates = []
stockham = []
degette = []
doane = []


with open(pypollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        total_votes.append(row[2])
        canidates.append(row[2])


total_votes = len(canidates)
canidate_name = list(canidates)

for canidate in canidates:
    if canidate == "stockham":
        stockham.append(canidates)
        stockhamvotes = len(stockham)
    elif canidate == "degette":
        degette.append(canidates)
        degettevotes = len(degette)
    elif canidate == "doane":
        doane.append(canidates)
        doanevotes = len(doane) 
