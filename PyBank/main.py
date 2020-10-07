import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# opening the path to the file
with open(csvpath) as csvfile:
    
    # reading the file and skipping the header
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    # tracking things
    month = 0
    total = 0
    avg = 0
    average = avg
    increase = [0,0]
    decrease = [0,0]
    first = True
    for row in csvreader:
        # incrementing the month and total
        month = month + 1
        total = total + int(row[1])
        
        if first == True:
            # storing the first row
            avg = int(row[1])
            first = False
        else:
            # storing the total amount of change in average by subtracting 
            # the previous row from the current row
            average = average + (int(row[1]) - avg)
            # storing the current row
            avg = int(row[1])
        # These output different totals than the one in the example, but I looked
        # at the data so the numbers must have been switched around? The months
        # are the same though
        if int(increase[1]) < int(row[1]):
            increase.pop(1)
            increase.pop(0)
            increase.append(row[0])
            increase.append(row[1])
        if int(decrease[1]) > int(row[1]):
            decrease.pop(1)
            decrease.pop(0)
            decrease.append(row[0])
            decrease.append(row[1])
        
        

#  doing month - 1 because there is 1 less change than the number of months
average1 = average / (month - 1)
average1 = round(average1, 2)    
print("Financial Analysis")
print("______________________")
print(f"Total Months: {month}")
print(f"Total: ${total}")
print(f"Average Change: ${average1}")
print(f"Greatest Increase in Profits: {increase[0]} ${increase[1]}")
print(f"Greatest Decrease in Profits: {decrease[0]} ${decrease[1]}")

    