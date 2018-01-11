# Optimal Bidding

This repository contains code for Optimal Bidding, an event based on stochastic dynamic optimisation held in the Inter IIT Tech Meet 2018. It includes both the approaches that we tried.

# Problem statement overview

In this problem, we had to minimise the electricity bill of a community in a day ahead market. We were given predictions of *energy demand*, *solar output* and *market price* for a period of time and we had to find the optimal *bid quantity* and *bid price*.

The community could meet its energy demands in four ways (in this order).

1. Buying electricity from market.  
    To buy electricity from the market, the community had to bid. The bid included the *bid quantity* and the *bid price*. Only if *bid price* was greater than the *market price*, the community would win the bid and get the desired electricity at the *bid price*. One important assumption given in the problem is that the communities' *bid prices* do not affect the *market price*. 

2. Solar plant.  
    Energy from the solar plant is obtained at no cost.

3. Battery  
    The battery supplies energy in case the community loses the bid or quantity of energy bid and energy from solar plant is less than the actual demand. The battery is charged in case the energy from market and the solar plant exceeds the demand. There is restriction given on how much battery can be charged or discharged in an hour.

4. DISCOM
    In case all other sources are unable to provide energy, community fulfills its energy demand from DISCOM at fixed rate of 7 money units per electricity unit.

For more details, refer to `Problem Statement.pdf`.

* In the training set we are given predictions along with the actual data of *energy demand*, *solar output* and *market price*, to find the optimal policy for calculating *bid quantity* and *bid price*.
* In public and private leaderboard dataset we are only given the predictions of *energy demand*, *solar output* and *market price*.

# Aproaches used

We tried two approaches to find *bid quantity* and *bid price*. The first one was based on time series analysis, while the second was based on optimisation through Stochastic Gradient Descent. We used the second approach to make the final submission.