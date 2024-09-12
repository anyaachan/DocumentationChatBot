from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import os
import pylibmagic
import magic
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import openai

load_dotenv()

DATA_PATH = "data"
openai.api_key = os.environ['OPENAI_API_KEY']

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents # list of Document objects

def clean_repeating_data(documents: list[Document]):
    for document in documents:
        start_index = document.page_content.find("Stable Diffusion API Documentation") #find strings positions 
        end_index = document.page_content.find("On this page")

        if start_index != -1 and end_index != -1: # -1 if the string is not found 
            cleaned_content = document.page_content[:start_index] + document.page_content[end_index:]
            document.page_content = cleaned_content

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter( # recommended splitter for generic text
        chunk_size=2000, # 1500 characters per chunk as the documentation is failry complex
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )

    chunks = text_splitter.split_documents(documents) # list of Document objects
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    return chunks

def save_chunks(chunks: list[Document]):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    
    vector_store = Chroma(
    collection_name="StableDiffusionAPIDocs",
    embedding_function=embeddings,
    persist_directory="chroma",  # Where to save data locally, remove if not neccesary
    )

    vector_store.add_documents(chunks)
    print(f"Saved {len(chunks)} chunks.")
    return vector_store

def main():
    documents = load_documents()
    clean_repeating_data(documents)
    chunks = split_text(documents)
    save_chunks(chunks)


if __name__ == "__main__":
    main()