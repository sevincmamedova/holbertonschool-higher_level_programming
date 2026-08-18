# SQL - More queries

Creating MySQL users, granting privileges, and querying across multiple tables
with joins, subqueries and unions.

## Files

| File | Description |
| ---- | ----------- |
| `0-privileges.sql` | Lists all privileges of the users `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates the user `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates the database `hbtn_0d_2` and a read-only user `user_0d_2` |
| `3-force_name.sql` | Creates the table `force_name` whose `name` field cannot be null |
| `4-never_empty.sql` | Creates the table `id_not_null` whose `id` defaults to 1 |
| `5-unique_id.sql` | Creates the table `unique_id` whose `id` defaults to 1 and is unique |
| `6-states.sql` | Creates `hbtn_0d_usa` and the `states` table |
| `7-cities.sql` | Creates `hbtn_0d_usa` and the `cities` table with a foreign key |
| `8-cities_of_california_subquery.sql` | Lists the cities of California using a subquery |
| `9-cities_by_state_join.sql` | Lists all cities with their state name |
