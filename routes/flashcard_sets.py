from flask import Blueprint, request, jsonify
import database.flashcard_sets

flashcardSetsBluePrint = Blueprint("flashcard_sets", __name__)

@flashcardSetsBluePrint.route("/flashcard-sets", methods=["GET"])
def list_flashcard_sets():
    rows = database.flashcard_sets.list_all_flashcard_sets()
    sets = [{"id": r[0], "name": r[1]} for r in rows]
    return jsonify(sets), 200

@flashcardSetsBluePrint.route("/folders/<int:folder_id>/flashcard-sets", methods=["GET"])
def list_flashcard_sets_in_folder(folderID):
    rows = database.flashcard_sets.list_all_flashcard_sets_in_folder(folderID)
    sets = [{"id": r[0], "name": r[1]} for r in rows]
    return jsonify(sets), 200

@flashcardSetsBluePrint.route("/folders/<int:folder_id>/flashcard-sets", methods=["POST"])
def create_flashcard_set(folderID):
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Missing 'name' field"}), 400

    database.flashcard_sets.make_new_flashcard_set(name, folderID)
    return jsonify({"message": "Flashcard set created"}), 201


@flashcardSetsBluePrint.route("/flashcard-sets/<int:set_id>/name", methods=["PATCH"])
def rename_flashcard_set(setID):
    data = request.get_json()
    new_name = data.get("name")

    if not new_name:
        return jsonify({"error": "Missing 'name' field"}), 400

    database.flashcard_sets.rename_flashcard_set(setID, new_name)
    return jsonify({"message": "Flashcard set renamed"}), 200

@flashcardSetsBluePrint.route("/flashcard-sets/<int:set_id>/folder")
def move_flashcard_set(setID):
    data = request.get_json()
    new_folder_id = data.get("folderID")

    if new_folder_id is None:
        return jsonify({"error": "Missing 'folderID' field"}), 400

    database.flashcard_sets.move_flashcard_set(setID, new_folder_id)

    return jsonify({"message": "Flashcard set moved"}), 200

@flashcardSetsBluePrint.route("/flashcard-sets/<int:set_id>", methods=["DELETE"])
def delete_flashcard_set(setID):
    database.flashcard_sets.delete_flashcard_set(setID)
    return "", 204

