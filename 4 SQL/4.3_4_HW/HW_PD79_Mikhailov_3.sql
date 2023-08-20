--Количество исполнителей в каждом жанре
SELECT jenre_name, count(singer_name) AS c_s 
FROM singer_jenre AS s_j
JOIN singer AS s ON s_j.singer_id = s.singer_id
JOIN jenre AS j ON s_j.jenre_id = j.jenre_id
GROUP BY jenre_name ORDER BY c_s desc;

-- Количество треков, вошедших в альбомы 2019–2020 годов
SELECT count(track_id)FROM track as tr
JOIN album as al ON tr.album_id = al.album_id
where album_years between 2019 and 2020;

-- Количество треков, вошедших в альбомы 2019–2020 годов с указанием альбомов
-- Добавил второй вариант кода, так как из задачи не понял, нужно ли общее количество треков
-- или количество треков в разрезе годов
SELECT count(track_id), album_years as a_e
FROM track as tr
JOIN album as al ON tr.album_id = al.album_id
where album_years between 2019 and 2020
GROUP by a_e ORDER by a_e;

--Средняя продолжительность треков по каждому альбому
SELECT avg(track_duration) as a_d, album_name as a_n
FROM track as tr
JOIN album as al ON tr.album_id = al.album_id
GROUP BY a_n ORDER BY a_d desc;

-- Доработка: Все исполнители, которые не выпустили альбомы в 2020 году
SELECT singer_name as s_n
FROM singer as si
where singer_name not in (SELECT singer_name as s_n
FROM singer as si
JOIN singer_album as s_a ON s_a.singer_id = si.singer_id
JOIN album as al ON al.album_id = s_a.album_id
where album_years = 2020
GROUP BY s_n ORDER BY s_n);

-- Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами)
SELECT singer_name, collection_name as c_n
FROM singer as si
JOIN singer_album as s_a ON s_a.singer_id = si.singer_id
JOIN album as al ON al.album_id = s_a.album_id
JOIN track as tr ON tr.album_id = al.album_id
JOIN track_collection as t_c ON t_c.track_id = tr.track_id
JOIN collection as co ON co.collection_id = t_c.collection_id
where singer_name = 'Britney Spears'
ORDER BY c_n;