#####################################################
# Tyler Hedegard
# 6/2/2016
# Th/inkful Data Science
# prob.py
#####################################################

import collections

testlist = [1, 4, 5, 6, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

c = collections.Counter(testlist)

# calculate the number of instances in the list
count_sum = sum(c.values())

print("From this list: {}".format(testlist))
for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9, 13]
plt.boxplot(x)
plt.savefig("images/boxplot.png")

plt.figure()
plt.hist(x, histtype='bar')
plt.savefig("images/histogram.png")

import numpy as np
import scipy.stats as stats

plt.figure()
test_data = np.random.normal(size=10000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("images/qq_normal_distribution.png")
plt.figure()
test_data2 = np.random.uniform(size=10000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("images/qq_uniform_distribution.png")
