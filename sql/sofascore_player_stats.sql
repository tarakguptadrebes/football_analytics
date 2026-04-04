DROP TABLE IF EXISTS sofascore_player_stats;

CREATE TABLE sofascore_player_stats AS
SELECT id, match_id, name, slug, position, "dateOfBirthTimestamp", rating
FROM sofascore_bundesliga_player_stats
UNION ALL
SELECT id, match_id, name, slug, position, "dateOfBirthTimestamp", rating
FROM sofascore_la_liga_player_stats
UNION ALL
SELECT id, match_id, name, slug, position, "dateOfBirthTimestamp", rating
FROM sofascore_ligue_1_player_stats
UNION ALL
SELECT id, match_id, name, slug, position, "dateOfBirthTimestamp", rating
FROM sofascore_premier_league_player_stats
UNION ALL
SELECT id, match_id, name, slug, position, "dateOfBirthTimestamp", rating
FROM sofascore_serie_a_player_stats;

SELECT * FROM sofascore_player_stats