import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# opening the path to the file
with open(csvpath) as csvfile:
    
    # reading the file and skipping the header
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    # Tracking the total votes and making an empty dictionary to hold candidates and votes 
    total = 0
    dicty = {}
    
    # Iterating through the reader and incrementing total votes
    for row in csvreader:
        total = total + 1
        # Finding each unique candidate and incrementing their votes in the dictionary
        if row[2] not in dicty:
            dicty.update({row[2]:{
                    "Votes": 1
            }})
        else:
            dicty[row[2]]["Votes"] += 1
        
# empty list to find who has the most votes
win= [0,0]

# iterating through the dictionary to find who has the most votes, and also calculating 
# what percentage of votes each candidate got 
for candidate, key1 in dicty.items():
    for key, votes in dicty[candidate].items():
        if votes > win[0]:
            win.pop()
            win.pop()
            win.append(votes)
            win.append(candidate)
        percent = (votes / total) * 100
        dicty[candidate].update({"Percent":percent})
        
        break
    continue


# Printing results
print(f'Election Results')
print('--------------------------')
print(f'Total Votes: {total}')
print('----------------------------------')
for candidate, votes in dicty.items():
    print(f'{candidate}: {dicty[candidate]["Percent"]:.3f}% ({dicty[candidate]["Votes"]})')
print('------------------------')
print(f"Winner: {win[1]}")

# Output path to txt file
output_path = os.path.join("Analysis", "Analysis.txt")

# writing to analysis txt file
f= open(output_path, "w")
f.write("Election Results")
f.write("\n----------------------")
for candidate, votes in dicty.items():
    f.write(f'\n{candidate}: {dicty[candidate]["Percent"]:.3f}% ({dicty[candidate]["Votes"]})')
f.write("\n----------------------")
f.write(f"\nWinner: {win[1]}")