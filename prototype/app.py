import gradio as gr
from io import BytesIO

from torch import autocast
import requests
import PIL
import torch
from diffusers import StableDiffusionInpaintPipeline as StableDiffusionInpaintPipeline

pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    revision="fp16",
    torch_dtype=torch.float16,
    use_auth_token=True,
)


def process_image(dict, prompt):
    init_img = dict["image"].convert("RGB").resize((512, 512))
    mask_img = dict["mask"].convert("RGB").resize((512, 512))
    images = pipe(
        prompt=prompt, init_image=init_img, mask_image=mask_img, strength=0.75
    )["sample"]
    return images[0]


iface = gr.Interface(
    fn=process_image,
    title="Stable Diffusion In-Painting Tool on Colab with Gradio",
    inputs=[
        gr.Image(source="upload", tool="sketch", type="pil"),
        gr.Textbox(label="prompt"),
    ],
    outputs=[gr.Image()],
    description="Choose a feature and upload an image to see the processed result.",
    article="<p style='text-align: center;'>Built with Gradio</p>",
)


iface.launch()
