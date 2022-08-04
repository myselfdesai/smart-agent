import re

from app import app, database
from app.models import Chat, Message
from flask import request
from http import HTTPStatus
from typing import Tuple


@app.route("/chats/<int:chat_id>/messages", methods=["POST"])
def post_message(chat_id: int) -> Tuple[str, int]:
    """
    Store a message. A message should be rejected if:

        - The chat hasn't started yet.
        - The chat is already finished.
        - The user on the message is not handling the chat.
        - The message is more than 500 characters.

    Credit cards should also be blanked out with asterisks before storage.

    :param chat_id: Store a message for a chat.
    """

    chat: Chat = Chat.query.get_or_404(chat_id)

    message = request.json.get("text")
    user_id = request.json.get("user_id")

    if message is None:
        return "Please provide valid parameter ex. {'text': 'some message'}", HTTPStatus.BAD_REQUEST
    elif chat.handle_start is None:
        return "Can't store a message before the chat has started.", HTTPStatus.BAD_REQUEST
    elif chat.handle_end is not None:
        return "Can't store a message after the chat has ended.", HTTPStatus.BAD_REQUEST
    elif user_id is not None and not _is_handling_agent(chat, user_id):
        return "That agent isn't handling the chat.", HTTPStatus.BAD_REQUEST
    elif _is_too_long(message):
        return "The message cannot be more than 500 characters.", HTTPStatus.BAD_REQUEST
    else:
        # Store the message.
        message = _strip_sensitive_text(message)

        message = Message(chat_id=chat.chat_id, text=message, user_id=chat.user_id)
        database.session.add(message)
        database.session.commit()

        return "stored", HTTPStatus.CREATED


def _is_handling_agent(chat: Chat, user_id: int) -> bool:
    """
    If the message has a user ID, it has to match the agent of the chat.
    :param chat:    Chat being updated.
    :return:        True if the agent is correct or False otherwise.
    """
    if user_id != chat.user_id:
        return False
    return True


def _is_too_long(message: str) -> bool:
    """
    Don't store messages that are too long.
    :param chat: Chat being updated.
    :return:     True if the message is too long.
    """
    if len(message) <= 500:
        return False
    return True


def _strip_sensitive_text(message: str) -> bool:
    """
    Remove credit card numbers.
    :param text: Message text.
    only handled visa, mastercard and american express for this project
    """

    message = re.sub('4[0-9]{12}(?:[0-9]{3})|(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|3[47][0-9]{13}', '*******', message)
    return message
