import csv

inFile = open('customers.csv', 'r')
outFile = open('customer_country.csv', 'w')

csv_obj = csv.reader(inFile)

next(csv_obj)

outFile.write('Full Name,Country\n')

count = 0

for rec in csv_obj:
    outFile.write(f"{rec[1]} ")
    outFile.write(f"{rec[2]}")
    outFile.write(f",")
    outFile.write(f"{rec[4]}\n")

    count += 1

print(count)

outFile.close()