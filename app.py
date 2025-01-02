import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# Initialize the Stable Diffusion pipeline
@st.cache_resource
def load_pipeline(api_token):
    """
    Load the Stable Diffusion pipeline using the provided Hugging Face API token.
    Caches the pipeline for reuse across app reruns.
    """
    try:
        pipeline = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            use_auth_token=API_TOKEN
        )
        device = "cuda" if torch.cuda.is_available() else "cpu"
        pipeline.to(device)
        return pipeline
    except Exception as e:
        st.error(f"Failed to load the Stable Diffusion pipeline: {e}")
        st.stop()

# Generate the image
def generate_image(pipeline, prompt):
    """
    Generate an image using the Stable Diffusion pipeline.
    """
    try:
        with st.spinner("Generating image..."):
            image = pipeline(prompt).images[0]
        return image
    except Exception as e:
        st.error(f"Image generation failed: {e}")
        return None

# Streamlit app
def main():
    st.title("Stable Diffusion Image Generator")
    st.markdown("Enter a prompt to generate an image using Stable Diffusion.")

    # Check if the API token is available
    if not API_TOKEN:
        st.error("Hugging Face API token is missing. Please add it to the .env file.")
        st.stop()

    # Prompt input
    prompt = st.text_area("Enter your image description:", placeholder="e.g., a futuristic cityscape at night with flying cars")
    
    # Generate button
    if st.button("Generate Image"):
        pipeline = load_pipeline(API_TOKEN)  # Load the pipeline (cached)
        if prompt:
            image = generate_image(pipeline, prompt)
            if image:
                st.image(image, caption="Generated Image", use_column_width=True)
        else:
            st.warning("Please enter a prompt to generate an image.")

if __name__ == "__main__":
    main()
