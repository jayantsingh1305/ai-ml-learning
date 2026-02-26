import pandas as pd

df1 = pd.DataFrame({
    "id" : [1,3],
    "name" : ["Jay","Raj"]
})

df2 = pd.DataFrame({
    "id" : [1,2],
    "order" : ["Shoes","Watch"]
})

#result = pd.merge(df1,df2,on="id")
#result = pd.merge(df1, df2, on="id", how="inner")
#result = pd.merge(df1, df2, on="id", how="left")
#result = pd.merge(df1,df2, on="id", how="right")
result = pd.merge(df1,df2,on="id",how="outer")
print(df1)
print(df2)
print(result)