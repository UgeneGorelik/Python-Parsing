#Example of Basic parsing using csv lib

import  csv

#simple parse and print

with open('a.csv','r') as csv_file:
    Cr=csv.reader(csv_file)
    for line in Cr:
        print(line)

print("----------------")

#parsing using Dict Reader lib that converts CSV do DIct
with open('a.csv','r') as csv_file:
    Cr=csv.DictReader(csv_file)
    for line in Cr:
        print(line['RowA'])







