import pandas as pd

df = pd.read_csv("../data/Superstore.csv", encoding='latin1')  # <--- added

print("Before cleaning:")
print(df.info())

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

df = df.dropna(subset=['Order Date'])

df.to_csv("../data/superstore_clean.csv", index=False, encoding='utf-8')

print("After cleaning saved to superstore_clean.csv")
