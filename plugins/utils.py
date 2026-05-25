import os
import uuid


def generate_filename(extension="png"):

    os.makedirs("temp", exist_ok=True)

    return f"temp/{uuid.uuid4().hex}.{extension}"


def cleanup_file(path):

    if path and os.path.exists(path):
        os.remove(path)
