import pandas as pd
data={"Months":["January","Feburary","March","April"]}
a=pd.DataFrame(data)
print(a)

def extract(value):
    return value[0:3]

a["short_months"]=a["Months"].map(extract)
print(a)