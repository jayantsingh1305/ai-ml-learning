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

df1.set_index("id", inplace=True)
df2.set_index("id", inplace=True)

result = df1.join(df2)
print(result)