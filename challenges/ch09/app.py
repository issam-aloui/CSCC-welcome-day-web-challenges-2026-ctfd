from flask import Flask, render_template_string, request, make_response
import base64

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CSCC Challenge 09 - Hack the Club</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; padding: 40px; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; max-width: 600px; margin: auto; }
        h1 { color: #4EA8DE; }
        .flag { background: #0B132B; padding: 10px; border: 1px dashed #3A86FF; font-family: monospace; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚩 Hack the Club (Final Challenge)</h1>
        <p>You have reached the final welcome challenge!</p>
        <p>Secret token header / cookie status: <code>{{ token }}</code></p>
        {% if unlocked %}
            <div class="flag">FLAG{WELCOME_TO_CYBERSECURITY_2026}</div>
        {% else %}
            <p>Inspect the page, check cookies for encoded strings (Base64), and unlock the final club flag.</p>
            <p><small>Hint: Try decoding <code>dGVhbV9hZG1pbl91bmxvY2tlZA==</code></small></p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    token = request.cookies.get('club_token', 'Z3Vlc3Q=')
    unlocked = False
    try:
        decoded = base64.b64decode(token).decode('utf-8')
        if 'admin' in decoded or 'unlock' in decoded:
            unlocked = True
    except:
        pass
    
    resp = make_response(render_template_string(TEMPLATE, token=token, unlocked=unlocked))
    if not request.cookies.get('club_token'):
        resp.set_cookie('club_token', 'Z3Vlc3Q=')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
