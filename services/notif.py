from aiogram import Bot
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)


async def send_notification(user_id: int, img_url: str, mes_text: str):
    await bot.send_photo(chat_id=user_id, photo=img_url, caption=mes_text)
