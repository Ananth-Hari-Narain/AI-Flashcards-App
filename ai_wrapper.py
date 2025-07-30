from google import genai
from os import getenv

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
        keywords = chat.send_message("List relevant keywords, separate by ;").text
        keywords = keywords.replace("; ", ";")
        for keyword in keywords.lower().split(";"):
            response = response.replace(keyword, f"_{keyword}_", -1)

    return response

def auto_generate_key_():
    """
    Uses an NLP to generate tags to determine the topics
    of a particular flashcard set
    :return:
    """
    pass

def check_answer_is_correct() -> bool:
    """
    Uses an NLP API to determine if an answer given by a user matches the answer
    given by the flashcards.
    """
    pass


print(auto_generate_answer("What is the purpose of the status register?", "CS A-Level", "brief", True))