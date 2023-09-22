from flask import Flask, request, render_template_string
import sqlite3
import os
import pickle

app = Flask(__name__)

# Hardcoded Secrets
SECRET_API_KEY = "my_super_secret_api_key"

@app.route('/')
def index():
    return "Welcome to the vulnerable app!"

# SQL Injection
@app.route('/sql_injection')
def sql_injection():
    user_id = request.args.get('user_id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT username FROM users WHERE id = {user_id}")  # Vulnerable to SQL Injection
    username = cursor.fetchone()
    return f"Username: {username}"

# Command Injection
@app.route('/command_injection')
def command_injection():
    filename = request.args.get('filename')
    os.system(f"cat {filename}")  # Vulnerable to Command Injection
    return "File content displayed"

# Insecure Deserialization
@app.route('/deserialize')
def insecure_deserialization():
    serialized_data = request.args.get('data')
    deserialized_data = pickle.loads(serialized_data)  # Vulnerable to Insecure Deserialization
    return f"Deserialized data: {deserialized_data}"

# Insecure File Handling
@app.route('/file_handling')
def insecure_file_handling():
    filepath = request.args.get('filepath')
    with open(filepath, 'r') as f:  # Vulnerable to Insecure File Handling
        content = f.read()
    return f"File content: {content}"

# Cross-Site Scripting (XSS)
@app.route('/xss')
def xss():
    user_input = request.args.get('user_input')
    return render_template_string(f"<h1>{user_input}</h1>")  # Vulnerable to XSS

if __name__ == '__main__':
    app.run(debug=True)
