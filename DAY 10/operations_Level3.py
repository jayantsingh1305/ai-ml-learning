import pandas as pd
import numpy as np

data = {
    "Customer": ["C1","C2","C3","C4","C5"],
    "Age": [25, 40, 35, 28, 50],
    "Income": [20000, 50000, 30000, 25000, 60000]
}

df = pd.DataFrame(data)

print(df)
print("------")
print(df[(df["Age"]>30)&(df["Income"]>30000)])
print("------")
df["Category"] = df["Income"].apply(lambda x: "High" if x >= 40000 else "Medium")
print(df)
print("------")