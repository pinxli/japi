#!/bin/bash
python manage.py loaddata agentlevels
python manage.py loaddata banks
python manage.py loaddata commissionsettings
python manage.py loaddata providers
python manage.py loaddata levels
python manage.py loaddata gametypes
python manage.py loaddata transactiontype
python manage.py loaddata groups
python manage.py loaddata application
python manage.py loaddata permission

