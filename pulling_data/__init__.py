import csv as csv

town= []
state = []
school= []

f = open("/home/VukVujcic/Downloads/Most+Recent+Cohorts+(Scorecard+Elements).csv")
csv.reader(f)
for line in f:
    if "null" not in line:
            splitline = line.split(',')
            town.append(splitline[4])
            state.append(splitline[5])
            school.append(splitline[3])
print (town)