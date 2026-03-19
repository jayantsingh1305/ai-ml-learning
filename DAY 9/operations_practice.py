import pandas as pd
import numpy as np

data = {
    "Name" : ["A", "B", "C", "D", "E"],
    "Marks" : [20, 50, 30, 70, 60]
}

df = pd.DataFrame(data)
print(df)
print("------")
print(df[df["Marks"]>50])
print("------")
df["Marks"]=df["Marks"]*1.2
print(df)
print("------")
df["Pass"] = df["Marks"].apply(lambda x: "Yes" if x >50 else "No")
print(df)