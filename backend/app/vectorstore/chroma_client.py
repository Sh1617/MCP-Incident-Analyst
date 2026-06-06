import chromadb


class ChromaClientManager:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="runbooks"
        )


chroma_manager = ChromaClientManager()