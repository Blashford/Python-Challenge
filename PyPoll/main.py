import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# opening the path to the file
with open(csvpath) as csvfile:
    
    # reading the file and skipping the header
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    khan = 0
    correy = 0
    li = 0
    otooley = 0
    total = 0
    

    for row in csvreader:
        total = total + 1

        if row[2] == "Khan":
            khan = khan + 1
        elif row[2] == "Correy":
            correy = correy + 1
        elif row[2] == "Li":
            li = li + 1
        elif row[2] == "O'Tooley":
            otooley = otooley + 1

perck = 0
percc = 0
percl = 0
perco = 0

perck = (khan / total) * 100
perck = round(perck, 3)
percc = (correy / total) * 100
percc = round(percc, 3)
percl = (li / total) * 100
percl = round(percl, 3)
perco = (otooley / total) * 100
perco = round(perco, 3)

candidatevotes = {
    "khan": ["Khan", perck, khan],
    "otooley": ["O'Tooley", perco, otooley],
    "correy": ["Correy", percc, correy],
    "li": ["Li", percl, li]
    
}

sorted(candidatevotes.items(), key=lambda e: e[1][1], reverse= True)
print(candidatevotes)

print(f'Election Results')
print('--------------------------')
print(f'Total Votes: {total}')
print('----------------------------------')
for candidate, percent, votes in candidatevotes.values():
    print(f'{candidate}: {percent}% ({votes})')
print('------------------------')
