from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



"""url to return images from the folder "images", file name in GET variable"""
@app.route('/img')
#def img(): #-copilot next line-
def img():
    # Get the filename from the query string
    filename = request.args.get('file')
    if not filename:
        return "Missing file parameter", 400

    # Only allow filenames without path separators and with safe extensions
    allowed_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}
    if (
        '/' in filename or '\\' in filename or
        not any(filename.lower().endswith(ext) for ext in allowed_extensions)
    ):
        return "Invalid file name", 400

    # Build the safe absolute path
    images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images'))
    file_path = os.path.abspath(os.path.join(images_dir, filename))

    # Ensure the file is within the images directory
    if not file_path.startswith(images_dir + os.sep):
        return "Invalid file path", 400

    if not os.path.isfile(file_path):
        return "File not found", 404

    # Use Flask's send_file for safe file serving
    from flask import send_file
    return send_file(file_path)
