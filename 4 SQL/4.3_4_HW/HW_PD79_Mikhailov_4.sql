-- Названия альбомов, в которых присутствуют исполнители более чем одного жанра
SELECT album_name
FROM album as al
JOIN singer_album as s_a ON s_a.album_id = al.album_id
JOIN singer_jenre as s_j ON s_j.singer_id = s_a.singer_id
JOIN jenre as je ON s_j.jenre_id = je.jenre_id
GROUP BY album_name
HAVING COUNT(jenre_name) > 1;

-- Доработка: Названия альбомов, в которых присутствуют исполнители более чем одного жанра
SELECT DISTINCT album_name
FROM album as al
JOIN singer_album as s_a ON s_a.album_id = al.album_id
JOIN singer_jenre as s_j ON s_j.singer_id = s_a.singer_id
JOIN jenre as je ON s_j.jenre_id = je.jenre_id
GROUP BY album_name, s_a.singer_id
HAVING COUNT(s_j.jenre_id) > 1
ORDER BY album_name;

-- Наименования треков, которые не входят в сборники
SELECT track_name
FROM track as tr
LEFT JOIN track_collection as t_c ON t_c.track_id = tr.track_id
where t_c.track_id IS NULL;

-- Доработка: Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, 
-- теоретически таких треков может быть несколько
SELECT track_duration as t_d, singer_name
FROM track as tr
JOIN singer_album as s_a ON s_a.album_id = tr.album_id
JOIN singer as si ON s_a.singer_id = si.singer_id
WHERE track_duration = (
	SELECT min(track_duration) from track);

-- Названия альбомов, содержащих наименьшее количество треков
SELECT album_name as a_n
FROM album as al
LEFT JOIN track as tr ON al.album_id = tr.album_id
GROUP BY a_n
HAVING count(track_id) = (
	SELECT COUNT(track_id) FROM track
	JOIN album ON track.album_id = album.album_id
	GROUP BY album_name 
	ORDER BY COUNT(track_id) LIMIT 1);

