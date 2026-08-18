-- Lists all cities with the state they belong to, sorted by cities.id
-- Each city is matched to its state through the state_id foreign key
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
