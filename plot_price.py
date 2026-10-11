import matplotlib.pyplot as plt
from price import simulate_mid
import numpy as np
path = simulate_mid(100.0, 2.0, 0.01, 1000, 42)
plt.plot(path)
plt.xlabel("Time")
plt.ylabel("Mid Price")
plt.title("Simulated Mid Price Path")
plt.savefig("price_path.png")  # Save the plot as a PNG file
plt.show()
