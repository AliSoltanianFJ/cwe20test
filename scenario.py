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

    # Validate: Only allow safe filenames (no path traversal, no special chars)
    if not filename or '/' in filename or '\\' in filename or filename.startswith('.'):
        abort(400, description="Invalid filename.")

    # Use werkzeug's secure_filename to sanitize the filename
    filename = werkzeug.utils.secure_filename(filename)

    # Only allow certain image extensions
    allowed_exts = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
    ext = filename.rsplit('.', 1)[-1].lower()
    if ext not in allowed_exts:
        abort(400, description="Invalid file extension.")

    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

    # Check if file exists in the images directory
    file_path = os.path.join(images_dir, filename)
    if not os.path.isfile(file_path):
        abort(404, description="File not found.")

    # Serve the file securely
    return send_from_directory(images_dir, filename)
