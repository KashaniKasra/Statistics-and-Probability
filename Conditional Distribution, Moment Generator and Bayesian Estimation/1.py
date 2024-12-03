import numpy as np
import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as mpl

tarbiat_data = pd.read_csv(r"c:\Users\Asus\Desktop\Tarbiat.csv")
metro = list(tarbiat_data.loc[:, "metro"])
BRT = list(tarbiat_data.loc[:, "BRT"])

   # Q1
mpl.hist(metro)
mpl.hist(BRT)
mpl.show()

   # Q2
landa_X = sum(metro) / len(metro)
landa_Y = sum(BRT) / len(BRT)

   # Q3 & Q4
poisson_X = ss.poisson.pmf(list(range(0, 20)), landa_X)
mpl.hist(metro, density=True)
mpl.plot(poisson_X)
mpl.show()

   # Q5
Z = metro + BRT
landa_Z = landa_X + landa_Y
poisson_Z = ss.poisson.pmf(list(range(0, 20)), landa_Z)
mpl.plot(poisson_Z)
mpl.hist(Z, density=True)
mpl.show()

   # Q7
n_W = 8
p_W = landa_X / landa_Z
binomial_W = ss.binom.pmf(list(range(0, 20)), n_W, p_W)
mpl.plot(binomial_W)
mpl.show()

   # Q8
metro_and_BRT = np.array(metro) + np.array(BRT)
indexes = np.where(metro_and_BRT == 8)
W = list(np.take(metro, indexes))
mpl.hist(W, density=True)
mpl.plot(binomial_W)
mpl.show()