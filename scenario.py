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
    import pathlib

    # Get the filename from the query string
    filename = request.args.get('file')
    if not filename:
        abort(400, description="Missing file parameter.")

    # Prevent directory traversal attacks
    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    safe_path = pathlib.Path(images_dir) / filename
    try:
        # Resolve the path and ensure it's within the images directory
        safe_path = safe_path.resolve(strict=False)
        if not str(safe_path).startswith(str(pathlib.Path(images_dir).resolve())):
            abort(403, description="Forbidden.")
    except Exception:
        abort(400, description="Invalid file path.")

    if not safe_path.is_file():
        abort(404, description="File not found.")

    # Serve the file
    return send_from_directory(images_dir, filename)
