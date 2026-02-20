SELECT
    country,
    SUM(total_price) AS total_revenue,
    COUNT(*) AS total_orders
FROM raw_orders
GROUP BY country;
