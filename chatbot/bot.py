from django.conf import settings

from chatterbot import ChatBot


def get_chatbot():
    return ChatBot(**settings.CHATTERBOT)
