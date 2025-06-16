import asyncio
from aiogram import Bot
from config import BOT_TOKEN, WEBHOOK_URL  # make sure you have these

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.set_webhook(WEBHOOK_URL)
    print("✅ Webhook set")

if __name__ == "__main__":
    asyncio.run(main())
