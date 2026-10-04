from flask import Flask, render_template_string, request, make_response

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CSCC Challenge 04 - Cookie Monster</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; padding: 40px; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; max-width: 600px; margin: auto; }
        h1 { color: #4EA8DE; }
        .flag { background: #0B132B; padding: 10px; border: 1px dashed #3A86FF; font-family: monospace; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🍪 Cookie Monster</h1>
        <p>Current role cookie: <b>{{ role }}</b></p>
        {% if role == 'admin' %}
            <p>Welcome back, Administrator! Here is your VIP flag:</p>
            <div class="flag">FLAG{COOKIES_ARE_NOT_AUTHORIZATION}</div>
        {% else %}
            <p>You are currently logged in as a <b>guest</b>. Only administrators can access the VIP flag.</p>
            <p><small>Hint: Check your browser developer tools (Storage → Cookies) and see if you can modify your role.</small></p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    role = request.cookies.get('role')
    if not role:
        resp = make_response(render_template_string(TEMPLATE, role='guest'))
        resp.set_cookie('role', 'guest')
        return resp
    return render_template_string(TEMPLATE, role=role)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
