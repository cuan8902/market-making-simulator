import numpy as np
from market_maker import make_quotes, check_fills
from price import simulate_mid

def run_simulation(mid_path, half_spread, A, k, dt, seed, skew=0.0):
    rng = np.random.default_rng(seed)
    cash = 0.0
    inventory = 0
    cash_history = []
    inventory_history = []
    pnl_history = []
    for t in range(len(mid_path)-1):
        mid = mid_path[t]
        bid, ask = make_quotes(mid, half_spread, inventory=inventory, skew=skew)
        bid_filled, ask_filled = check_fills(mid, bid, ask, rng, A, k, dt)
        if bid_filled:
            cash -= bid
            inventory += 1
        if ask_filled:
            cash += ask
            inventory -= 1

        pnl = cash + inventory * mid_path[t+1]    
        pnl_history.append(pnl)
        inventory_history.append(inventory)
        cash_history.append(cash)
    return np.array(inventory_history),np.array(cash_history), np.array(pnl_history)

if __name__ == "__main__":
    path = simulate_mid(100.0, 2.0, 0.01, 1000, 42)
    inv,cash, pnl = run_simulation(path, 0.05, 20, 10, 0.01, 7, 0.01)
    print(inv[-1], cash[-1], pnl[-1])
    print(pnl[-1], cash[-1] + inv[-1] * path[-1])
    print(make_quotes(100.0, 0.05, inventory=5, skew=0.1))