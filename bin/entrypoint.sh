#!/bin/bash

# Wait until the PostgreSQL database is ready before starting the application
let "attempts = 0";
while ! python -c 'import psycopg2; psycopg2.connect("dbname=postgres user=postgres host=db")' &> /dev/null ;
do
    if [ $attempts == "0" ] ; then
        echo "Waiting for the postgres server:";
    fi;

    let "attempts = attempts + 1";
    let "give_up = attempts == 30";

    echo "Attempt ${attempts} of 30"

    if [ $give_up = "1" ] ; then
        echo "Cannot connect to the postgres server after 30 seconds; exiting";
        exit;
    fi;

    sleep 1;
done;

# We can start
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
