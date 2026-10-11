from simulate import run_simulation
from price import simulate_mid 

if __name__ == "__main__":
    path = simulate_mid(100.0, 2.0, 0.01, 1000, 42)
    inv,cash, pnl = run_simulation(path, 0.05, 20, 10, 0.01, 7)
    print(inv[-1], cash[-1], pnl[-1])
    print(pnl[-1], cash[-1] + inv[-1] * path[-1])