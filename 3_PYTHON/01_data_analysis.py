# ============================================================
# AI-POWERED DYNAMIC PRICING & REVENUE OPTIMIZATION ENGINE
# BASIC DATA ANALYSIS
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------

sales = pd.read_csv("../1_DATA/sales_data.csv")
products = pd.read_csv("../1_DATA/products.csv")
competitors = pd.read_csv("../1_DATA/competitor_prices.csv")
inventory = pd.read_csv("../1_DATA/inventory.csv")

print("Data loaded successfully!")


# ------------------------------------------------------------
# 2. BASIC DATA CHECK
# ------------------------------------------------------------

print("\nSales Dataset:")
print(sales.shape)

print("\nProducts Dataset:")
print(products.shape)

print("\nCompetitor Dataset:")
print(competitors.shape)

print("\nInventory Dataset:")
print(inventory.shape)


# ------------------------------------------------------------
# 3. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\nMissing Values in Sales Data:")
print(sales.isnull().sum())


# ------------------------------------------------------------
# 4. BASIC SALES ANALYSIS
# ------------------------------------------------------------

total_revenue = sales["revenue"].sum()
total_profit = sales["gross_profit"].sum()
total_units = sales["quantity_sold"].sum()

print("\nBusiness Summary")
print("----------------")
print("Total Revenue:", round(total_revenue, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Units Sold:", total_units)


# ------------------------------------------------------------
# 5. CATEGORY PERFORMANCE
# ------------------------------------------------------------

category_summary = (
    sales.groupby("category")
    .agg(
        revenue=("revenue", "sum"),
        units_sold=("quantity_sold", "sum"),
        profit=("gross_profit", "sum")
    )
    .sort_values("revenue", ascending=False)
)

print("\nCategory Performance:")
print(category_summary)


# ------------------------------------------------------------
# 6. TOP 10 PRODUCTS
# ------------------------------------------------------------

top_products = (
    sales.groupby("product_id")
    .agg(
        revenue=("revenue", "sum"),
        units_sold=("quantity_sold", "sum")
    )
    .sort_values("revenue", ascending=False)
    .head(10)
)

print("\nTop 10 Products by Revenue:")
print(top_products)


# ------------------------------------------------------------
# 7. AVERAGE PRICE COMPARISON
# ------------------------------------------------------------

sales["price_difference"] = (
    sales["unit_price"] - sales["competitor_price"]
)

print("\nAverage Price Difference:")
print(round(sales["price_difference"].mean(), 2))


# ------------------------------------------------------------
# 8. SAVE ANALYSIS OUTPUT
# ------------------------------------------------------------

category_summary.to_csv(
    "../1_DATA/category_summary.csv"
)

top_products.to_csv(
    "../1_DATA/top_products.csv"
)

print("\nAnalysis completed successfully!")
