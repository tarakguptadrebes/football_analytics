DROP TABLE IF EXISTS market_values_with_age;

CREATE TABLE market_values_with_age AS
WITH player_age_avg AS (
	SELECT pv.player_id, 
		AVG(pv.market_value_in_eur) AS market_value_in_eur,
		FLOOR((pv.date::date - p.date_of_birth::date) / 365.25) AS age
	FROM transfermarkt_player_valuations AS pv
	INNER JOIN transfermarkt_players AS p
		ON pv.player_id = p.player_id
	WHERE pv.date::date >= '2020-08-01'
		AND pv.date::date <  '2025-08-01'
		AND pv.player_club_domestic_competition_id IN ('ES1','FR1','GB1','IT1','L1')
	GROUP BY pv.player_id, FLOOR((pv.date::date - p.date_of_birth::date) / 365.25)
),
ranked AS (
	SELECT *,
		ROW_NUMBER() OVER(
			PARTITION BY age
			ORDER BY market_value_in_eur DESC
		) AS rn
	FROM player_age_avg
),
valid_ages AS (
	SELECT age
	FROM ranked
	GROUP BY age
	HAVING COUNT(*) >= 500
)

SELECT player_id, age, market_value_in_eur
FROM ranked
WHERE rn <= 500
	AND age IN (SELECT age FROM valid_ages);

SELECT * FROM market_values_with_age