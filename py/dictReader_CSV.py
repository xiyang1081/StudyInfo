import csv
with open('MF65+_AUTO_HSPA_IPV4&v6.csv','rb+') as csv_file:
    for d in csv.DictReader(csv_file):
        print d
