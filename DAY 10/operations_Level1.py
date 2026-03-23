import pandas as pd
import numpy as np

data = {
    "Name" : ["A","B","C","D"],
    "Age" : [22,25,21,23],
    "Marks" : [45,60,30,80] 
}

df = pd.DataFrame(data)

print(df)
print("------")
print(df["Name"])
print("------")
print(df[["Name","Marks"]])
print("------")
print(df[df["Marks"]>50])