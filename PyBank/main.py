#This is the Main Code for PyBank '..', 'Resources', 'budget_data.csv'
import os
import csv

filepath = ('C:\\Users\\mrrit\\OneDrive\\Documents\\UofO Data Class\\Wk3_Python\\python-challenge\\PyBank\\Resources\\budget_data.csv')
Total_Months = 0
Net_Profit_Loss = 0
Average_Change = 0
Great_Increase = 0
Great_Inc_Date = 0
Great_Decrease = 0
Great_Dec_Date = 0


with open(filepath, encoding='utf') as budget_file:
    
    budget_reader = csv.reader(budget_file, delimiter=",")
    next(budget_reader, None)

    for row in budget_reader:
        inc_dec = int(row[1])
        date = row[0]
        Total_Months += 1
        Net_Profit_Loss += inc_dec

        if inc_dec > Great_Increase:
            Great_Increase = inc_dec
            Great_Inc_Date = date

        if inc_dec < Great_Decrease:
            Great_Decrease = inc_dec
            Great_Dec_Date = date


    print(Great_Decrease)
    print(Great_Dec_Date)
    print(Great_Increase)
    print(Great_Inc_Date)
