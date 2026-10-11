import numpy as np
from price import simulate_mid
from market_maker import make_quotes, fill_probability

import numpy as np
from market_maker import make_quotes, fill_probability
from price import simulate_mid


def test_quotes_straddle_mid():
    bid, ask = make_quotes(100.0, 0.05)
    assert bid < 100.0 < ask


def test_skew_lowers_both_quotes_when_long():
    bid0, ask0 = make_quotes(100.0, 0.05, inventory=0, skew=0.1)
    bid1, ask1 = make_quotes(100.0, 0.05, inventory=5, skew=0.1)
    assert bid1 < bid0
    assert ask1 < ask0


def test_fill_probability_falls_with_distance():
    near = fill_probability(0.05, 20, 10, 0.01)
    far = fill_probability(0.5, 20, 10, 0.01)
    assert far < near


def test_same_seed_gives_same_path():
    a = simulate_mid(100.0, 2.0, 0.01, 100, 5)
    b = simulate_mid(100.0, 2.0, 0.01, 100, 5)
    assert np.array_equal(a, b)