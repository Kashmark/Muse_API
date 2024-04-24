#!/bin/bash

rm db.sqlite3
rm -rf ./museapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations museapi
python3 manage.py migrate museapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

