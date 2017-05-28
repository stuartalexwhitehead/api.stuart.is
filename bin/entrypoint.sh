#!/bin/bash

# Check we have a task
if [ -z "$1" ] ; then
    echo "No command chosen"
    echo "-------------------------------------------------"
    echo "start                       start the application"
    echo "test                        run tests"
    echo "lint                        run flake8 linting"
    echo "-------------------------------------------------"
    exit 0
fi

# Run flake8 linting
# --------------------------------
# Lint whole working directory by default
# Can accept space-separated list of filenames to lint
if [ "$1" == "lint" ] ; then
    shift

    if [ -z "$1" ] ; then
        LINT_TARGET=$(pwd)
    else
        LINT_TARGET="$@"
    fi

    flake8 ${LINT_TARGET}
    exit 0
fi

# All other commands require PostgreSQL
# Wait until the PostgreSQL database is ready before continuing
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

if [ "$1" == "start" ] ; then
    python manage.py migrate --settings=stuart_is.settings.dev
    python manage.py runserver 0.0.0.0:8000
fi

if [ "$1" == "test" ] ; then
    coverage run --source='.' manage.py test --settings=stuart_is.settings.test
    coverage report
fi
