from langchain_openai import ChatOpenAI
import openai
from dotenv import load_dotenv
import os 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

model = ChatOpenAI()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

question = "What is image to image API?"
follow_up_question = "What are the schedulers avaliable for it?"

# setup chat history
chat_history = []

rag_prompt = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.\

{context}"""

# rephrasing follow-up questions to match with the context
contextualize_system_prompt =  (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

rag_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", rag_prompt),
        MessagesPlaceholder("chat_history"),
        ("user", "{input}"), # question
    ]
)

# load vector store
vector_store = Chroma(collection_name="StableDiffusionAPIDocs",
    embedding_function=embeddings,
    persist_directory="chroma")
retriever = vector_store.as_retriever()

contextualize_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("user", "{input}"), # question
    ]
)

# incorporate chat history into the retrieval process
history_aware_retriever = create_history_aware_retriever(
    model, retriever, contextualize_prompt
)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

question_answer_chain = create_stuff_documents_chain(model, rag_prompt)
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

def ask_question(chain, question, chat_history):
    return chain.invoke({"input": question, "chat_history": chat_history})

def update_chat_history(chat_history, question, answer):
    chat_history.append(HumanMessage(content=question))
    chat_history.append(HumanMessage(content=answer))

answer_01 = ask_question(rag_chain, question, chat_history)
update_chat_history(chat_history, question, answer_01["answer"])

answer_02 = ask_question(rag_chain, follow_up_question, chat_history)
update_chat_history(chat_history, follow_up_question, answer_02["answer"])

print(answer_01["answer"])
print(answer_02["answer"])
