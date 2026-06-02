DROP TABLE IF EXISTS player_mappings;

CREATE TABLE player_mappings AS
WITH sofascore_players AS(
	SELECT DISTINCT
        name,
        date_of_birth
    FROM sofascore_player_match_data
)

SELECT
	t.player_id,
    s.name,
    s.date_of_birth
FROM sofascore_players AS s
INNER JOIN transfermarkt_players AS t
   ON LOWER(s.name) = LOWER(t.name)
   AND s.date_of_birth::date = t.date_of_birth::date
ORDER BY s.name;

SELECT * FROM player_mappings
