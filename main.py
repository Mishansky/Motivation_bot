import logging
import asyncio
from aiogram import Bot, Dispatcher
from bot import start_bot  # Импортируем функцию для запуска бота
from scheduler import start_scheduler  # Импортируем функцию для запуска планировщика
from config import TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Создание объекта бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Точка входа для запуска бота
async def main():
    logging.info("Бот запускается...")
    
    # Запуск планировщика задач (отправка мотивации)
    start_scheduler(bot)
    
    # Запуск бота и ожидание новых сообщений
    await start_bot(dp, bot)

if __name__ == "__main__":
    asyncio.run(main())  # Запуск асинхронного цикла
