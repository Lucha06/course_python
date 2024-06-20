import numpy as np
import math

# Step 1: Create the functions in Python
def f1(x):
    x1 = np.where(x >= 0, x / 3, -(x + 5) / 6)
    return x1

def f2(x):
    x1 = np.where(x < 0, np.sqrt(np.abs(x)),
                  np.where(x < 1, 4 * np.cos(2 * np.pi * x),
                           x * np.log2(np.e ** x * np.tanh(x))))
    return x1

# Step 2: Create a list with 10,000 random numbers from a Normal distribution with mu = 2 and sigma_squared = 5
mu = 2
sigma_squared = 5
sigma = np.sqrt(sigma_squared)
random_numbers = np.random.normal(mu, sigma, 10000)

# Step 3: Evaluate the functions with the random numbers
results_f1 = f1(random_numbers)
results_f2 = f2(random_numbers)

# Step 4: Print out the results
print("Random Numbers:")
print(random_numbers)
print("\nResults for f1:")
print(results_f1)
print("\nResults for f2:")
print(results_f2)
