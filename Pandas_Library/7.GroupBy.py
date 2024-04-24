import pandas as pd
data=pd.read_excel("/media/bilal/5F943841302CBE71/Python-Practice/Pandas_Library/ESD.xlsx")
print(data)

#count the number of gender in the dept.
gp=data.groupby("Department").agg({"Gender":"count"})
print(gp)

#count the number of male and females in the dept
gp1=data.groupby(["Department","Gender"]).agg({"Gender":"count"})
print(gp1)


gp2=data.groupby("Country").agg({"Age":"mean"})
print(gp2)

#find annula salary
gp3=data.groupby("Country").agg({"Annual Salary":"mean"})
print(gp3)
#find max annula salary
gp3=data.groupby(["Country","Gender"]).agg({"Annual Salary":"max","Age":"min"})
print(gp3)