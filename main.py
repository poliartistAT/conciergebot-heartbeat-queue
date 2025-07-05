import os
import asyncio
from telegram import Bot

# Konfiguration
TOKEN = "8174717147:AAFiKODunG7z174F2_KRAFPvoci_givGX_E"
CHAT_ID = 881200366  # Deine Telegram-ID
HEARTBEAT_INTERVAL = 300  # alle 5 Minuten
QUEUE_FILE = "queue.txt"

bot = Bot(TOKEN)

async def heartbeat():
    while True:
        await bot.send_message(chat_id=CHAT_ID, text="⏳ Status: Ich arbeite noch …")
        await asyncio.sleep(HEARTBEAT_INTERVAL)

async def process_queue():
    while True:
        if os.path.exists(QUEUE_FILE):
            with open(QUEUE_FILE, "r") as f:
                tasks = [line.strip() for line in f if line.strip()]
            if tasks:
                current_task = tasks.pop(0)
                await bot.send_message(chat_id=CHAT_ID, text=f"📌 Bearbeite: {current_task}")
                # hier könntest du später echte Logik ergänzen
                with open(QUEUE_FILE, "w") as f:
                    for task in tasks:
                        f.write(task + "\n")
        await asyncio.sleep(10)

async def main():
    await asyncio.gather(heartbeat(), process_queue())

if __name__ == "__main__":
    asyncio.run(main())
