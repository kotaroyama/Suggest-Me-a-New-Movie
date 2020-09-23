import os
import splite3

def init_table(db_name='movies.db'):
    # If the database already exists, quit
    if os.path.exists(db_name):
        return
    
    # Create the .db file and connect to it
    os.mknod(db_name)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    table_name = 'retrieved'
    t = (table_name, )

    # Create table
    c.excecute('''CREATE TABLE ? 
                    (imdb_id text, title text, year real, country text,
                     language text)''', t)

    # Save changes
    conn.commit()

    # Close the connection to the database
    conn.close()

def insert_new_movie(movie, db_name='movies.db'):
    # Extract all the data
    imdb_id = movie['imdbID']
    title = movie['Title']
    year = int(movie['Year'])
    country = movie['Country']
    language = movie['Language']

    table_name = 'retrieved'
    t = (table_name, imdb_id, title, year, country, language, )

    # Database connection
    conn = sqlite.connect(db_name)
    c = conn.cursor()
    c.execute('INSERT INTO ? VALUES (?, ?, ?, ?, ?)', t)
    c.close()

def is_movie_already_checked(imdb_id, db_name='movies.db'):
    # Connect to the database
    conn = splite3.connect(db_name) 
    c = conn.cursor()
    table_name = 'retrieved'
    t = (table_name, )

    for row in c.execute('SELECT * FROM ?', t):
        row_dict = dict_factory(c, row)
        if (imdb_id is row_dict['imdb_id']):
            return True

    return False

def dict_factory(cursor, row):
    d = {}
    for index, col in enumerate(cursor.description):
        d[col[0]] = row[index]
    return d


