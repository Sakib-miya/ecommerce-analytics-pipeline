📦 Ecommerce Analytics Pipeline

A complete end-to-end data project built with Python, NumPy, Pandas and a self-generated ecommerce dataset.

This project simulates the internal data workflow of a real ecommerce company.
Everything starts from scratch — I generated the raw datasets myself using Python, cleaned them, merged them into a master table, and finally used the cleaned data to build an analytics dashboard.

The goal of this project is to show the full process a data analyst would follow in a real company:
data creation → cleaning → transformation → analysis → dashboard.

🔹 Project Overview

The project contains two main Python scripts:

1. Data Generator (generate_ecom_data.py)

This script creates realistic synthetic ecommerce data, including:

100,000 customers

2,000 products

300,000 orders

400,000 website sessions

Monthly ad spend

The dataset includes customer demographics, acquisition channels, product details, pricing, margins, order behavior, device usage, sessions, and marketing spend.
It is designed to look similar to what a real ecommerce company would store.

2. Data Cleaning & Master File Builder (clean_data.py)

This script:

Removes duplicate rows

Standardizes and cleans each dataset

Creates a separate clean_data/ folder

Merges customers, orders, and products into a single master dataset

Saves master_dataset.csv for analysis or dashboard use

The master file is structured so it can be used directly for SQL queries, dashboard creation, or deeper analysis.

📊 Dashboard

Using the cleaned data, I built an analytics dashboard to explore:

Sales trends

Customer demographics

Product performance

Order behavior

Revenue patterns

Profitability

Device and channel attribution

Ad spend patterns

This dashboard can be found in the dashboard/ folder (or screenshots if uploading PBIX).

📂 Folder Structure
ecommerce-analytics-pipeline/
│── data/                     # Raw generated datasets
│── clean_data/               # Cleaned datasets
│── generate_ecom_data.py     # Data generator script
│── clean_data.py             # Data cleaning + master dataset script
│── master_dataset.csv        # Final combined dataset
│── dashboard/                # Dashboard files or images
│── README.md

🧠 Skills Demonstrated

Data cleaning and preprocessing

Working with large datasets

NumPy and Pandas for data manipulation

Merging multiple tables

Creating realistic synthetic data

Building KPI-driven dashboards

Understanding ecommerce analytics

🚀 How to Run the Project

Download the repository

Run generate_ecom_data.py to create raw data inside data/

Run clean_data.py to clean the data and create the master dataset

Use the master file to build dashboards or do analysis

Both scripts run in a standard Python environment with Pandas and NumPy installed.

📎 Why I Created This Project

I wanted a project that shows real analyst workflow, not just a visualization.
This repository demonstrates:

How data is created

How it is cleaned and structured

How multiple tables are connected

How insights come after proper data preparation

It represents the type of work expected from a data analyst in ecommerce, marketing, or product teams.

⭐ Final Note

This project is designed to be simple to run but complex enough to show real-world thinking.
The dataset sizes are large, the tables are realistic, and the workflow reflects actual industry practices.
