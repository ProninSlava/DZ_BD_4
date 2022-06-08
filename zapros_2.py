import sqlalchemy
from pprint import pprint
from functools import reduce

engine = sqlalchemy.create_engine('postgresql://slava:7548@localhost:5432/music')
connection = engine.connect()

# __________________________________________________________
# 1 количество исполнителей в каждом жанре                  OK

# sel = connection.execute(
#     '''
#     SELECT name_style, COUNT(name) n FROM music_style s
#     JOIN musicianmusic_style ms ON s.id = ms.music_style_id
#     JOIN musician m ON ms.musician_id = m.id
#     GROUP BY s.id
#     ORDER BY n;
#     ''').fetchall()
# pprint(sel)

# __________________________________________________________
# 2 количество треков, вошедших в альбомы 2019-2020 годов   OK

# sel = connection.execute(
#     '''
#     SELECT a.name_album, COUNT(t.name_track) FROM music_album a
#     JOIN music_track t ON t.music_album_id = a.id
#     WHERE a.years BETWEEN 2019 AND 2020
#     GROUP BY a.name_album;
#     ''').fetchall()
# pprint(sel)

# __________________________________________________________
# 3 средняя продолжительность трека по каждому альбому      OK

# sel = connection.execute(
#     '''
#     SELECT a.name_album, AVG(t.times) FROM music_album a
#     JOIN music_track t on t.music_album_id = a.id
#     GROUP BY a.name_album
#     ORDER BY AVG(t.times)
#     ''').fetchall()
# pprint(sel)

# __________________________________________________________
# 4 все исполнители, которые не выпустили альбомы           OK
# в 2020 году

# sel = connection.execute(
#     '''
#     SELECT DISTINCT m.name FROM musician m
#     WHERE m.name NOT IN
#     (SELECT DISTINCT m.name FROM musician m
#     JOIN musicianmusic_album ma ON m.id = ma.musician_id
#     JOIN music_album a ON ma.music_album_id = a.id
#     WHERE a.years = 2020)
#     ORDER BY m.name
#     ''').fetchall()
# pprint(sel)

# __________________________________________________________
# 5 названия сборников, в которых присутствует конкретный   OK
# исполнитель (выберите сами)

# sel = connection.execute(
#     '''
#     SELECT DISTINCT c.name_music_collection FROM music_collection c
#     JOIN music_trackmusic_collection tc  ON c.id = tc.music_collection_id
#     JOIN music_track t ON tc.music_track_id = t.id
#     JOIN music_album a ON t.music_album_id = a.id
#     JOIN musicianmusic_album ma ON a.id = ma.music_album_id
#     JOIN musician m ON ma.musician_id = m.id
#     WHERE m.name iLIKE '%%bon%%'
#     ORDER BY c.name_music_collection;
#      ''').fetchall()
# pprint(sel)

# __________________________________________________________
# 6 название альбомов, в которых присутствуют исполнители   OK
# более 1 жанра

# sel = connection.execute(
#     '''
#     SELECT a.name_album FROM music_album a
#     JOIN musicianmusic_album ma ON a.id = ma.music_album_id
#     JOIN musician m ON ma.musician_id = m.id
#     JOIN musicianmusic_style ms ON m.id = ms.musician_id
#     JOIN music_style s ON ms.music_style_id = s.id
#     GROUP BY a.name_album
#     HAVING COUNT(DISTINCT s.name_style) > 1
#     ORDER by a.name_album;
#     ''').fetchall()
# pprint(sel)

# __________________________________________________________
# 7 наименование треков, которые не входят в сборники       (не работает)

# sel = connection.execute(
#     '''
#     SELECT t.name_track FROM music_track t
#     JOIN music_trackmusic_collection mt ON t.id = mt.music_track_id
#     WHERE mt.music_track_id IS NULL;
#     ''').fetchall()
# pprint(sel)

# __________________________________________________________
# 8 исполнителя(-ей), написавшего самый короткий по         OK
# продолжительности трек (теоретически таких треков
# может быть несколько)

# sel = connection.execute(
#     '''
#     SELECT m.name, t.times FROM music_track t
#     JOIN music_album a ON t.music_album_id = a.id
#     JOIN musicianmusic_album ma ON a.id = ma.musician_id
#     JOIN musician m ON ma.music_album_id = m.id
#     GROUP BY m.name, t.times
#     HAVING t.times = (SELECT MIN(times) FROM music_track)
#     ORDER BY t.times;
#     ''').fetchall()
# pprint(sel)

# __________________________________________________________
# 9 название альбомов, содержащих наименьшее количество     !?
# треков

sel = connection.execute(
    '''
    SELECT name_album, COUNT(name_track) tr FROM music_album a
    JOIN music_track t ON a.id = t.music_album_id
    GROUP BY a.id
    HAVING COUNT(name_track) =  
    (
    SELECT COUNT(name_track) tr FROM music_album a
    JOIN music_track t ON a.id = t.music_album_id
    GROUP BY a.id
    ORDER BY COUNT(name_track)
    LIMIT 1
    )
   
    ''').fetchall()
pprint(sel)
