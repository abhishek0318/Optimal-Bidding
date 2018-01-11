# Splits the training data into training and validation data

import pandas as pd

pd.read_csv('./Data/Demand_Train.csv', header=None)[:-50].to_csv('./Processed Data/Demand_Train.csv', index=False, header=False)
pd.read_csv('./Data/Demand_Train.csv', header=None)[-50:].to_csv('./Processed Data/Demand_Val.csv', index=False, header=False)

pd.read_csv('./Data/Demand_Train_pred.csv', header=None)[:-50].to_csv('./Processed Data/Demand_Train_pred.csv', index=False, header=False)
pd.read_csv('./Data/Demand_Train_pred.csv', header=None)[-50:].to_csv('./Processed Data/Demand_Val_pred.csv', index=False, header=False)

pd.read_csv('./Data/Price_Train.csv', header=None)[:-50].to_csv('./Processed Data/Price_Train.csv', index=False, header=False)
pd.read_csv('./Data/Price_Train.csv', header=None)[-50:].to_csv('./Processed Data/Price_Val.csv', index=False, header=False)

pd.read_csv('./Data/Price_Train_pred.csv', header=None)[:-50].to_csv('./Processed Data/Price_Train_pred.csv', index=False, header=False)
pd.read_csv('./Data/Price_Train_pred.csv', header=None)[-50:].to_csv('./Processed Data/Price_Val_pred.csv', index=False, header=False)

pd.read_csv('./Data/Solar_Train.csv', header=None)[:-50].to_csv('./Processed Data/Solar_Train.csv', index=False, header=False)
pd.read_csv('./Data/Solar_Train.csv', header=None)[-50:].to_csv('./Processed Data/Solar_Val.csv', index=False, header=False)

pd.read_csv('./Data/Solar_Train_pred.csv', header=None)[:-50].to_csv('./Processed Data/Solar_Train_pred.csv', index=False, header=False)
pd.read_csv('./Data/Solar_Train_pred.csv', header=None)[-50:].to_csv('./Processed Data/Solar_Val_pred.csv', index=False, header=False)
