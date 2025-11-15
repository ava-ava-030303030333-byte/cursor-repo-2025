import os
from dotenv import load_dotenv

load_dotenv()

# Токен Telegram бота
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    # Для тестов можно временно вписать сюда токен (не коммить!)
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_TOKEN_HERE"

# Путь к JSON файлу с регистрациями
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'registrations.json')

# Приветственное сообщение
WELCOME_MESSAGE = "Привет! Я - бот регистрации на мероприятие."
