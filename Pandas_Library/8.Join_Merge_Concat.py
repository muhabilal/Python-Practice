import pandas as pd
data1={"Emp Id":["E01","E02","E03","E04","E05","E06"],
       "Names":["Bilal","Ariz","Zeshan","Yasir","Zohaib","Ali"],
       "Age":[25,30,38,41,42,50],
       
       }
data2={"Emp Id":["E01","E02","E03","E04","E05","E06"],
       "Salary":[45000,52000,60000,56000,30000,20000],
       
       }
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

print(df1)
print()
print(df2)
print(pd.merge(df1,df2,on="Emp Id"))



data3={"Emp Id":["E01","E02","E03","E04","E05","E06"],
       "Names":["Bilal","Ariz","Zeshan","Yasir","Zohaib","Ali"],
       "Age":[25,30,38,41,42,50],
       
       }
data4={"Emp Id":["E01","E07","E03","E04","E08","E06"],
       "Salary":[45000,52000,60000,56000,30000,20000],
       
       }
df3=pd.DataFrame(data3)
df4=pd.DataFrame(data4)


print(pd.merge(left=df3,right=df4,on="Emp Id",how="left"))
print(pd.merge(left=df3,right=df4,on="Emp Id",how="right"))



data5={"Emp Id":["E01","E02","E03","E04","E05","E06"],
       "Names":["Bilal","Ariz","Zeshan","Yasir","Zohaib","Ali"],
       "Age":[25,30,38,41,42,50],
       
       }
data6={"Emp Id":["E71","E08","E09","E010","E011","E012"],
       "Names":["Hassan","Wajid","Imran","Akash","Usman","Ahmed"],
       "Age":[25,30,38,41,42,50],
       
       }
df5=pd.DataFrame(data5)
df6=pd.DataFrame(data6)
print(pd.concat([df5,df6]))