SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS month, SUM(Sales) AS sales
FROM sales
GROUP BY month
ORDER BY month;






