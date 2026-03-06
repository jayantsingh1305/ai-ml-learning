import pandas as pd
import numpy as py

users = pd.DataFrame({
    "user_id" : [1,2,3,4],
    "name" : ["Raman","Rahul","Pavan","Sahil"]
})

orders = pd.DataFrame({
    "order_id" : [123,456,789],
    "user_id" : [2,3,6],
    "product" : ["shoes","socks","bottom"]
})

payments = pd.DataFrame({
    "order_id" : [123,456,789],
    "amount" : [2000,600,1600]
})

final_table_1 = pd.merge(users,orders,on="user_id",how="inner")
final_table_2 = pd.merge(payments,final_table_1,on="order_id",how="inner")
print(final_table_2)