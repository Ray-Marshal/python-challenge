#This is the Main Code for PyBank
import os
import csv

filepath = ('C:\\Users\\mrrit\\OneDrive\\Documents\\UofO Data Class\\Wk3_Python\\python-challenge\\PyBank\\Resources\\budget_data.csv')
total_months = 0
net_profit_loss = 0
great_increase = 0
great_decrease = 0
this_month = 0
tot_cume_change = 0
row_num = 0
average_change = 0


with open(filepath, "r", encoding='utf') as budget_file:
    
    budget_reader = csv.reader(budget_file, delimiter=",")
    last_row = sum(1 for _ in budget_reader)
    #last_row = index.budget_reader[-1]
    budget_file.seek(0)
    next(budget_reader, None)

    for row in (budget_reader):
        last_month = this_month
        this_month = int(row[1])
        total_change = this_month - last_month
        date = row[0]
        total_months += 1
        net_profit_loss += this_month
        average_change += total_change

        if row_num == 0:
            first_month = this_month

        row_num += 1

        if total_change > great_increase:
            great_increase = total_change
            great_inc_date = date

        if total_change < great_decrease:
            great_decrease = total_change
            great_dec_date = date

        if row_num == last_row - 1:
            tot_cume_change = last_month - first_month

    average_change = average_change / total_months

    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_profit_loss}")
    print(f"Avereage Change: ${average_change}")
    print(f"Greatest Increase in Profits: {great_inc_date} (${great_increase})")
    print(f"Greatest Decrease in Profits: {great_dec_date} (${great_decrease})")

    pybank_results_file = open("pybank_results_file.txt", "w")
    print("Financial Analysis", file=pybank_results_file)
    print("-------------------------", file=pybank_results_file)
    print(f"Total Months: {total_months}", file=pybank_results_file)
    print(f"Total: ${net_profit_loss}", file=pybank_results_file)
    print(f"Avereage Change: ${average_change}", file=pybank_results_file)
    print(f"Greatest Increase in Profits: {great_inc_date} (${great_increase})", file=pybank_results_file)
    print(f"Greatest Decrease in Profits: {great_dec_date} (${great_decrease})", file=pybank_results_file)

    pybank_results_file.close()
    budget_file.close()
    
#print(last_row)