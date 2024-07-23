import asyncio
from config.settings import bot

def send_telegram_message(chat_id, text):
    async def send_message():
        await bot.send_message(chat_id=chat_id, text=text)
    asyncio.run(send_message())


