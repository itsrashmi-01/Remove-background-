from rembg import remove


print("📦 Loading Rembg Model...")


async def remove_background(input_path, output_path):

    with open(input_path, "rb") as input_file:
        input_data = input_file.read()

    output_data = remove(
        input_data,
        model_name="isnet-general-use"
    )

    with open(output_path, "wb") as output_file:
        output_file.write(output_data)

    return output_path


print("✅ Rembg Ready")
