# RAG Company Policy QA

## Overview

This project is a Retrieval-Augmented Generation (RAG) system designed to answer questions about company rules and internal regulations. It uses Google Gemini (via LangChain) to generate answers based strictly on the provided documents (Word, Excel, PDF) in the `document/` folder. The assistant will respond in Vietnamese, using simple and clear language, and will cite the relevant rules after each answer.

## Features

- Automatically loads and parses all `.docx`, `.xlsx`, `.xls`, and `.pdf` files from the `document/` folder and its subfolders.
- Rotates through multiple Google API keys if one fails.
- Answers are generated strictly based on the provided documents.
- Responses are translated into Vietnamese and include citations.

## Project Structure

```
rag/
├── document/                # Input documents (Word, Excel, PDF, etc.)
├── rag.py                   # Main script
├── system_prompt.py         # System prompt configuration
├── utils.py                 # Utility functions for reading files
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/CongHieuTruong/rag.git
   cd rag
   ```

2. **Install Python dependencies:**

   ```
   pip install -r requirements.txt
   ```

   _Required libraries include:_

   - langchain-google-genai
   - langchain-core
   - python-docx
   - pandas
   - openpyxl
   - PyPDF2
   - python-dotenv

3. **Prepare your documents:**

   - Place all company policy documents in the `document/` folder. You can organize them in subfolders if needed.

4. **Set up your Google API keys:**
   - Create a `.env` file in the project root:
     ```
     google_api_key=your_api_key_1,your_api_key_2,...
     ```
   - You can add multiple API keys separated by commas.

## Usage

Run the main script:

```
python rag.py
```

The assistant will load all documents, prompt for a question (you can edit the question in `rag.py`), and print the answer in Vietnamese.

## Customization

- **Change the system prompt:** Edit `system_prompt.py`.
- **Add more document types:** Extend `utils.py` with new file readers.
- **Modify questions:** Change the `question` variable in `rag.py`.

## Notes

- Make sure your documents are clear and well-formatted for best results.
- The system only answers based on the provided documents; it will not guess or use external information.

## License

MIT License
