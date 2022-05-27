
CREATE TABLE IF NOT EXISTS musician(
id SERIAL PRIMARY KEY,
name VARCHAR(40) NOT NULL,
music_style VARCHAR(40) NOT null
);

--INSERT INTO musician (name, music_style) VALUES 
--      ('Ñòèíã','rock');

 CREATE TABLE IF NOT EXISTS music_album(
id SERIAL PRIMARY KEY,
name_album VARCHAR(40) NOT NULL,
years DATE NOT NULL
);

--INSERT INTO music_album (name_album, years) VALUES 
--      ('Slippery When Wet', '1986-08-01'),
--      ('The Soul Cages', '1991-05-01'),
--      ('19', '2008-01-25'),     
--      ('Hello Dolly', '1948-01-25'), 
--      ('Taylor Swift', '2006-10-24'),
--      ('Eric Clapton', '1970-09-11'),   
--      ('Baby One More Time', '1999-01-15'), 
--      ('Thriller', '1982-11-30'); 
    

CREATE TABLE IF NOT EXISTS musicianmusic_album(
musician_id INTEGER REFERENCES musician(id),
music_album_id INTEGER REFERENCES music_album(id),
CONSTRAINT ma PRIMARY KEY (musician_id, music_album_id)
);

--INSERT INTO musicianmusic_album (musician_id, music_album_id) VALUES 
--      (1, 1),
--      (2, 2),
--      (3, 3),     
--      (5, 4), 
--      (4, 5),
--      (6, 6),   
--      (7, 7), 
--      (8, 8); 

CREATE TABLE IF NOT EXISTS music_style(
id SERIAL PRIMARY KEY,
name_style VARCHAR(40) NOT null
);

--INSERT INTO music_style (name_style) VALUES 
--      ('pop'),
--      ('rock'),
--      ('jazz'),
--      ('blues'),
--      ('country');

CREATE TABLE IF NOT EXISTS musicianmusic_style(
musician_id INTEGER REFERENCES musician(id),
music_style_id INTEGER REFERENCES music_style(id),
CONSTRAINT ms PRIMARY KEY (musician_id, music_style_id)
);

--INSERT INTO musicianmusic_style (musician_id, music_style_id) VALUES 
--      (1,39),
--      (2,39),
--      (3,38),
--      (4,42),
--      (5,40),
--      (6,41),
--      (7,38),
--      (8,38);
     
CREATE TABLE IF NOT EXISTS music_track(
id SERIAL PRIMARY KEY,
music_album_id INTEGER REFERENCES music_album(id),
name_track VARCHAR(40) NOT NULL,
times INTEGER
);

--INSERT INTO music_track (music_album_id, name_track, times) VALUES 
--      (1, 'Let It Rock', 325),
--      (1, 'You Give Love a Bad Name', 224),
--      (1, 'Livin on a Prayer', 265),
--      (1, 'Social Disease', 258),
--      (2, 'Island of Souls', 401),
--      (2, 'All This Time', 295),
--      (2, 'Mad About You', 234),
--      (2, 'The Wild Wild Sea', 420),
--      (3, 'Daydreamer', 232),
--      (3, 'Best for Last', 256),
--      (3, 'Cold Shoulder', 192),
--      (4, 'Hello Dolly', 359),
--      (4, 'Jazz Festivall', 325),
--      (4, 'A Rhapsody in Black and Blue', 334),
--      (5, 'Tim McGraw', 210),
--      (5, 'Picture to Burn', 178),
--      (5, 'Teardrops on My Guitar', 216),
--      (6, '«After Midnight', 170),
--      (6, 'Easy Now', 180),
--      (6, 'Blues Power', 189),
--      (7, 'Baby One More Time', 282),
--      (7, 'Sometimes', 245),
--      (7, 'Born to Make You Happy', 243),
--      (8, 'Thriller', 360),
--      (8, 'Billie Jean', 300),
--      (8, 'The Girl Is Mine', 234);

CREATE TABLE IF NOT EXISTS music_collection(
id SERIAL PRIMARY KEY,
name_music_collection VARCHAR(40) NOT NULL,
years DATE
);

--INSERT INTO music_collection (name_music_collection, years) VALUES 
--      ('first', '1980-01-01'),
--      ('second', '1990-01-01'),
--      ('third', '2000-01-01'),
--      ('fourth', '2005-01-01'),
--      ('fifth', '2010-01-01'),
--      ('sixth', '2015-01-01'),
--      ('seventh', '2020-01-01'),
--      ('eighth', '2022-01-01');

CREATE TABLE IF NOT EXISTS music_trackmusic_collection(
music_track_id INTEGER REFERENCES music_track(id),
music_collection_id INTEGER REFERENCES music_collection(id),
CONSTRAINT tc PRIMARY KEY (music_track_id, music_collection_id)
);

--INSERT INTO music_trackmusic_collection (music_track_id, music_collection_id) VALUES 
--      (1,1),
--      (2,1),
--      (3,1),
--      (5,1),
--      (13,1),
--      (6,2),
--      (7,2),
--      (8,2),
--      (9,2),
--      (15,2),
--      (10,3),
--      (11,3),
--      (12,3),
--      (13,3),
--      (15,3),
--      (16,4),
--      (17,4),
--      (18,4),
--      (19,4),
--      (20,4),
--      (21,5),
--      (22,5),
--      (23,5),
--      (24,5),
--      (25,5),
--      (26,6),
--      (22,6),
--      (23,6),
--      (24,6),
--      (25,6),
--      (1,7),
--      (5,7),
--      (10,7),
--      (15,7),
--      (20,7),
--      (2,8),
--      (6,8),
--      (11,8),
--      (16,8),
--      (26,8);
