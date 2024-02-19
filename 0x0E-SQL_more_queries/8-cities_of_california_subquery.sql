-- list all cities in California
-- states where name = California 
-- sorted ascending order by cities.id
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
