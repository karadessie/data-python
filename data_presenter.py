open_file = open("CupcakeInvoices.csv")

for line in open_file:
    print(line)

for cupcake_type in open_file:
  line = line.strip()
  values = line.split(',')
  print(values[2])

for invoice_total in open_file:
  line = line.strip()
  values = line.split(',')
  total = int(values[3]) * float(values[4])
  print(total)

total = 0

for grand_total in open_file:
  line = line.strip()
  values = line.split(',')
  total = total + (int(values[3]) * float(values[4]))

print(total)

open_file.close()