from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import pylibmagic
import magic

DATA_PATH = "data"

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md", use_multithreading=True)
    documents = loader.load()
    return documents # list of Document objects

def clean_repeating_data(documents: list[Document]):
    for document in documents:
        start_index = document.page_content.find("Stable Diffusion API Documentation") #find strings positions 
        end_index = document.page_content.find("On this page")

        if start_index != -1 and end_index != -1: # -1 if the sting is not found 
            cleaned_content = document.page_content[:start_index] + document.page_content[end_index:]
            document.page_content = cleaned_content

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter( # recommended splitter for generic text
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[5]
    print(document.page_content)
    print(document.metadata)

    return chunks

def main():
    documents = load_documents()
    clean_repeating_data(documents)
    split_text(documents)
    
if __name__ == "__main__":
    main()