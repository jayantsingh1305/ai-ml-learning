import pandas as pd

data = {
    "OrderID" : [1,2,3,4,5,6,7],
    "Category" : ["Electronics","Clothing","Electronics","Clothing","Electronics","Clothing","Electronics"],
    "Price" : [1000,500,1200,700,900,650,1100]
}

df = pd.DataFrame(data)

print(df)
print("------")
print(df.groupby("Category")["Price"].sum())
print("------")
print(df.groupby("Category")["Price"].mean())
print("------")
print(df.groupby("Category")["Price"].max())