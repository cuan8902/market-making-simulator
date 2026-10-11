import numpy as np
from price import simulate_mid
from simulate import run_simulation

skews = [0.0, 0.002, 0.005, 0.01, 0.02, 0.05]
for skew in skews:
    final_pnl = []
    max_invs = []
    for s in range(300):
        path = simulate_mid(100.0, 2.0, 0.01, 1000, 1000 + s)
        inv,cash, pnl = run_simulation(path, 0.05, 20, 10, 0.01, s, skew)
        final_pnl.append(pnl[-1])
        max_invs.append(np.max(np.abs(inv)))
    print(f"Skew: {skew}, Mean final PnL: {round(np.mean(final_pnl), 1)}, Std final PnL: {round(np.std(final_pnl), 1)}, Mean max inventory: {round(np.mean(max_invs), 1)}")
