import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_ID = int(os.getenv("OWNER_ID", "0"))

MAX_IMAGE_SIZE = 10 * 1024 * 1024

TEMP_DIR = "temp"

RMBG_MODEL_NAME = "briaai/RMBG-2.0"
