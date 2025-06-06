from llama_index.core import VectorStoreIndex
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.settings import Settings

import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(model, documents):
    """
    Initializes Gemini Embedding and builds a VectorStoreIndex using LlamaIndex Settings API.

    Parameters:
    - model: LLM instance
    - documents: List of loaded documents

    Returns:
    - query_engine: Configured query engine
    """
    try:
        logging.info("🔄 Initializing Gemini embedding model...")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")

        logging.info("⚙️ Applying global settings...")
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        logging.info("📦 Building VectorStoreIndex from documents...")
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist()

        logging.info("✅ Index created and query engine initialized.")
        query_engine = index.as_query_engine()
        return query_engine

    except Exception as e:
        logging.error("❌ Error in embedding setup.", exc_info=True)
        raise customexception(e, sys)
