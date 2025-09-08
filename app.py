from flask import Flask
from routes import foldersBluePrint, flashcardSetsBluePrint, flashcardsBluePrint

app = Flask(__name__)
app.register_blueprint(foldersBluePrint, url_prefix="/api")
app.register_blueprint(flashcardsBluePrint, url_prefix="/api")
app.register_blueprint(flashcardSetsBluePrint, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
