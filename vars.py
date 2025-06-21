#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21905616"))
API_HASH = environ.get("API_HASH", "0506d1a8b04f4c580c369b47c885bbd4")
BOT_TOKEN = environ.get("BOT_TOKEN", "7842100793:AAExTtWhAGdpY0-q8Z0AAJmIlBnsfbPv6LI")
OWNER = int(environ.get("OWNER", "7912270773"))
CREDIT = "JAANIBOTS"
AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
