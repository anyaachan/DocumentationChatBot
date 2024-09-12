from langchain_openai import ChatOpenAI
import openai
from dotenv import load_dotenv
import os 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

RAG_TEMPLATE = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

<context>
{context}
</context>

Answer the following question:

{question}"""

question = "Name all of the schedulers in text to video stable diffusion endpoint"
model = ChatOpenAI()

rag_prompt = ChatPromptTemplate.from_template(RAG_TEMPLATE)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(collection_name="StableDiffusionAPIDocs",
    embedding_function=embeddings,
    persist_directory="chroma")

docs = vector_store.similarity_search(question)
retriever = vector_store.as_retriever()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | model
    | StrOutputParser()
)

print(chain.invoke(question))