#default show me 5 values from top and 5 values from end
import pandas as pd
data=pd.read_excel("/media/bilal/5F943841302CBE71/Python-Practice/Pandas_Library/ESD.xlsx")
#print(data)

#to check if we want to see the top and end 10 values
#print(data.head(10))
#print(data.tail(10))

#to see the data-type
#print(data.info())


#to see the int and float value in the given excel file
#print(data.describe())

#to see the null values in the excel file
#print(data.isnull())

#to see the null values in the sum form
print(data.isnull().sum())
