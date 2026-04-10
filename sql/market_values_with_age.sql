DROP TABLE IF EXISTS market_values_with_age;

CREATE TABLE market_values_with_age AS
WITH ranked AS (
	SELECT pv.player_id, 
		pv.market_value_in_eur,
		pv.player_club_domestic_competition_id,
		pv.date::date, 
		p.date_of_birth::date,
		FLOOR((pv.date::date - p.date_of_birth::date) / 365.25) AS age,
		ROW_NUMBER() OVER(
			PARTITION BY FLOOR((pv.date::date - p.date_of_birth::date) / 365.25)
			ORDER BY pv.market_value_in_eur DESC
		) AS rn
	FROM transfermarkt_player_valuations AS pv
	INNER JOIN transfermarkt_players AS p
		ON pv.player_id = p.player_id
	WHERE pv.date::date >= '2020-08-01'
		AND pv.date::date <  '2025-08-01'
		AND pv.player_club_domestic_competition_id IN ('ES1','FR1','GB1','IT1','L1')
),
valid_ages AS (
	SELECT age
	FROM ranked
	GROUP BY age
	HAVING COUNT(*) >= 1000
)

SELECT *
FROM ranked
WHERE rn <= 1000
	AND age IN (SELECT age FROM valid_ages);

SELECT * FROM market_values_with_age