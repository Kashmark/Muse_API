#!/bin/bash

rm db.sqlite3
rm -rf ./museapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations museapi
python3 manage.py migrate museapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata mediums
python3 manage.py loaddata artists
python3 manage.py loaddata categories
python3 manage.py loaddata payment_types
python3 manage.py loaddata artworks
python3 manage.py loaddata orders
python3 manage.py loaddata order_artworks
python3 manage.py loaddata saved_artworks



