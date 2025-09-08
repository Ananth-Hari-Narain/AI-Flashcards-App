import mysql.connector
from os import getenv
from dotenv import load_dotenv
from pathlib import Path

def get_connection():
    project_root = Path(__file__).resolve().parent.parent
    load_dotenv(dotenv_path=project_root / "file.env")

    return mysql.connector.connect(
        host="localhost",
        user=getenv("DB_USERNAME"),
        password=getenv("DB_PASSWORD"),
        database="flashcardsdb"
    )
