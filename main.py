import os
import threading
import uvicorn

from server.client import app
from server.api import api

import plugins.start
import plugins.remove_bg


def run_bot():

    print("🤖 Starting Bot...")

    app.run()

    print("✅ Bot Started")


def run_api():

    print("🌐 Starting API...")

    uvicorn.run(
        api,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        log_level="info"
    )


if __name__ == "__main__":

    bot_thread = threading.Thread(target=run_bot)

    bot_thread.start()

    run_api()
