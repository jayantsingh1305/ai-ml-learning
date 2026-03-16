import pandas as pd

data = {
    "Employee" : ["A","B","C","D","E","F"],
    "Department" : ["IT","HR","IT","HR","SALES","SALES"],
    "Salary" : [50000,40000,60000,45000,55000,52000]
}

df = pd.DataFrame(data)

print(df)
print("------")
print(df.groupby("Department")["Salary"].mean())
print("------")
print(df.groupby("Department")["Salary"].sum())
print("------")
print(df.groupby("Department")["Salary"].max())