import sqlalchemy
from pprint import pprint
from functools import reduce

engine = sqlalchemy.create_engine('postgresql://slava:7548@localhost:5432/music')
connection = engine.connect()

# 1
sel = connection.execute(
    '''
    SELECT name_album, years FROM music_album
    WHERE years == 2008;
    ''').fetchall()
pprint(sel)

# __________________________________________________________
# 2
sel = connection.execute(
    '''
    SELECT name_track, times FROM music_track
    ''').fetchall()
name = ''
time = 0
for item in sel:
    if item[1] > time:
        time = item[1]
        name = item[0]
pprint(name)

# __________________________________________________________
# 3
sel = connection.execute(
    '''
    SELECT name_track FROM music_track
    WHERE times > 210;
    ''').fetchall()
pprint(sel)

# __________________________________________________________
# 4
sel = connection.execute(
    '''
    SELECT name_music_collection FROM music_collection
    WHERE years BETWEEN 2018 AND 2022;
    ''').fetchall()
pprint(sel)

# __________________________________________________________
# 5
sel = connection.execute(
    '''
    SELECT name FROM musician;
    ''').fetchall()
print(list(filter(lambda name: ' ' not in name[0], sel)))

# __________________________________________________________
# 6
sel = connection.execute(
    '''
    SELECT name_track FROM music_track
    WHERE name_track iLIKE '%%my%%';
    ''').fetchall()
pprint(sel)
