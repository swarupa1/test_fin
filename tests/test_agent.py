import unittest
from AGENT.agent import Agent
from AGENT.retriever import Retriever
from AGENT.llm import LLM
from AGENT.embeddings import Embeddings

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = Agent()
        self.retriever = Retriever()
        self.llm = LLM()
        self.embeddings = Embeddings()

    def test_agent_initialization(self):
        self.assertIsInstance(self.agent, Agent)

    def test_retriever_initialization(self):
        self.assertIsInstance(self.retriever, Retriever)

    def test_llm_initialization(self):
        self.assertIsInstance(self.llm, LLM)

    def test_embeddings_initialization(self):
        self.assertIsInstance(self.embeddings, Embeddings)

    def test_agent_interaction(self):
        response = self.agent.interact("What is a chatbot?")
        self.assertIsInstance(response, str)

    def test_retriever_functionality(self):
        documents = self.retriever.retrieve("finance")
        self.assertIsInstance(documents, list)

    def test_llm_response_generation(self):
        response = self.llm.generate_response("Explain the role of a chatbot in finance.")
        self.assertIsInstance(response, str)

    def test_embeddings_generation(self):
        embedding = self.embeddings.generate_embedding("Sample text")
        self.assertIsInstance(embedding, list)

if __name__ == '__main__':
    unittest.main()