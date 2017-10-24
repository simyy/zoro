#!/bin/bash


if [[ $# == 1 && "$1" == "debug" ]]; then 
    export FLASK_CONFIG="development"
    python manage.py runserver --port=4000
else
    export FLASK_CONFIG="production"
    /opt/work/zoro/bin/python /opt/work/zoro/src/manage.py runserver --port 4000
fi
