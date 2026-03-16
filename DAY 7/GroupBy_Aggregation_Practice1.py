import pandas as pd

data = pd.DataFrame({
    "Name" : ["A","B","C","D","E"],
    "Department" : ["IT","HR","IT","HR","IT"],
    "Salary" : [50000,40000,60000,45000,70000]
})

print(data.groupby("Department")["Salary"].sum())
print("------")
print(data.groupby("Department")["Salary"].max())
print("------")
print(data.groupby("Department")["Name"].count())