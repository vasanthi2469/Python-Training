import numpy as np

# Simulate 1000 experiments of flipping a coin 10 times
n_trials = 10
p_success = 0.5
binomial_samples = np.random.binomial(n_trials, p_success, 1000)

# Print the first 10 samples
print(binomial_samples[:10])