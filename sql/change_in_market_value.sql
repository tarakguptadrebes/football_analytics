DROP TABLE IF EXISTS change_in_market_value;

CREATE TABLE change_in_market_value AS
WITH valuation_changes AS (
	SELECT age,
		avg_market_value-LAG(avg_market_value) OVER (ORDER BY age) AS change
	FROM avg_market_value_with_age
)
SELECT * FROM valuation_changes
WHERE change IS NOT NULL
ORDER BY age;


SELECT * FROM change_in_market_value