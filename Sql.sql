CREATE DATABASE ecommerce;
USE ecommerce;
SHOW DATABASES;

SELECT *
FROM `sample - superstore`
LIMIT 10;
RENAME TABLE `sample - superstore`
TO orders;
SELECT *
FROM orders
LIMIT 10;
SELECT COUNT(*) AS Total_Records
FROM orders;
DESCRIBE orders;
SELECT
ROUND(SUM(Sales),2) AS Total_Sales
FROM orders;
SELECT
ROUND(SUM(Profit),2) AS Total_Profit
FROM orders;
SELECT
COUNT(DISTINCT `Order ID`) AS Total_Orders
FROM orders;
SELECT
COUNT(DISTINCT `Customer ID`) AS Total_Customers
FROM orders;
SELECT
Category,
ROUND(SUM(Sales),2) AS Sales
FROM orders
GROUP BY Category
ORDER BY Sales DESC;
SELECT
Category,
ROUND(SUM(Profit),2) AS Profit
FROM orders
GROUP BY Category
ORDER BY Profit DESC;
SELECT
Region,
ROUND(SUM(Sales),2) AS Sales
FROM orders
GROUP BY Region
ORDER BY Sales DESC;
SELECT
`Product Name`,
ROUND(SUM(Sales),2) AS Sales
FROM orders
GROUP BY `Product Name`
ORDER BY Sales DESC
LIMIT 10;
SELECT
`Customer Name`,
ROUND(SUM(Sales),2) AS Sales
FROM orders
GROUP BY `Customer Name`
ORDER BY Sales DESC
LIMIT 10;
SELECT
`Product Name`,
ROUND(SUM(Profit),2) AS Profit
FROM orders
GROUP BY `Product Name`
HAVING Profit < 0
ORDER BY Profit;
SELECT
State,
ROUND(SUM(Profit),2) AS Profit
FROM orders
GROUP BY State
ORDER BY Profit DESC;
DESCRIBE orders;
ALTER TABLE orders
CHANGE COLUMN `ï»¿Row ID` `Row ID` INT;
DESCRIBE orders;
