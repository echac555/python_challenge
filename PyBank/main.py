#Import csv module
import os
import csv

#Locate csv file
budget_data = os.path.join("PyBank/Resources/budget_data.csv")

#Reading CSV Module
with open (budget_data, newline="") as csvfile:

    #Determine variables and delimiter 
    csvreader = csv.reader(csvfile, delimiter =',')

    print(csvreader)

    #Skip Header Title
    csv_header = next(csvreader)

    #Determine variables, making a list of each one
    #Create list for date converted to months
    months=[]

    #Create list for Profit/Losses
    PL=[]

    #Read each row of data after header
    for row in csvreader:
        months.append(row[0])
        PL.append(int(row[1]))

    #Find variation in revenue
    revenue_variation = []

    for x in range(1, len(PL)):
            revenue_variation.append((int(PL[x]) - int(PL[x-1])))

    #Determine average variation in revenue
    revenue_average = sum(revenue_variation) / len(revenue_variation)

    #Determine total length of months
    month_total = len(months)

    #Determine greatest increase in revenue
    greatest_increase = max(revenue_variation)

    #Determine greatest decrease in revenue
    greatest_decrease = min(revenue_variation)

    #Printing Results
    print("Financial Analysis")

    print("------------------------------")

    print("Total Months: " + str(month_total))

    print("Total: " + "$" + str(sum(PL)))
          
    print("Average Change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_variation.index(max(revenue_variation))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[revenue_variation.index(min(revenue_variation))+1]) + " " + "$" + str(greatest_decrease))
         
    #Write results into text file
    #Open the file in write mode
    with open("financial_analysis.txt", "w") as file:

    # Write the financial analysis content to text file
        file.write("Financial Analysis\n")
        file.write("------------------------------\n")
        file.write("Total Months: " + str(month_total) + "\n")
        file.write("Total: $" + str(sum(PL)) + "\n")
        file.write("Average Change: $" + str(revenue_average) + "\n")
        file.write("Greatest Increase in Profits: " + str(months[revenue_variation.index(max(revenue_variation)) + 1]) + " $" + str(greatest_increase) + "\n")
        file.write("Greatest Decrease in Profits: " + str(months[revenue_variation.index(min(revenue_variation)) + 1]) + " $" + str(greatest_decrease) + "\n")
