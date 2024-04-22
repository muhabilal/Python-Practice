import pandas as pd
df=pd.read_excel("/media/bilal/5F943841302CBE71/Python-Practice/Pandas_Library/ESD.xlsx")
#print(df)
df.loc[(df["Bonus %"]==0),"GetsBonus"]="no-bonus"
df.loc[(df["Bonus %"]>0,"GetsBonus" )]="bonus"
print(df.head(10))