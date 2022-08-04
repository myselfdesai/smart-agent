from app import app
from flask import jsonify


# TODO: Give the route a name/path.
@app.route("/your-route-name-here", methods=["GET"])
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

    return jsonify([
        {"userId": 1, "name": "Test User 1", "chatsHandled": 10, "averageHandlingSeconds": 120},
        {"userId": 2, "name": "Test User 2", "chatsHandled": 0, "averageHandlingSeconds": 0},
        # etc.
    ])
