from rembg import remove


async def remove_background(input_path, output_path):

    print("✂️ Processing Image...")

    with open(input_path, "rb") as input_file:
        input_data = input_file.read()

    output_data = remove(input_data)

    with open(output_path, "wb") as output_file:
        output_file.write(output_data)

    print("✅ Background Removed")

    return output_path
