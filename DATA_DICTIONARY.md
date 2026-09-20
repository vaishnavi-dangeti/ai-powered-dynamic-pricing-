# 📊 Data Dictionary

This document describes the datasets used in the AI-Powered Dynamic Pricing & Revenue Optimization Engine.

All datasets are synthetic and created for portfolio and educational purposes.

---

## 1. products.csv

Contains the master information for all products.

| Column | Description |
|---|---|
| product_id | Unique identifier for each product |
| product_name | Product name |
| category | Product category |
| base_cost | Base cost of the product |
| base_price | Standard selling price |
| min_price | Minimum allowed selling price |
| max_price | Maximum allowed selling price |

**Records:** 500 products

---

## 2. sales_data.csv

Contains historical e-commerce sales transactions.

| Column | Description |
|---|---|
| transaction_id | Unique transaction identifier |
| date | Transaction date |
| product_id | Product identifier |
| category | Product category |
| unit_price | Selling price per unit |
| discount_pct | Discount percentage |
| competitor_price | Competitor reference price |
| promotion_flag | Indicates whether a promotion was active |
| quantity_sold | Number of units sold |
| revenue | Revenue generated from the transaction |
| gross_profit | Gross profit generated |

**Records:** 100,000 transactions

---

## 3. competitor_prices.csv

Contains competitor pricing information used to evaluate market pricing.

| Column | Description |
|---|---|
| date | Price observation date |
| product_id | Product identifier |
| competitor_a_price | Competitor A price |
| competitor_b_price | Competitor B price |
| competitor_c_price | Competitor C price |
| competitor_avg_price | Average competitor price |

**Records:** 26,500 observations

---

## 4. inventory.csv

Contains product inventory information over time.

| Column | Description |
|---|---|
| date | Inventory snapshot date |
| product_id | Product identifier |
| opening_inventory | Inventory at the beginning of the period |
| units_sold_estimate | Estimated units sold |
| closing_inventory | Inventory remaining |
| reorder_point | Inventory reorder threshold |
| inventory_status | Inventory condition/status |

**Records:** 6,000 observations

---

## 5. promotions.csv

Contains information about promotional campaigns.

| Column | Description |
|---|---|
| promotion_id | Unique promotion identifier |
| date | Promotion date |
| promotion_type | Type of promotion |
| promotion_discount_pct | Promotional discount percentage |

**Records:** 365 observations

---

## 6. calendar.csv

Contains calendar and seasonal information.

| Column | Description |
|---|---|
| date | Calendar date |
| day_of_week | Day of the week |
| month | Month number |
| quarter | Quarter |
| is_weekend | Weekend indicator |
| season | Season |

**Records:** 365 days

---

## 🔗 Dataset Relationships

The datasets are connected primarily through:

- `product_id`
- `date`

### Main relationships

products  
↓  
sales_data

products  
↓  
competitor_prices

products  
↓  
inventory

sales_data  
↓  
calendar

sales_data  
↓  
promotions

These relationships allow the project to combine sales, competition, inventory, promotions, and calendar effects for pricing analysis.

---

## 🎯 Purpose of the Data

The combined datasets support:

- Historical sales analysis
- Demand prediction
