import pandas as pd
data = pd.read_csv("company1.csv")
#print(data)

#find null values
#print(data.isnull().sum())

#to find the duplicate values in the file
#print(data["EEID"].duplicated())

#to find the duplicate values in the file and count it
#print(data["EEID"].duplicated().sum())

#to remove the duplicates when we run the below code duplication is not removed bcz i not provided the column name
print(data.drop_duplicates("EEID"))