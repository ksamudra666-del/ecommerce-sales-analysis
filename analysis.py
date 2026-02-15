import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/ecommerce_sales.csv")

# Create Total Sales column
df["Total"] = df["Price"] * df["Quantity"]

print("\nDataset Preview:")
print(df.head())

# ==============================
# 📊 Total Revenue
# ==============================
total_revenue = df["Total"].sum()
print("\nTotal Revenue:", total_revenue)

# ==============================
# 📊 Sales by Category
# ==============================
category_sales = df.groupby("Category")["Total"].sum()
print("\nSales by Category:")
print(category_sales)

# ==============================
# 📊 Sales by City
# ==============================
city_sales = df.groupby("City")["Total"].sum()
print("\nSales by City:")
print(city_sales)

# ==============================
# 📈 Visualization
# ==============================
category_sales.plot(kind="bar")
plt.title("E-commerce Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

city_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("City-wise Sales Distribution")
plt.show()
