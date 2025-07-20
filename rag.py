import os
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from system_prompt import system_prompt  
from utils import build_transcript, load_api_keys

def get_api_keys():
    api_keys = load_api_keys()
    if not api_keys:
        raise ValueError("No valid API keys found in environment variable 'google_api_key'.")
    return api_keys

def create_prompt():
    return PromptTemplate(
        template=system_prompt + """
        {context}
        Question: {question}
        """,
        input_variables=['context', 'question']
    )

def ask_question_with_auto_key_switch(prompt, question, transcript, api_keys):
    for idx, api_key in enumerate(api_keys):
        try:
            os.environ["GOOGLE_API_KEY"] = api_key
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)
            final_prompt = prompt.invoke({"context": transcript, "question": question})
            answer = llm.invoke(final_prompt)
            print(answer.content)
            return answer.content
        except Exception as e:
            print(f"API key index {idx} failed: {e}")
            time.sleep(1)
    print("All API keys exhausted or failed.")
    return None

def main():
    api_keys = get_api_keys()
    transcript = build_transcript()
    prompt = create_prompt()
    question = "Công ty có bao nhiêu ngày nghỉ phép hằng năm?"
    # question = "Vào công ty có được kéo xì dách, làm con lô đề hay cho đồng nghiệp bốc bát họ không?"
    ask_question_with_auto_key_switch(prompt, question, transcript, api_keys)

if __name__ == "__main__":
    main()