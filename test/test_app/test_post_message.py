from http import HTTPStatus

from flask.testing import FlaskClient
from sqlalchemy import null

from app import database
from app.models import Chat, Message
from datetime import datetime, timedelta

now = datetime.utcnow()

def test_post_message(client: FlaskClient):
    """
    Test POST message route.
    :param client: Flask test client.
    """

    # Insert a test chat.
    chat = Chat(
        created=now - timedelta(minutes=10),
        handle_start=now - timedelta(minutes=5),
        handle_end=None,
        user_id=1,
        messages=[
                Message(text='Hello, I need to cancel my reservation.', sent_at=now - timedelta(minutes=5))
            ]
    )
    database.session.add(chat)
    database.session.commit()

    # Store a message.
    response = client.post(f"/chats/{chat.chat_id}/messages", json={"text": "Sample message"})
    assert response.status_code == HTTPStatus.CREATED

def test_post_message_400(client: FlaskClient):
    """
    Test POST message route.
    :param client: Flask test client.
    """

    # Insert a test chat.
    chat = Chat(
        created=now - timedelta(minutes=10),
        handle_start=now - timedelta(minutes=5),
        handle_end=now,
        user_id=1,
        messages=[
                Message(text='Hello.', sent_at=now - timedelta(minutes=5))
            ]
    )
    database.session.add(chat)
    database.session.commit()

    # Store a message.
    response = client.post(f"/chats/{chat.chat_id}/messages", json={"text": "Sample message"})
    assert response.status_code == HTTPStatus.BAD_REQUEST
