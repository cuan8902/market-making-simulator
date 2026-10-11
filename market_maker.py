import math 
import numpy as np

def make_quotes(mid, half_spread, tick = 0.01):
    bid = mid - half_spread
    ask = mid + half_spread
    bid = round(math.floor(bid/tick)*tick, 2)
    ask = round(math.ceil(ask/tick)*tick, 2)
    return bid, ask

def fill_probability(delta, A, k, dt):
    delta = max(delta,0)
    rate = A * math.exp(-k * delta)
    prob = 1 - math.exp(-rate * dt)
    return prob

def check_fills(mid, bid, ask, rng, A, k, dt):
    bid_delta = mid - bid
    ask_delta = ask - mid
    bid_fill_prob = fill_probability(bid_delta, A, k, dt)
    ask_fill_prob = fill_probability(ask_delta, A, k, dt)
    bid_filled = rng.random() < bid_fill_prob
    ask_filled = rng.random() < ask_fill_prob
    return bid_filled, ask_filled

if __name__ == "__main__":
    rng = np.random.default_rng(42)
    results = [check_fills(100.0, 99.8, 100.05, rng, 20, 10, 0.01) for _ in range(100000)]
    print(sum(r[0] for r in results) / len(results))
    print(sum(r[1] for r in results) / len(results))
