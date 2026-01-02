import os

class Config:
    def __init__(self):
        self.API_KEY = os.getenv("API_KEY", "your_api_key_here")
        self.MODEL_NAME = os.getenv("MODEL_NAME", "default_model")
        self.EMBEDDING_DIM = int(os.getenv("EMBEDDING_DIM", 768))
        self.RETRIEVER_K = int(os.getenv("RETRIEVER_K", 5))
        self.CHATBOT_CONTEXT = os.getenv("CHATBOT_CONTEXT", "Your context here")

    def display_config(self):
        print(f"API_KEY: {self.API_KEY}")
        print(f"MODEL_NAME: {self.MODEL_NAME}")
        print(f"EMBEDDING_DIM: {self.EMBEDDING_DIM}")
        print(f"RETRIEVER_K: {self.RETRIEVER_K}")
        print(f"CHATBOT_CONTEXT: {self.CHATBOT_CONTEXT}")