from http import HTTPStatus

from flask.testing import FlaskClient

from app import database
from app.models import Chat


def test_post_message(client: FlaskClient):
    """
    Test POST message route.
    :param client: Flask test client.
    """

    # Insert a test chat.
    chat = Chat(user_id=1)
    database.session.add(chat)
    database.session.commit()

    # Store a message.
    response = client.post(f"/chats/{chat.chat_id}/messages", json={"text": "Sample message"})
    assert response.status_code == HTTPStatus.CREATED
