import pandas as pd
import numpy as np

demand_val_actual = pd.read_csv("./Processed Data/Demand_Val.csv", header=None)
solar_val_actual = pd.read_csv("./Processed Data/Solar_Val.csv", header=None)
price_val_actual = pd.read_csv("./Processed Data/Price_Val.csv", header=None)

bill = pd.DataFrame(np.random.rand(50,24))

def bill_maker(bid_price,bid_quantity):
	battery = np.float64(0.0)
	for i in range(50):
	    for j in range(24):
	        block_bill = np.float64(0.0)
	        if(bid_price.loc[i,j] > price_val_actual.loc[i,j]):
	            block_bill=block_bill + bid_price.loc[i,j]*bid_quantity.loc[i,j]
	            if(bid_quantity.loc[i,j] > demand_val_actual.loc[i,j] or bid_quantity.loc[i,j] + solar_val_actual.loc[i,j] > demand_val_actual.loc[i,j]):
	                if(battery<np.float64(25.0)):
	                    if(bid_quantity.loc[i,j] - demand_val_actual.loc[i,j] + solar_val_actual.loc[i,j] <= np.float64(5.0)):
	                        battery = battery + bid_quantity.loc[i,j] - demand_val_actual.loc[i,j] + solar_val_actual.loc[i,j]
	                    else:
	                        battery=battery + np.float64(5.0)
	                    if(battery > np.float64(25.0)):
	                        battery = np.float64(25.0)
	                else:
	                    battery = np.float64(25.0)
	            else:
	                if(battery <= np.float64(5.0)):
	                    if(demand_val_actual.loc[i,j] > bid_quantity.loc[i,j] + solar_val_actual.loc[i,j] + np.float64(0.8) * battery):
	                        block_bill = block_bill + (np.float64(7.0) * (demand_val_actual.loc[i,j] - bid_quantity.loc[i,j] - solar_val_actual.loc[i,j] - np.float64(0.8)*battery))
	                        battery = np.float64(0.0)
	                    else:
	                        battery = battery - (np.float64(1.25) * (demand_val_actual.loc[i,j] - bid_quantity.loc[i,j] - solar_val_actual.loc[i,j]))
	                else:
	                    if(demand_val_actual.loc[i,j] > bid_quantity.loc[i,j] + solar_val_actual.loc[i,j] + np.float64(4.0)):
	                        block_bill = block_bill + (np.float64(7.0) * (demand_val_actual.loc[i,j] - bid_quantity.loc[i,j] - solar_val_actual.loc[i,j] - np.float64(4.0)))
	                        battery = battery - np.float64(5.0)
	                    else:
	                        battery = battery - (np.float64(1.25) * (demand_val_actual.loc[i,j] - bid_quantity.loc[i,j] - solar_val_actual.loc[i,j]))
	        else:
	            if(solar_val_actual.loc[i,j] > demand_val_actual.loc[i,j]):
	                if(battery < np.float64(25.0)):
	                    if(solar_val_actual.loc[i,j] - demand_val_actual.loc[i,j] <= np.float64(5.0)):
	                        battery = battery + solar_val_actual.loc[i,j] - demand_val_actual.loc[i,j]
	                    else:
	                        battery = battery+np.float64(5.0)
	                    if(battery > np.float64(25.0)):
	                        battery = np.float64(25.0)
	                else:
	                    battery = np.float64(25.0)
	            else:
	                if(battery <= np.float64(5.0)):
	                    if(demand_val_actual.loc[i,j] > solar_val_actual.loc[i,j] + np.float64(0.8) * battery):
	                        block_bill = block_bill + (np.float64(7.0) * (demand_val_actual.loc[i,j] - solar_val_actual.loc[i,j] - np.float64(0.8) * battery))
	                        battery = np.float64(0.0)
	                    else:
	                        battery = battery - (np.float64(1.25) * (demand_val_actual.loc[i,j] - solar_val_actual.loc[i,j]))
	                else:
	                    if(demand_val_actual.loc[i,j] > solar_val_actual.loc[i,j] + np.float64(4.0)):
	                        block_bill = block_bill + (np.float64(7.0) * (demand_val_actual.loc[i,j] - solar_val_actual.loc[i,j] - np.float64(4.0)))
	                        battery = battery - np.float64(5.0)
	                    else:
	                        battery = battery - (np.float64(1.25) * (demand_val_actual.loc[i,j] - solar_val_actual.loc[i,j]))
	        bill.loc[i,j] = block_bill
	daily_bill = pd.DataFrame(bill.sum(axis=1), columns=['Daily Bill'])
	total_bill=daily_bill.sum()[0]
	return (daily_bill,total_bill)