import os
from huggingface_hub import InferenceClient

def initialize_huggingface_client():
    """Initialize the Hugging Face client."""
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    if not HUGGINGFACE_API_KEY:
        raise ValueError("Please set your HUGGINGFACE_API_KEY in the .env file.")
    
    MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.3"
    return InferenceClient(model=MODEL_NAME, token=HUGGINGFACE_API_KEY)