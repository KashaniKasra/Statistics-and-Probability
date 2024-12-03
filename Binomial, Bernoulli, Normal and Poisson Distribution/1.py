import numpy as np
import matplotlib.pyplot as mpl

def binomial(n, m, pp):
    sample = np.random.choice([1, 0], p=[pp, 1 - pp], size=(n * m))
    sample_matrix = sample.reshape(n, m)
    success_numbers = np.sum(sample_matrix, axis=0)
    return success_numbers

def bin_practical_Exp():
    Exps = []
    for p in range(0, 101):
        success_numbers = binomial(500, 5000, p / 100)
        Exp = np.sum(success_numbers) / 5000
        Exps.append(Exp)
    mpl.plot(np.array(range(0, 101)), np.array(Exps))

def bin_practical_Var():
    Vars = []
    for p in range(0, 101):
        success_numbers = binomial(500, 5000, p / 100)
        Var = np.var(success_numbers)
        Vars.append(Var)
    mpl.plot(np.array(range(0, 101)), np.array(Vars))
    
def bin_theoretical_Exp():
    n = 500
    Exps = []
    for p in range(0, 101):
        Exp = n * (p / 100)
        Exps.append(Exp)
    mpl.plot(np.array(range(0, 101)), np.array(Exps))
    
def bin_theoretical_Var():
    n = 500
    Vars = []
    for p in range (0, 101):
        Var = n * (p / 100) * (1 - (p / 100))    
        Vars.append(Var)
    mpl.plot(np.array(range(0, 101)), np.array(Vars))
    
bin_practical_Exp()
bin_theoretical_Exp()
mpl.show()
bin_practical_Var()
bin_theoretical_Var()
mpl.show()