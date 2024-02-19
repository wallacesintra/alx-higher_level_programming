-- List all shows in 'hbtn_0d_tvshows'
-- display:
-- tv_shows.title, tv_show_genres.genre_id
-- in ascending order by tv_shows.title
-- tv_show_genres.genre_id
-- only use one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
