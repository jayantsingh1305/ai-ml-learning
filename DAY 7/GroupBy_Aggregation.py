import pandas as pd

data = {
    "Name" : ["A","B","C","D","E"],
    "Department" : ["IT","HR","IT","HR","IT"],
    "Salary": [50000,40000,60000,45000,55000]
}

df = pd.DataFrame(data)
print(df)
print("------")
print(df.groupby("Department"))
print("------")
print(df.groupby("Department")["Salary"].mean())