#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 3, Exercise 3

import csv
import matplotlib.pyplot as plt

# Parsing cencus data
populations = []
with open('CensusTownAndCityPopulation.csv', 'r') as census:
    for town in csv.reader(census):
        populations.append(town[2])

# Taking first significant digit
sig_dig = []
for p in range(len(populations)):
    sig_dig.append(int(populations[p][0]))

# Adding the figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(sig_dig, 9, align = 'left')
ax.set(title = 'Distribution of American city populations', xlabel = '1st significant digit', ylabel = 'Frequency')
plt.savefig('sig_digit.png')
plt.show()
