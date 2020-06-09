
import os
import csv

budget_data = os.path.join("Resources", "PybankData.csv")

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)



    # find net amount of profit and loss
    P = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    revenue_change = []

    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))
    
    # calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase/decrease in revenue
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)


    # print the Results
    print("Financial Analysis")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(sum(P)))
    print("Average change: $" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

    
    #create text file
    
    file = open("output.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total: $" + str(sum(P)) + "\n")
    file.write("Average change: $" + str(revenue_average) + "\n")
    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
    file.close()
