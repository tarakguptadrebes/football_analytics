SELECT
	p.id,
	p.match_id,
	p.name,
	p.slug,
	p.position,
	p."dateOfBirthTimestamp",
	p.rating,
	m.slug,
	m."startTimestamp"
FROM sofascore_player_stats AS p
INNER JOIN sofascore_matches AS m
ON p.match_id = m.id
