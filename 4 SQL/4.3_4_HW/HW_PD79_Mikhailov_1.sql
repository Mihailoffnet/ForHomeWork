-- Добавляем жанры
INSERT INTO jenre(jenre_name) 
VALUES 
	('Rock'),
	('Metall'),
	('POP'),
	('Hip-Hop'),
	('RAP');

-- Добавляем исполнителей
INSERT INTO singer(singer_name) 
VALUES 
	('Metallica'),
	('Eminem'),
	('Kurt Cobain'),
	('Morgenstern'),
	('Britney Spears'),
	('AC/DC'),
	('Bazzy');


-- Создаем связку исполнителей с жанрами
INSERT INTO singer_jenre 
VALUES 
	(1, 3),
	(2, 1),
	(3, 5),
	(4, 2),
	(5, 4),
	(5, 2),
	(1, 1),
	(1, 6),
	(2, 6),
	(3, 7);

-- Добавляем альбомы
INSERT INTO album(album_name, album_years) 
VALUES 
	('Cadillac', 2020), -- Морген
	('Circus', 2008), -- Спирс
	('In the Zone', 2020), -- Спирс
	('Ride the Lightning', 1986), -- Металлика
	('Kill Em All', 1983), -- Металлика
	('The Slim Shady LP', 1991), -- Эминем
	('Nevermind', 1991), --Кобейн 
	('COSMIC', 2019); --Bazzy 

-- Создаем связку исполнителей с альбомами
INSERT INTO singer_album 
VALUES 
	(1, 4), -- Cadillac - Морген
	(2, 5), -- Circus - Спирс
	(3, 5), -- In the Zone - Спирс
	(4, 1), -- Ride the Lightning - Металлика
	(5, 1), -- Kill Em All - Металлика
	(6, 2), -- The Slim Shady LP - Эминем
	(7, 3), -- Nevermind -Кобейн 
	(8, 7); -- COSMIC -Bazzy 

-- Добавляем треки
INSERT INTO track(track_name, album_id, track_duration) 
VALUES 
	('Мой Cadillac', 1, 192), -- Морген
	('In Bloom', 7, 255), -- Кобейн
	('Hold It Against Me', 3, 310), -- Спирс
	('Escape', 4, 261), -- Металлика
	('My Name Is', 6, 268), -- Эминем
	('Jump In The Fire', 5, 281), -- Металлика
	('Love Story (Taylor Swift)', 2, 207), -- Спирс
	('Stay Away', 7, 211), -- Кобейн
	('Myself', 8, 256); -- Bazzy

-- Добавляем сборники
INSERT INTO collection(collection_name, collection_years) 
VALUES 
	('TOP 100 2023', 2023), -- Морген
	('Rock Ballads', 2002), -- Металлика
	('Disco 2010', 2018), -- Спирс
	('RAPsody', 2020), -- Эминем
	('POPs 2000', 2008); -- Спирс

-- Создаем связку сборника с треком
INSERT INTO track_collection 
VALUES 
	(1, 1),
	(6, 2),
	(7, 3),
	(5, 4),
	(3, 5);