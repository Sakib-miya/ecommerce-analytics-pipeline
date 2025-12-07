# eCommerce Analytics Project

This project is a comprehensive eCommerce data analysis workflow built using **Python, NumPy, and pandas**, featuring **data generation, cleaning, master dataset creation, exploratory data analysis (EDA), and a Power BI dashboard**. It’s designed as a **portfolio-ready project** to showcase data analytics skills.

---

## Project Structure

```
ecommerce-analytics/
│
├── master_dataset.csv          # Final master dataset (orders + customers + products)
├── generate_ecom_data.py       # Script to generate synthetic eCommerce data
├── clean_master_data.py        # Script to clean and merge datasets into master
├── eda_analysis.py             # Script to perform EDA and generate charts
├── README.md                   # Project explanation (this file)
├── dashboard.pbix              # Interactive Power BI dashboard
```

---

## Overview

This project simulates a realistic eCommerce business with:

- **100,000 customers**  
- **2,000 products**  
- **300,000 orders**  
- **400,000 website sessions**  
- **Monthly ad spend by channel**  

The workflow covers:  

1. **Data Generation** – Creates synthetic but realistic eCommerce datasets.  
2. **Data Cleaning & Master Dataset** – Removes duplicates, merges orders, customers, and product info into one master dataset.  
3. **Exploratory Data Analysis (EDA)** – Analyzes trends such as top customers, product category revenue, monthly sales, and order metrics.  
4. **Visualization** – Plots key metrics and trends using Matplotlib.  
5. **Power BI Dashboard** – Interactive visualization to analyze business performance.

---

## EDA Highlights

- **Top 10 Customers by Revenue** – Identify your most valuable customers.  
- **Sales by Product Category** – Understand which categories generate the most revenue.  
- **Average Order Value** – Assess typical order sizes.  
- **Monthly Revenue Trend** – Track revenue growth over time.

All EDA results are saved in `eda_output/` including CSVs and charts (`.png`).

---

## Usage

1. **Generate Data** (optional if you want to reproduce):
```bash
python generate_ecom_data.py
```

2. **Clean and Merge Datasets**:
```bash
python clean_master_data.py
```

3. **Perform EDA**:
```bash
python eda_analysis.py
```

4. **Open Power BI Dashboard**:  
Open `dashboard.pbix` to explore interactive visualizations of revenue, customers, products, and trends.

---

## Key Insights

- Most revenue comes from **top 10% of customers**.  
- **Electronics** and **Apparel** categories dominate sales.  
- **Monthly revenue trend** shows a steady increase over the years.  
- Power BI dashboard allows filtering by **category, customer, device, and channel** for deeper analysis.

---

## Technologies Used

- **Python**  
- **NumPy**  
- **pandas**  
- **Matplotlib**  
- **Power BI Desktop**

---

## Portfolio Impact

This project demonstrates ability to:

- Generate synthetic datasets for analytics practice.  
- Clean and merge multiple data sources into a master dataset.  
- Perform actionable EDA and visualize results.  
- Build a professional Power BI dashboard with insights for decision-making.

---

## Dashboard
![Uploading Screenshot 2025-12-06 011345.png…]()
<img width="1299" height="725" alt="Screenshot 2025-12-06 011022" src="https://github.com/user-attachments/assets/c798d3b3-02d5-43f2-94ab-7e370165dac7" />




## Author

**Sakib Miya**  
Data Analyst Portfolio Project
