import pandas as pd
import numpy as np

data = {
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Mumbai"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Clothing", "Electronics"],
    "Sales": [20000, 15000, 30000, 10000, 12000, 25000]
}

df = pd.DataFrame(data)

print(df)
print("------")
print(pd.pivot_table(df, values="Sales", index="City", aggfunc="sum"))
print("------")
print(pd.pivot_table(df, values="Sales", index="City", columns="Category", aggfunc="sum"))
print("------")
print(pd.pivot_table(df, values="Sales", index="Category", columns="City", aggfunc="sum"))