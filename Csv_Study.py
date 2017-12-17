import  csv

with open('a.csv','r') as csv_file:
    Cr=csv.reader(csv_file)
    for line in Cr:
        print(line)

print("----------------")

with open('a.csv','r') as csv_file:
    Cr=csv.DictReader(csv_file)
    for line in Cr:
        print(line['RowA'])







