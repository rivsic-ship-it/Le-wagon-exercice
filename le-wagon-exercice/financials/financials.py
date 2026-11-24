# pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function

# TODO: 2nd exercise: Define the `short_pnl` function
import math

def forward_price (spot, interest_rate, temps):
    calcul = spot * math.exp(interest_rate * temps)
    return (calcul)    
print(forward_price(10.5, 0.02, 3))