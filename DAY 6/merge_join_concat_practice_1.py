import pandas as pd
import numpy as py

customers = pd.DataFrame({
    "customer_id" : [1,2,3],
    "name" : ["Aman","Riya","Kabir"]
})

orders = pd.DataFrame({
    "customer_id" : [1,2],
    "order_amount" : [500,800]
})

#print(pd.merge(customers,orders,on='customer_id',how='inner'))
#print(pd.merge(customers,orders,on='customer_id',how='left'))
print(pd.concat([customers,orders]))