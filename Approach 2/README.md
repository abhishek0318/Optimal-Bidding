# Aproach 2

In this approach, we make a model which decides the `bid quantity` and `bid price` given the oracle's prediction for `energy demand`, `solar output` and `market price`. This model simply multiplies oracle's predicted demand and oracle's predicted market price by a value, which is different for each hour.

The model is made in this way because we observed that the standard deviation of error in oracle's prediction is directly proportional to the mean of actual values (See `Presentation.pdf` for more).

We find these parameters by simply minimising the bill by using stochastic gradient descent.