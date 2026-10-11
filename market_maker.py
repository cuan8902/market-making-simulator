import math 

def make_quotes(mid, half_spread, tick = 0.01):
    bid = mid - half_spread
    ask = mid + half_spread
    bid = round(math.floor(bid/tick)*tick, 2)
    ask = round(math.ceil(ask/tick)*tick, 2)
    return bid, ask

def fill_probability(delta, A, k, dt):
    rate = A * math.exp(-k * delta)
    prob = 1 - math.exp(-rate * dt)
    return prob

if __name__ == "__main__":
    print(fill_probability(0.05, 20, 10, 0.01))
    print(fill_probability(0.2, 20, 10, 0.01))
  

