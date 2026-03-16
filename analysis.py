import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Load dataset
data = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

# Clean data
data["Order Date"] = pd.to_datetime(data["Order Date"], errors="coerce")
data = data.dropna(subset=["Order Date"])
data = data[data["Sales"] != 0].copy()

print("Dataset shape:", data.shape)

# ---------------------------
# Sales by Category
# ---------------------------
sales_by_category = data.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=sales_by_category.index, y=sales_by_category.values)
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.close()

# ---------------------------
# Profit by Category
# ---------------------------
profit_by_category = data.groupby("Category")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=profit_by_category.index, y=profit_by_category.values)
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.close()

# ---------------------------
# Monthly Sales Trend
# ---------------------------
data["Month"] = data["Order Date"].dt.to_period("M").astype(str)
monthly_sales = data.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

# ---------------------------
# Sales by Region
# ---------------------------
region_sales = data.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.close()

# ---------------------------
# Profit Margin by Category
# ---------------------------
data["Profit Margin"] = data["Profit"] / data["Sales"]
margin_by_category = data.groupby("Category")["Profit Margin"].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=margin_by_category.index, y=margin_by_category.values)
plt.title("Average Profit Margin by Category")
plt.xlabel("Category")
plt.ylabel("Profit Margin")
plt.tight_layout()
plt.savefig("profit_margin_by_category.png")
plt.close()

# ---------------------------
# Top 10 Products by Sales
# ---------------------------
top_products = (
    data.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Sales:")
print(top_products)

# ---------------------------
# Executive Insights
# ---------------------------
top_category = sales_by_category.idxmax()
top_profit_category = profit_by_category.idxmax()
top_region = region_sales.idxmax()
top_margin_category = margin_by_category.idxmax()

print("\n===== KEY BUSINESS INSIGHTS =====")
print(f"1. Highest sales category: {top_category}")
print(f"2. Most profitable category: {top_profit_category}")
print(f"3. Top-performing region: {top_region}")
print(f"4. Highest average profit margin category: {top_margin_category}")
print("5. Monthly sales trends can support seasonal planning and inventory decisions.")
print("6. Top-performing products can be prioritised for promotions and stock optimisation.")

print("\nAll charts saved successfully.")