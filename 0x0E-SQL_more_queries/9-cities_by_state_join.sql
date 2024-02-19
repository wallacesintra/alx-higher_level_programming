-- script that lists all cities
-- display id,name,states.name
-- ascending order by cities.id
-- use only one SELECT statement
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON state_id = cities.state_id;
