import os
import csv

pybankcsv = os.path.join("Resources", 'budget_data.csv')
pybanktxt = os.path.join("Analysis", 'budget_analysis.txt')
months = []
profit = []
changes = []

with open(pybankcsv) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    first_data_row = next(csvreader)
    months.append(first_data_row[0])
    profit.append(int(first_data_row[1]))

    previous_profit = int(first_data_row[1])

    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
        change = (int(row[1])) - previous_profit
        changes.append(change)
        previous_profit = (int(row[1]))


total_months = len(months)
profit = sum(profit)
avg_change = round(sum(changes)/len(changes), 2)

max_change = max(changes)
min_change = min(changes)

max_change_index = changes.index(max_change) + 1
min_change_index = changes.index(min_change) + 1
max_month = months[max_change_index]
min_month = months[min_change_index]


budget_output = (f'Financial Analysis\n'
f'----------------------------\n'
f'Total Months: {total_months}\n'
f'Total: ${profit}\n'
f'Average Change: ${avg_change}\n'
f'Greatest Increase in Profits: {max_month} (${max_change})\n'
f'Greatest Decrease in Profits: {min_month} (${min_change})')

with open(pybanktxt, 'w') as f:
    f.write(budget_output)

print(budget_output)




