"""
Management command: an interactive terminal client for chatting with
the ChatterBot instance.

Usage:
    python manage.py chat

Type "quit", "exit", or "bye" to end the session.
"""
from django.core.management.base import BaseCommand

from chatbot.bot import get_chatbot

EXIT_WORDS = {'quit', 'exit', 'bye'}


class Command(BaseCommand):
    help = 'Start an interactive terminal chat session with the bot.'

    def handle(self, *args, **options):
        bot = get_chatbot()

        self.stdout.write(
            f"Chatting with {bot.name}. Type 'quit', 'exit', or 'bye' to stop.\n"
        )

        while True:
            try:
                user_input = input('user: ')
            except (EOFError, KeyboardInterrupt):
                # Ctrl+D / Ctrl+C should end the chat cleanly, not crash.
                self.stdout.write('\nbot: Goodbye!')
                break

            if user_input.strip().lower() in EXIT_WORDS:
                self.stdout.write('bot: Goodbye!')
                break

            response = bot.get_response(user_input)
            self.stdout.write(f'bot: {response}')
