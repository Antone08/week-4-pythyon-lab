data = open('CupcakeInvoices.csv')

# Question 3
for row in data:
    print(row)

# Question 4
    line = row.split(',')
    print(line[2])

# Question 5
    total = int(line[3]) * float(line[4])
    print(total)

# Question 6 
total = 0 

for row in data:
    line = row.split(',')

    total += (int(line[3]) * float(line[4]))
    rounded = round(total, 2)
    print(rounded)

data.close()

import matplotlib.pyplot as plt


plt.bar([1,2,3], [4,5,6])

plt.show()


total_chocolate = 0
total_vanilla = 0 
total_strawberry = 0 

for row in data:
    