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

    filename = request.args.get('file')
    if not filename:
        return "No file specified", 400

    # Only allow files with specific image extensions
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
    ext = filename.rsplit('.', 1)[-1].lower()
    if ext not in allowed_extensions:
        return "Unsupported file type", 400

    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    try:
        # Only serve files from the images directory
        return send_from_directory(images_dir, filename)
    except Exception:
        abort(404)
