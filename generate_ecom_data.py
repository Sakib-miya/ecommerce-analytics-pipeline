"""
generate_ecom_data.py
Produces realistic eCommerce datasets for the 10000/10 portfolio project.

Outputs (data/):
 - customers.csv        (100_000 rows)
 - products.csv         (2_000 rows)
 - orders.csv           (300_000 rows)
 - sessions.csv         (400_000 rows)
 - ad_spend_monthly.csv (monthly ad spend by channel)
"""

import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# ---------- CONFIG ----------
OUT_DIR = "data"
os.makedirs(OUT_DIR, exist_ok=True)

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

N_CUSTOMERS = 100_000
N_PRODUCTS = 2_000
N_ORDERS = 300_000
N_SESSIONS = 400_000

START_DATE = pd.Timestamp("2019-01-01")
END_DATE = pd.Timestamp("2025-12-31")
DAYS = (END_DATE - START_DATE).days + 1

# ---------- HELPER FUNCS ----------
def random_dates(n, start=START_DATE, days=DAYS):
    offsets = np.random.randint(0, days, size=n)
    times = [start + pd.Timedelta(int(o), unit="D") + pd.Timedelta(np.random.randint(0, 86400), unit="s") for o in offsets]
    return pd.to_datetime(times)

# ---------- 1) CUSTOMERS ----------
first_names = ["Alex","Sam","Taylor","Jordan","Casey","Riley","Morgan","Jamie","Avery","Cameron","Chris","Pat"]
last_names = ["Lee","Kim","Patel","Garcia","Smith","Wang","Brown","Nguyen","Lopez","Martinez","Khan","Singh"]
countries = ["USA","UK","Canada","Australia","Germany","India","France","Spain","Brazil","Japan"]
channels = ["Organic","Paid Search","Social","Referral","Email","Affiliate"]

cust_ids = np.arange(1, N_CUSTOMERS+1)
customers = pd.DataFrame({
    "customer_id": cust_ids,
    "full_name": [f"{np.random.choice(first_names)} {np.random.choice(last_names)}" for _ in range(N_CUSTOMERS)],
    "email": [f"user{cid}@example.com" for cid in cust_ids],
    "age": np.random.randint(18, 75, N_CUSTOMERS),
    "country": np.random.choice(countries, N_CUSTOMERS, p=[0.35,0.15,0.1,0.08,0.07,0.08,0.05,0.05,0.04,0.03]),
    "signup_date": random_dates(N_CUSTOMERS, start=pd.Timestamp("2016-01-01"), days=365*6).date,
    "acquisition_channel": np.random.choice(channels, N_CUSTOMERS, p=[0.25,0.2,0.2,0.15,0.15,0.05]),
    "is_loyalty_member": np.random.choice([0,1], N_CUSTOMERS, p=[0.8,0.2])
})
customers["signup_date"] = pd.to_datetime(customers["signup_date"])

# ---------- 2) PRODUCTS ----------
categories = ["Electronics","Apparel","Home","Beauty","Sports","Toys","Outdoors","Books"]
subcat_map = {
    "Electronics":["Phones","Computers","Audio","Accessories"],
    "Apparel":["Men","Women","Kids"],
    "Home":["Kitchen","Furniture","Decor"],
    "Beauty":["Skin","Makeup","Hair"],
    "Sports":["Fitness","Outdoor","TeamSport"],
    "Toys":["Indoor","Outdoor","Educational"],
    "Outdoors":["Camping","Gardening","Boating"],
    "Books":["Fiction","Nonfiction","Education"]
}

prod_ids = np.arange(1, N_PRODUCTS+1)
prod_category = np.random.choice(categories, N_PRODUCTS, p=[0.18,0.15,0.14,0.12,0.12,0.1,0.1,0.09])
prod_subcat = [np.random.choice(subcat_map[c]) for c in prod_category]
base_price = np.round(np.random.lognormal(mean=3.5, sigma=0.9, size=N_PRODUCTS),2)  # wide price distribution
cost = np.round(base_price * np.random.uniform(0.4, 0.8, N_PRODUCTS),2)
rating = np.round(np.random.uniform(2.5,5.0, N_PRODUCTS),2)
stock = np.random.randint(0, 2000, N_PRODUCTS)

products = pd.DataFrame({
    "product_id": prod_ids,
    "product_name": [f"P-{pid:05d}" for pid in prod_ids],
    "category": prod_category,
    "subcategory": prod_subcat,
    "price": base_price,
    "cost": cost,
    "margin": np.round((base_price - cost) / base_price, 3),
    "rating": rating,
    "stock": stock
})

