"""
Shared helper for building the ChatterBot instance used by both the
`train` and `chat` management commands.

Keeping this in one place means the terminal client and the training
script always build the exact same bot (same name, same storage
adapter, same logic adapters) instead of two slightly different copies.
"""
from django.conf import settings

from chatterbot import ChatBot


def get_chatbot():
    """Create a ChatBot configured from the CHATTERBOT dict in settings.py.

    Using the Django storage adapter means every statement the bot
    learns is persisted to the project's database (see the
    django_chatterbot app / db.sqlite3), so training survives restarts.
    """
    return ChatBot(**settings.CHATTERBOT)
