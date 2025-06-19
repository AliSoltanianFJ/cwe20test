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
    import werkzeug.utils

    # Get the filename from the query string
    filename = request.args.get('file', '')

    # Validate: Only allow filenames with safe characters, no path traversal
    if not filename or '/' in filename or '\\' in filename or filename.startswith('.'):
        abort(400, description="Invalid filename.")

    # Only allow specific image extensions
    allowed_exts = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}
    _, ext = os.path.splitext(filename)
    if ext.lower() not in allowed_exts:
        abort(400, description="Invalid file extension.")

    # Sanitize filename
    filename = werkzeug.utils.secure_filename(filename)

    images_dir = os.path.join(os.path.dirname(__file__), 'images')

    # Check if file exists in the images directory
    file_path = os.path.join(images_dir, filename)
    if not os.path.isfile(file_path):
        abort(404, description="File not found.")

    # Serve the file securely
    return send_from_directory(images_dir, filename)
