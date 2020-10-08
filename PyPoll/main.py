import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# opening the path to the file
with open(csvpath) as csvfile:
    
    # reading the file and skipping the header
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    # Tracking the votes
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    total = 0
    
    # Iterating through the reader and incrementing total votes
    for row in csvreader:
        total = total + 1

        # Counting votes for each candidate
        if row[2] == "Khan":
            khan = khan + 1
        elif row[2] == "Correy":
            correy = correy + 1
        elif row[2] == "Li":
            li = li + 1
        elif row[2] == "O'Tooley":
            otooley = otooley + 1

# finding who had the most votes
win= [0]
can = [correy, li, otooley, khan]
for name in can:
    if name > win[0]:
        win.pop()
        win.append(name)

# Tracking the percentage of each vote
perck = 0
percc = 0
percl = 0
perco = 0
# finding the percentage of each vote
perck = (khan / total) * 100
perck = round(perck, 3)
percc = (correy / total) * 100
percc = round(percc, 3)
percl = (li / total) * 100
percl = round(percl, 3)
perco = (otooley / total) * 100
perco = round(perco, 3)

# storing everything together
candidatevotes = {
    "otooley": ["O'Tooley", perco, otooley],
    "khan": ["Khan", perck, khan],
    "correy": ["Correy", percc, correy],
    "li": ["Li", percl, li]      
}
# iterating through the dictionary to find the winners name
for key, value in candidatevotes.items():
    if value[2] == win[0]:
        win.append(value[0])



print(f'Election Results')
print('--------------------------')
print(f'Total Votes: {total}')
print('----------------------------------')
for candidate, percent, votes in candidatevotes.values():
    print(f'{candidate}: {percent}% ({votes})')
print('------------------------')
print(f"Winner: {win[1]}")