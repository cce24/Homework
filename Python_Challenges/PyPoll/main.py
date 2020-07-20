# PyPoll HW - Colin Ek
# Import required packages
import csv
import os

# Files to load and output 
file_to_load = os.path.join(r"PyPoll\Resources\election_data.csv")
file_to_output = os.path.join(r"PyPoll\Analysis\election_data.txt")

# Placeholders for Variables
total_votes = 0
interim = 0
Khan = 0
Correy = 0
Li= 0
OTooley = 0
total_votes_by_can = []
Winner = 0
Winner_Name = ()

#load csv file and read it
with open(file_to_load) as data:
    reader = csv.reader(data)
    header = next(reader)


    #Loop through each row, re-grab each field and store in a new list
    for row in reader:
        if row[0] != '' :
            total_votes = int(total_votes) + 1
        if row[2] == "Khan":
            Khan = Khan + 1
        if row[2] == "Correy":
            Correy = Correy + 1
        if row[2] == "Li":
            Li = Li + 1
        if row[2] == "O'Tooley":
            OTooley = OTooley + 1

    #Create Winner variable
    if Khan > Winner:
        Winner = Khan
        Winner_Name = "Khan"
    elif Correy > Winner:
        Winner = Correy
        Winner_Name = "Correy"
    elif Li > Winner:
        Winner = Li
        Winner_Name = "Li"
    elif OTooley > Winner:
        Winner = OTooley
        Winner_Name = "O'Tooley"
    # Test Winner variable to make sure it works
    # print(str(Winner))
    # print(str(Winner_Name))

    #create percentages for each result
    KP = (Khan/total_votes)*100
    CP = (Correy/total_votes)*100
    LP = (Li/total_votes)*100
    OP = (OTooley/total_votes)*100

    
    #print result to terminal
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    print("Khan: " + format(KP,'0.3f') + "% (" + str(Khan) + ")")
    print("Correy: " + format(CP, '0.3f') + "% (" + str(Correy) + ")")
    print("Li: " + format(LP, '0.3f') + "% (" + str(Li) + ")")
    print("O'Tooley: " + format(OP, '0.3f') + "% (" + str(OTooley) + ")")
    print("-------------------------")
    print("Winner: " + str(Winner_Name))
    print("-------------------------")

    #gather text lines for export to text file
    line1 = ("Election Results\n")
    line2 = ("-------------------------\n")
    line3 = ("Total Votes: " + str(total_votes) + "\n")
    line4 = ("-------------------------\n")
    line5 = ("Khan: " + format(KP,'0.3f') + "% (" + str(Khan) + ")" + "\n")
    line6 = ("Correy: " + format(CP, '0.3f') + "% (" + str(Correy) + ")") + "\n"
    line7 = ("Li: " + format(LP, '0.3f') + "% (" + str(Li) + ")" + "\n")
    line8 = ("O'Tooley: " + format(OP, '0.3f') + "% (" + str(OTooley) + ")" + "\n")
    line9 = ("-------------------------\n")
    line10 = ("Winner: " + str(Winner_Name) + "\n")
    line11 = ("-------------------------\n")

    #test to make sure iot works
    print(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11)


#Export results to text file
with open(file_to_output, 'w') as f:
    # text_writer = writer(f)
    f.writelines([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11])



