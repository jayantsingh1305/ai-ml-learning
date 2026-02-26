import pandas as pd
import numpy as py

df1 = pd.DataFrame({
    "id" : [1,2],
    "name" : ["Jay","Raj"]
})

df2 = pd.DataFrame({
    "id" : [1,2],
    "order" : ["Shoes","Watch"]
})

print(df1)
print(df2)

#result = pd.concat([df1, df2])
result = pd.concat([df1, df2], axis=1)
print(result)