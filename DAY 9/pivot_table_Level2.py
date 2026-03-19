import pandas as pd
import numpy as np

data = {
    "Department": ["IT","HR","IT","HR","IT","HR"],
    "Salary": [50000, 40000, 60000, 45000, 70000, 42000],
    "Experience": [2, 5, 3, 4, 6, 2]
}

df = pd.DataFrame(data)

print(df)
print("------")
print(pd.pivot_table(df, values="Salary", index="Department", aggfunc= "mean"))
print("------")
print(pd.pivot_table(df, values="Salary", index="Department", columns="Experience", aggfunc= "sum"))