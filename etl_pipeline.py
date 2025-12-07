import pandas as pd
import os

# Base folders
BASE = r"C:\Users\empir\OneDrive\Desktop\ram thapa"
DATA = os.path.join(BASE, "data")
CLEAN = os.path.join(BASE, "clean_data")

# Create clean_data folder if missing
os.makedirs(CLEAN, exist_ok=True)

# Load CSV files
customers = pd.read_csv(os.path.join(DATA, "customers.csv"))
orders = pd.read_csv(os.path.join(DATA, "orders.csv"))
products = pd.read_csv(os.path.join(DATA, "products.csv"))
sessions = pd.read_csv(os.path.join(DATA, "sessions.csv"))
ads = pd.read_csv(os.path.join(DATA, "ad_spend_monthly.csv"))

print("All CSV Files Loaded Successfully!")

# ---------------------------
# CLEANING
# ---------------------------

customers.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
sessions.drop_duplicates(inplace=True)
ads.drop_duplicates(inplace=True)

print("Cleaning Done!")

# Save cleaned files
customers.to_csv(os.path.join(CLEAN, "customers_clean.csv"), index=False)
orders.to_csv(os.path.join(CLEAN, "orders_clean.csv"), index=False)
products.to_csv(os.path.join(CLEAN, "products_clean.csv"), index=False)
sessions.to_csv(os.path.join(CLEAN, "sessions_clean.csv"), index=False)
ads.to_csv(os.path.join(CLEAN, "ad_spend_monthly_clean.csv"), index=False)

print("Cleaned files saved in clean_data folder!")

# ---------------------------
# CREATE MASTER DATASET
# ---------------------------

# Merge orders + customers
master = orders.merge(customers, on="customer_id", how="left")

# Merge orders + products
master = master.merge(products, on="product_id", how="left")

# Save master dataset
master_file = os.path.join(BASE, "master_dataset.csv")
master.to_csv(master_file, index=False)

print("Master Dataset Created:", master_file)
