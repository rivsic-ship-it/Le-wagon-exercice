# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

# Keys: ticker of each stock (str)
# Values: a dict with the volume (int) and the strike price (float)
portfolio = {
    "AAPL": {"volume": 10, "strike": 154.12},
    "GOOG": {"volume": 2,  "strike": 812.56},
    "TSLA": {"volume": 12, "strike": 342.12},
    "FB":   {"volume": 18, "strike": 209.0},     # # Compared to the list version, portfolio[3][0] becomes portfolio["FB"]["volume"].
# Now I can understand what I'm reading right away, without remembering. 
}

print(portfolio['TSLA']['volume'])
print(portfolio['GOOG']['strike'])

# Keys: ticker of each stock (str)
# Values: current spot price (float)
market = {
    "AAPL": 198.84,
    "GOOG": 1217.93,
    "TSLA": 267.66,
    "FB":   179.06,
}

#Now lets compute the PNL 
pnl = 0

# .items() gives each key and its value at the same time
# ticker = "AAPL", position = {"volume": 10, "strike": 154.12}, etc.
for ticker, position in portfolio.items():
    spot = market[ticker]  # we find the price by its ticker, not by its position
    position_pnl = position["volume"] * (spot - position["strike"])
    print(ticker, round(position_pnl, 2))  # debug: P&L of each stock
    pnl = pnl + position_pnl

print("Total P&L:", round(pnl, 2)) # This is way clearer that the list imputs.
#It's more explicit with position["volume"] and market[ticker] tell me exactly what I'm using, instead of portfolio[i][0] and market[i].


