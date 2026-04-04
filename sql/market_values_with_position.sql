DROP TABLE IF EXISTS market_valuations_with_position;

CREATE TABLE market_valuations_with_position AS
SELECT pv.player_id, 
	pv.market_value_in_eur,
	pv.player_club_domestic_competition_id,
	pv.date::date, 
	p.position,
	p.sub_position
FROM transfermarkt_player_valuations AS pv
INNER JOIN transfermarkt_players AS p
	ON pv.player_id = p.player_id
WHERE pv.date::date >= '2020-08-01'
	AND pv.date::date <  '2025-08-01'
	AND pv.player_club_domestic_competition_id IN ('ES1','FR1','GB1','IT1','L1');

SELECT * FROM market_valuations_with_position