import pandas as pd
import numpy as np

data = {
    "Name": ["A","B","C","D"],
    "Salary": [20000,30000,25000,28000],
    "Experience": [1,3,2,4]
}

df = pd.DataFrame(data)

print(df)
print("------")
print(df[df["Salary"] > 25000])
print("------")
df["Senior"] = df["Experience"].apply(lambda x: "Yes" if x >= 3 else "No")
print(df)
print("------")
df["Salary"]=df["Salary"]*1.2
print(df)