import pandas as pd
dict={"Keys":["k1","k2","k1","k2"],
      "Names":["Bilal","Akash","Ali","Zohaib"],
      "Houses":["red","blue","green","red"],
      "Grades":["3rd","8th","9th","3rd"]}
df=pd.DataFrame(dict)
print(df)
print(df.pivot(index="Keys", columns="Names", values=["Houses","Grades"]))