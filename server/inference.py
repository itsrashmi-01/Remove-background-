from PIL import Image
from transformers import AutoModelForImageSegmentation
import torch
import torchvision.transforms as transforms
import numpy as np

from config import RMBG_MODEL_NAME

device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoModelForImageSegmentation.from_pretrained(
    RMBG_MODEL_NAME,
    trust_remote_code=True
)

model.to(device)
model.eval()

transform_image = transforms.Compose([
    transforms.Resize((1024, 1024)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

async def remove_background(input_path, output_path):

    image = Image.open(input_path).convert("RGB")

    original_size = image.size

    input_tensor = transform_image(image).unsqueeze(0).to(device)

    with torch.no_grad():
        preds = model(input_tensor)[-1].sigmoid().cpu()

    mask = preds[0].squeeze().numpy()

    mask = (mask * 255).astype(np.uint8)

    mask_image = Image.fromarray(mask).resize(original_size)

    image.putalpha(mask_image)

    image.save(output_path)
