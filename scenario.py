from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



"""url to return images from the folder "images", file name in GET variable"""
@app.route('/img')
#def img(): #-copilot next line-
def img():
    from flask import send_from_directory, abort

    # Get the filename from the query string
    filename = request.args.get('file')
    if not filename:
        abort(400, description="Missing file parameter.")

    # Only allow filenames without path separators and with safe extensions
    allowed_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}
    if (
        '/' in filename or '\\' in filename or
        not any(filename.lower().endswith(ext) for ext in allowed_extensions)
    ):
        abort(400, description="Invalid file name or extension.")

    # Use a fixed directory for images
    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

    # Ensure the file exists in the images directory
    file_path = os.path.join(images_dir, filename)
    if not os.path.isfile(file_path):
        abort(404, description="File not found.")

    # Serve the file securely
    return send_from_directory(images_dir, filename)
