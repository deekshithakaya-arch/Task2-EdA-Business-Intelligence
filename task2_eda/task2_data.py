# TASK 2 : EXPLORATORY DATA ANALYSIS (EDA) & BUSINESS INTELLIGENCE

import pandas as pd
import matplotlib.pyplot as plt

# Better chart style
plt.style.use('ggplot')

print("=" * 60)
print("TASK 2 : EXPLORATORY DATA ANALYSIS & BUSINESS INTELLIGENCE")
print("=" * 60)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

print("\n[1] Loading Dataset...")

df = pd.read_csv("Superstore data.csv")  
print("Dataset Loaded Successfully!")

# --------------------------------------------------
# Dataset Overview
# --------------------------------------------------

print("\n[2] DATASET OVERVIEW")

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

# --------------------------------------------------
# Sales Analysis
# --------------------------------------------------

print("\n" + "=" * 60)
print("SALES ANALYSIS")
print("=" * 60)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nMaximum Sales:")
print(df["Sales"].max())

print("\nMinimum Sales:")
print(df["Sales"].min())

# --------------------------------------------------
# Profit Analysis
# --------------------------------------------------

print("\n" + "=" * 60)
print("PROFIT ANALYSIS")
print("=" * 60)

print("\nTotal Profit:")
print(df["Profit"].sum())

print("\nAverage Profit:")
print(df["Profit"].mean())

print("\nMaximum Profit:")
print(df["Profit"].max())

print("\nMinimum Profit:")
print(df["Profit"].min())

# --------------------------------------------------
# Region Analysis
# --------------------------------------------------

print("\n" + "=" * 60)
print("REGION WISE SALES")
print("=" * 60)

region_sales = df.groupby("Region")["Sales"].sum()

print(region_sales)

# --------------------------------------------------
# Category Analysis
# --------------------------------------------------

print("\n" + "=" * 60)
print("CATEGORY ANALYSIS")
print("=" * 60)

category_sales = df.groupby("Category")["Sales"].sum()
category_profit = df.groupby("Category")["Profit"].sum()

print("\nSales by Category:")
print(category_sales)

print("\nProfit by Category:")
print(category_profit)

# --------------------------------------------------
# Top States By Sales
# --------------------------------------------------

print("\n" + "=" * 60)
print("TOP 10 STATES BY SALES")
print("=" * 60)

state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(state_sales)

# --------------------------------------------------
# Univariate Analysis
# --------------------------------------------------

print("\n" + "=" * 60)
print("UNIVARIATE ANALYSIS")
print("=" * 60)

print("\nCategory Count:")
print(df["Category"].value_counts())

# --------------------------------------------------
# Business Insights
# --------------------------------------------------

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

best_region = region_sales.idxmax()
best_category = category_sales.idxmax()

print(f"\nBest Performing Region : {best_region}")
print(f"Best Performing Category : {best_category}")

# --------------------------------------------------
# VISUALIZATION 1
# Sales Distribution
# --------------------------------------------------
plt.figure(figsize=(10,6))

plt.hist(
    df["Sales"],
    bins=15,
    edgecolor="black"
)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()
# --------------------------------------------------
# VISUALIZATION 2
# Profit Distribution
# --------------------------------------------------
plt.figure(figsize=(10,6))

plt.hist(
    df["Profit"],
    bins=15,
    edgecolor="black"
)
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()

# --------------------------------------------------
# VISUALIZATION 3
# Region Wise Sales
# --------------------------------------------------

plt.figure(figsize=(10, 6))
region_sales.plot(kind="bar")
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# VISUALIZATION 4
# Category Wise Sales
# --------------------------------------------------

plt.figure(figsize=(10, 6))
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# VISUALIZATION 5
# Category Wise Profit
# --------------------------------------------------

plt.figure(figsize=(10, 6))
category_profit.plot(kind="bar")
plt.title("Category Wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# VISUALIZATION 6
# Top 10 States By Sales
# --------------------------------------------------

plt.figure(figsize=(12, 6))
state_sales.plot(kind="bar")
plt.title("Top 10 States By Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# VISUALIZATION 7
# Sales Vs Profit
# --------------------------------------------------

plt.figure(figsize=(10, 6))
plt.scatter(
    df["Sales"],
    df["Profit"],
    alpha=0.6
)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.show()

# --------------------------------------------------
# Completion
# --------------------------------------------------
print("\nEDA Generated Successfully!")
print("Task 2 Completed Successfully!")
print("=" * 60)