import random
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as pld

digits_data = pd.read_csv(r"c:\Users\Asus\Desktop\digits.csv")

label_201 = digits_data.loc[200]
label_202 = digits_data.loc[201]
digits_data = digits_data.drop(201)
digits_data = digits_data.drop(200)

for i in range(len(digits_data)):
    for j in range(1, len(digits_data.loc[i])):
        if (digits_data.iat[i, j] < 128):
            digits_data.iat[i, j] = 0
        else:
            digits_data.iat[i, j] = 1

row_index = random.randint(0, len(digits_data) - 1)
row = digits_data.loc[row_index]
row = np.reshape(row[1:], (28, 28))
pld.imshow(row)
pld.show()