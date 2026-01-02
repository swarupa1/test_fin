class Retriever:
    def __init__(self, document_store):
        self.document_store = document_store

    def retrieve(self, query, top_k=5):
        """
        Retrieve the top_k relevant documents based on the query.
        
        Args:
            query (str): The query string to search for.
            top_k (int): The number of top relevant documents to retrieve.
        
        Returns:
            list: A list of retrieved documents.
        """
        # Implement the retrieval logic here
        # This is a placeholder for the actual retrieval implementation
        relevant_documents = self.document_store.search(query, top_k)
        return relevant_documents