from dotenv import load_dotenv
import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

load_dotenv()

CHROMA_DIR = "data/rag_store"

def build_rag_pipeline(source_folder="data/converted"):
    all_docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    embeddings = OpenAIEmbeddings()

    for filename in os.listdir(source_folder):
        if filename.endswith(".txt"):
            try:
                loader = TextLoader(os.path.join(source_folder, filename), encoding="utf-8")
                docs = loader.load()
                chunks = splitter.split_documents(docs)
                all_docs.extend(chunks)
            except Exception as e:
                print(f"❌ Skipped {filename} due to error: {e}")

    vectordb = Chroma.from_documents(
        documents=all_docs,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    rag_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        retriever=retriever,
        return_source_documents=True
    )

    return rag_chain
