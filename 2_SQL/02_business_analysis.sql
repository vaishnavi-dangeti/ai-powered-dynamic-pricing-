-- ============================================================
-- AI-POWERED DYNAMIC PRICING & REVENUE OPTIMIZATION ENGINE
-- BUSINESS ANALYSIS USING SQL
-- ============================================================

USE dynamic_pricing;


-- 1. OVERALL BUSINESS PERFORMANCE
-- What is the overall revenue, sales and profit?

SELECT
    COUNT(DISTINCT transaction_id) AS total_transactions,
    SUM(quantity_sold) AS total_units_sold,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(gross_profit), 2) AS total_profit
FROM sales;


-- 2. MONTHLY REVENUE
-- How does revenue change month by month?

SELECT
    MONTH(date) AS month,
    ROUND(SUM(revenue), 2) AS revenue,
    SUM(quantity_sold) AS units_sold
FROM sales
GROUP BY MONTH(date)
ORDER BY month;


-- 3. CATEGORY PERFORMANCE
-- Which categories generate the most revenue?

SELECT
    category,
    SUM(quantity_sold) AS units_sold,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(SUM(gross_profit), 2) AS profit
FROM sales
GROUP BY category
ORDER BY revenue DESC;


-- 4. TOP 10 PRODUCTS BY REVENUE
-- Which products generate the highest revenue?

SELECT
    s.product_id,
    p.product_name,
    p.category,
    ROUND(SUM(s.revenue), 2) AS revenue,
    SUM(s.quantity_sold) AS units_sold
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY
    s.product_id,
    p.product_name,
    p.category
ORDER BY revenue DESC
LIMIT 10;


-- 5. OUR PRICE VS COMPETITOR PRICE
-- Are our prices higher or lower than competitors?

SELECT
    s.product_id,
    p.product_name,
    ROUND(AVG(s.unit_price), 2) AS our_price,
    ROUND(AVG(s.competitor_price), 2) AS competitor_price,
    ROUND(
        AVG(s.unit_price) - AVG(s.competitor_price),
        2
    ) AS price_difference
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY
    s.product_id,
    p.product_name
ORDER BY price_difference DESC
LIMIT 10;


-- 6. PROMOTION PERFORMANCE
-- Does promotion activity affect sales and revenue?

SELECT
    promotion_flag,
    SUM(quantity_sold) AS units_sold,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(SUM(gross_profit), 2) AS profit
FROM sales
GROUP BY promotion_flag
ORDER BY promotion_flag;


-- 7. INVENTORY STATUS
-- How many products are in each inventory condition?

SELECT
    inventory_status,
    COUNT(DISTINCT product_id) AS product_count,
    ROUND(AVG(closing_inventory), 0) AS average_inventory
FROM inventory
GROUP BY inventory_status
ORDER BY product_count DESC;


-- 8. PRICING OPPORTUNITIES
-- Identify products that may need a pricing review.

SELECT
    s.product_id,
    p.product_name,
    p.category,
    ROUND(AVG(s.unit_price), 2) AS current_price,
    ROUND(AVG(s.competitor_price), 2) AS competitor_price,

    CASE
        WHEN AVG(s.unit_price) > AVG(s.competitor_price)
            THEN 'Review Price'
        WHEN AVG(s.unit_price) < AVG(s.competitor_price)
            THEN 'Competitive Price'
        ELSE 'Similar Price'
    END AS pricing_status 

FROM sales s
JOIN products p
    ON s.product_id = p.product_id

GROUP BY
    s.product_id,
    p.product_name,
    p.category

ORDER BY
    s.product_id;
