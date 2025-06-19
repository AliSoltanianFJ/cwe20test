from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



"""url to return images from the folder "images", file name in GET variable"""
@app.route('/img')
#def img(): #-copilot next line-
def img():
    filename = request.args.get('file')
    if not filename:
        return "No file specified", 400
    filepath = os.path.join('images', filename)
    if not os.path.exists(filepath):
        return "File not found", 404
    # Ensure the path is safe and does not allow directory traversal
    if '..' in filepath or os.path.isabs(filepath):
        return "Invalid file path", 400
    return redirect(f'/static/{filepath}', code=302)
