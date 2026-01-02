class SimpleRetriever:
    """Very small fallback retriever used when none is provided."""
    def retrieve(self, query: str) -> str:
        # Simple heuristic: return a short context that echoes the query
        return f"Context for query: {query}"


class SimpleLLM:
    """Very small fallback LLM used when none is provided."""
    def generate_response(self, context: str, query: str) -> str:
        # Simple echoing response; replace with real LLM call in production
        return f"I received your question: '{query}'. Context used: '{context}'"


class Agent:
    def __init__(self, retriever=None, llm=None):
        # Use provided components or fall back to simple defaults so Agent can be
        # instantiated without extra wiring for quick testing.
        self.retriever = retriever or SimpleRetriever()
        self.llm = llm or SimpleLLM()

    def interact(self, user_query):
        # Retrieve relevant context based on the user query
        context = self.retriever.retrieve(user_query)

        # Generate a response using the language model
        response = self.llm.generate_response(context, user_query)

        return response

    def handle_query(self, user_query):
        """Compatibility wrapper used by src/main.py"""
        return self.interact(user_query)

    def run_chat(self):
        print("Welcome to the AGENT Chatbot. Type 'exit' to end the conversation.")
        while True:
            user_query = input("You: ")
            if user_query.lower() in ["exit", "quit"]:
                break
            response = self.handle_query(user_query)
            print(f"Agent: {response}")