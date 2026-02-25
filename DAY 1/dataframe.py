import pandas as pd

#Example 1 with dictionary
# data = {
#     "Name" : ["Jayant","Rahul"],
#     "Age" : [25,30]
# }

#df = pd.DataFrame(data)
#print(df)

#Example 2 with list of list
# data = [
#     ["Jayant",22],
#     ["Rahul",30]
# ]

# df = pd.DataFrame(data,columns=["Name","Age"])
# print(df)

#Example 3 with csv file
# df = pd.read_csv("data.csv")
# print(df)

#Example 4 with empty dataframe
# df = pd.DataFrame()
# print(df)

data = {
    "Name" : ["Jayant","Rahul","Amit","Neha","Rahul"],
    "Age" : [25,30,22,28,30],
    "City" : ["Delhi","Mumbai","Bangalore","Chennai","Mumbai"],
    "Marks" : [85,90,78,92,88],
    "Passed" : [True,True,False,True,True]
}

df = pd.DataFrame(data)

# print(df[["Name","City"]])
# print(df.Age)

#print(df)

df["Salary"] = [50000,60000,45000,70000,65000]
df["Age_plus_10"] = df["Age"] + 10
df["Country"] = "India"
df.drop("Age_plus_10",axis=1,inplace=True)
df.drop("Country",axis=1,inplace=True)
del df["Salary"]
# print(df.loc[[0,2],["Name","Marks"]])
# print(df.iloc[[0,2],[0,3]])
#print(df.loc[[1,3],["Name","City"]])
# print(df.iloc[[1,3],[0,2]])
# print(df[df["Age"]>22])
# print(df[df["Marks"]>=85])
# print(df[(df["Age"]>21) & (df["Marks"]>80)])
print(df[(df["City"]=="Delhi") | (df["Marks"]>90)])