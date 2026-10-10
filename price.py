import numpy as np
def simulate_mid(mid0, sigma, dt, n_steps, seed):  #mid0 is intial mid price, sigma is volatility, dt is delta time, n_steps is the number is steps, seed is the random seed 
    rng = np.random.default_rng(seed)  # Set the random seed for reproducibility
    z = rng.normal(0, 1, n_steps)
    changes = sigma * np.sqrt(dt) * z  # Calculate the changes in mid price
    mid_prices = mid0 + np.cumsum(changes)  # Cumulative sum to get the mid price changes
    return np.concatenate(([mid0], mid_prices))  # Include the initial mid price in the result

if __name__ == "__main__":
    path = simulate_mid(100.0, 2.0, 0.01, 1000, 43)
    print(path[:5])
    print(len(path))
