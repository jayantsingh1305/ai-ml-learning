import pandas as pd

data = {
    "Name" : ["Jayant","Rahul","Amit","Neha","Priya"],
    "Age" : [25,30,22,28,30],
    "City" : ["Delhi","Mumbai","Bangalore","Chennai","Mumbai"],
    "Marks" : [85,90,78,92,88], 
    "Passed" : [True,True,False,True,True]
}

df = pd.DataFrame(data)
#print(df)
#print(df["Name"])
#print(df[["Name","City"]])
#print(df.Age)
#print(df.loc[2])
#print(df.iloc[3])
#print(df.loc[[1,3]])
#print(df.loc[[0,2],["Name","City"]])
#print(df.iloc[[0,2],[0,2]])
#print(df[df["Marks"]>85])
#print(df[df["City"]=="Delhi"])
#print(df[(df["Age"]>21) & (df["Marks"]>80)])
#print(df.drop("Passed",axis=1,inplace=True))
#df["Country"]="India"
df["Bonus"]=df["Marks"]+5
print(df)