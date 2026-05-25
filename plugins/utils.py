import os
import uuid

def generate_filename(extension="png"):
    return f"temp/{uuid.uuid4().hex}.{extension}"

def cleanup_file(path):
    if os.path.exists(path):
        os.remove(path)
