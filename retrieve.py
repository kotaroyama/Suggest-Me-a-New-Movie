import json
import random

import requests

import credentials
import database


def generate_imdb_id():
    imdb_id_int = random.randint(0, 9999999)
    imdb_id_string = 'tt' + str(imdb_id_int).zfill(8)
    return imdb_id_string

def retrieve_movie():
    while True:
        imdb_id = generate_imdb_id()
        url = f'http://www.omdbapi.com/?apikey={credentials.OBDB_API}&i={imdb_id}'
        r = requests.get(url)
        r_json = json.loads(r.text)
        if r_json['Response'] != 'False':
            break
    return r_json

def main():
    movie = {}
    while True:
        movie = retrieve_movie()
        imdb_id = movie['imdbID']
        if database.is_movie_already_checked(imdb_id) is False:
            database.insert_new_movie(r_json)
            break

if __name__ == "__main__":
    main()
