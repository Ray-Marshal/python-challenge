#This is the Main Code for PyBank '..', 'Resources', 'budget_data.csv'
import os
import csv

filepath = ('C:\\Users\\mrrit\\OneDrive\\Documents\\UofO Data Class\\Wk3_Python\\python-challenge\\PyBank\\Resources\\budget_data.csv')
total_months = 0
net_profit_loss = 0
great_increase = 0
great_decrease = 0
this_month = 0
tot_cume_change = 0


with open(filepath, "r", encoding='utf') as budget_file:
    
    budget_reader = csv.reader(budget_file, delimiter=",")
    last_row = sum(1 for _ in budget_reader)
    budget_file.seek(0)
    next(budget_reader, None)

    for row_num, row in enumerate(budget_reader, start=1):
        last_month = this_month
        this_month = int(row[1])
        total_change = this_month - last_month
        date = row[0]
        total_months += 1
        net_profit_loss += this_month

        if row_num == 0:
            first_month = this_month

        if total_change > great_increase:
            great_increase = total_change
            great_inc_date = date

        if total_change < great_decrease:
            great_decrease = total_change
            great_dec_date = date

        if row_num == last_row:
            tot_cume_change = this_month - first_month

    average_change = tot_cume_change / total_months

print("Financial Analysis")
print("-------------------------")
print(f"Total Months:{total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Avereage Change: ${average_change}")
print(f"Greatest Increase in Profits: {great_inc_date} (${great_increase})")
print(f"Greatest Decrease in Profits: {great_dec_date} (${great_decrease})")