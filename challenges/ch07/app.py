from flask import Flask, render_template_string, request

app = Flask(__name__)

MESSAGES = ["Hello everyone! Welcome to the CSCC CTF!"]

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CSCC Challenge 07 - Say Something</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; padding: 40px; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; max-width: 600px; margin: auto; }
        h1 { color: #4EA8DE; }
        textarea, button { width: 100%; padding: 8px; margin-top: 10px; border-radius: 4px; border: 1px solid #3A86FF; background: #0B132B; color: #E0FBFC; box-sizing: border-box; }
        button { background: #3A86FF; cursor: pointer; font-weight: bold; width: auto; }
        .msg { background: #0B132B; padding: 10px; border: 1px solid #3A86FF; margin-top: 10px; border-radius: 4px; }
        .flag { background: #111; padding: 10px; border: 1px dashed #3A86FF; font-family: monospace; margin-top: 15px; color: #3A86FF; }
    </style>
</head>
<body>
    <div class="card">
        <h1>💬 Club Guestbook (XSS)</h1>
        <p>Leave a message for fellow club members!</p>
        <form method="POST">
            <textarea name="msg" rows="3" placeholder="Say something..."></textarea>
            <button type="submit">Post Message</button>
        </form>
        <hr style="border-color: #3A86FF; margin: 20px 0;">
        <h3>Recent Messages:</h3>
        {% for m in messages %}
            <div class="msg">{{ m | safe }}</div>
        {% endfor %}
        <div class="flag"><b>Admin Notice:</b> If you can execute JavaScript in the guestbook (e.g. <code>&lt;script&gt;alert('FLAG{XSS_INJECTION_SUCCESS}')&lt;/script&gt;</code>), the flag will pop up!</div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form.get('msg', '')
        if msg:
            MESSAGES.append(msg)
    return render_template_string(TEMPLATE, messages=MESSAGES)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
