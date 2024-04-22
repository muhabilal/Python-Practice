import pandas as pd

data={
    "Name":["Bilal","Zohaib","Ali"],
    "Age":[25,28,30],
    "Salary":[45000,55000,58000]
}
df=pd.DataFrame(data)
print(df)