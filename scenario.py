from flask import request, send_from_directory, abort
from werkzeug.utils import secure_filename
import os

def img():
    filename = request.args.get('file')
    if not filename:
        return "No file specified", 400

    # Sanitize the filename
    safe_filename = secure_filename(filename)
    if not safe_filename:
        return "Invalid file name", 400

    image_dir = os.path.join(os.path.dirname(__file__), 'images')
    image_path = os.path.join(image_dir, safe_filename)

    # Ensure the file exists in the images directory
    if not os.path.isfile(image_path):
        return "File not found", 404

    # Only serve files from the images directory
    return send_from_directory(image_dir, safe_filename)
