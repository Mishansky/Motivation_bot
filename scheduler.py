import random
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from messages import motivational_quotes  # Список мотивационных сообщений
from config import USER_ID  # ID пользователя для отправки сообщений

# Инициализация планировщика
scheduler = AsyncIOScheduler()

async def send_motivation(bot):
    """Функция для отправки мотивационного сообщения"""
    if USER_ID:  # Проверяем, что ID пользователя установлен
        message = random.choice(motivational_quotes)  # Случайное сообщение
        await bot.send_message(USER_ID, message)  # Отправляем сообщение

def start_scheduler(bot):
    """Настройка и запуск планировщика задач"""
    # Отправлять мотивационное сообщение каждые 24 часа
    scheduler.add_job(send_motivation, IntervalTrigger(seconds=15), args=[bot])
    scheduler.start()  # Запуск планировщика
