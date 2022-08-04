
# Application 

The application uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) with [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/). There is an in-memory SQLite database automatically created and populated with some data every time the application starts. The database tables are defined in `/app/models.py`. The data can be seen in `/configuration/insert_data.py` (and at the bottom of this page for ease of reference).

`/app/routes/get_user.py` has been provided as an example as a finished route with tests in `/test/test_app/test_get_user.py` to help. For those with no experience of SQLAlchemy, you can just write raw SQL if you prefer and `/app/get_user.py` has an example of how to do that. 

## Setup

* Install Python 3.6+.
* Install SQLite. Mac already has this installed already most of the time.
* `git clone` the repository.

### Run With PyCharm

1. Open the project, select your Project Interpreter from preferences and install all packages from `requirements.txt`.
1. Create a new run configuration ("Edit Configurations..." at the top right).
2. Set the "script path" to your virtual environment's `bin/flask`.
3. In "parameters" type "run".

You should now be able to run `main.py`. Go to http://localhost:8484/users/1 to confirm it's running.

### Run With Command Line

1. Create and activate a new virtual environment.
2. `pip install requirements.txt`.
3. `flask run`.

Go to http://localhost:5000/users/1 to confirm it's running.
