open_file = open("CupcakeInvoices.csv")

for row in open_file:
    print(row) 
    break

for cupcake_type in open_file:
    values = row.split(',')
    print(values[2])
    break

for invoice_total in open_file:
    values = row.split(',')
    total = int(values[3]) * float(values[4])
    total = round(total, 2)
    print(total)
    break

total = 0

for gtotal in open_file:
    values = row.split(',')
    total = total + (int(values[3]) * float(values[4]))
    total = round(total, 2)
    print(total)

open_file.close()