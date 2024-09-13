from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

import os
from dotenv import load_dotenv
import openai

load_dotenv()

DATA_PATH = "data"
openai.api_key = os.environ['OPENAI_API_KEY']

def load_documents():
    """Load Markdown documents into list of Document objects."""
    try: 
        loader = DirectoryLoader(DATA_PATH, glob="*.md")
        documents = loader.load()
        return documents # list of Document objects
    except Exception as e:
        print(f"Error loading documents: {e}")
        return []

def clean_repeating_data(documents: list[Document], start_string, end_string):
    """Removes the text between the first occurrence of the specified start and end strings in each document's content."""
    for document in documents:
        start_index = document.page_content.find(start_string) #find strings positions 
        end_index = document.page_content.find(end_string)
        
        if start_index != -1 and end_index != -1: # -1 -> string not found
            cleaned_content = document.page_content[:start_index] + document.page_content[end_index:]
            document.page_content = cleaned_content

def split_text(documents: list[Document]):
    """Split documents into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter( # finds best split recursively
        chunk_size=2000, # 2000 characters per chunk as the documentation is failry complex
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )

    chunks = text_splitter.split_documents(documents) # list of Document objects
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    return chunks

def save_chunks(chunks: list[Document]):
    """Save splitted document chunks with embeddings in Chroma vector store."""
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    
    vector_store = Chroma(
        collection_name="StableDiffusionAPIDocs",
        embedding_function=embeddings,
        persist_directory="chroma", 
    )

    vector_store.add_documents(chunks)
    return vector_store

def main():
    documents = load_documents()
    if documents: 
        clean_repeating_data(documents, "Stable Diffusion API Documentation", "On this page")
        chunks = split_text(documents)
        save_chunks(chunks)

if __name__ == "__main__":
    main()