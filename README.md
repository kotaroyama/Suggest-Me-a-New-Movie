# Suggest Random Movie

## What it is
This script suggests random movie for you using the [OMBd API](http://www.omdbapi.com/). It never suggests the same movie. Once a movie has been retrieved by the script, it will be added to the database, and whenever the script retrieves a movie, it will go through the database to see if it has already been retrieved. 

## Motivation
I got the idea from [this list of project ideas](https://github.com/jorgegonzalez/beginner-projects).

## TODO
The fact that every time the script has to go through all the movies on the database gives you the complexity of O(n), which I think could be improved by using some sort of hash table when adding a movie to the database.
