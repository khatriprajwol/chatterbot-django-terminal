# Django + ChatterBot Terminal Client

A terminal chat client built with Django and ChatterBot, a machine-learning
based conversational dialog engine. The bot is trained on ChatterBot's
built-in English corpus (greetings and small talk) and its learned
statements are persisted to a Django/SQLite database via ChatterBot's
Django storage adapter.

## Project layout

- `chatbot_project/` - Django project settings/urls, including the
  `CHATTERBOT` config block in `settings.py`.
- `chatbot/bot.py` - builds the `ChatBot` instance from settings.
- `chatbot/management/commands/train.py` - trains the bot on the corpus.
- `chatbot/management/commands/chat.py` - the interactive terminal client.
- `requirements.txt` - manifest of pinned Python dependencies.

## Setup

Requires Python 3.10+ (ChatterBot's spaCy dependency does not support
Python 3.9 or earlier).

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm   # NLP model used for tagging

python manage.py migrate        # creates db.sqlite3 + chatterbot tables
python manage.py train          # trains the bot on the English corpus
```

## Usage

```bash
python manage.py chat
```

Example session:

```
Chatting with ChatterBot. Type 'quit', 'exit', or 'bye' to stop.
user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.
user: You're welcome.
bot: Do you like hats?
user: quit
bot: Goodbye!
```

Responses are drawn from the trained corpus and from any conversations
had during previous sessions, so wording may vary slightly between runs.
