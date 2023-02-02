import csv
data = open('input','r')
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for line in data:
        writer.writerow(line)