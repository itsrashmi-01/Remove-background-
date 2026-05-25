import asyncio
import os
import uvicorn

from pyrogram import idle

from server.client import app
from server.api import api

import plugins.start
import plugins.remove_bg


async def start_bot():
    await app.start()
    print("✅ Bot Started")
    await idle()


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
