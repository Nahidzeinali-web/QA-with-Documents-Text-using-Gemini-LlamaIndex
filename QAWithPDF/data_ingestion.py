from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(data_path="Data"):
    """
    Load documents from a specified directory using LlamaIndex's SimpleDirectoryReader.

    Parameters:
    - data_path (str): The path to the directory containing documents (e.g., PDFs, text).

    Returns:
    - documents: A list of loaded document objects.
    """
    try:
        logging.info("📥 Data loading started from directory: %s", data_path)
        loader = SimpleDirectoryReader(data_path)
        documents = loader.load_data()
        logging.info("✅ Data loading completed. Total documents loaded: %d", len(documents))
        return documents
    except Exception as e:
        logging.error("❌ Exception occurred while loading data.", exc_info=True)
        raise customexception(e, sys)
