# ============================================================
# AI-POWERED DYNAMIC PRICING & REVENUE OPTIMIZATION ENGINE
# PRICE OPTIMIZATION
# ============================================================

import pandas as pd


# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------

sales = pd.read_csv("../1_DATA/sales_data.csv")
products = pd.read_csv("../1_DATA/products.csv")
inventory = pd.read_csv("../1_DATA/inventory.csv")

print("Data loaded successfully!")


# ------------------------------------------------------------
# 2. CREATE PRODUCT SUMMARY
# ------------------------------------------------------------

summary = (
    sales.groupby("product_id")
    .agg(
        current_price=("unit_price", "mean"),
        competitor_price=("competitor_price", "mean"),
        units_sold=("quantity_sold", "sum"),
        revenue=("revenue", "sum")
    )
    .reset_index()
)


# ------------------------------------------------------------
# 3. ADD PRODUCT INFORMATION
# ------------------------------------------------------------

summary = summary.merge(
    products[
        [
            "product_id",
            "product_name",
            "category",
            "min_price",
            "max_price"
        ]
    ],
    on="product_id",
    how="left"
)


# ------------------------------------------------------------
# 4. SIMPLE PRICE RECOMMENDATION
# ------------------------------------------------------------

def recommend_price(row):

    price = row["current_price"]

    # If our price is much higher than competitors
    if price > row["competitor_price"] * 1.05:
        price = price * 0.97

    # If our price is much lower than competitors
    elif price < row["competitor_price"] * 0.95:
        price = price * 1.03

    # Keep price within allowed limits
    price = max(price, row["min_price"])
    price = min(price, row["max_price"])

    return round(price, 2)


summary["recommended_price"] = summary.apply(
    recommend_price,
    axis=1
)


# ------------------------------------------------------------
# 5. CALCULATE PRICE CHANGE
# ------------------------------------------------------------

summary["price_change_pct"] = (
    (summary["recommended_price"] - summary["current_price"])
    / summary["current_price"]
) * 100


# ------------------------------------------------------------
# 6. PRICING ACTION
# ------------------------------------------------------------

summary["pricing_action"] = summary.apply(
    lambda row:
        "Decrease Price"
        if row["recommended_price"] < row["current_price"]
        else "Increase Price"
        if row["recommended_price"] > row["current_price"]
        else "Hold Price",
    axis=1
)


# ------------------------------------------------------------
# 7. DISPLAY TOP OPPORTUNITIES
# ------------------------------------------------------------

opportunities = summary.sort_values(
    "price_change_pct"
)

print("\nTop Pricing Opportunities:")
print(
    opportunities[
        [
            "product_id",
            "product_name",
            "current_price",
            "competitor_price",
            "recommended_price",
            "pricing_action"
        ]
    ].head(10)
)


# ------------------------------------------------------------
# 8. SAVE RESULTS
# ------------------------------------------------------------

summary.to_csv(
    "../1_DATA/pricing_recommendations.csv",
    index=False
)

print("\nPrice optimization completed successfully!")
print("Pricing recommendations saved.")
