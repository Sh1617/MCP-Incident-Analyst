from backend.app.vectorstore.chroma_client import (
    chroma_manager
)


def search_runbooks(query: str):

    results = chroma_manager.collection.query(
        query_texts=[query],
        n_results=2
    )

    return results