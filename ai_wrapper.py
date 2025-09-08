from google import genai
from os import getenv
from dotenv import load_dotenv

load_dotenv("file.env")

def auto_generate_answer(term: str, subject, length="brief", underlineKeyWords=False) -> str:
    """
    Uses an LLM API
    :return: answer to a question or give a definition to a term.
    """
    client = genai.Client(api_key=getenv("GEMINI_API_KEY"))
    chat = client.chats.create(model="gemini-2.5-flash")
    prompt = f"Flashcard answer {subject}:{term}[{length}, no #s/links]"
    response = chat.send_message(prompt).text
    if underlineKeyWords:
        keywords = chat.send_message("List only most relevant keywords, separate by ;").text
        keywords = keywords.replace("; ", ";")
        for keyword in keywords.lower().split(";"):
            response = response.replace(keyword, f"_{keyword}_", -1)

    return response

def check_answer_is_correct(user_answer, actual_answer) -> bool:
    """
    Uses an LLM API to determine if an answer given by a user matches the answer
    given by the flashcards.
    """
    client = genai.Client(api_key=getenv("GEMINI_API_KEY"))
    chat = client.chats.create(model="gemini-2.5-flash")
    prompt = f'yes or no: does "{user_answer}" match the real answer: "{actual_answer}"'
    response = chat.send_message(prompt).text
    response.removesuffix(".")
    return response.lower() == "yes"
