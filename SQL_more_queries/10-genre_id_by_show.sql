-- Lists all shows that are linked to at least one genre, with the genre id
-- Only the shows having a match in the linking table are kept
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
