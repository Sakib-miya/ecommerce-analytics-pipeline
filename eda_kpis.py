import pandas as pd
import matplotlib.pyplot as plt
import os

BASE = r"C:\Users\empir\OneDrive\Desktop\ram thapa"
DATA = os.path.join(BASE)
OUTPUT = os.path.join(BASE, "eda_output")
os.makedirs(OUTPUT, exist_ok=True)

df = pd.read_csv(os.path.join(DATA, "master_dataset.csv"))

# Top 10 customers by revenue
top_customers = df.groupby("full_name")["total_value"].sum().sort_values(ascending=False).head(10)
top_customers.to_csv(os.path.join(OUTPUT, "top_customers.csv"))

# Sales by product category
category_sales = df.groupby("category")["total_value"].sum().sort_values(ascending=False)
category_sales.to_csv(os.path.join(OUTPUT, "category_sales.csv"))

# Average order value
avg_order = df.groupby("order_id")["total_value"].sum().mean()
with open(os.path.join(OUTPUT, "average_order_value.txt"), "w") as f:
    f.write(f"Average Order Value: ${avg_order:.2f}")

# Monthly revenue trends
df["order_date"] = pd.to_datetime(df["order_date"])
monthly_sales = df.groupby(df["order_date"].dt.to_period("M"))["total_value"].sum()
monthly_sales.to_csv(os.path.join(OUTPUT, "monthly_sales.csv"))

# Plot top customers
plt.figure(figsize=(10,6))
top_customers.plot(kind="bar", color="skyblue")
plt.title("Top 10 Customers by Revenue")
plt.ylabel("Revenue USD")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT, "top_customers.png"))
plt.close()

# Plot sales by category
plt.figure(figsize=(10,6))
category_sales.plot(kind="bar", color="orange")
plt.title("Sales by Product Category")
plt.ylabel("Revenue USD")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT, "category_sales.png"))
plt.close()

# Plot monthly revenue trend
plt.figure(figsize=(12,6))
monthly_sales.plot(kind="line", color="green", marker="o")
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue USD")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT, "monthly_sales.png"))
plt.close()

print("EDA Completed. All CSVs and charts saved in 'eda_output' folder.")
