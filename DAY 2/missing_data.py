# import pandas as pd
# import numpy as np

# data = {
#     "Name": ["A","B","C"],
#     "Age": [25,np.nan,30],
#     "Salary":[50000,60000,np.nan]
# }

# df = pd.DataFrame(data)
# print(df)
# #print(df.isnull())
# #print(df.isnull().sum())
# #df.dropna(inplace=True)
# #df.dropna(axis=1,inplace=True)
# #df.dropna(how='all',inplace=True)
# #df.fillna(0, inplace=True)
# #df["Age"].fillna(df["Age"].mean(),inplace=True)
# df.ffill(inplace=True)
# print(df)

# import pandas as pd
# import numpy as np

# data = {
#     "Name" : ["A", "B", "C"],
#     "Age" : [20, np.nan, 22],
#     "Marks" : [80, 90, np.nan]
# }

# df = pd.DataFrame(data)
# print(df)

# #print(df.dropna())
# #df["Age"].fillna(df["Age"].mean(), inplace=True)
# print(df)

import pandas as pd
import numpy as np

data = {
    "Name" : ["John","Anna","Peter","Linda"],
    "Age" : [28,np.nan,35,np.nan],
    "Salary" : [50000,60000,np.nan,80000]
}

df = pd.DataFrame(data)
print(df)