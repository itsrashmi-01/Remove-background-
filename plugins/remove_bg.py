from pyrogram import filters

from server.client import app

from plugins.utils import generate_filename, cleanup_file
from server.inference import remove_background

print("✅ remove_bg plugin loaded")


@app.on_message(filters.photo | filters.document.image)
async def remove_bg_handler(client, message):

    print("🔥 REMOVE BG TRIGGERED")

    status = await message.reply_text(
        "✂️ Removing background..."
    )

    input_path = generate_filename("jpg")
    output_path = generate_filename("png")

    try:

        downloaded_file = await message.download(
            file_name=input_path
        )

        await remove_background(
            downloaded_file,
            output_path
        )

        await message.reply_document(
            document=output_path,
            caption="✨ Background removed successfully."
        )

        await status.delete()

    except Exception as e:

        print(f"❌ ERROR: {e}")

        await status.edit_text(
            f"❌ Error:\n`{str(e)}`"
        )

    finally:
        cleanup_file(input_path)
        cleanup_file(output_path)
