# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]
#           AAPL     GOOG    TSLA      FB
market = [198.84, 1217.93, 267.66, 179.06]

pnl = 0
for i in range(len(portfolio)):
    volume = portfolio[i][0]
    strike = portfolio[i][1]
    spot = market[i]
    position_pnl = volume * (spot - strike)
    print(i, position_pnl)
    pnl = pnl + position_pnl

print(pnl)    # here the final results is that the portfolio is losing.
#Total = -174.50, so the portfolio is losing $174.50 right now.
# Apple and Google went up, but Tesla and Facebook dropped more.


# 1. Is a nested list a good approach? Why?

# It works for a small example, but it is not very clear.
# When I write portfolio[3][0], nothing tells me it is the volume of FB.
# I have to remember that index 3 is FB and index 0 is the volume.
# With a bigger portfolio it gets easy to make a mistake with the indexes,
# and Python will not warn me, it will just give a wrong number.

# 2. Is there a link between the order / number of elements in portfolio
#    and market? Is it realistic? What's the problem?

# Yes, the code only works if both lists have the same number of elements


# 3. How could we make it more reliable, using only lists?

# We could add the ticker inside each list, for example:
# portfolio = [["AAPL", 10, 154.12], ["FB", 18, 209.0]]
# market = [["AAPL", 198.84], ["FB", 179.06]]
# Then, for each stock, we look for the matching ticker in market instead of
# trusting the order. It is safer, but we need a loop inside the loop
# to find each price, so the code is longer and slower.

# 4. What type should we use to improve the code?

# A dictionary (dict).It links a key (the ticker) to a value:
# market = {"AAPL": 198.84, "FB": 179.06}
# market["FB"] gives 179.06 directly, so the order does not matter anymore
# and the code is much easier to read.



students = [ "george" ]
students.append("jose")
students.append("steven")
print(len(students))

print(",".join([ "paris", "london", "lisbon" ]))