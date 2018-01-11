# Approach 1

In this approach, we obtain better predictions of the actual `demand`, `solar output` and `price` than the oracle. Afterwards, we bid at value greater than the predicted market price so as to win the bid,keeping the bill low.

# Files

`Prediction.ipynb` contains code for making prediction of the actual `demand`, `solar output` and `price`.
`Bidding.ipynb` contains code for determing optimal `bid quantity` and `bid price`.