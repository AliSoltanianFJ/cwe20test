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
    if filename:
        file_path = os.path.join('images', filename)
        if os.path.exists(file_path):
            return redirect(file_path)
    return "Image not found", 404
