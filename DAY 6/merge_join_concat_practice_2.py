import pandas as pd
import numpy as np

employees = pd.DataFrame({
    "emp_id": [101,102,103],
    "name": ["Rahul","Simran","Arjun"]
})

salaries = pd.DataFrame({
    "emp_id": [101,102,104],
    "salary": [50000,60000,70000],
})

#print(pd.merge(employees,salaries,on="emp_id",how="left"))
print(pd.merge(employees,salaries,on="emp_id",how="inner"))