DROP TABLE IF EXISTS avg_market_value_with_age;

CREATE TABLE avg_market_value_with_age AS
SELECT age, AVG(market_value_in_eur) AS avg_market_value
FROM values_ratings_with_age
GROUP BY age
ORDER BY age;

SELECT * FROM avg_market_value_with_age