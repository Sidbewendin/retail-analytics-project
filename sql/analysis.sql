-- Total revenue
SELECT SUM("TotalPrice") FROM factsales;

-- Revenue by country
SELECT "Country", SUM("TotalPrice") AS revenue
FROM factsales
GROUP BY "Country"
ORDER BY revenue DESC;

-- At-risk customers
SELECT COUNT(*) AS at_risk_customers
FROM dimcustomer
WHERE "Recency" > 90;

-- VIP customers
SELECT 
    COUNT(*) AS vip_customers
FROM dimcustomer
WHERE "Monetary" > 5000;