-- Script that lists all shows and all genres
-- The list should display tv_shows.title, tv_genres.name
-- The list should be sorted by tv_shows.title and tv_genres.name
-- If a show doesn't have a genre, display NULL
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
     LEFT JOIN tv_show_genres
     	  ON tv_show_genres.show_id = tv_shows.id
     LEFT JOIN tv_genres
     	  ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name;
