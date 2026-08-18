-- Lists all the cities of California, sorted in ascending order by cities.id
-- The id of California is looked up with a subquery on the states table
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT states.id FROM states WHERE states.name = 'California'
)
ORDER BY cities.id;
