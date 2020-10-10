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
    crease = 0
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
            # finding the greatest increase and decrease by storing the current change
            # and putting it up against what was already stored, and replacing, if necessary
            crease = int(row[1]) - avg
            if int(increase[1]) < crease:
                increase.pop(1)
                increase.pop(0)
                increase.append(row[0])
                increase.append(crease)
            if int(decrease[1]) > crease:
                decrease.pop(1)
                decrease.pop(0)
                decrease.append(row[0])
                decrease.append(crease)
            # storing the current row
            avg = int(row[1])
        
        

#  doing month - 1 because there is 1 less change than the number of months
average = average / (month - 1)
average = round(average, 2)    
print("Financial Analysis")
print("______________________")
print(f"Total Months: {month}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {increase[0]} (${increase[1]})")
print(f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})")

# Making output path for the txt
output_path = os.path.join("Analysis", "Analysis.txt")

# writing to the txt
f = open(output_path, "w")
f.write("Financial Analysis \n")
f.write("______________________\n")
f.write(f"Total Months: {month}\n")
f.write(f"Total: ${total}\n")
f.write(f"Average Change: ${average}\n")
f.write(f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n")
f.write(f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})")

    