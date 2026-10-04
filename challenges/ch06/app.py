from flask import Flask, render_template_string, request

app = Flask(__name__)

USERS = {
    "1": {"name": "Alice Student", "role": "Member", "bio": "Just joined the university cybersecurity club!"},
    "2": {"name": "Bob Member", "role": "Member", "bio": "Learning CTFs for the first time."},
    "67": {"name": "Dr. Cyber (Club President)", "role": "Administrator", "bio": "Secret Admin Profile", "flag": "FLAG{IDOR_EXPOSES_SECRETS}"}
}

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CSCC Challenge 06 - Who Am I?</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; padding: 40px; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; max-width: 600px; margin: auto; }
        h1 { color: #4EA8DE; }
        .flag { background: #0B132B; padding: 10px; border: 1px dashed #3A86FF; font-family: monospace; margin-top: 15px; }
        a { color: #4EA8DE; }
    </style>
</head>
<body>
    <div class="card">
        <h1>👤 User Profile Viewer</h1>
        {% if user %}
            <p><b>Name:</b> {{ user.name }}</p>
            <p><b>Role:</b> {{ user.role }}</p>
            <p><b>Bio:</b> {{ user.bio }}</p>
            {% if user.flag %}
                <div class="flag"><b>Flag:</b> {{ user.flag }}</div>
            {% endif %}
        {% else %}
            <p>User not found.</p>
        {% endif %}
        <hr style="border-color: #3A86FF; margin: 20px 0;">
        <p><small>Viewing profile ID: {{ user_id }} (Try changing the <code>?id=</code> parameter in the URL)</small></p>
    </div>
</body>
</html>
"""

@app.route('/')
def profile():
    user_id = request.args.get('id', '1')
    user = USERS.get(user_id)
    return render_template_string(TEMPLATE, user=user, user_id=user_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
