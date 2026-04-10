DROP TABLE IF EXISTS avg_rating_with_age;

CREATE TABLE avg_rating_with_age AS
WITH mapping AS (
	SELECT pm.player_id, 
		s.rating,
		FLOOR((s.match_date::date - s.date_of_birth::date) / 365.25) AS age
	FROM sofascore_player_match_data AS s
	INNER JOIN player_mappings AS pm
		ON s.name = pm.name
		AND s.date_of_birth = pm.date_of_birth
),
market_value_players_by_age AS (
	SELECT DISTINCT player_id, age
	FROM market_values_with_age
)

SELECT m.age, AVG(m.rating) AS avg_rating
FROM mapping AS m
INNER JOIN market_value_players_by_age AS mv
	ON m.player_id = mv.player_id
	AND m.age = mv.age
GROUP BY m.age
ORDER BY m.age;

SELECT * FROM avg_rating_with_age