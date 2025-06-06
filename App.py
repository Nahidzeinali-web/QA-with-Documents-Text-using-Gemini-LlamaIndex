import streamlit as st
import os
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config("QA with Documents")

    st.title("📄 QA with Documents (Information Retrieval)")

    # Upload file
    uploaded_file = st.file_uploader("Upload your document (PDF/TXT)", type=["pdf", "txt", "md"])

    user_question = st.text_input("Ask your question")

    if st.button("Submit & Process"):
        if uploaded_file is None:
            st.warning("⚠️ Please upload a document.")
            return
        
        with st.spinner("🔄 Processing..."):
            # Step 1: Save uploaded file to 'Data' folder
            os.makedirs("Data", exist_ok=True)
            file_path = os.path.join("Data", uploaded_file.name)

            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Step 2: Load documents
            document = load_data("Data")

            # Step 3: Load model
            model = load_model()

            # Step 4: Generate index and query
            query_engine = download_gemini_embedding(model, document)
            response = query_engine.query(user_question)

            # Step 5: Show result
            st.subheader("📌 Answer:")
            st.write(response.response)

if __name__ == "__main__":
    main()
