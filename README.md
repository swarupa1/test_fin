# finagent-app

## Overview
The FinAgent application is designed to provide a chatbot interface for financial queries. It utilizes advanced language models and document retrieval techniques to deliver accurate and relevant responses to user inquiries.

## Project Structure
```
finagent-app
├── AGENT
│   ├── __init__.py
│   ├── agent.py
│   ├── retriever.py
│   ├── llm.py
│   └── embeddings.py
├── src
│   ├── main.py
│   ├── config.py
│   └── chatbot_dev.ipynb
├── tests
│   └── test_agent.py
├── .gitignore
├── .env.example
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Installation
To set up the FinAgent application, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd finagent-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Copy `.env.example` to `.env` and fill in the necessary values.

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Testing
To run the unit tests for the AGENT package, use:
```
pytest tests/test_agent.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.