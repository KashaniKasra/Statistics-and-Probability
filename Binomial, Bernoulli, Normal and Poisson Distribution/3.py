import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as mpl

mean = 80
std = 12

normal = ss.norm(mean, std * std)

ceil_grades = 1 - 0.1
cdf_0 = 0
cdf_x = ceil_grades + cdf_0
Q1 = ss.norm.ppf(cdf_x, mean, std)

perc_50th = ss.norm.ppf(0.5, mean, std)
perc_75th = ss.norm.ppf(0.75, mean, std)
Q2 = (perc_50th, perc_75th)

Q3 = normal.cdf(90) - normal.cdf(80)

print (Q1)
print(Q2)
print(Q3)