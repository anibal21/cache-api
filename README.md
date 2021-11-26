### Cache API

##### Set up your virtual environment and install app dependencies

- `python 3 -m venv env `
- `source env/bin/activate `
- `pip install -r requirements.txt`

##### Add environment variables, create a new .env in your root folder directory , add the following

- `FLASK_APP=main.py`
- `FLASK_DEBUG=1`
- `FLASK_ENV=development`
- `OBJECTS_SLOT_NUMBER=2`
- `OBJECTS_TIME_TO_LIVE=10`
- `OBJECTS_EVICTION_POLICY=OLDEST_FIRST`

###### Properties:

| PropertyName | value |
| --- | --- |
| FLASK_DEBUG |  1-Enabled, 0-Disabled|
| FLASK_ENV |  development, production|
| OBJECTS_SLOT_NUMBER |  0 to N|
| OBJECTS_TIME_TO_LIVE |  0 to N |
| OBJECTS_EVICTION_POLICY | OLDEST_FIRST, NEWEST_FIRST, REJECT|

##### Upgrade database and run your flask app

- `flask db upgrade`
- `flask run`

##### Run tests locally

`flask test` or `python -m unittest`

##### Get Test Coverage

`flask test --coverage`

##### Notes from Author:
- Project Developed by Anibal Rodriguez for CBInsights.
- Python 3.7 is recommended.
- It is design for Heroku first
- It was used GitFlow for this Project
