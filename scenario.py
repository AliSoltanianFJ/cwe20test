from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



"""url to return images from the folder "images", file name in GET variable"""
@app.route('/img')
#def img(): #-copilot next line-
def img():
    from flask import send_from_directory

    filename = request.args.get('file')
    if not filename:
        return "No file specified", 400

    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    # Only allow files that exist in the images directory
    if not os.path.isfile(os.path.join(images_dir, filename)):
        return "File not found", 404

    return send_from_directory(images_dir, filename)
