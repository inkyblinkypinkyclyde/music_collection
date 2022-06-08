import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist1 = Artist("Nirvana")
artist_repository.save(artist1)

album1 = Album("Bleach", "Grunge", artist1)
album_repository.save(album1)

album2 = Album("Nevermind", "Grunge", artist1)
album_repository.save(album2)




result = album_repository.select_all()

for item in result:
    print(item.__dict__)

pdb.set_trace()