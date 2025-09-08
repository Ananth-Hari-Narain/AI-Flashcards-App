from flask import Blueprint, request, jsonify
import database.flashcards

flashcardsBluePrint = Blueprint("flashcards", __name__)

@flashcardsBluePrint.route("/flashcard-sets/<int:setID>/flashcards", methods=["GET"])
def list_flashcards_in_set(setID):
    rows = database.flashcards.list_flashcards_in_set(setID)
    cards = [{"id": r[0], "term": r[1], "definition": r[2]} for r in rows]
    return jsonify(cards), 200

@flashcardsBluePrint.route("/flashcard-sets/<int:setID>/flashcards", methods=["POST"])
def create_flashcard(setID):
    data = request.get_json()
    term = data.get("term")
    definition = data.get("definition")
    if not term or not definition:
        return jsonify({"error": "Missing 'term' or 'definition'"}), 400
    database.flashcards.add_flashcard(term, definition, setID)
    return jsonify({"message": "Flashcard created"}), 201

@flashcardsBluePrint.route("/flashcards/<int:cardID>/term", methods=["PATCH"])
def update_flashcard_term(cardID):
    data = request.get_json()
    new_term = data.get("term")
    if not new_term:
        return jsonify({"error": "Missing 'term'"}), 400
    database.flashcards.change_flashcard_term(cardID, new_term)
    return jsonify({"message": "Flashcard term updated"}), 200

@flashcardsBluePrint.route("/flashcards/<int:cardID>/definition", methods=["PATCH"])
def update_flashcard_definition(cardID):
    data = request.get_json()
    new_definition = data.get("definition")
    if not new_definition:
        return jsonify({"error": "Missing 'definition'"}), 400
    database.flashcards.change_flashcard_definition(cardID, new_definition)
    return jsonify({"message": "Flashcard definition updated"}), 200

@flashcardsBluePrint.route("/flashcards/<int:cardID>", methods=["DELETE"])
def delete_flashcard(cardID):
    database.flashcards.delete_flashcard(cardID)
    return "", 204
