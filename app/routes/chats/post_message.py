from http import HTTPStatus
from typing import Tuple
import re

from app import app, database
from flask import request

from app.models import Chat, Message


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

    if _strip_sensitive_text(request.json.get("text")):
        return "Credit card numbers are not allowed.", HTTPStatus.BAD_REQUEST

    # Store the message.
    message = Message(chat=chat, text=request.json.get("text"))
    database.session.add(message)
    database.session.commit()

    if chat.handle_start is None:
        return "Can't store a message before the chat has started.", HTTPStatus.BAD_REQUEST

    if chat.handle_end is None:
        return "Can't store a message after the chat has ended.", HTTPStatus.BAD_REQUEST

    if not _is_handling_agent(chat, message):
        return "That agent isn't handling the chat.", HTTPStatus.BAD_REQUEST

    if _is_too_long(chat):
        return "The message cannot be more than 400 characters.", HTTPStatus.BAD_REQUEST

    return "", HTTPStatus.CREATED


def _is_handling_agent(chat: Chat, message: Message) -> bool:
    """
    If the message has a user ID, it has to match the agent of the chat.
    :param chat:    Chat being updated.
    :param message: Message being stored.
    :return:        True if the agent is correct or False otherwise.
    """
    if request.json.get("user_id") != chat.user_id:
        database.session.delete(message)
        database.session.commit()
        return False

    return True


def _is_too_long(chat: Chat) -> bool:
    """
    Don't store messages that are too long.
    :param chat: Chat being updated.
    :return:     True if the message is too long.
    """
    message: Message = chat.messages[0]
    return len(message.text) >= 500


def _strip_sensitive_text(text: str) -> bool:
    """
    Remove credit card numbers.
    :param text: Message text.
    """
    return re.search(r"\d{4} \d{4} \d{4} \d{4}", text) is not None
