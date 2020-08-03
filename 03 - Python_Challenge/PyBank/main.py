#PyBank HW - Colin Ek
# Import required packages
import csv
import os
import statistics

# Files to load and output 
file_to_load = os.path.join(r"PyBank\Resources\budget_data.csv")
file_to_output = os.path.join(r"PyBank\Analysis\budget_data.txt")

# Placeholders for Variables
total_months = 0
total = 0
average_change = []
greatest_increase = 0
greatest_decrease = 0
ans=[]
col=1
greatest_month = ()

#load csv file and read it
with open(file_to_load) as data:
    reader = csv.reader(data)
    header = next(reader)

    #Count Total Months
    for row in reader:    
        total = int(total) + int(row[1])
        total_months = int(total_months) + 1

        
#load data for greatest increase and decrease calculations that require list reading
with open(file_to_load) as data:
    reader = csv.reader(data)
    header = next(reader) 
    
    numrows=list(reader) 
    
    #creat greatest increase and decrease variables
    for i in range(len(numrows)-1):
        diff = int(numrows[i+1][1])-int(numrows[i][1])
        ans.append(diff)
        if diff>greatest_increase:
            greatest_increase=diff
        if diff<greatest_decrease:
            greatest_decrease=diff
    
    #create mean change variable
    x=statistics.mean(ans)
     

# Find month and year assocaited with greatest increase and decrease, respectively, and split those values so that they can be reformatted
with open(file_to_load) as data:
    reader = csv.reader(data)
    header = next(reader) 
    
    numrows=list(reader) 

    for i in range(len(numrows)-1): 
        if (int(numrows[i+1][1])-int(numrows[i][1])) == int(greatest_increase):
            greatest_increase_month=numrows[i+1][0]
        if (int(numrows[i+1][1])-int(numrows[i][1])) == int(greatest_decrease):
            greatest_decrease_month=numrows[i+1][0]    

    #Split and reformat greatest increase
    GIM = greatest_increase_month.split("-")
    GIyear = GIM[0]
    GImonth = GIM[1]
    GID = (f"{GImonth}-20{GIyear}")
    
    #Split and reformat greatest decrease
    GDM = greatest_decrease_month.split("-")
    GDyear = GDM[0]
    GDmonth = GDM[1]
    GDD = (f"{GDmonth}-20{GDyear}")

    #print result to terminal
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total))
    print("Average Change: $" + format(x, '0.2f'))
    print("Greatest Increase in Profits: " + (GID) + " ($" + str(max(ans)) + ")")
    print("Greatest Increase in Profits: " + (GDD) + " ($" + str(min(ans)) + ")")

    #gather text lines for export to text file
    line1 = ("Financial Analysis\n")
    line2 = ("-------------------------\n")
    line3 = ("Total Months: " + str(total_months) + "\n")
    line4 = ("Total: $" + str(total) + "\n")
    line5 = ("Average Change: $" + format(x, '0.2f') + "\n")
    line6 = ("Greatest Increase in Profits: " + (GID) + " ($" + str(max(ans)) + ")" + "\n")
    line7 = ("Greatest Increase in Profits: " + (GDD) + " ($" + str(min(ans)) + ")" + "\n")

    #test to make sure iot works
    print(line1, line2, line3, line4, line5, line6, line7)

#Export results to text file
with open(file_to_output, 'w') as f:
    # text_writer = writer(f)
    f.writelines([line1, line2, line3, line4, line5, line6, line7])
