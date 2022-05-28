import sqlalchemy
from pprint import pprint
from functools import reduce

engine = sqlalchemy.create_engine('postgresql://slava:7548@localhost:5432/music')
connection = engine.connect()

# 1 название и год выхода альбомов, вышедших в 2018 году
sel = connection.execute(
    '''
    SELECT name_album, years FROM music_album
    WHERE years == 2008;
    ''').fetchall()
pprint(sel)

# __________________________________________________________
# 2 название и продолжительность самого длительного трека
sel = connection.execute(
    '''
    SELECT name_track, times FROM music_track
    ORDER BY times DESC;
    ''').fetchone()
pprint(sel)

# __________________________________________________________
# 3 название треков, продолжительность которых не менее 3,5 минуты
sel = connection.execute(
    '''
    SELECT name_track FROM music_track
    WHERE times > 210;
    ''').fetchall()
pprint(sel)

# __________________________________________________________
# 4 названия сборников, вышедших в период с 2018 по 2020 год включительно
sel = connection.execute(
    '''
    SELECT name_music_collection FROM music_collection
    WHERE years BETWEEN 2018 AND 2022;
    ''').fetchall()
pprint(sel)

# __________________________________________________________
# 5 исполнители, чье имя состоит из 1 слова
sel = connection.execute(
    '''
    SELECT name FROM musician
    WHERE name NOT iLIKE '%% %%';
    ''').fetchall()
pprint(sel)

# __________________________________________________________
# 6 название треков, которые содержат слово "мой"/"my"
sel = connection.execute(
    '''
    SELECT name_track FROM music_track
    WHERE name_track iLIKE '%%my%%';
    ''').fetchall()
pprint(sel)
