import csv

inFile = open('employee_data.csv', 'r')

csv_obj = csv.reader(inFile)

next(csv_obj)

for rec in csv_obj:
    print(f"Name: {rec[1]}")
    print(f"Salary: $   {float(rec[3]):,.2f}")

    bonus = float(rec[3]) * float(rec[7])

    print(f"Bonus:  $   {bonus:,.2f}")

    pay = float(rec[3]) + bonus

    print(f"Pay:    $   {pay:,.2f}")
    print()
    input()