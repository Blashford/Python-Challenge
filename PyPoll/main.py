import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# opening the path to the file
with open(csvpath) as csvfile:
    
    # reading the file and skipping the header
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)