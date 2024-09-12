import csv

file_obj = open('customers.csv', 'r')

csv_obj = csv.reader(file_obj)

next(csv_obj)

# rec in this case is already a list, don't need to split it
for rec in csv_obj:
    print(rec)
    print(f"First Name: {rec[1]}")
    print(f"Last Name: {rec[2]}")
    print(f"Country: {rec[4]}")

    # we just want the program to pause, this is how you do it
    input()