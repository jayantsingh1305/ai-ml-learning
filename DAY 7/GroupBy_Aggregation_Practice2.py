import pandas as pd

dataset = pd.DataFrame({
    "Customer" : ["A","B","C","D","E"],
    "City" : ["Delhi","Mumbai","Delhi","Mumbai","Delhi"],
    "Purchase" : [200,300,150,400,250]
})

print(dataset.groupby("City")["Purchase"].mean())