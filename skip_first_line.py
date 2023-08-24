import csv

with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    headers = next(rdr)
    for row in rdr:
        print(row)