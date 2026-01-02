import os
import sys
from pathlib import Path



project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from AGENT.agent import Agent

def main():
    # Initialize the agent
    agent = Agent()

    # Start the chatbot or application logic
    print("Welcome to the FinAgent Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Goodbye!")
            break
        response = agent.handle_query(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()