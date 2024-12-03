import scipy.stats as ss
import matplotlib.pyplot as mpl

n = 7072
p = 0.45

binomial = ss.binom.pmf(list(range(0, n + 1)), n, p)
poisson = ss.poisson.pmf(list(range(0, n + 1)), n * p)
normal = ss.norm.pdf(list(range(0, n + 1)), n * p, n * p * (1 - p))

mpl.plot(binomial)
mpl.plot(poisson)
mpl.plot(normal)
mpl.show()