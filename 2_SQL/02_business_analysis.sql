-- ============================================================
-- AI-POWERED DYNAMIC PRICING & REVENUE OPTIMIZATION ENGINE
-- BUSINESS ANALYSIS QUERIES
-- ============================================================

USE dynamic_pricing;

-- ============================================================
-- 1. OVERALL BUSINESS PERFORMANCE
-- ============================================================

SELECT
    COUNT(DISTINCT transaction_id) AS total_transactions,
    COUNT(DISTINCT product_id) AS products_sold,
    SUM(quantity_sold) AS total_units_sold,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(gross_profit), 2) AS total_gross_profit,
    ROUND(SUM(gross_profit) / SUM(revenue) * 100, 2) AS profit_margin_pct
FROM sales;


-- ============================================================
-- 2. MONTHLY REVENUE TREND
-- ============================================================

SELECT
    YEAR(date) AS year,
    MONTH(date) AS month,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(quantity_sold) AS units_sold,
