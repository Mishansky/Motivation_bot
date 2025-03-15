import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")  # Токен бота из .env
USER_ID = "732711001" # ID пользователя, заполняется после /start
