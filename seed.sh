#!/bin/bash

rm -rf maneapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations maneapi
python3 manage.py migrate maneapi
python3 manage.py loaddata styles 
python3 manage.py loaddata users 
python3 manage.py loaddata tokens
python3 manage.py loaddata customers
python3 manage.py loaddata equipment_types 
python3 manage.py loaddata equipment 
python3 manage.py loaddata appointments