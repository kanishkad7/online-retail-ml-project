import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_retail_data.csv")

# Top countries by revenue
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
country_sales.plot(kind='bar')
plt.title("Top Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../Figures/country_revenue.png")
plt.show()
