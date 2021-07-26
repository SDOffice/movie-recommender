# TMDb API
from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import TV
# For loading JSON file
import json

# Open the JSON file
with open('./everything.json', encoding='utf-8') as fh:
    file = json.load(fh)

tmdb = TMDb()
tmdb.api_key = 'a9545ec1bd745e79c447cdadf22cb82c'
tmdb.language = 'en'
tmdb.debug = True

tv = TV()
movie = Movie()

data = []

for i in range(1):
    print(obj['title'])
    if(obj['type'] == "TV Show"):

        show = tv.search(obj['title'])

        try:
            print(show[0].name)
            print(show[0].poster_path)

            obj |= {
                'img': show[0].poster_path
            }
        except IndexError:
            print("NULL")

            obj |= {
                'img': "NULL"
            }

    elif(obj['type'] == "Movie"):

        m = movie.search(obj['title'])

        try:
            print(m[0].title)
            print(m[0].poster_path)

            obj |= {
                'img': m[0].poster_path
            }
        except IndexError:
            print("NULL")

            obj |= {
                'img': "NULL"
            }


with open('./everything.json', 'w', encoding='utf-8') as outfile:
    json.dump(file, outfile, indent=2, ensure_ascii=False)
