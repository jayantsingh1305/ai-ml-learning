import pandas as pd

data = {
    "Applicant": ["A1", "A2", "A3", "A4", "A5"],
    "Income": [2000, 40000, 30000, 50000, 25000],
    "CreditScore": [600, 750, 650, 800, 620],
    "Age": [22, 35, 28, 45, 30],
}

df = pd.DataFrame(data)

risk = (df["Income"]<30000) & (df["CreditScore"]<650)

df["Loan_Status"] = "Approve"
df.loc[risk, "Loan_Status"] = "Reject"

final_df = df[["Applicant", "Loan_Status"]]

print(final_df)