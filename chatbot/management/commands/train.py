from django.core.management.base import BaseCommand

from chatterbot.trainers import ChatterBotCorpusTrainer

from chatbot.bot import get_chatbot


class Command(BaseCommand):
    help = 'Train the chatbot on the ChatterBot English corpus.'

    def handle(self, *args, **options):
        bot = get_chatbot()
        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train(
            'chatterbot.corpus.english.greetings',
            'chatterbot.corpus.english.conversations',
        )

        self.stdout.write(self.style.SUCCESS('Training complete.'))
