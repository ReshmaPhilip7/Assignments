# Assignment: Descriptive and Inferential Statistics Using Python
# Section 1: Descriptive Statistics
# 1. Measures of Central Tendency:
# Given the dataset data = [12, 15, 14, 10, 18, 20, 22, 24, 17, 19],
# calculate the Mean,Median, and Mode using both Excel/Google Sheets/ Python.
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt

x = [12, 15, 14, 10, 18, 20, 22, 24, 17, 19]
Nr = x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9]
Dr = 10
mean = Nr / Dr
print("mean=", mean)
sortx = sorted(x)
count = len(x)
if count % 2 == 0:
    sum1 = int(sortx[4]) + int(sortx[5])
    med1 = sum1 / 2
    print("median=", med1)
else:
    med1 = sortx[5]
    print("median=", med1)
mode1 = stat.mode(x)
print("mode=", mode1)
# 2. Percentiles and Quartiles:
# Compute the 25th percentile (Q1), 50th percentile (Q2),
# and 75th percentile (Q3) for the dataset using both tools.
percentile25 = np.percentile(sortx, 25)
percentile50 = np.percentile(sortx, 50)
percentile75 = np.percentile(sortx, 75)
print("25th percentile=", percentile25)
print("50th percentile=", percentile50)
print("75th percentile=", percentile75)
# 6. Measures of Dispersion:
# Compute the Range, Variance, and Standard Deviation using both Excel/Google
# Sheets/Python.
max1 = max(x)
min1 = min(x)
range1 = max1 - min1
print("range=", range1)
std = stat.stdev(sortx)
print("standard deviation=", std)
varnce = stat.variance(sortx)
print("variance=", varnce)
# 9. Scatter Plot Visualization:
# Create a scatter plot using both Excel/Python to visually inspect the
# correlation between x and y.
x = [10, 20, 30, 40, 50]
y = [5, 10, 15, 20, 25]
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plot of x")
plt.show()
