from telegram import Bot
import asyncio

async def main():
    bot = Bot("8174717147:AAFiKODunG7z174F2_KRAFPvoci_givGX_E")
    async with bot:
        print(await bot.get_me())

asyncio.run(main())
