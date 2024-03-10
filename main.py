import asyncio
from aiogram import Bot, Dispatcher
from handlers import user_commands, bot_messages, quest
from config_reader import config





async def main():
    bot=Bot(config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        bot_messages.router,
        quest.router

    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
