open_file = open("CupcakeInvoices.csv")

for line in open_file:
    print(line) 

open_file.seek(0, 0)
for line in open_file:
    values = line.split(',')
    print(values[2])



open_file.seek(0, 0)
for line in open_file:
    values = line.split(',')
    total = int(values[3]) * float(values[4])
    total = round(total, 2)
    print(total)

total = 0

open_file.seek(0, 0)
for line in open_file:
    values = line.split(',')
    total = total + (int(values[3]) * float(values[4]))
    total = round(total, 2)
    print(total)

open_file.close()