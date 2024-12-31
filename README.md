# Stable Diffusion Image Generator

This Streamlit application generates images based on text prompts using the Stable Diffusion model. The app utilizes the Hugging Face `diffusers` library and can run on both CPU and GPU.

## Features

- Load and cache the Stable Diffusion pipeline for efficient reuse
- Generate images from text prompts
- Display generated images within the app

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/stable-diffusion-image-generator.git
    cd stable-diffusion-image-generator
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables by creating a `.env` file and adding your Hugging Face API key:

    ```env
    HUGGINGFACE_API_KEY=your_huggingface_api_key_here
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Enter a prompt in the text area and click "Generate Image" to create an image.

## Code Overview

### Main Application

The main application is contained in `app.py` and includes:

- `load_pipeline`: Loads the Stable Diffusion pipeline using the Hugging Face API token. The pipeline is cached for reuse across app reruns.
- `generate_image`: Generates an image based on the provided text prompt using the Stable Diffusion pipeline.
- `main`: Sets up the Streamlit interface, handles user inputs, and displays generated images.

### Additional Files

- `requirements.txt`: Lists all the dependencies needed for the project.
- `.env`: Contains the environment variables, specifically the Hugging Face API key.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Hugging Face](https://huggingface.co/)
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion)
- [Diffusers](https://github.com/huggingface/diffusers)

Feel free to fork this repository and customize it to suit your needs. Contributions are welcome!
