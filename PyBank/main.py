#This is the Main Code for PyBank
import os
import csv

#Establishing variables
#filepath = '../Resources/budget_data.csv' - I could never get this method to work, so I opted for what you see below
filepath = ('C:\\Users\\mrrit\\OneDrive\\Documents\\UofO Data Class\\Wk3_Python\\python-challenge\\PyBank\\Resources\\budget_data.csv')
total_months = 0
net_profit_or_loss = 0
great_increase = 0
great_decrease = 0
this_month = 0
row_num = 0
average_change = 0
previous_month = None
monthly_change = 0

#opening the file and skipping the header row
with open(filepath, "r", encoding='utf') as budget_file:
    
    budget_reader = csv.reader(budget_file, delimiter=",")
    #last_row = sum(1 for _ in budget_reader)
    budget_file.seek(0)
    next(budget_reader, None)

    for row in (budget_reader):

        #Calculating the month to month changes excluding 0 --> first month change
        if row_num == 0:
            this_month = int(row[1])
        else:    
            previous_month = this_month
            this_month = int(row[1])
            monthly_change = this_month - previous_month
        
        #finding the date for code below, and adding all of the data we needed from this row to the cumulative variables 
        date = row[0]
        total_months += 1
        net_profit_or_loss += this_month
        average_change += monthly_change
        row_num += 1

        #Adding the motnthly changes to greatest increase or decrease as necessary
        if monthly_change > great_increase:
            great_increase = monthly_change
            great_inc_date = date

        if monthly_change < great_decrease:
            great_decrease = monthly_change
            great_dec_date = date

    average_change = average_change / (total_months - 1)

    #printing results to terminal
    print("Financial Analysis \n-------------------------")
    print(f"Total Months: {total_months} \nTotal: ${net_profit_or_loss} \nAvereage Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {great_inc_date} (${great_increase}) \nGreatest Decrease in Profits: {great_dec_date} (${great_decrease})")

    #writing results to new text file
    pybank_results_file = open("pybank_results_file.txt", "w")
    print("Financial Analysis \n-------------------------", file=pybank_results_file)
    print(f"Total Months: {total_months} \nTotal: ${net_profit_or_loss} \nAvereage Change: ${round(average_change, 2)}", file=pybank_results_file)
    print(f"Greatest Increase in Profits: {great_inc_date} (${great_increase}) \nGreatest Decrease in Profits: {great_dec_date} (${great_decrease})", file=pybank_results_file)

    pybank_results_file.close()
budget_file.close()