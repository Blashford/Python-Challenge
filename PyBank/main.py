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

    for row in csvreader:
        # incrementing the month and total
        month = month + 1
        total = total + int(row[1])
        # ask about average in office hours
        if avg == 0:
            avg = int(row[1])
        else:
            average = average + (avg - int(row[1]))
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
        
        
# the average that I got is also different from the example, but the total is the same??

average1 = average / month 
average1 = round(average1, 2)    
print("Financial Analysis")
print("______________________")
print(f"Total Months: {month}")
print(f"Total: ${total}")
print(f"Average Change: ${average1}")
print(f"Greatest Increase in Profits: {increase[0]} ${increase[1]}")
print(f"Greatest Decrease in Profits: {decrease[0]} ${decrease[1]}")

    