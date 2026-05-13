DROP TABLE IF EXISTS values_ratings_with_age;

CREATE TABLE values_ratings_with_age AS
SELECT mv.player_id, mv.age, mv.market_value_in_eur, r.rating
FROM market_values_with_age AS mv
INNER JOIN ratings_with_age AS r
    ON mv.player_id = r.player_id
    AND mv.age = r.age
WHERE r.rating IS NOT NULL;

SELECT * FROM values_ratings_with_age