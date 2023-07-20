import os
import csv

budget_data = os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Read the header row first 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

          
    months = []
    profit_losses = []
    changes = []

    for row in csv_reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

# Calculate the total number of months
total_months = len(months)    

# Calculate the net total amount of profit/losses
net_total = sum(profit_losses)

# Calculate the changes in profit/losses Store them in a list
for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

# Print the analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")