import pandas as pd

# Load dataset
df = pd.read_excel("online_retail_II.xlsx")

# Remove missing values
df = df.dropna()

# Remove negative quantities
df = df[df['Quantity'] > 0]

# Remove negative prices
df = df[df['Price'] > 0]

# Create TotalPrice feature
df['TotalPrice'] = df['Quantity'] * df['Price']

# Save cleaned dataset
df.to_csv("cleaned_retail_data.csv", index=False)

print(df.head())
