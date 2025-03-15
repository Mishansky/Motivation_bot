from aiogram import Dispatcher, types
from aiogram.filters import CommandStart

async def start_handler(message: types.Message):
    """Обработка команды /start"""
    await message.answer("Привет! Я буду присылать тебе мотивационные сообщения каждый день!")

async def start_bot(dp: Dispatcher, bot):
    """Запуск бота и регистрация хэндлеров"""
    dp.message.register(start_handler, CommandStart())  # Регистрируем хэндлер на команду /start
    
    # Запуск бота
    await dp.start_polling(bot)
