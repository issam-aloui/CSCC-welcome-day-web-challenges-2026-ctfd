from flask import Flask, render_template_string, request
import sqlite3
import os

app = Flask(__name__)

DB_PATH = 'ch08.db'

def init_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, is_admin INTEGER, flag TEXT)')
    cursor.execute("INSERT INTO users (username, password, is_admin, flag) VALUES ('admin', 'SuperSecretAdminPassword123', 1, 'FLAG{SQL_INJECTION_BYPASS}')")
    cursor.execute("INSERT INTO users (username, password, is_admin, flag) VALUES ('student', 'student123', 0, '')")
    conn.commit()
    conn.close()

init_db()

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CSCC Challenge 08 - Broken Login</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; padding: 40px; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; max-width: 600px; margin: auto; }
        h1 { color: #4EA8DE; }
        input, button { width: 100%; padding: 8px; margin-top: 10px; border-radius: 4px; border: 1px solid #3A86FF; background: #0B132B; color: #E0FBFC; box-sizing: border-box; }
        button { background: #3A86FF; cursor: pointer; font-weight: bold; width: auto; }
        .flag { background: #0B132B; padding: 10px; border: 1px dashed #3A86FF; font-family: monospace; margin-top: 15px; }
        .error { color: #ff6b6b; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🔐 Member Login Portal</h1>
        <p>Vulnerable database authentication portal.</p>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" value="{{ username }}">
            <input type="password" name="password" placeholder="Password">
            <button type="submit">Login</button>
        </form>
        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
        {% if success %}
            <div class="flag"><b>Success! Logged in as Admin.</b><br>Flag: {{ flag }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    success = False
    flag = ""
    username = ""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Vulnerable SQL query construction
        query = f"SELECT is_admin, flag FROM users WHERE username = '{username}' AND password = '{password}'"
        try:
            cursor.execute(query)
            row = cursor.fetchone()
            if row:
                success = True
                flag = row[1] if row[1] else "FLAG{LOGGED_IN_AS_NORMAL_USER}"
            else:
                error = "Invalid username or password."
        except Exception as e:
            error = f"Database Error: {e}"
        conn.close()
    return render_template_string(TEMPLATE, error=error, success=success, flag=flag, username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
