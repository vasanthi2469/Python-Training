import numpy as np
from scipy import stats

# Set random seed for reproducibility
np.random.seed(42)

# Generate data points
x = np.linspace(-5, 5, 1000)

# 1. Normal (Gaussian) Distribution
mu, sigma = 0, 1  # mean and standard deviation
normal_dist = stats.norm(mu, sigma)

# 2. Uniform Distribution
a, b = -2, 2  # lower and upper bounds
uniform_dist = stats.uniform(a, b-a)

# 3. Exponential Distribution
lambda_param = 1.0  # rate parameter
exponential_dist = stats.expon(scale=1/lambda_param)

# Generate random samples
n_samples = 1000
normal_samples = normal_dist.rvs(n_samples)
uniform_samples = uniform_dist.rvs(n_samples)
exponential_samples = exponential_dist.rvs(n_samples)

# Calculate basic statistics
print("\nSample Statistics:")
print("\nNormal Distribution:")
print(f"Mean: {np.mean(normal_samples):.3f}")
print(f"Variance: {np.var(normal_samples):.3f}")
print(f"Standard Deviation: {np.std(normal_samples):.3f}")
print(f"Median: {np.median(normal_samples):.3f}")

print("\nUniform Distribution:")
print(f"Mean: {np.mean(uniform_samples):.3f}")
print(f"Variance: {np.var(uniform_samples):.3f}")
print(f"Standard Deviation: {np.std(uniform_samples):.3f}")
print(f"Median: {np.median(uniform_samples):.3f}")

print("\nExponential Distribution:")
print(f"Mean: {np.mean(exponential_samples):.3f}")
print(f"Variance: {np.var(exponential_samples):.3f}")
print(f"Standard Deviation: {np.std(exponential_samples):.3f}")
print(f"Median: {np.median(exponential_samples):.3f}")

# Calculate probabilities for specific ranges
print("\nProbability Calculations:")

# Normal Distribution Probabilities
print("\nNormal Distribution Probabilities:")
print(f"P(X ≤ 0): {normal_dist.cdf(0):.3f}")
print(f"P(X > 1): {1 - normal_dist.cdf(1):.3f}")
print(f"P(-1 ≤ X ≤ 1): {normal_dist.cdf(1) - normal_dist.cdf(-1):.3f}")
print(f"P(-2 ≤ X ≤ 2): {normal_dist.cdf(2) - normal_dist.cdf(-2):.3f}")

# Uniform Distribution Probabilities
print("\nUniform Distribution Probabilities:")
print(f"P(X ≤ 0): {uniform_dist.cdf(0):.3f}")
print(f"P(X > 1): {1 - uniform_dist.cdf(1):.3f}")
print(f"P(-1 ≤ X ≤ 1): {uniform_dist.cdf(1) - uniform_dist.cdf(-1):.3f}")

# Exponential Distribution Probabilities
print("\nExponential Distribution Probabilities:")
print(f"P(X ≤ 1): {exponential_dist.cdf(1):.3f}")
print(f"P(X > 1): {1 - exponential_dist.cdf(1):.3f}")
print(f"P(0 ≤ X ≤ 2): {exponential_dist.cdf(2) - exponential_dist.cdf(0):.3f}")

# Calculate percentiles
percentiles = [25, 50, 75]
print("\nPercentiles:")

print("\nNormal Distribution Percentiles:")
for p in percentiles:
    value = normal_dist.ppf(p/100)
    print(f"{p}th percentile: {value:.3f}")

print("\nUniform Distribution Percentiles:")
for p in percentiles:
    value = uniform_dist.ppf(p/100)
    print(f"{p}th percentile: {value:.3f}")

print("\nExponential Distribution Percentiles:")
for p in percentiles:
    value = exponential_dist.ppf(p/100)
    print(f"{p}th percentile: {value:.3f}")

# Calculate moments
print("\nDistribution Moments:")

print("\nNormal Distribution:")
print(f"Mean (1st moment): {normal_dist.moment(1):.3f}")
print(f"Variance (2nd central moment): {normal_dist.var():.3f}")
print(f"Skewness: {normal_dist.stats(moments='s'):.3f}")
print(f"Kurtosis: {normal_dist.stats(moments='k'):.3f}")

print("\nUniform Distribution:")
print(f"Mean (1st moment): {uniform_dist.moment(1):.3f}")
print(f"Variance (2nd central moment): {uniform_dist.var():.3f}")
print(f"Skewness: {uniform_dist.stats(moments='s'):.3f}")
print(f"Kurtosis: {uniform_dist.stats(moments='k'):.3f}")

print("\nExponential Distribution:")
print(f"Mean (1st moment): {exponential_dist.moment(1):.3f}")
print(f"Variance (2nd central moment): {exponential_dist.var():.3f}")
print(f"Skewness: {exponential_dist.stats(moments='s'):.3f}")
print(f"Kurtosis: {exponential_dist.stats(moments='k'):.3f}")