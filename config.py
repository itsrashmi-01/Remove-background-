import os

from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

HF_TOKEN = os.getenv("HF_TOKEN")

RMBG_MODEL_NAME = "briaai/RMBG-2.0"
