import json
import sqlite3
import unittest

import requests

import credentials
import database
import retrieve

# Database and table
DB_NAME = 'test.db'
TABLE_NAME = 'retrieved'

# Movies to be used
MOVIE1_IMDB_ID = 'tt7959026' # The Mule
MOVIE2_IMDB_ID = 'tt1596363' # The Big Short


class RetrieveTestCase(unittest.TestCase):

    def test_movie_dict(self):
        """ Check if movie object is dictionary"""
        movie = retrieve.retrieve_movie()
        self.assertIsInstance(movie, dict)
        
    def test_movie_none(self):
        """ Check if movie object is not empty """
        movie = retrieve.retrieve_movie()
        self.assertIsNotNone(movie)


class DatabaseTestCase(unittest.TestCase):
    
    def test_insert_movie(self):
        """ Insert new movie into the database and check if it exists """
        movie1 = retrieve_movie(MOVIE1_IMDB_ID)
        movie2 = retrieve_movie(MOVIE2_IMDB_ID)
        database.insert_new_movie(movie1, DB_NAME)
        database.insert_new_movie(movie2, DB_NAME)

        self.assertTrue(database.is_movie_already_checked(MOVIE1_IMDB_ID, DB_NAME))
        self.assertTrue(database.is_movie_already_checked(MOVIE2_IMDB_ID, DB_NAME))

def retrieve_movie(imdb_id):
    """ Retrieve movie based on the IMDb ID"""
    url = f'http://www.omdbapi.com/?apikey={credentials.OBDB_API}&i={imdb_id}'
    r = requests.get(url)
    movie = json.loads(r.text)
    return movie

def print_database():
    """ Print the db file (for debugging purposes)"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    for row in c.execute(f"SELECT * FROM {TABLE_NAME}"):
        print(row)

    c.close()

if __name__ == '__main__':
    database.init_table(DB_NAME)
    unittest.main()
    print_database()
