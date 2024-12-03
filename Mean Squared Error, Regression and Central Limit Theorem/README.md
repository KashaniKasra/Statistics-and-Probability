## Project Overview

This project explores key concepts in statistics, including **Mean Squared Error (MSE)**, **Regression**, and the **Central Limit Theorem (CLT)**. The project applies these theoretical concepts to various datasets and utilizes Python for simulations and data analysis.

## Key Components of the Project:

### 1. Mean Squared Error (MSE)
The project focuses on calculating MSE in the context of image reconstruction using an autoencoder model on the **MNIST** dataset.
   - The goal is to analyze the reconstruction error and evaluate the autoencoder's performance by calculating MSE between original and reconstructed images.
   - Histogram plots and Kolmogorov-Smirnov tests are used to assess the distribution of MSE values.

### 2. Regression & Least Squares
The project applies regression analysis on a dataset to fit a line to the data using the least squares method.
   - Outlier detection and the impact of leverage points are investigated by analyzing specific data points that influence the regression line.
   - The project calculates the **R² (coefficient of determination)** to evaluate the fit of the regression model and explores methods to handle outliers.

### 3. Central Limit Theorem (CLT) and Sampling
The project involves simulations demonstrating the CLT, which states that the sum of a large number of independent and identically distributed random variables tends to follow a normal distribution.
   - Using the **FIFA 2020** dataset, the project explores sampling techniques, computes summary statistics, and generates **Q-Q plots** to compare data distributions against a theoretical normal distribution.
   - The **Shapiro-Wilk Test** is used to test for normality, and the project simulates Poisson-distributed data to investigate how the CLT applies as the sample size increases.

## Deliverables:

1. **Python Code**:
   - Code for calculating MSE using the MNIST dataset and pre-trained autoencoder models.
   - Python scripts for performing regression analysis, detecting outliers, and calculating R².
   - Code for CLT demonstrations, including sampling, generating Q-Q plots, and performing the Shapiro-Wilk test.

2. **Graphical Analysis**:
   - Histogram and Q-Q plots to visualize data distributions and compare them with theoretical distributions.
   - Regression plots showcasing the impact of outliers and leverage points on the regression line.

3. **Statistical Analysis**:
   - Analysis of the results from MSE calculations, regression, and CLT simulations.
   - Interpretation of the outcomes of normality tests and hypothesis tests.

This project is part of the **Probability and Statistics** course at the University of Tehran.