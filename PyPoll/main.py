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
    perc = 0

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

    perc = (khan / total) * 100
    perc = round(perc, 3)
    lk = ["Khan"]
    lk.append(perc)
    lk.append(khan)
    
    lc = ["Correy"]
    perc = (correy / total) * 100
    perc = round(perc, 3)
    lc.append(perc)
    lc.append(correy)

    ll = ["Li"]
    perc = (li / total) * 100
    perc = round(perc, 3)
    ll.append(perc)
    ll.append(li)
    
    lo = ["O'Tooley"]
    perc = (otooley / total) * 100
    perc = round(perc, 3)
    lo.append(perc)
    lo.append(otooley)

    winlist = [otooley, khan, li, correy]
    winlist.sort(reverse= True)
    winner = winlist[0]
    print(winlist)