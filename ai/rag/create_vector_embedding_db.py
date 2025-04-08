import os
import shutil
from config import env, logger

from langchain_chroma import Chroma
from langchain.schema import Document
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



def load_documents() -> list[Document]:
    loader = DirectoryLoader(env.data_path, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    logger.info(f"Split {len(documents)} documents into {len(chunks)} chunks")
    return chunks


def save_to_chroma(chunks: list[Document]):
    if os.path.exists(env.chroma_path):
        shutil.rmtree(env.chroma_path)

    db = Chroma.from_documents(
        chunks,
        embedding=OpenAIEmbeddings(api_key=env.openai_api_key),
        persist_directory=env.chroma_path,
    )
    logger.info(f"Saved {len(chunks)} chunks to {env.chroma_path}")


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)    


if __name__ == "__main__":
    generate_data_store()