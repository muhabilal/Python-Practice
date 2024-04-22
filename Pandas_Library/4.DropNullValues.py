import pandas as pd
import numpy as np
data=pd.read_csv("company1.csv")
#print(data.isnull().sum())


#to drop null values
#print(data.dropna())

#to replace the NAN values
#print(data.replace(np.nan,"hi"))

#to replace just one column
#data["salary"]=data["salary"].replace(np.nan,30000)
#print(data)

#best approach to find nan mean for salary column
#print(data)
#print(data["salary"].mean())
#data["salary"]=data["salary"].replace(np.nan,24400)
#print(data)
#print(data["salary"].mean())


#if i want to fill values backward
#print(data.fillna(method="bfill"))

#if i want to fill uper values in the below
print(data.fillna(method="ffill"))
