DROP TABLE IF EXISTS ratings_with_position;

CREATE TABLE ratings_with_position AS
WITH mapping AS (
	SELECT pm.player_id, s.rating
	FROM sofascore_player_match_data AS s
	INNER JOIN player_mappings AS pm
		ON s.name = pm.name
			AND s.date_of_birth = pm.date_of_birth
),
market_value_ids AS (
	SELECT DISTINCT player_id
	FROM market_valuations_with_position
)	

SELECT m.player_id, m.rating, t.position, t.sub_position
FROM mapping AS m
INNER JOIN market_value_ids AS mv
	ON m.player_id = mv.player_id
INNER JOIN transfermarkt_players AS t
	ON m.player_id = t.player_id