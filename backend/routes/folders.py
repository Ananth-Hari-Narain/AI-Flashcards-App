from flask import Blueprint, jsonify, request
import database.folders

foldersBluePrint = Blueprint("folders", __name__)

# Adds a new folder
@foldersBluePrint.route("/folders", methods=['POST'])
def add_folder():
    data = request.get_json()
    name = data.get("Name")
    parentFolderID = data.get("parentID")

    if name is None:
        return jsonify({"error": "Folder name is missing"}), 400
    elif parentFolderID is None:
        return jsonify({"error": "Parent Folder ID is missing"}), 400

    database.folders.make_new_folder(name, parentFolderID)

# Deletes a specified folder from the database provided it is empty
@foldersBluePrint.route("/folders/<folder_id>", methods=['DELETE'])
def remove_empty_folder(folder_id):
    deleteSuccessful = database.folders.delete_empty_folder(folder_id)
    if deleteSuccessful:
        return {"message": "Folder deleted"}, 204
    else:
        return jsonify({"error": "Delete unsuccessful"}, 409)

# Get all folders in the given folder, returning the folder id and folder name
@foldersBluePrint.route("/folders/<folder_id>/children", methods=["GET"])
def get_folders_in_folder(folder_id):
    rows = database.folders.list_all_folders_in_folder(folder_id)
    all_folders = [{"id": r[0], "name": r[1]} for r in rows]
    return jsonify(all_folders)


# Get all folders in the database, returning the folder id and folder name
@foldersBluePrint.route("/folders", methods=["GET"])
def get_all_folders():
    rows = database.folders.list_all_folders()
    all_folders = [{"id": r[0], "name": r[1]} for r in rows]
    return jsonify(all_folders)

@foldersBluePrint.route("/folders/<int:folder_id>/name", methods=["PATCH"])
def rename_folder(folder_id):
    data = request.get_json()
    new_name = data.get("name")
    if not new_name:
        return jsonify({"error": "Missing name"}), 400

    database.folders.rename_folder(folder_id, new_name)
    return jsonify({"message": "Folder renamed"}), 200

@foldersBluePrint.route("/folders/<int:folder_id>/parent", methods=["PATCH"])
def change_parent_folder(folder_id):
    data = request.get_json()
    newParentID = data.get("parentFolder")
    if newParentID is None:
        return jsonify({"error": "Missing parentFolder"}), 400

    database.folders.move_folder(folder_id, newParentID)
    return jsonify({"message": "Folder moved"}), 200
