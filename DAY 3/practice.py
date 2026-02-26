# import pandas as pd
# import numpy as py

# df1 = pd.DataFrame({
#     "Name" : ["Jayant","Rahul"],
#     "Age" : [25,30]
# })

# df2 = pd.DataFrame({
#     "Name" : ["Jayant","Rakesh"],
#     "Marks" : [85,90]
# })

# print(df1)
# print(df2)

# #result = pd.merge(df1,df2,on="Name",how="inner")
# #result = pd.merge(df1,df2,on="Name",how="left")
# #result = pd.merge(df1,df2, on="Name",how="right")
# #result = pd.merge(df1,df2, on="Name", how="outer")
# #result = pd.concat([df1,df2])
# result = pd.concat([df1,df2],axis=1)
# print(result)

# import pandas as pd
# import numpy as py

# users = pd.DataFrame ({
#     "user_id" : [1,2],
#     "name" : ["Jayant","Rahul"]
# })

# orders = pd.DataFrame ({
#     "user_id" : [1,2],
#     "order_id" : [1532, 1246]
# })

# payments = pd.DataFrame ({
#     "order_id" : [1532,1246],
#     "amount" : [4000, 6000]
# })

# df1 = pd.merge(users, orders, on="user_id")
# df2 = pd.merge(orders, payments, on="order_id")
# result = pd.merge(df1,df2)
# print (df1)
# print (df2)

# import pandas as pd
# import numpy as np

# data = {
#     "Name" : ["A","B","C","D"],
#     "Age" : [22,np.nan,25,np.nan],
#     "Marks" : [80,90,np.nan,70]
# }

# df = pd.DataFrame(data)

# #print(df.isnull())
# df["Age"].fillna(df["Age"].mean(),inplace=True)
# df["Marks"].fillna(0, inplace=True)
# print(df)

import pandas as pd
import numpy as np

data = {
    "Age": [20,22,np.nan,25,np.nan,30],
    "Salary": [30000,32000,35000,np.nan,40000,42000],
    "Experience": [1,2,3,np.nan,np.nan,5]
}

df = pd.DataFrame(data)
df["Age"]=df["Age"].fillna(df["Age"].mean(),inplace=True)

print((df.isnull().sum()/len(df))*100)
