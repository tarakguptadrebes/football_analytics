DROP TABLE IF EXISTS ratings_with_age;
CREATE Table ratings_with_age AS
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

SELECT m.player_id, m.age, AVG(m.rating) AS rating
FROM mapping AS m
INNER JOIN market_value_players_by_age AS mv
	ON m.player_id = mv.player_id
	AND m.age = mv.age
GROUP BY m.player_id, m.age;

SELECT * FROM ratings_with_age