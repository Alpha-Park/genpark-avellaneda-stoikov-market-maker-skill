import math

class AvellanedaStoikovMM:
    """
    Avellaneda-Stoikov Optimal Market Making Model.
    Reservation price: r(s, q) = s - q * gamma * sigma^2 * (T - t).
    Optimal spread: delta_a + delta_b = gamma * sigma^2 * (T - t) + (2 / gamma) * ln(1 + gamma / k).
    """
    def __init__(self, gamma=0.1, sigma=1.5, k=1.5):
        self.gamma = gamma
        self.sigma = sigma
        self.k = k

    def get_quotes(self, mid_price, inventory_q, time_remaining=1.0):
        r = mid_price - inventory_q * self.gamma * (self.sigma**2) * time_remaining
        half_spread = 0.5 * (self.gamma * (self.sigma**2) * time_remaining + (2.0 / self.gamma) * math.log(1.0 + self.gamma / self.k))
        bid_price = round(r - half_spread, 2)
        ask_price = round(r + half_spread, 2)
        return bid_price, ask_price, round(r, 2)
