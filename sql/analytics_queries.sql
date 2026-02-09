-- Average price by city
SELECT city, AVG(price) AS avg_price
FROM HOTEL_DB.ANALYTICS.HOTELS_CLEANED
GROUP BY city
ORDER BY avg_price DESC;

-- Availability percentage
SELECT city,
       AVG(CASE WHEN availability THEN 1 ELSE 0 END) * 100 AS availability_pct
FROM HOTEL_DB.ANALYTICS.HOTELS_CLEANED
GROUP BY city
ORDER BY availability_pct DESC;

-- Price trend
SELECT date, AVG(price) AS avg_price
FROM HOTEL_DB.ANALYTICS.HOTELS_CLEANED
GROUP BY date
ORDER BY date;
