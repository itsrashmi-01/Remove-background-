from pyrogram import filters

from server.client import app

print("✅ start plugin loaded")


@app.on_message(filters.command("start"))
async def start_handler(client, message):

    text = """
🌌 Welcome to Creator Cut AI

✂️ AI Background Remover

Send any image to remove background.
"""

    await message.reply_text(text)
