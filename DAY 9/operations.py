import pandas as pd

data = {
    "Name" : ["A", "B", "C", "D"],
    "Age" : [22, 25, 21, 23],
    "Salary" : [20000, 30000, 25000, 28000],
}

df = pd.DataFrame(data)

print(df)
print("------")
print(df["Name"])
print("------")
print(df[["Name", "Salary"]])
print("------")
print(df[df["Salary"]>25000])
print("------")
df["Bonus"] = df["Salary"]*0.1
print(df)
print("------")
df["Salary"] = df["Salary"] + 5000
print(df)