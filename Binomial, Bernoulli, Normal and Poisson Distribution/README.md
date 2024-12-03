## Project Overview

This project focuses on the exploration and implementation of different statistical distributions, including **Binomial**, **Bernoulli**, **Normal**, and **Poisson** distributions. The primary goal is to use these distributions to solve real-world problems through simulations and analysis.

## Key Components of the Project:

### 1. Binomial and Bernoulli Distributions
The relationship between **Binomial** and **Bernoulli** distributions is explored. The project demonstrates how repeated trials of Bernoulli-distributed random variables result in a Binomial distribution.
   - The variance and mean of the Binomial distribution are calculated and compared with theoretical values for different probabilities of success \( p \).

Key formulas:
\[
E[Y] = np, \quad Var(Y) = np(1 - p)
\]
where \( n \) is the number of trials and \( p \) is the probability of success.

### 2. Poisson and Normal Approximations of the Binomial Distribution
The project demonstrates how the **Poisson** and **Normal** distributions can approximate the **Binomial** distribution under specific conditions.
   - The Poisson approximation is particularly effective for small probabilities of success, while the Normal approximation is more accurate for probabilities close to 0.5.

Approximation example:
\[
X \sim Bin(n, p) \quad \text{is approximated by} \quad X \sim Poi(\mu) \quad \text{or} \quad X \sim N(\mu, \sigma^2)
\]
depending on the scenario.

### 3. Normal Distribution
The project highlights the importance of the **Normal distribution** and its use in various statistical analyses, such as calculating probabilities for real-world events.
   - The Central Limit Theorem is referenced, showing how the sum of independent random variables tends to follow a Normal distribution.

## Deliverables:

1. **Code Implementations**:
   - Python code for simulating Binomial, Bernoulli, Poisson, and Normal distributions.
   - Use of libraries such as `numpy` and `scipy` for generating random variables and performing statistical analysis.

2. **Graphs and Comparisons**:
   - Graphs comparing the variance and mean of the simulated and theoretical distributions.
   - Visualization of how the Poisson and Normal distributions approximate the Binomial distribution.

3. **Analysis**:
   - Statistical comparison between theoretical and experimental results.
   - Discussion on when and why certain approximations are more appropriate.

This project is part of the **Probability and Statistics** course at the University of Tehran.