# ---------- 3) ORDERS ----------
# Simulate order dates skewed to recent years
order_dates = random_dates(N_ORDERS)
# Assign customers and products
order_customer = np.random.choice(customers["customer_id"], size=N_ORDERS)
order_product = np.random.choice(products["product_id"], size=N_ORDERS, p=None)
# quantity skewed to small ints
quantity = np.random.choice([1,1,1,2,2,3,4], size=N_ORDERS, p=[0.45,0.2,0.15,0.1,0.06,0.03,0.01])
# map product price at order time and compute totals
prod_price_map = products.set_index("product_id")["price"].to_dict()
prices = np.array([prod_price_map[p] for p in order_product]) * np.random.uniform(0.85,1.2, N_ORDERS)
prices = np.round(prices,2)
# discounts and promo flags
discount_pct = np.random.choice([0,5,10,15,20], size=N_ORDERS, p=[0.7,0.12,0.08,0.06,0.04])
total_value = np.round(prices * quantity * (1 - discount_pct/100),2)
# statuses, payment, channel
status = np.random.choice(["completed","returned","cancelled"], size=N_ORDERS, p=[0.93,0.05,0.02])
payment = np.random.choice(["card","paypal","applepay","googlepay","giftcard"], size=N_ORDERS, p=[0.6,0.15,0.08,0.08,0.09])
device = np.random.choice(["desktop","mobile","tablet"], size=N_ORDERS, p=[0.55,0.4,0.05])
booking_platform = np.random.choice(["site","app","marketplace"], size=N_ORDERS, p=[0.6,0.3,0.1])

orders = pd.DataFrame({
    "order_id": np.arange(1, N_ORDERS+1),
    "customer_id": order_customer,
    "product_id": order_product,
    "order_date": order_dates,
    "quantity": quantity,
    "unit_price": prices,
    "discount_pct": discount_pct,
    "total_value": total_value,
    "status": status,
    "payment_method": payment,
    "device": device,
    "platform": booking_platform
})
orders["order_date"] = pd.to_datetime(orders["order_date"])

# Add derived columns: order_month, days_since_signup
orders = orders.merge(customers[["customer_id","signup_date"]], on="customer_id", how="left")
orders["days_since_signup"] = (orders["order_date"] - orders["signup_date"]).dt.days.clip(lower=0)
orders["order_month"] = orders["order_date"].dt.to_period("M").astype(str)

# ---------- 4) SESSIONS (user website sessions / interactions) ----------
session_dates = random_dates(N_SESSIONS)
session_customer = np.random.choice(customers["customer_id"], size=N_SESSIONS)
session_duration = np.random.exponential(scale=300, size=N_SESSIONS).astype(int)  # seconds
pages = np.random.poisson(4, N_SESSIONS) + 1
session_device = np.random.choice(["desktop","mobile","tablet"], size=N_SESSIONS, p=[0.55,0.4,0.05])
session_channel = np.random.choice(channels, size=N_SESSIONS, p=[0.25,0.2,0.2,0.15,0.15,0.05])

sessions = pd.DataFrame({
    "session_id": np.arange(1, N_SESSIONS+1),
    "customer_id": session_customer,
    "session_start": session_dates,
    "duration_seconds": session_duration,
    "pages": pages,
    "device": session_device,
    "acquisition_channel": session_channel
})
sessions["session_start"] = pd.to_datetime(sessions["session_start"])

# ---------- 5) AD SPEND (monthly, by channel) ----------
months = pd.period_range(start=START_DATE.to_period("M"), end=END_DATE.to_period("M"), freq="M").astype(str)
ad_channels = ["Paid Search","Social","Display","Affiliate","Email"]
rows = []
for m in months:
    for ch in ad_channels:
        # trend upward over time + noise
        month_index = int(m.split("-")[0]) * 12 + int(m.split("-")[1])
        base = 20000 + (month_index - 201900) * 50  # small upward trend
        spend = max(1000, base * np.random.uniform(0.6,1.6))
        rows.append((m, ch, round(spend,2)))
ad_spend = pd.DataFrame(rows, columns=["month","channel","spend_usd"])

# ---------- SAVE CSVs ----------
customers.to_csv(os.path.join(OUT_DIR, "customers.csv"), index=False)
products.to_csv(os.path.join(OUT_DIR, "products.csv"), index=False)
orders.to_csv(os.path.join(OUT_DIR, "orders.csv"), index=False)
sessions.to_csv(os.path.join(OUT_DIR, "sessions.csv"), index=False)
ad_spend.to_csv(os.path.join(OUT_DIR, "ad_spend_monthly.csv"), index=False)

print("Data generation completed. Files in 'data/' folder:")
print(" - customers.csv,", customers.shape)
print(" - products.csv,", products.shape)
print(" - orders.csv,", orders.shape)
print(" - sessions.csv,", sessions.shape)
print(" - ad_spend_monthly.csv,", ad_spend.shape)
