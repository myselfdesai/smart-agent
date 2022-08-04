from sqlalchemy import text
from app import app, database
from flask import jsonify


# TODO: Give the route a name/path.
@app.route("/users/stats", methods=["GET"])
def get_users_performance():
    """
    Return the interactions completed and average handling time of every user.
    :return: JSON array:

    [
        {
            "userId": 1,
            "name": "Test User",
            "chatsHandled": 10,
            "averageHandlingSeconds": 120
        },
        ...
    ]

    """

    # TODO: Calculate the statistics for each agent.


    query = text('SELECT user.user_id, user.name, COUNT(chat.user_id), AVG(strftime("%s",chat.handle_end)-strftime("%s",chat.handle_start)) FROM user LEFT JOIN chat ON chat.user_id = user.user_id GROUP BY chat.user_id')
    result = database.session.execute(query)
    payload = []
  
    for res in result.fetchall() :
        payload.append({"userId": res[0], "name": res[1], "chatsHandled": res[2], "averageHandlingSeconds": int(res[3] or 0)})

    return jsonify(payload)