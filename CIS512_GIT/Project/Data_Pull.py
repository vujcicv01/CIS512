import csv as csv

year = []
college_name= []
group = []
count= []
dollars= []

f = open("c:\scholarships.csv")
csv.reader(f)
for line in f:
    if "null" not in line:
        if ("1-CUNY SR" in line or "2-CUNY CC" in line or "3-SUNY SO" in line or "4-SUNY CC" in line):

            splitline = line.split(',')
            year.append(splitline[0])
            college_name.append(splitline[3])
            group.append(splitline[4])
            count.append(splitline[5])
            dollars.append(splitline[7])
print (year,college_name,group,count,dollars)
