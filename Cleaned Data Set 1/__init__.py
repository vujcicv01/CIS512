import csv as csv

academic_year = []
college_name = []
sector = []
headcount = []
dollars = []
f = open("C:\\Users\\vvujcic\\pycharmprojects\\cis512\\Cleaned Data Set 1\\dataset.csv")
csv.reader(f)
for line in f:
    if "null" not in line:
        if "3-SUNY SO" in line:
                splitline = line.split(',')
                academic_year.append(splitline[0])
                college_name.append(splitline[3])
                sector.append(splitline[4])
                headcount.append(splitline[5])
                dollars.append(splitline[7])
print (college_name)
print (dollars)