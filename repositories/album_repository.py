from asyncio import tasks
from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist_id = row["artist_id"]
        artist = artist_repository.select(artist_id)
        album = Album(
            row['title'],
            row['genre'],
            artist,
        )
        albums.append(album)
    return albums

def save(album):
    sql = "INSERT INTO albums (title, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results
    album.id = id
    return album