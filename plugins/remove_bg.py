from pyrogram import filters
from server.client import app

from plugins.utils import generate_filename, cleanup_file
from server.inference import remove_background

@app.on_message(filters.photo)
async def remove_bg_handler(client, message):

    status = await message.reply_text(
        "✂️ Removing background..."
    )

    input_path = generate_filename("jpg")
    output_path = generate_filename("png")

    try:

        photo = await message.download(file_name=input_path)

        await remove_background(photo, output_path)

        await message.reply_document(
            document=output_path,
            caption="✨ Background removed successfully."
        )

        await status.delete()

    except Exception as e:

        await status.edit_text(
            f"❌ Error:\n`{str(e)}`"
        )

    finally:
        cleanup_file(input_path)
        cleanup_file(output_path)
