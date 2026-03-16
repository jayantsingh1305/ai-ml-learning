import pandas as pd

data = {
    "Customer" : ["A","B","C","D","E","F"],
    "City": ["Delhi","Mumbai","Delhi","Mumbai","Delhi","Mumbai"],
    "Purchase": [200,300,150,400,250,350]
}

df = pd.DataFrame(data)

print(df)
print("------")
print(df.groupby("City")["Purchase"].sum())
print("------")
print(df.groupby("City")["Purchase"].mean())
print("------")
print(df.groupby("City")["Customer"].count())