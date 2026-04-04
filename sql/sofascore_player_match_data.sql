DROP TABLE IF EXISTS sofascore_player_match_data;

CREATE TABLE sofascore_player_match_data AS
SELECT
    p.id,
    p.match_id,
    p.name,
    p.slug,
    p.position,
    TO_TIMESTAMP(p."dateOfBirthTimestamp")::date AS date_of_birth,
    p.rating,
    TO_TIMESTAMP(m."startTimestamp")::date AS match_date
FROM sofascore_player_stats AS p
INNER JOIN sofascore_matches AS m
	ON p.match_id = m.id;

SELECT * FROM sofascore_player_match_data;