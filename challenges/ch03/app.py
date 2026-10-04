from flask import Flask, render_template_string

app = Flask(__name__)

INDEX = """
<!DOCTYPE html>
<html>
<head>
    <title>CSCC Challenge 03 - Secret Door</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; margin: 0; }
        nav { background: #1C2541; padding: 15px 30px; display: flex; gap: 20px; border-bottom: 1px solid #3A86FF; }
        nav a { color: #E0FBFC; text-decoration: none; font-weight: bold; }
        nav a:hover { color: #4EA8DE; }
        .content { padding: 40px; max-width: 600px; margin: auto; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; }
        h1 { color: #4EA8DE; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <!-- <a href="/secret-door.html">Admin Portal</a> -->
    </nav>
    <div class="content">
        <div class="card">
            <h1>🚪 Secret Door</h1>
            <p>The club navigation menu had a special admin portal link removed from the visible UI.</p>
            <p>Can you find where it leads?</p>
        </div>
    </div>
</body>
</html>
"""

SECRET = """
<!DOCTYPE html>
<html>
<head>
    <title>Secret Door - Admin Portal</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; padding: 40px; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; max-width: 600px; margin: auto; }
        h1 { color: #4EA8DE; }
        .flag { background: #0B132B; padding: 10px; border: 1px dashed #3A86FF; font-family: monospace; }
        a { color: #4EA8DE; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🎉 Admin Portal Unlocked</h1>
        <p>You successfully discovered the unlinked page!</p>
        <div class="flag">FLAG{HIDDEN_IN_PLAIN_SIGHT}</div>
        <p><a href="/">← Back to Home</a></p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(INDEX)

@app.route('/about')
def about():
    return render_template_string(INDEX.replace("Secret Door", "About"))

@app.route('/secret-door.html')
def secret():
    return render_template_string(SECRET)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
