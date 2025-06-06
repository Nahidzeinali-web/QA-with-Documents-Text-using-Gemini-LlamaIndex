import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
import google.generativeai as genai

from exception import customexception
from logger import logging

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Google Gemini SDK
genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        logging.info("🚀 Initializing Gemini LLM model (gemini-pro)...")
        model = Gemini(models="gemini-pro", api_key=GOOGLE_API_KEY)
        logging.info("✅ Gemini LLM model loaded successfully.")
        return model
    except Exception as e:
        logging.error("❌ Failed to load Gemini model.", exc_info=True)
        raise customexception(e, sys)
