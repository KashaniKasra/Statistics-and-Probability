## Project Overview

This project focuses on the exploration and application of key concepts in probability theory, including **Conditional Distribution**, **Moment Generating Functions**, and **Bayesian Estimation**. The project applies these theoretical concepts to practical problems, utilizing datasets and computational methods for real-world analysis.

## Key Components of the Project:

### 1. Conditional Distribution
The project involves analyzing the number of bus and metro station passes using the provided `tarbiat.csv` dataset.
   - The dataset is explored through histogram plots and the definition of random variables for bus and metro passes.
   - The goal is to identify which distribution best models these variables based on histograms and derived parameters.

### 2. Moment Generating Functions (MGF)
The project involves solving a variant of the **Coupon Collector's Problem**, where the moment generating function of a random variable \( X \), representing the number of attempts to collect all coupons, is calculated.
   - The Monte Carlo method is used to estimate the solution, running multiple trials to approximate the expected number of attempts required.
   - SymPy, a symbolic math library, is utilized to define the MGF and derive the expected value.

### 3. Bayesian Estimation
The dataset `digits.csv` contains hand-written digit data, and the goal is to estimate probabilities using Bayesian inference.
   - A Bernoulli distribution is used for each pixel, where the task is to estimate whether a pixel is lit or not, given a prior Beta distribution.
   - The problem explores updating the prior distribution to a posterior as new data is observed and inferring the most likely outcome using Bayesian updating.

## Deliverables:

1. **Python Implementations**:
   - Python scripts to calculate conditional distributions, moment generating functions, and apply Bayesian estimation using Monte Carlo simulations.
   - Use of libraries like `matplotlib` for plotting, `SymPy` for symbolic calculations, and `numpy` for numerical operations.

2. **Graphical Representations**:
   - Plots of histograms and density functions for the bus and metro dataset, showing how well the theoretical models fit the observed data.
   - Visualizations demonstrating the process of Bayesian updating and posterior distribution calculation.

3. **Statistical Analysis**:
   - Theoretical and experimental results comparing different distributions, moment generating functions, and Bayesian estimations.
   - Discussion on the applicability and accuracy of the methods used.

This project is part of the **Probability and Statistics** course at the University of Tehran.