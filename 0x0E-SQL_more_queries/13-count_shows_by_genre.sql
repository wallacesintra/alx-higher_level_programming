-- Script that lists genres and number of shows
-- The number of shows should be sorted in descending order
-- The genres should be sorted in ascending order
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC, tv_genres.id ASC;
