from pyrogram import Client

from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "rmbg_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=20,
    sleep_threshold=30
)
