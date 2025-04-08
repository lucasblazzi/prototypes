import argparse

from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_openai.embeddings import OpenAIEmbeddings


from config import env


PROMPT_TEMPLATE = """"
You are a helpful assistant. Use the following context to answer the question.

Context: {context}

Question: {question}

Answer:
"""


def get_context(query):
    embeddings = OpenAIEmbeddings(api_key=env.openai_api_key)
    db = Chroma(
        embedding_function=embeddings,
        persist_directory=env.chroma_path,
    )

    results = db.similarity_search_with_relevance_scores(query, k=5)

    if len(results) == 0 or results[0][1] < env.similarity_threshold:
        print("No results found.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    return context_text, results


def get_answer(context, query, similarity_search):
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(question=query, context=context)

    model = ChatOpenAI(
        openai_api_key=env.openai_api_key
    )
    response = model.invoke(prompt)
    sources = [docs.metadata.get("source") for docs, _score in similarity_search]
    formatted_response = f"Answer: {response.content}\n\nSources:\n" + "\n".join(sources)
    return formatted_response


def handler():
    parser = argparse.ArgumentParser(description="Query the RAG system")
    parser.add_argument("query", type=str, help="The query string")
    args = parser.parse_args()
    query = args.query

    context, similarity_search = get_context(query)
    answer = get_answer(context, query, similarity_search)
    print(answer)


if __name__ == "__main__":
    handler()