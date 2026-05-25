import os
import asyncio
import uvicorn

from pyrogram import idle, filters

from server.client import app
from server.api import api

import plugins.start
import plugins.remove_bg


@app.on_message(filters.all)
async def debug_all(client, message):
    print(f"📩 MESSAGE RECEIVED: {message.chat.id}")


async def start_bot():
    await app.start()
    print("✅ Bot Started")
    await idle()
    await app.stop()


async def start_api():

    config = uvicorn.Config(
        app=api,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        log_level="info"
    )

    server = uvicorn.Server(config)

    await server.serve()


async def main():
    await asyncio.gather(
        start_bot(),
        start_api()
    )


if __name__ == "__main__":
    asyncio.run(main())
