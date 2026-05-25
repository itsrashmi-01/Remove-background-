import asyncio
import uvicorn

from server.client import app
from server.api import api

import plugins.start
import plugins.remove_bg

async def start_services():

    bot_task = asyncio.create_task(app.start())

    api_config = uvicorn.Config(
        api,
        host="0.0.0.0",
        port=10000,
        log_level="info"
    )

    api_server = uvicorn.Server(api_config)

    api_task = asyncio.create_task(api_server.serve())

    await asyncio.gather(bot_task, api_task)

if __name__ == "__main__":
    asyncio.run(start_services())
