from flask import Flask, request, redirect, make_response
import os
import re
import pickle
import hashlib

app = Flask(__name__)

@app.route('/redirect')
def open_redirect():
    target = request.args.get('url', '')
    if "example.com" in target:  # CWE-020: Incomplete URL sanitization
        return redirect(target)   # CWE-601: Open redirect
    return redirect('/')

@app.route('/insecure-hash')
def insecure_hash():
    password = request.args.get('password', '')
    hash = hashlib.md5(password.encode()).hexdigest()  # CWE-327: Use of weak hash function
    return f"Hash: {hash}"

@app.route('/deserialize')
def unsafe_deserialization():
    data = request.args.get('data', '')
    obj = pickle.loads(bytes(data, 'utf-8'))  # CWE-502: Unsafe deserialization
    return str(obj)

@app.route('/command')
def command_injection():
    filename = request.args.get('filename', '')
    os.system(f"ls {filename}")  # CWE-78: Command injection
    return "Command executed."

@app.route('/cookie')
def insecure_cookie():
    resp = make_response("Here's a cookie")
    resp.set_cookie("session", "abc123")  # CWE-614: Failure to set secure cookie flags
    return resp
