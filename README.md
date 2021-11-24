### Cache API

##### Set up your virtual environment and install app dependencies

- `python 3 -m venv env `
- `source env/bin/activate `
- `pip install -r requirements.txt`

##### Add environment variables, create a new .env in your root folder directory , add the following

- `FLASK_APP=main.py`
- `FLASK_DEBUG=1 `
- `FLASK_ENV=development`
- `MAIL_PORT=587`
- `MAIL_USE_TLS = True`
- `DEV_DATABASE_URL=''`
- `TEST_DATABASE_URL=''`
- `SECRET_KEY=''`
- `MAIL_SERVER = ''`
- `MAIL_USERNAME = ''`
- `MAIL_PASSWORD = ''`
- `SENDGRID_API_KEY = ''`
- `SECURITY_PASSWORD_SALT=''`
- `MAIL_DEFAULT_SENDER=''`
- `OBJECTS_SLOT_NUMBER=10`
- `OBJECTS_TIME_TO_LIVE=10`
-
- OBJECTS_SLOT_NUMBER=10
  OBJECTS_TIME_TO_LIVE=10
  OBJECTS_EVICTION_POLICY = REJECT

##### Upgrade database and run your flask app

- `flask db upgrade`
- `flask run`

##### Run tests locally

`flask test` or `python -m unittest`

##### Get Test Coverage

`flask test --coverage`

##### Artifact from

`https://github.com/oluchilinda/diary-api`

Code Challenge Enterprise: CBInsights

Implementation author: Anibal Rodriguez
