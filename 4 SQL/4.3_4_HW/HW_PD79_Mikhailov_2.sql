-- самый длинный трек и его название
SELECT track_name, track_duration FROM track 
WHERE track_duration = 
      (SELECT MAX(track_duration) from track);
      
-- Название треков, продолжительность которых не менее 3,5 минут
SELECT track_name, track_duration FROM track 
WHERE track_duration >= 210;
     
-- Названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT collection_name, collection_years FROM collection 
WHERE collection_years BETWEEN 2018 AND 2020;

-- Исполнители, чьё имя состоит из одного слова
SELECT singer_name FROM singer 
WHERE singer_name NOT LIKE '% %';

-- Доработка 1: Название треков, которые содержат слово «мой» или «my»
SELECT track_name FROM track 
WHERE track_name ILIKE 'my %' 
OR track_name ILIKE 'мой %'
OR track_name ILIKE '% my'
OR track_name ILIKE '% мой'
OR track_name ILIKE '% мой %'
OR track_name ILIKE '% my %'
OR track_name ILIKE 'my'
OR track_name ILIKE 'мой';

-- Доработка 2: Название треков, которые содержат слово «мой» или «my»
SELECT track_name FROM track 
WHERE string_to_array(LOWER(track_name), ' ') && ARRAY['my', 'мой']; 
-- Это самая красивая реализация, на мой взгляд. Я как раз искал как сделать выборку из переченя.
-- Но что будет с таким запросом, если название трека будет с запятой или со скобками, например 'Remix (my way)'?
-- В этом случае нужно использовать все варианты разделителей через OR?
-- OR string_to_array(LOWER(track_name), '(') && ARRAY['my', 'мой']
-- OR string_to_array(LOWER(track_name), ')') && ARRAY['my', 'мой']
-- OR string_to_array(LOWER(track_name), '(,) && ARRAY['my', 'мой']
-- OR string_to_array(LOWER(track_name), '(.) && ARRAY['my', 'мой']; 

-- Доработка 3: Название треков, которые содержат слово «мой» или «my»
SELECT track_name FROM track 
WHERE LOWER(track_name) ~* '^my '
OR LOWER(track_name) ~*  '^мой '
OR LOWER(track_name) ~*  ' my$'
OR LOWER(track_name) ~*  ' мой$'
OR LOWER(track_name) ~*  ' мой '
OR LOWER(track_name) ~*  ' my '
OR LOWER(track_name) ~*  '^my$'
OR LOWER(track_name) ~*  '^мой$';