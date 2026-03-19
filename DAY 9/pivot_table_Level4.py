import pandas as pd
import numpy as np

data = {
    "Department":["IT","IT","HR","HR","IT","HR","FINANCE","FINANCE"],
    "Gender":["M","F","M","F","M","F","M","F"],
    "Salary":[60000,65000,40000,42000,70000,45000,50000,52000],
    "Experience":[3,5,2,4,6,3,4,5]
}

df = pd.DataFrame(data)
print(df)
print("------")
print(pd.pivot_table(df, values="Salary", index="Department", aggfunc="mean"))
print("------")
print(pd.pivot_table(df, values="Salary", index="Department", columns = "Gender", aggfunc="mean"))
print("------")
print(df.groupby("Experience")["Salary"].mean())