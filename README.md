# EdgeTier Python Challenge

**Note:** Please do not put your solution in a public repository (GitHub etc.). We are sending this to multiple candidates and do not want anyone to have an unfair advantage.

# Description

One of EdgeTier's products, Arthur, allows contact centre agents to answer customer queries via live chat and email. This project contains a tiny subset of the system with a database of users, chats, and chat messages. 

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

## Tests

There are some sample tests in `/test` written using [pytest](https://docs.pytest.org/en/stable/). Testing and code quality is important at EdgeTier so we would appreciate if the tests were extended for your solution.

### Run Tests With PyCharm

1. Create a new configuration selecting pytest from the "Templates".
2. See the root of the project as the working directory if it's not already.

You should now be able to run the tests.

### Run Tests With Command Line

1. Activate your virtual environment. 
2. `pytest test` to run all tests.

# Tasks

## Task 1

Managers in contact centres like to see statistics on agents' performance. A blank route has been created (see `/app/routes/users/get_users_performance.py`) that needs to be completed. Calculate and return the total number of chats handled and the average handling time for all users in the database. We also haven't decided yet what the route should be called so you will need to give it a name (and rename the file if you prefer).

## Task 2

There is an existing route `POST` `/chats/<chat_id>/messages`, for storing messages in a chat. This is an old route that has been badly written and is full of bugs. During QA testing some problems were identified. 

Please look at the route `/app/routes/chats/post_message.py` and try to fix as many problems as you can. The code is also (deliberately) badly written so make any improvements that you think make sense.

# Submission

Complete the challenge and submit a link to a private repository on BitBucket/GitHub etc. Please try to have clear commits for the changes that you have made for Task 1 and Task 2 for ease of review.

# Data

## Users

```
+-------------------+
|user_id|name       |
+-------------------+
|1      |Test User 1|
|2      |Test User 2|
|3      |Test User 3|
+-------------------+
```

## Chats

```
+--------------------------------------------------------------------------------------------------------------+
|chat_id|created                   |customer_name|user_id|handle_start              |handle_end                |
+--------------------------------------------------------------------------------------------------------------+
|1      |2020-09-29 08:55:20.540957|John         |1      |2020-09-29 09:00:20.540957|2020-09-29 09:05:20.540957|
|2      |2020-09-29 09:00:20.540957|Jane         |1      |2020-09-29 09:02:20.540957|                          |
|3      |2020-09-29 09:00:20.540957|Jerry        |3      |2020-09-29 09:02:20.540957|2020-09-29 09:05:20.540957|
|4      |2020-09-29 08:40:20.540957|Jacintha     |3      |2020-09-29 08:44:20.540957|2020-09-29 08:54:20.540957|
|5      |2020-09-29 08:55:20.540957|Julia        |       |                          |                          |
|6      |2020-09-29 08:50:20.540957|Joseph       |       |                          |                          |
+--------------------------------------------------------------------------------------------------------------+
```

## Messages

```
+-------------------------------------------------------------------------------------------------+
|message_id|chat_id    |text                                   |user_id|sent_at                   |
+-------------------------------------------------------------------------------------------------+
|1         |1          |Hello, I need to cancel my reservation.|       |2020-09-29 09:00:20.540957|
|2         |1          |I can do that.                         |1      |2020-09-29 09:01:20.540957|
|3         |1          |That has been cancelled.               |1      |2020-09-29 09:02:20.540957|
|4         |1          |Sound, thanks.                         |       |2020-09-29 09:04:20.540957|
|5         |2          |Your website is giving me an error.    |       |2020-09-29 09:02:20.540957|
|6         |2          |Sorry to hear that, what is the error? |1      |2020-09-29 09:04:20.540957|
|7         |3          |What are your opening hours?.          |       |2020-09-29 09:02:20.540957|
|8         |3          |Monday to Friday, 9am to 6pm.          |3      |2020-09-29 09:04:20.540957|
|9         |3          |Thanks.                                |       |2020-09-29 09:04:20.540957|
|10        |4          |I'd like to make a complaint.          |       |2020-09-29 08:44:20.540957|
|11        |4          |Please fill out a complaint form.      |3      |2020-09-29 08:46:20.540957|
|12        |4          |You can find it on our website.        |3      |2020-09-29 08:53:20.540957|
|13        |4          |OK I'll do that.                       |       |2020-09-29 09:01:20.540957|
+-------------------------------------------------------------------------------------------------+
```
