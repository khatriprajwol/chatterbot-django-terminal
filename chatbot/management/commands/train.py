"""
Management command: trains the ChatterBot instance on the built-in
English corpus so it has something to draw responses from before the
first `chat` session.

Usage:
    python manage.py train
"""
from django.core.management.base import BaseCommand

from chatterbot.trainers import ChatterBotCorpusTrainer

from chatbot.bot import get_chatbot


class Command(BaseCommand):
    help = 'Train the chatbot on the ChatterBot English corpus.'

    def handle(self, *args, **options):
        bot = get_chatbot()
        trainer = ChatterBotCorpusTrainer(bot)

        # Each string names a YAML file in chatterbot_corpus/data/english/.
        # Training is idempotent - statements that already exist in the
        # database are not duplicated, so re-running this is safe.
        trainer.train(
            'chatterbot.corpus.english.greetings',
            'chatterbot.corpus.english.conversations',
        )

        self.stdout.write(self.style.SUCCESS('Training complete.'))
