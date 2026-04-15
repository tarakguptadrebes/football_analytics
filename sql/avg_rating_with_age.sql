DROP TABLE IF EXISTS avg_rating_with_age;

CREATE TABLE avg_rating_with_age AS
SELECT age, AVG(rating) AS avg_rating
FROM values_ratings_with_age
GROUP BY age
ORDER BY age;

SELECT * FROM avg_rating_with_age