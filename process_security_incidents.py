import csv

inputCsv = "security_incidents.csv"
outputCsv = "security_incidents_modified.csv"

with open(inputCsv, mode = 'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

nuCol = "Status"
colVal = "Pending"

header = data[0] + [nuCol]

nuRows = [row + [colVal] for row in data[1:]]

with open(outputCsv, mode = 'w', newline= '') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(nuRows)

    