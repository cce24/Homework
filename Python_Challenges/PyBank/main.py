# -*- coding: UTF-8 -*-
# Import required packages
import csv
import os
import statistics

# Files to load and output 
file_to_load = os.path.join(r"PyBank\Resources\budget_data.csv")
file_to_output = os.path.join(r"PyBank\Analysis\budget_data.txt")



# Placeholders for re-formatted contents
total_months = 0
total = 0
average_change = []
greatest_increase = 0
greatest_decrease = 0
ans=[]
col=1
greatest_month = ()


with open(file_to_load) as data:
    reader = csv.reader(data)
    header = next(reader)

    for row in reader:    
        total = int(total) + int(row[1])
        total_months = int(total_months) + 1


        # date = row[0].split("-")
        # year = date[0]
        # month = date[1]
        # reformatted_date = (f"{month}-20{year}")

        


with open(file_to_load) as data:
    reader = csv.reader(data)
    header = next(reader) 
    
    numrows=list(reader) 
    

    #THIS WORKS, DON'T DELETE
    for i in range(len(numrows)-1):
        diff = int(numrows[i+1][1])-int(numrows[i][1])
        ans.append(diff)
        if diff>greatest_increase:
            greatest_increase=diff
        if diff<greatest_decrease:
            greatest_decrease=diff
    #print(greatest_increase)
    #print(greatest_decrease)
    
    x=statistics.mean(ans)
     


with open(file_to_load) as data:
    reader = csv.reader(data)
    header = next(reader) 
    
    numrows=list(reader) 

    for i in range(len(numrows)-1): 
        if (int(numrows[i+1][1])-int(numrows[i][1])) == int(greatest_increase):
            greatest_increase_month=numrows[i+1][0]
        if (int(numrows[i+1][1])-int(numrows[i][1])) == int(greatest_decrease):
            greatest_decrease_month=numrows[i+1][0]    
    #print(greatest_month)

    GIM = greatest_increase_month.split("-")
    GIyear = GIM[0]
    GImonth = GIM[1]
    GID = (f"{GImonth}-20{GIyear}")
    #print(str(GID))

    
    GDM = greatest_decrease_month.split("-")
    GDyear = GDM[0]
    GDmonth = GDM[1]
    GDD = (f"{GDmonth}-20{GDyear}")
    #print(str(GDD))


    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total))
    print("Average Change: $" + format(x, '0.2f'))
    print("Greatest Increase in Profits: " + (GID) + " ($" + str(max(ans)) + ")")
    print("Greatest Increase in Profits: " + (GDD) + " ($" + str(min(ans)) + ")")

    line1 = ("Financial Analysis\n")
    line2 = ("-------------------------\n")
    line3 = ("Total Months: " + str(total_months) + "\n")
    line4 = ("Total: $" + str(total) + "\n")
    line5 = ("Average Change: $" + format(x, '0.2f') + "\n")
    line6 = ("Greatest Increase in Profits: " + (GID) + " ($" + str(max(ans)) + ")" + "\n")
    line7 = ("Greatest Increase in Profits: " + (GDD) + " ($" + str(min(ans)) + ")" + "\n")

    print(line1, line2, line3, line4, line5, line6, line7)


with open(file_to_output, 'w') as f:
    # text_writer = writer(f)
    f.writelines([line1, line2, line3, line4, line5, line6, line7])
