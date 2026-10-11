import numpy as np
from price import simulate_mid

finals = [simulate_mid(100.0, 2.0, 0.01, 1000, s)[-1] for s in range(5000)]
print(np.std(finals))