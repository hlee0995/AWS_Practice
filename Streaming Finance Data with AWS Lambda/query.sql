SELECT MAX(sub.high) as high, sub.name, sub.time
FROM (SELECT high,
	name,
	SUBSTRING(ts, 11,3) AS time,
	SUBSTRING(ts, 1, 16) AS dates
FROM "17"
) sub
GROUP BY sub.name, sub.time


